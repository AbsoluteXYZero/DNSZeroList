# Blocklist stats

_Generated 2026-07-05 13:12:01 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 155,194 | 56,965 | 36.7% |
| HaGeZi Normal | 158,177 | 59,101 | 37.4% |
| AdAway | 6,540 | 3,533 | 54.0% |
| OISD Big | 351,194 | 269,281 | 76.7% |
| Dan Pollock | 12,909 | 9,705 | 75.2% |
| Peter Lowe | 7,058 | 3,844 | 54.5% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 53,936 | 9,312 | 17.3% |
| EasyPrivacy | 55,465 | 26,658 | 48.1% |
| uBO Ads | 1,787 | 1,738 | 97.3% |
| uBO Privacy | 1,372 | 1,290 | 94.0% |
| uBO Badware | 4,163 | 4,118 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,925 | 1,921 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **810,329** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 810,329 |
| **DNSZeroList.txt** (all sources, deduped) | **575,893** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **306,612** |

Deduplication removed 234,436 duplicate rule instances (28.9% of the raw total).
Dropping OISD Big removes a further 269,281 rules (46.8% of the full list).
