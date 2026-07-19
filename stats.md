# Blocklist stats

_Generated 2026-07-19 12:57:12 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,335 | 56,833 | 35.9% |
| HaGeZi Normal | 177,972 | 81,597 | 45.8% |
| AdAway | 6,540 | 3,461 | 52.9% |
| OISD Big | 326,828 | 246,067 | 75.3% |
| Dan Pollock | 12,947 | 9,800 | 75.7% |
| Peter Lowe | 7,066 | 3,834 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 57,179 | 9,308 | 16.3% |
| EasyPrivacy | 55,527 | 26,727 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,381 | 1,299 | 94.1% |
| uBO Badware | 4,182 | 4,135 | 98.9% |
| uBO Quick Fixes | 96 | 86 | 89.6% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **812,275** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 812,275 |
| **DNSZeroList.txt** (all sources, deduped) | **576,796** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **330,729** |

Deduplication removed 235,479 duplicate rule instances (29.0% of the raw total).
Dropping OISD Big removes a further 246,067 rules (42.7% of the full list).
