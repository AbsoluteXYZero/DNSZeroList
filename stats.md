# Blocklist stats

_Generated 2026-07-20 02:09:34 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,495 | 56,837 | 35.9% |
| HaGeZi Normal | 177,899 | 81,550 | 45.8% |
| AdAway | 6,540 | 3,461 | 52.9% |
| OISD Big | 327,141 | 246,455 | 75.3% |
| Dan Pollock | 12,947 | 9,800 | 75.7% |
| Peter Lowe | 7,066 | 3,834 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 57,351 | 9,325 | 16.3% |
| EasyPrivacy | 55,528 | 26,729 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,383 | 1,301 | 94.1% |
| uBO Badware | 4,182 | 4,135 | 98.9% |
| uBO Quick Fixes | 96 | 86 | 89.6% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **812,850** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 812,850 |
| **DNSZeroList.txt** (all sources, deduped) | **577,148** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **330,693** |

Deduplication removed 235,702 duplicate rule instances (29.0% of the raw total).
Dropping OISD Big removes a further 246,455 rules (42.7% of the full list).
