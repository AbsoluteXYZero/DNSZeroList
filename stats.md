# Blocklist stats

_Generated 2026-07-08 01:52:57 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 155,152 | 56,987 | 36.7% |
| HaGeZi Normal | 161,090 | 63,432 | 39.4% |
| AdAway | 6,540 | 3,534 | 54.0% |
| OISD Big | 327,626 | 245,166 | 74.8% |
| Dan Pollock | 12,923 | 9,715 | 75.2% |
| Peter Lowe | 7,060 | 3,837 | 54.3% |
| Dandelion Sprout | 480 | 284 | 59.2% |
| EasyList | 53,827 | 9,303 | 17.3% |
| EasyPrivacy | 55,472 | 26,684 | 48.1% |
| uBO Ads | 1,787 | 1,738 | 97.3% |
| uBO Privacy | 1,374 | 1,292 | 94.0% |
| uBO Badware | 4,166 | 4,120 | 98.9% |
| uBO Quick Fixes | 94 | 85 | 90.4% |
| uBO Unbreak | 1,925 | 1,920 | 99.7% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **789,552** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 789,552 |
| **DNSZeroList.txt** (all sources, deduped) | **556,061** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **310,895** |

Deduplication removed 233,491 duplicate rule instances (29.6% of the raw total).
Dropping OISD Big removes a further 245,166 rules (44.1% of the full list).
