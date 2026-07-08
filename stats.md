# Blocklist stats

_Generated 2026-07-08 13:43:17 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 155,310 | 56,986 | 36.7% |
| HaGeZi Normal | 160,811 | 63,435 | 39.4% |
| AdAway | 6,540 | 3,534 | 54.0% |
| OISD Big | 327,757 | 245,347 | 74.9% |
| Dan Pollock | 12,923 | 9,723 | 75.2% |
| Peter Lowe | 7,062 | 3,839 | 54.4% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 53,982 | 9,311 | 17.2% |
| EasyPrivacy | 55,474 | 26,685 | 48.1% |
| uBO Ads | 1,787 | 1,738 | 97.3% |
| uBO Privacy | 1,376 | 1,294 | 94.0% |
| uBO Badware | 4,166 | 4,120 | 98.9% |
| uBO Quick Fixes | 92 | 83 | 90.2% |
| uBO Unbreak | 1,925 | 1,920 | 99.7% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **789,721** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 789,721 |
| **DNSZeroList.txt** (all sources, deduped) | **556,411** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **311,064** |

Deduplication removed 233,310 duplicate rule instances (29.5% of the raw total).
Dropping OISD Big removes a further 245,347 rules (44.1% of the full list).
