# Blocklist stats

_Generated 2026-11-16 21:26:53 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 190,532 | 90,160 | 47.3% |
| HaGeZi Normal | 184,108 | 79,721 | 43.3% |
| AdAway | 6,540 | 3,444 | 52.7% |
| OISD Big | 228,635 | 131,850 | 57.7% |
| Dan Pollock | 13,090 | 9,954 | 76.0% |
| Peter Lowe | 7,162 | 3,885 | 54.2% |
| Dandelion Sprout | 490 | 307 | 62.7% |
| EasyList | 52,179 | 9,265 | 17.8% |
| EasyPrivacy | 56,639 | 26,025 | 45.9% |
| uBO Ads | 1,766 | 1,722 | 97.5% |
| uBO Privacy | 1,471 | 1,379 | 93.7% |
| uBO Badware | 4,744 | 4,688 | 98.8% |
| uBO Quick Fixes | 173 | 162 | 93.6% |
| uBO Unbreak | 1,951 | 1,947 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **749,517** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 749,517 |
| **DNSZeroList.txt** (all sources, deduped) | **501,427** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **369,577** |

Deduplication removed 248,090 duplicate rule instances (33.1% of the raw total).
Dropping OISD Big removes a further 131,850 rules (26.3% of the full list).
