# Blocklist stats

_Generated 2026-09-10 02:15:50 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,765 | 74,942 | 42.2% |
| HaGeZi Normal | 181,417 | 78,512 | 43.3% |
| AdAway | 6,540 | 3,470 | 53.1% |
| OISD Big | 255,395 | 169,658 | 66.4% |
| Dan Pollock | 13,063 | 9,919 | 75.9% |
| Peter Lowe | 7,116 | 3,869 | 54.4% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 54,268 | 9,233 | 17.0% |
| EasyPrivacy | 56,001 | 25,667 | 45.8% |
| uBO Ads | 1,770 | 1,727 | 97.6% |
| uBO Privacy | 1,432 | 1,350 | 94.3% |
| uBO Badware | 4,236 | 4,187 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,937 | 1,933 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **761,550** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 761,550 |
| **DNSZeroList.txt** (all sources, deduped) | **515,121** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **345,463** |

Deduplication removed 246,429 duplicate rule instances (32.4% of the raw total).
Dropping OISD Big removes a further 169,658 rules (32.9% of the full list).
