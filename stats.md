# Blocklist stats

_Generated 2026-09-03 15:31:20 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 179,730 | 74,981 | 41.7% |
| HaGeZi Normal | 190,433 | 85,220 | 44.8% |
| AdAway | 6,540 | 3,462 | 52.9% |
| OISD Big | 269,843 | 182,249 | 67.5% |
| Dan Pollock | 13,054 | 9,907 | 75.9% |
| Peter Lowe | 7,122 | 3,871 | 54.4% |
| Dandelion Sprout | 480 | 298 | 62.1% |
| EasyList | 56,345 | 9,213 | 16.4% |
| EasyPrivacy | 55,981 | 25,662 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,428 | 1,346 | 94.3% |
| uBO Badware | 4,227 | 4,179 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,936 | 1,932 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **789,017** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 789,017 |
| **DNSZeroList.txt** (all sources, deduped) | **536,243** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **353,994** |

Deduplication removed 252,774 duplicate rule instances (32.0% of the raw total).
Dropping OISD Big removes a further 182,249 rules (34.0% of the full list).
