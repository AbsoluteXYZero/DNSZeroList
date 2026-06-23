# Blocklist stats

_Generated 2026-06-23 02:29:09 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,339 | 56,939 | 36.0% |
| HaGeZi Normal | 159,008 | 57,119 | 35.9% |
| AdAway | 6,540 | 3,536 | 54.1% |
| OISD Big | 333,254 | 248,333 | 74.5% |
| Dan Pollock | 12,882 | 9,676 | 75.1% |
| Peter Lowe | 7,048 | 3,833 | 54.4% |
| Dandelion Sprout | 480 | 284 | 59.2% |
| EasyList | 57,195 | 9,353 | 16.4% |
| EasyPrivacy | 55,387 | 26,638 | 48.1% |
| uBO Ads | 1,786 | 1,736 | 97.2% |
| uBO Privacy | 1,362 | 1,281 | 94.1% |
| uBO Badware | 4,151 | 4,103 | 98.8% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,924 | 1,920 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **799,483** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 799,483 |
| **DNSZeroList.txt** (all sources, deduped) | **553,309** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **304,976** |

Deduplication removed 246,174 duplicate rule instances (30.8% of the raw total).
Dropping OISD Big removes a further 248,333 rules (44.9% of the full list).
