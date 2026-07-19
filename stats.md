# Blocklist stats

_Generated 2026-07-19 01:51:58 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,179 | 56,832 | 35.9% |
| HaGeZi Normal | 177,840 | 81,597 | 45.9% |
| AdAway | 6,540 | 3,462 | 52.9% |
| OISD Big | 326,430 | 245,803 | 75.3% |
| Dan Pollock | 12,947 | 9,800 | 75.7% |
| Peter Lowe | 7,066 | 3,834 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 57,048 | 9,323 | 16.3% |
| EasyPrivacy | 55,528 | 26,727 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,381 | 1,299 | 94.1% |
| uBO Badware | 4,174 | 4,127 | 98.9% |
| uBO Quick Fixes | 95 | 85 | 89.5% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **811,450** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 811,450 |
| **DNSZeroList.txt** (all sources, deduped) | **576,364** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **330,561** |

Deduplication removed 235,086 duplicate rule instances (29.0% of the raw total).
Dropping OISD Big removes a further 245,803 rules (42.6% of the full list).
