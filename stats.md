# Blocklist stats

_Generated 2026-08-16 12:20:33 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 156,497 | 56,989 | 36.4% |
| HaGeZi Normal | 182,539 | 82,872 | 45.4% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 267,849 | 185,526 | 69.3% |
| Dan Pollock | 13,008 | 9,856 | 75.8% |
| Peter Lowe | 7,074 | 3,842 | 54.3% |
| Dandelion Sprout | 480 | 294 | 61.3% |
| EasyList | 54,469 | 9,323 | 17.1% |
| EasyPrivacy | 55,830 | 26,757 | 47.9% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,407 | 1,328 | 94.4% |
| uBO Badware | 4,166 | 4,122 | 98.9% |
| uBO Quick Fixes | 90 | 81 | 90.0% |
| uBO Unbreak | 1,934 | 1,929 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **753,690** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 753,690 |
| **DNSZeroList.txt** (all sources, deduped) | **515,069** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **329,543** |

Deduplication removed 238,621 duplicate rule instances (31.7% of the raw total).
Dropping OISD Big removes a further 185,526 rules (36.0% of the full list).
