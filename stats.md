# Blocklist stats

_Generated 2026-09-04 15:29:20 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 180,030 | 74,982 | 41.6% |
| HaGeZi Normal | 190,523 | 85,083 | 44.7% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 270,077 | 182,355 | 67.5% |
| Dan Pollock | 13,054 | 9,907 | 75.9% |
| Peter Lowe | 7,112 | 3,868 | 54.4% |
| Dandelion Sprout | 480 | 298 | 62.1% |
| EasyList | 56,634 | 9,220 | 16.3% |
| EasyPrivacy | 55,994 | 25,672 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,429 | 1,346 | 94.2% |
| uBO Badware | 4,229 | 4,181 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,936 | 1,932 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **789,936** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 789,936 |
| **DNSZeroList.txt** (all sources, deduped) | **536,495** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **354,140** |

Deduplication removed 253,441 duplicate rule instances (32.1% of the raw total).
Dropping OISD Big removes a further 182,355 rules (34.0% of the full list).
