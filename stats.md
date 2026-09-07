# Blocklist stats

_Generated 2026-09-07 02:02:06 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 180,800 | 74,972 | 41.5% |
| HaGeZi Normal | 192,712 | 86,824 | 45.1% |
| AdAway | 6,540 | 3,464 | 53.0% |
| OISD Big | 268,640 | 180,502 | 67.2% |
| Dan Pollock | 13,057 | 9,911 | 75.9% |
| Peter Lowe | 7,112 | 3,868 | 54.4% |
| Dandelion Sprout | 480 | 298 | 62.1% |
| EasyList | 57,425 | 9,253 | 16.1% |
| EasyPrivacy | 56,007 | 25,678 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,430 | 1,347 | 94.2% |
| uBO Badware | 4,229 | 4,181 | 98.9% |
| uBO Quick Fixes | 92 | 83 | 90.2% |
| uBO Unbreak | 1,937 | 1,933 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **792,268** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 792,268 |
| **DNSZeroList.txt** (all sources, deduped) | **537,186** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **356,684** |

Deduplication removed 255,082 duplicate rule instances (32.2% of the raw total).
Dropping OISD Big removes a further 180,502 rules (33.6% of the full list).
