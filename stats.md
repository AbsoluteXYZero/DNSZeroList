# Blocklist stats

_Generated 2026-08-14 01:11:07 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 155,591 | 57,043 | 36.7% |
| HaGeZi Normal | 180,742 | 82,139 | 45.4% |
| AdAway | 6,540 | 3,460 | 52.9% |
| OISD Big | 265,605 | 183,977 | 69.3% |
| Dan Pollock | 13,007 | 9,856 | 75.8% |
| Peter Lowe | 7,084 | 3,847 | 54.3% |
| Dandelion Sprout | 480 | 294 | 61.3% |
| EasyList | 53,739 | 9,313 | 17.3% |
| EasyPrivacy | 55,694 | 26,783 | 48.1% |
| uBO Ads | 1,769 | 1,725 | 97.5% |
| uBO Privacy | 1,404 | 1,326 | 94.4% |
| uBO Badware | 4,156 | 4,112 | 98.9% |
| uBO Quick Fixes | 90 | 81 | 90.0% |
| uBO Unbreak | 1,933 | 1,928 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **747,871** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 747,871 |
| **DNSZeroList.txt** (all sources, deduped) | **511,722** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **327,745** |

Deduplication removed 236,149 duplicate rule instances (31.6% of the raw total).
Dropping OISD Big removes a further 183,977 rules (36.0% of the full list).
