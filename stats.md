# Blocklist stats

_Generated 2026-07-31 01:58:49 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 161,569 | 56,697 | 35.1% |
| HaGeZi Normal | 180,483 | 81,829 | 45.3% |
| AdAway | 6,540 | 3,464 | 53.0% |
| OISD Big | 336,815 | 255,485 | 75.9% |
| Dan Pollock | 12,971 | 9,820 | 75.7% |
| Peter Lowe | 7,058 | 3,830 | 54.3% |
| Dandelion Sprout | 480 | 290 | 60.4% |
| EasyList | 60,224 | 9,339 | 15.5% |
| EasyPrivacy | 55,621 | 26,762 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,388 | 1,308 | 94.2% |
| uBO Badware | 4,186 | 4,140 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **831,168** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 831,168 |
| **DNSZeroList.txt** (all sources, deduped) | **588,950** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **333,465** |

Deduplication removed 242,218 duplicate rule instances (29.1% of the raw total).
Dropping OISD Big removes a further 255,485 rules (43.4% of the full list).
