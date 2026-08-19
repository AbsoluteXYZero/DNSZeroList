# Blocklist stats

_Generated 2026-08-19 00:43:01 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,044 | 75,277 | 42.5% |
| HaGeZi Normal | 186,453 | 84,624 | 45.4% |
| AdAway | 6,540 | 3,460 | 52.9% |
| OISD Big | 272,438 | 188,529 | 69.2% |
| Dan Pollock | 13,015 | 9,860 | 75.8% |
| Peter Lowe | 7,076 | 3,844 | 54.3% |
| Dandelion Sprout | 480 | 293 | 61.0% |
| EasyList | 53,767 | 9,318 | 17.3% |
| EasyPrivacy | 55,849 | 25,607 | 45.9% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,408 | 1,329 | 94.4% |
| uBO Badware | 4,170 | 4,126 | 98.9% |
| uBO Quick Fixes | 89 | 80 | 89.9% |
| uBO Unbreak | 1,934 | 1,929 | 99.7% |
| uBO Resource Abuse | 38 | 36 | 94.7% |
| **Sum (before dedup)** | **782,071** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 782,071 |
| **DNSZeroList.txt** (all sources, deduped) | **539,466** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **350,937** |

Deduplication removed 242,605 duplicate rule instances (31.0% of the raw total).
Dropping OISD Big removes a further 188,529 rules (34.9% of the full list).
