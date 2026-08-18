# Blocklist stats

_Generated 2026-08-18 12:26:46 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 176,901 | 75,276 | 42.6% |
| HaGeZi Normal | 186,453 | 84,497 | 45.3% |
| AdAway | 6,540 | 3,460 | 52.9% |
| OISD Big | 270,598 | 186,654 | 69.0% |
| Dan Pollock | 13,012 | 9,857 | 75.8% |
| Peter Lowe | 7,076 | 3,844 | 54.3% |
| Dandelion Sprout | 480 | 293 | 61.0% |
| EasyList | 53,628 | 9,314 | 17.4% |
| EasyPrivacy | 55,846 | 25,607 | 45.9% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,408 | 1,329 | 94.4% |
| uBO Badware | 4,169 | 4,125 | 98.9% |
| uBO Quick Fixes | 89 | 80 | 89.9% |
| uBO Unbreak | 1,934 | 1,929 | 99.7% |
| uBO Resource Abuse | 38 | 36 | 94.7% |
| **Sum (before dedup)** | **779,942** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 779,942 |
| **DNSZeroList.txt** (all sources, deduped) | **537,438** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **350,784** |

Deduplication removed 242,504 duplicate rule instances (31.1% of the raw total).
Dropping OISD Big removes a further 186,654 rules (34.7% of the full list).
