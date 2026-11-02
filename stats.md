# Blocklist stats

_Generated 2026-11-02 03:35:31 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 186,543 | 84,412 | 45.3% |
| HaGeZi Normal | 175,760 | 73,777 | 42.0% |
| AdAway | 6,540 | 3,451 | 52.8% |
| OISD Big | 231,568 | 147,449 | 63.7% |
| Dan Pollock | 12,971 | 9,867 | 76.1% |
| Peter Lowe | 7,156 | 3,897 | 54.5% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 52,191 | 9,249 | 17.7% |
| EasyPrivacy | 56,416 | 26,117 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,458 | 1,371 | 94.0% |
| uBO Badware | 4,687 | 4,631 | 98.8% |
| uBO Quick Fixes | 222 | 211 | 95.0% |
| uBO Unbreak | 1,947 | 1,943 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **739,751** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 739,751 |
| **DNSZeroList.txt** (all sources, deduped) | **497,318** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **349,869** |

Deduplication removed 242,433 duplicate rule instances (32.8% of the raw total).
Dropping OISD Big removes a further 147,449 rules (29.6% of the full list).
