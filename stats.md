# Blocklist stats

_Generated 2026-09-05 02:09:32 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 180,168 | 74,972 | 41.6% |
| HaGeZi Normal | 192,721 | 87,104 | 45.2% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 270,033 | 182,180 | 67.5% |
| Dan Pollock | 13,057 | 9,910 | 75.9% |
| Peter Lowe | 7,112 | 3,867 | 54.4% |
| Dandelion Sprout | 480 | 298 | 62.1% |
| EasyList | 56,777 | 9,232 | 16.3% |
| EasyPrivacy | 55,997 | 25,670 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,429 | 1,346 | 94.2% |
| uBO Badware | 4,229 | 4,181 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,936 | 1,932 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **792,377** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 792,377 |
| **DNSZeroList.txt** (all sources, deduped) | **538,516** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **356,336** |

Deduplication removed 253,861 duplicate rule instances (32.0% of the raw total).
Dropping OISD Big removes a further 182,180 rules (33.8% of the full list).
