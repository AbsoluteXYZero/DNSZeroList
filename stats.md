# Blocklist stats

_Generated 2026-08-23 00:47:17 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,865 | 75,191 | 42.3% |
| HaGeZi Normal | 188,355 | 85,184 | 45.2% |
| AdAway | 6,540 | 3,460 | 52.9% |
| OISD Big | 268,160 | 184,745 | 68.9% |
| Dan Pollock | 13,029 | 9,877 | 75.8% |
| Peter Lowe | 7,064 | 3,838 | 54.3% |
| Dandelion Sprout | 480 | 296 | 61.7% |
| EasyList | 54,809 | 9,324 | 17.0% |
| EasyPrivacy | 55,879 | 25,613 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,424 | 1,343 | 94.3% |
| uBO Badware | 4,181 | 4,134 | 98.9% |
| uBO Quick Fixes | 89 | 80 | 89.9% |
| uBO Unbreak | 1,935 | 1,931 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **781,617** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 781,617 |
| **DNSZeroList.txt** (all sources, deduped) | **537,112** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **352,367** |

Deduplication removed 244,505 duplicate rule instances (31.3% of the raw total).
Dropping OISD Big removes a further 184,745 rules (34.4% of the full list).
