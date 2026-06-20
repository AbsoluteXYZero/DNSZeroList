#!/usr/bin/env python3
"""Build a unified, deduplicated AdGuard Home blocklist from multiple sources.

Strategy:
- Fetch every source in parallel.
- Drop cosmetic rules (## / #@# / #?# / #$# / #%#) since AdGuard Home is
  DNS-level only and cannot apply them. Keeps the file lean.
- Normalize hosts-format lines (0.0.0.0 / 127.0.0.1 domain) and bare domains
  into adblock syntax (||domain^) so they dedup against the adblock lists.
- Keep network/exception rules as-is.
- Deduplicate exactly, then sort (blocks first, @@ exceptions last).

Origin tracking (ANNOTATE):
- AdGuard Home does NOT support inline/trailing comments on adblock-style rules
  (`||domain^ # note` would be parsed as a literal pattern and match nothing).
  Inline comments only work in hosts-style lines. So when ANNOTATE is on, each
  rule is preceded by a `! source, source` comment line, which AGH ignores. To
  find which list a blocked domain came from:  grep -A1 "||domain^" blocklist.txt
  (the line above it lists every source carrying that rule).

A failed source is logged and skipped; it never fails the whole build unless
EVERY source fails.
"""

import concurrent.futures
import datetime
import re
import sys
import urllib.request
from collections import Counter

SOURCES = {
    "AdGuard DNS Filter": "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt",
    "HaGeZi Normal": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_34.txt",
    "AdAway": "https://adaway.org/hosts.txt",
    "OISD Big": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_27.txt",
    "Dan Pollock": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_4.txt",
    "Peter Lowe": "https://pgl.yoyo.org/adservers/serverlist.php?hostformat=adblock",
    "Dandelion Sprout": "https://adguardteam.github.io/HostlistsRegistry/assets/filter_39.txt",

    "EasyList": "https://easylist.to/easylist/easylist.txt",
    "EasyPrivacy": "https://easylist.to/easylist/easyprivacy.txt",

    "uBO Ads": "https://ublockorigin.github.io/uAssets/filters/filters.txt",
    "uBO Privacy": "https://ublockorigin.github.io/uAssets/filters/privacy.txt",
    "uBO Badware": "https://ublockorigin.github.io/uAssets/filters/badware.txt",
    "uBO Quick Fixes": "https://ublockorigin.github.io/uAssets/filters/quick-fixes.txt",
    "uBO Unbreak": "https://ublockorigin.github.io/uAssets/filters/unbreak.txt",
    "uBO Resource Abuse": "https://ublockorigin.github.io/uAssets/filters/resource-abuse.txt",
}

# Output files: filename -> set of source names to EXCLUDE from that file.
# A rule is dropped from a file only if every one of its sources is excluded.
OUTPUTS = {
    "DNSZeroList.txt": set(),
    "DNSZeroList_no_oisd.txt": {"OISD Big"},
}
# Prefix each rule with a "! source, source" comment line showing its origin(s).
# AGH ignores ! lines, so this is functionally identical to a clean list, just
# ~2x the line count. Set False for a lean, unannotated file.
ANNOTATE = True
TIMEOUT = 60
UA = "Mozilla/5.0 (compatible; AdGuardBlocklistBuilder/1.0; +https://github.com)"

# Cosmetic / scriptlet markers AdGuard Home cannot use.
COSMETIC = ("##", "#@#", "#?#", "#$#", "#%#", "#$?#", "#@$#", "#@?#")
HOSTS_IP = re.compile(r"^(?:0\.0\.0\.0|127\.0\.0\.1|::1?|::|255\.255\.255\.255)\s+(.+)$")
BARE_DOMAIN = re.compile(r"^(?:\*\.)?[a-z0-9_](?:[a-z0-9_-]*[a-z0-9_])?(?:\.[a-z0-9_](?:[a-z0-9_-]*[a-z0-9_])?)+$")
LOCAL_NAMES = {"localhost", "localhost.localdomain", "local", "broadcasthost",
               "ip6-localhost", "ip6-loopback", "ip6-localnet", "ip6-mcastprefix",
               "ip6-allnodes", "ip6-allrouters", "0.0.0.0"}


def fetch(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        data = resp.read().decode("utf-8", errors="replace")
    print(f"  ok    {name}: {len(data.splitlines())} lines", flush=True)
    return name, data


def add(rule, source, table):
    """Record that `rule` came from `source` (a rule may have many sources)."""
    table.setdefault(rule, set()).add(source)


def normalize(raw, source, blocks, exceptions):
    """Parse one raw line and record any resulting rule(s) under `source`."""
    line = raw.strip()
    if not line:
        return
    # Adblock comments.
    if line.startswith("!"):
        return
    # Cosmetic / scriptlet rules: not usable by AGH.
    if any(m in line for m in COSMETIC):
        return
    # Hosts/plain-list comments.
    if line.startswith("#"):
        return

    # Exception rules pass through untouched.
    if line.startswith("@@"):
        add(line, source, exceptions)
        return

    # Hosts-format line -> one ||domain^ per hostname.
    m = HOSTS_IP.match(line)
    if m:
        rest = m.group(1).split("#", 1)[0]  # strip inline hosts comment
        for host in rest.split():
            host = host.strip().lower().rstrip(".")
            if host and host not in LOCAL_NAMES:
                add(f"||{host}^", source, blocks)
        return

    # Bare domain (some lists are just domain-per-line).
    low = line.lower()
    if BARE_DOMAIN.match(low):
        add(f"||{low.rstrip('.')}^", source, blocks)
        return

    # Anything else that looks like an adblock rule: keep as-is.
    # (||domain^, /regex/, |http..., rules with $modifiers, etc.)
    add(line, source, blocks)


def emit(f, table, exclude):
    """Write rules in sorted order. Drop rules sourced only from excluded lists;
    strip excluded names from the origin comment. Add origin comment if ANNOTATE."""
    for rule in sorted(table):
        kept = table[rule] - exclude
        if not kept:
            continue
        if ANNOTATE:
            f.write(f"! {', '.join(sorted(kept))}\n")
        f.write(rule + "\n")


def count(table, exclude):
    return sum(1 for srcs in table.values() if srcs - exclude)


def write_list(filename, exclude, results, blocks, exceptions):
    nblocks = count(blocks, exclude)
    nexcept = count(exceptions, exclude)
    total = nblocks + nexcept
    used = [n for n in SOURCES if n in results and n not in exclude]
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    header = [
        "! Title: Zero Unified Blocklist" + (" (no OISD)" if exclude else ""),
        "! Description: Deduplicated merge of multiple ad/tracker/malware lists for AdGuard Home.",
        f"! Last modified: {now}",
        f"! Sources: {len(used)} included",
        f"! Total rules: {total} (blocks: {nblocks}, exceptions: {nexcept})",
        "! Cosmetic/scriptlet rules are stripped (not usable by DNS-level filtering).",
        "! Each rule is preceded by a comment listing its source list(s)." if ANNOTATE else "!",
        "!",
    ]
    for name in SOURCES:
        if name not in results:
            mark = "x (fetch failed)"
        elif name in exclude:
            mark = "- (excluded)"
        else:
            mark = "+"
        header.append(f"! [{mark}] {name}")
    header.append("!")

    with open(filename, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(header) + "\n")
        emit(f, blocks, exclude)
        emit(f, exceptions, exclude)
    print(f"Wrote {filename}: {total} rules ({len(used)} sources).", flush=True)


def write_stats(results, blocks, exceptions):
    """Per-source totals + unique (exclusive) counts, and final dedup totals."""
    total = Counter()   # rules each source carries (incl. shared with others)
    unique = Counter()  # rules exclusive to a single source
    for table in (blocks, exceptions):
        for srcs in table.values():
            for s in srcs:
                total[s] += 1
            if len(srcs) == 1:
                unique[next(iter(srcs))] += 1

    sum_total = sum(total.values())
    full = len(blocks) + len(exceptions)
    no_oisd = count(blocks, {"OISD Big"}) + count(exceptions, {"OISD Big"})
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    lines = [
        "# Blocklist stats",
        "",
        f"_Generated {now}_",
        "",
        "- **Total rules** = rules a source carries (after parsing to adblock form, "
        "including ones also present in other lists).",
        "- **Unique** = rules that ONLY that source provides (exclusive contribution).",
        "- **% unique** = Unique / Total for that source.",
        "",
        "## Per source",
        "",
        "| Source | Total rules | Unique | % unique |",
        "| --- | ---: | ---: | ---: |",
    ]
    for name in SOURCES:
        if name not in results:
            lines.append(f"| {name} | _fetch failed_ | - | - |")
            continue
        t = total.get(name, 0)
        u = unique.get(name, 0)
        pct = f"{(u / t * 100):.1f}%" if t else "-"
        lines.append(f"| {name} | {t:,} | {u:,} | {pct} |")
    lines.append(f"| **Sum (before dedup)** | **{sum_total:,}** | | |")

    lines += [
        "",
        "## Deduplicated totals",
        "",
        "| Output | Rules |",
        "| --- | ---: |",
        f"| Sum of all sources before dedup | {sum_total:,} |",
        f"| **DNSZeroList.txt** (all sources, deduped) | **{full:,}** |",
        f"| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **{no_oisd:,}** |",
        "",
        f"Deduplication removed {sum_total - full:,} duplicate rule instances "
        f"({(1 - full / sum_total) * 100:.1f}% of the raw total)."
        if sum_total else "",
        f"Dropping OISD Big removes a further {full - no_oisd:,} rules "
        f"({(1 - no_oisd / full) * 100:.1f}% of the full list)."
        if full else "",
        "",
    ]
    with open("stats.md", "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))
    print(f"Wrote stats.md (full: {full:,}, no_oisd: {no_oisd:,}).", flush=True)


def main():
    print(f"Fetching {len(SOURCES)} sources...", flush=True)
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        futures = {ex.submit(fetch, n, u): n for n, u in SOURCES.items()}
        for fut in concurrent.futures.as_completed(futures):
            name = futures[fut]
            try:
                n, data = fut.result()
                results[n] = data
            except Exception as e:  # noqa: BLE001
                print(f"  FAIL  {name}: {e}", flush=True)

    if not results:
        print("All sources failed. Aborting (keeping previous output).", file=sys.stderr)
        return 1

    blocks, exceptions = {}, {}
    # Iterate SOURCES order for deterministic source-set construction.
    for name in SOURCES:
        data = results.get(name)
        if not data:
            continue
        for raw in data.splitlines():
            normalize(raw, name, blocks, exceptions)

    for filename, exclude in OUTPUTS.items():
        write_list(filename, exclude, results, blocks, exceptions)

    write_stats(results, blocks, exceptions)
    return 0


if __name__ == "__main__":
    sys.exit(main())