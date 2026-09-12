# Blocklist stats

_Generated 2026-09-12 14:41:16 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 178,708 | 74,956 | 41.9% |
| HaGeZi Normal | 180,141 | 79,699 | 44.2% |
| AdAway | 6,540 | 3,472 | 53.1% |
| OISD Big | 245,374 | 166,936 | 68.0% |
| Dan Pollock | 13,064 | 9,921 | 75.9% |
| Peter Lowe | 7,150 | 3,886 | 54.3% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 55,140 | 9,207 | 16.7% |
| EasyPrivacy | 56,012 | 25,673 | 45.8% |
| uBO Ads | 1,764 | 1,720 | 97.5% |
| uBO Privacy | 1,433 | 1,352 | 94.3% |
| uBO Badware | 4,239 | 4,189 | 98.8% |
| uBO Quick Fixes | 94 | 85 | 90.4% |
| uBO Unbreak | 1,935 | 1,931 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **752,111** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 752,111 |
| **DNSZeroList.txt** (all sources, deduped) | **512,582** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **345,646** |

Deduplication removed 239,529 duplicate rule instances (31.8% of the raw total).
Dropping OISD Big removes a further 166,936 rules (32.6% of the full list).
