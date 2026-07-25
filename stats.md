# Blocklist stats

_Generated 2026-07-25 13:04:20 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 160,098 | 56,746 | 35.4% |
| HaGeZi Normal | 180,504 | 82,509 | 45.7% |
| AdAway | 6,540 | 3,464 | 53.0% |
| OISD Big | 333,806 | 252,530 | 75.7% |
| Dan Pollock | 12,961 | 9,807 | 75.7% |
| Peter Lowe | 7,056 | 3,829 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 58,831 | 9,322 | 15.8% |
| EasyPrivacy | 55,565 | 26,738 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,384 | 1,302 | 94.1% |
| uBO Badware | 4,185 | 4,138 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **825,245** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 825,245 |
| **DNSZeroList.txt** (all sources, deduped) | **585,797** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **333,267** |

Deduplication removed 239,448 duplicate rule instances (29.0% of the raw total).
Dropping OISD Big removes a further 252,530 rules (43.1% of the full list).
