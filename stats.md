# Blocklist stats

_Generated 2026-08-19 12:27:05 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,188 | 75,266 | 42.5% |
| HaGeZi Normal | 186,566 | 84,590 | 45.3% |
| AdAway | 6,540 | 3,460 | 52.9% |
| OISD Big | 272,433 | 188,552 | 69.2% |
| Dan Pollock | 13,015 | 9,860 | 75.8% |
| Peter Lowe | 7,076 | 3,844 | 54.3% |
| Dandelion Sprout | 480 | 293 | 61.0% |
| EasyList | 53,900 | 9,317 | 17.3% |
| EasyPrivacy | 55,839 | 25,597 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,408 | 1,329 | 94.4% |
| uBO Badware | 4,170 | 4,125 | 98.9% |
| uBO Quick Fixes | 89 | 80 | 89.9% |
| uBO Unbreak | 1,934 | 1,929 | 99.7% |
| uBO Resource Abuse | 38 | 36 | 94.7% |
| **Sum (before dedup)** | **782,446** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 782,446 |
| **DNSZeroList.txt** (all sources, deduped) | **539,495** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **350,943** |

Deduplication removed 242,951 duplicate rule instances (31.1% of the raw total).
Dropping OISD Big removes a further 188,552 rules (34.9% of the full list).
