# Blocklist stats

_Generated 2026-11-17 05:49:53 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 190,665 | 90,162 | 47.3% |
| HaGeZi Normal | 184,508 | 79,810 | 43.3% |
| AdAway | 6,540 | 3,444 | 52.7% |
| OISD Big | 228,221 | 131,273 | 57.5% |
| Dan Pollock | 13,090 | 9,954 | 76.0% |
| Peter Lowe | 7,162 | 3,885 | 54.2% |
| Dandelion Sprout | 490 | 307 | 62.7% |
| EasyList | 52,305 | 9,268 | 17.7% |
| EasyPrivacy | 56,643 | 26,027 | 45.9% |
| uBO Ads | 1,766 | 1,722 | 97.5% |
| uBO Privacy | 1,471 | 1,379 | 93.7% |
| uBO Badware | 4,744 | 4,688 | 98.8% |
| uBO Quick Fixes | 173 | 162 | 93.6% |
| uBO Unbreak | 1,951 | 1,947 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **749,766** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 749,766 |
| **DNSZeroList.txt** (all sources, deduped) | **501,157** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **369,884** |

Deduplication removed 248,609 duplicate rule instances (33.2% of the raw total).
Dropping OISD Big removes a further 131,273 rules (26.2% of the full list).
