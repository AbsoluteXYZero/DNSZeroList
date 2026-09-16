# Blocklist stats

_Generated 2026-09-16 15:49:18 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 179,792 | 74,791 | 41.6% |
| HaGeZi Normal | 183,088 | 80,817 | 44.1% |
| AdAway | 6,540 | 3,459 | 52.9% |
| OISD Big | 246,651 | 167,356 | 67.9% |
| Dan Pollock | 13,072 | 9,922 | 75.9% |
| Peter Lowe | 7,152 | 3,891 | 54.4% |
| Dandelion Sprout | 480 | 298 | 62.1% |
| EasyList | 56,601 | 9,230 | 16.3% |
| EasyPrivacy | 56,059 | 25,692 | 45.8% |
| uBO Ads | 1,763 | 1,719 | 97.5% |
| uBO Privacy | 1,435 | 1,354 | 94.4% |
| uBO Badware | 4,132 | 4,083 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,939 | 1,935 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **758,834** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 758,834 |
| **DNSZeroList.txt** (all sources, deduped) | **515,819** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **348,463** |

Deduplication removed 243,015 duplicate rule instances (32.0% of the raw total).
Dropping OISD Big removes a further 167,356 rules (32.4% of the full list).
