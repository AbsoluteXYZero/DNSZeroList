# Blocklist stats

_Generated 2026-08-12 12:47:35 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 155,087 | 56,999 | 36.8% |
| HaGeZi Normal | 181,366 | 84,729 | 46.7% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 251,792 | 171,268 | 68.0% |
| Dan Pollock | 12,998 | 9,846 | 75.8% |
| Peter Lowe | 7,080 | 3,845 | 54.3% |
| Dandelion Sprout | 480 | 291 | 60.6% |
| EasyList | 53,269 | 9,318 | 17.5% |
| EasyPrivacy | 55,680 | 26,783 | 48.1% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,404 | 1,325 | 94.4% |
| uBO Badware | 4,155 | 4,110 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,933 | 1,928 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **733,684** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 733,684 |
| **DNSZeroList.txt** (all sources, deduped) | **500,246** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **328,978** |

Deduplication removed 233,438 duplicate rule instances (31.8% of the raw total).
Dropping OISD Big removes a further 171,268 rules (34.2% of the full list).
