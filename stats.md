# Blocklist stats

_Generated 2026-10-05 03:11:43 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 178,425 | 77,317 | 43.3% |
| HaGeZi Normal | 157,607 | 61,592 | 39.1% |
| AdAway | 6,540 | 3,458 | 52.9% |
| OISD Big | 243,943 | 165,170 | 67.7% |
| Dan Pollock | 13,083 | 9,977 | 76.3% |
| Peter Lowe | 7,134 | 3,884 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 54,694 | 9,220 | 16.9% |
| EasyPrivacy | 56,227 | 25,746 | 45.8% |
| uBO Ads | 1,777 | 1,734 | 97.6% |
| uBO Privacy | 1,445 | 1,363 | 94.3% |
| uBO Badware | 4,252 | 4,201 | 98.8% |
| uBO Quick Fixes | 147 | 138 | 93.9% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **727,731** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 727,731 |
| **DNSZeroList.txt** (all sources, deduped) | **490,808** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **325,638** |

Deduplication removed 236,923 duplicate rule instances (32.6% of the raw total).
Dropping OISD Big removes a further 165,170 rules (33.7% of the full list).
