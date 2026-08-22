# Blocklist stats

_Generated 2026-08-22 12:20:27 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,709 | 75,192 | 42.3% |
| HaGeZi Normal | 188,355 | 85,100 | 45.2% |
| AdAway | 6,540 | 3,460 | 52.9% |
| OISD Big | 268,918 | 185,560 | 69.0% |
| Dan Pollock | 13,029 | 9,877 | 75.8% |
| Peter Lowe | 7,064 | 3,838 | 54.3% |
| Dandelion Sprout | 480 | 296 | 61.7% |
| EasyList | 54,659 | 9,330 | 17.1% |
| EasyPrivacy | 55,878 | 25,612 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,424 | 1,343 | 94.3% |
| uBO Badware | 4,173 | 4,126 | 98.9% |
| uBO Quick Fixes | 89 | 80 | 89.9% |
| uBO Unbreak | 1,935 | 1,931 | 99.8% |
| uBO Resource Abuse | 38 | 36 | 94.7% |
| **Sum (before dedup)** | **782,061** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 782,061 |
| **DNSZeroList.txt** (all sources, deduped) | **537,768** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **352,208** |

Deduplication removed 244,293 duplicate rule instances (31.2% of the raw total).
Dropping OISD Big removes a further 185,560 rules (34.5% of the full list).
