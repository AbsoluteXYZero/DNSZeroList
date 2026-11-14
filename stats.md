# Blocklist stats

_Generated 2026-11-14 17:29:31 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 191,589 | 79,777 | 41.6% |
| HaGeZi Normal | 212,130 | 83,496 | 39.4% |
| AdAway | 6,540 | 3,441 | 52.6% |
| OISD Big | 227,989 | 131,566 | 57.7% |
| Dan Pollock | 13,090 | 9,948 | 76.0% |
| Peter Lowe | 7,160 | 3,882 | 54.2% |
| Dandelion Sprout | 490 | 306 | 62.4% |
| EasyList | 53,280 | 9,270 | 17.4% |
| EasyPrivacy | 56,614 | 26,013 | 45.9% |
| uBO Ads | 1,766 | 1,722 | 97.5% |
| uBO Privacy | 1,469 | 1,377 | 93.7% |
| uBO Badware | 4,741 | 4,685 | 98.8% |
| uBO Quick Fixes | 172 | 161 | 93.6% |
| uBO Unbreak | 1,951 | 1,947 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **779,018** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 779,018 |
| **DNSZeroList.txt** (all sources, deduped) | **505,231** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **373,665** |

Deduplication removed 273,787 duplicate rule instances (35.1% of the raw total).
Dropping OISD Big removes a further 131,566 rules (26.0% of the full list).
