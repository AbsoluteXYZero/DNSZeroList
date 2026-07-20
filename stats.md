# Blocklist stats

_Generated 2026-07-20 13:49:53 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,637 | 56,821 | 35.8% |
| HaGeZi Normal | 178,416 | 81,889 | 45.9% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 326,846 | 246,378 | 75.4% |
| Dan Pollock | 12,947 | 9,793 | 75.6% |
| Peter Lowe | 7,066 | 3,834 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 57,487 | 9,324 | 16.2% |
| EasyPrivacy | 55,527 | 26,729 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,383 | 1,301 | 94.1% |
| uBO Badware | 4,182 | 4,135 | 98.9% |
| uBO Quick Fixes | 96 | 86 | 89.6% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **813,349** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 813,349 |
| **DNSZeroList.txt** (all sources, deduped) | **577,550** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **331,172** |

Deduplication removed 235,799 duplicate rule instances (29.0% of the raw total).
Dropping OISD Big removes a further 246,378 rules (42.7% of the full list).
