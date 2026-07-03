# Blocklist stats

_Generated 2026-07-03 13:45:29 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 154,540 | 56,907 | 36.8% |
| HaGeZi Normal | 154,822 | 57,792 | 37.3% |
| AdAway | 6,540 | 3,532 | 54.0% |
| OISD Big | 325,959 | 246,999 | 75.8% |
| Dan Pollock | 12,909 | 9,809 | 76.0% |
| Peter Lowe | 7,056 | 3,844 | 54.5% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 53,323 | 9,331 | 17.5% |
| EasyPrivacy | 55,457 | 26,676 | 48.1% |
| uBO Ads | 1,787 | 1,738 | 97.3% |
| uBO Privacy | 1,372 | 1,290 | 94.0% |
| uBO Badware | 4,159 | 4,114 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,925 | 1,921 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **780,458** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 780,458 |
| **DNSZeroList.txt** (all sources, deduped) | **549,174** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **302,175** |

Deduplication removed 231,284 duplicate rule instances (29.6% of the raw total).
Dropping OISD Big removes a further 246,999 rules (45.0% of the full list).
