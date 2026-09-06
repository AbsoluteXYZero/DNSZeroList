# Blocklist stats

_Generated 2026-09-06 14:40:16 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 180,693 | 74,972 | 41.5% |
| HaGeZi Normal | 192,712 | 86,808 | 45.0% |
| AdAway | 6,540 | 3,464 | 53.0% |
| OISD Big | 269,303 | 181,231 | 67.3% |
| Dan Pollock | 13,057 | 9,911 | 75.9% |
| Peter Lowe | 7,112 | 3,868 | 54.4% |
| Dandelion Sprout | 480 | 298 | 62.1% |
| EasyList | 57,263 | 9,209 | 16.1% |
| EasyPrivacy | 56,007 | 25,678 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,430 | 1,347 | 94.2% |
| uBO Badware | 4,229 | 4,181 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,937 | 1,933 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **792,661** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 792,661 |
| **DNSZeroList.txt** (all sources, deduped) | **537,752** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **356,521** |

Deduplication removed 254,909 duplicate rule instances (32.2% of the raw total).
Dropping OISD Big removes a further 181,231 rules (33.7% of the full list).
