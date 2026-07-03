# Blocklist stats

_Generated 2026-07-03 02:05:26 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 154,404 | 56,915 | 36.9% |
| HaGeZi Normal | 155,371 | 58,056 | 37.4% |
| AdAway | 6,540 | 3,531 | 54.0% |
| OISD Big | 325,669 | 246,760 | 75.8% |
| Dan Pollock | 12,909 | 9,809 | 76.0% |
| Peter Lowe | 7,064 | 3,845 | 54.4% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 53,178 | 9,322 | 17.5% |
| EasyPrivacy | 55,454 | 26,671 | 48.1% |
| uBO Ads | 1,787 | 1,738 | 97.3% |
| uBO Privacy | 1,372 | 1,290 | 94.0% |
| uBO Badware | 4,153 | 4,108 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,925 | 1,921 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **780,435** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 780,435 |
| **DNSZeroList.txt** (all sources, deduped) | **549,053** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **302,293** |

Deduplication removed 231,382 duplicate rule instances (29.6% of the raw total).
Dropping OISD Big removes a further 246,760 rules (44.9% of the full list).
