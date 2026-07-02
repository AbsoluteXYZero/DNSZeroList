# Blocklist stats

_Generated 2026-07-02 13:40:29 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 154,250 | 56,907 | 36.9% |
| HaGeZi Normal | 155,519 | 57,953 | 37.3% |
| AdAway | 6,540 | 3,532 | 54.0% |
| OISD Big | 326,476 | 247,392 | 75.8% |
| Dan Pollock | 12,908 | 9,758 | 75.6% |
| Peter Lowe | 7,064 | 3,845 | 54.4% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 53,034 | 9,322 | 17.6% |
| EasyPrivacy | 55,453 | 26,670 | 48.1% |
| uBO Ads | 1,787 | 1,746 | 97.7% |
| uBO Privacy | 1,372 | 1,290 | 94.0% |
| uBO Badware | 4,152 | 4,107 | 98.9% |
| uBO Quick Fixes | _fetch failed_ | - | - |
| uBO Unbreak | 1,925 | 1,921 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **780,996** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 780,996 |
| **DNSZeroList.txt** (all sources, deduped) | **549,391** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **301,999** |

Deduplication removed 231,605 duplicate rule instances (29.7% of the raw total).
Dropping OISD Big removes a further 247,392 rules (45.0% of the full list).
