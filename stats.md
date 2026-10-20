# Blocklist stats

_Generated 2026-10-20 16:04:12 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 188,740 | 81,396 | 43.1% |
| HaGeZi Normal | 167,139 | 68,667 | 41.1% |
| AdAway | 6,540 | 3,448 | 52.7% |
| OISD Big | 233,484 | 153,524 | 65.8% |
| Dan Pollock | 13,085 | 9,966 | 76.2% |
| Peter Lowe | 7,176 | 3,907 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 59,528 | 9,253 | 15.5% |
| EasyPrivacy | 56,337 | 26,083 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,451 | 1,366 | 94.1% |
| uBO Badware | 4,284 | 4,234 | 98.8% |
| uBO Quick Fixes | 213 | 202 | 94.8% |
| uBO Unbreak | 1,943 | 1,939 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **742,212** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 742,212 |
| **DNSZeroList.txt** (all sources, deduped) | **498,661** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **345,137** |

Deduplication removed 243,551 duplicate rule instances (32.8% of the raw total).
Dropping OISD Big removes a further 153,524 rules (30.8% of the full list).
