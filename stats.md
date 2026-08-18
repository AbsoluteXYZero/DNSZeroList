# Blocklist stats

_Generated 2026-08-18 00:42:41 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 176,752 | 75,935 | 43.0% |
| HaGeZi Normal | 183,588 | 83,724 | 45.6% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 269,836 | 186,012 | 68.9% |
| Dan Pollock | 13,012 | 9,859 | 75.8% |
| Peter Lowe | 7,076 | 3,844 | 54.3% |
| Dandelion Sprout | 480 | 294 | 61.3% |
| EasyList | 53,495 | 9,317 | 17.4% |
| EasyPrivacy | 55,845 | 25,599 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,408 | 1,329 | 94.4% |
| uBO Badware | 4,168 | 4,124 | 98.9% |
| uBO Quick Fixes | 90 | 81 | 90.0% |
| uBO Unbreak | 1,934 | 1,929 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **776,031** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 776,031 |
| **DNSZeroList.txt** (all sources, deduped) | **535,756** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **349,744** |

Deduplication removed 240,275 duplicate rule instances (31.0% of the raw total).
Dropping OISD Big removes a further 186,012 rules (34.7% of the full list).
