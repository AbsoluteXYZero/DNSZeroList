# Blocklist stats

_Generated 2026-09-04 02:08:59 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 179,860 | 74,984 | 41.7% |
| HaGeZi Normal | 190,433 | 85,240 | 44.8% |
| AdAway | 6,540 | 3,462 | 52.9% |
| OISD Big | 269,652 | 181,922 | 67.5% |
| Dan Pollock | 13,054 | 9,907 | 75.9% |
| Peter Lowe | 7,122 | 3,871 | 54.4% |
| Dandelion Sprout | 480 | 298 | 62.1% |
| EasyList | 56,481 | 9,227 | 16.3% |
| EasyPrivacy | 55,984 | 25,662 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,429 | 1,346 | 94.2% |
| uBO Badware | 4,227 | 4,179 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,936 | 1,932 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **789,096** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 789,096 |
| **DNSZeroList.txt** (all sources, deduped) | **536,056** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **354,134** |

Deduplication removed 253,040 duplicate rule instances (32.1% of the raw total).
Dropping OISD Big removes a further 181,922 rules (33.9% of the full list).
