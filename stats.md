# Blocklist stats

_Generated 2026-10-06 17:38:25 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 178,907 | 77,126 | 43.1% |
| HaGeZi Normal | 159,845 | 62,099 | 38.8% |
| AdAway | 6,540 | 3,456 | 52.8% |
| OISD Big | 240,615 | 161,251 | 67.0% |
| Dan Pollock | 13,083 | 9,980 | 76.3% |
| Peter Lowe | 7,136 | 3,887 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 55,163 | 9,235 | 16.7% |
| EasyPrivacy | 56,231 | 25,746 | 45.8% |
| uBO Ads | 1,777 | 1,734 | 97.6% |
| uBO Privacy | 1,445 | 1,363 | 94.3% |
| uBO Badware | 4,261 | 4,210 | 98.8% |
| uBO Quick Fixes | 152 | 143 | 94.1% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **727,612** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 727,612 |
| **DNSZeroList.txt** (all sources, deduped) | **489,131** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **327,880** |

Deduplication removed 238,481 duplicate rule instances (32.8% of the raw total).
Dropping OISD Big removes a further 161,251 rules (33.0% of the full list).
