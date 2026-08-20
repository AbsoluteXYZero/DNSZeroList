# Blocklist stats

_Generated 2026-08-20 00:43:00 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,349 | 75,260 | 42.4% |
| HaGeZi Normal | 186,566 | 84,593 | 45.3% |
| AdAway | 6,540 | 3,460 | 52.9% |
| OISD Big | 273,323 | 189,335 | 69.3% |
| Dan Pollock | 13,018 | 9,863 | 75.8% |
| Peter Lowe | 7,076 | 3,844 | 54.3% |
| Dandelion Sprout | 480 | 293 | 61.0% |
| EasyList | 54,044 | 9,314 | 17.2% |
| EasyPrivacy | 55,848 | 25,598 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,408 | 1,329 | 94.4% |
| uBO Badware | 4,170 | 4,125 | 98.9% |
| uBO Quick Fixes | 89 | 80 | 89.9% |
| uBO Unbreak | 1,935 | 1,930 | 99.7% |
| uBO Resource Abuse | 38 | 36 | 94.7% |
| **Sum (before dedup)** | **783,654** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 783,654 |
| **DNSZeroList.txt** (all sources, deduped) | **540,441** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **351,106** |

Deduplication removed 243,213 duplicate rule instances (31.0% of the raw total).
Dropping OISD Big removes a further 189,335 rules (35.0% of the full list).
