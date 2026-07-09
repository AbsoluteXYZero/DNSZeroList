# Blocklist stats

_Generated 2026-07-09 02:06:00 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 155,417 | 56,984 | 36.7% |
| HaGeZi Normal | 160,562 | 63,447 | 39.5% |
| AdAway | 6,540 | 3,533 | 54.0% |
| OISD Big | 327,261 | 244,895 | 74.8% |
| Dan Pollock | 12,930 | 9,731 | 75.3% |
| Peter Lowe | 7,062 | 3,846 | 54.5% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 54,131 | 9,364 | 17.3% |
| EasyPrivacy | 55,478 | 26,686 | 48.1% |
| uBO Ads | 1,787 | 1,738 | 97.3% |
| uBO Privacy | 1,376 | 1,294 | 94.0% |
| uBO Badware | 4,166 | 4,120 | 98.9% |
| uBO Quick Fixes | 92 | 83 | 90.2% |
| uBO Unbreak | 1,925 | 1,920 | 99.7% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **789,243** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 789,243 |
| **DNSZeroList.txt** (all sources, deduped) | **556,097** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **311,202** |

Deduplication removed 233,146 duplicate rule instances (29.5% of the raw total).
Dropping OISD Big removes a further 244,895 rules (44.0% of the full list).
