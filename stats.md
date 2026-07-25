# Blocklist stats

_Generated 2026-07-25 01:53:18 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 159,972 | 56,750 | 35.5% |
| HaGeZi Normal | 180,316 | 82,452 | 45.7% |
| AdAway | 6,540 | 3,464 | 53.0% |
| OISD Big | 333,475 | 252,324 | 75.7% |
| Dan Pollock | 12,961 | 9,807 | 75.7% |
| Peter Lowe | 7,056 | 3,829 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 58,717 | 9,326 | 15.9% |
| EasyPrivacy | 55,564 | 26,738 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,384 | 1,302 | 94.1% |
| uBO Badware | 4,185 | 4,138 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **824,485** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 824,485 |
| **DNSZeroList.txt** (all sources, deduped) | **585,420** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **333,096** |

Deduplication removed 239,065 duplicate rule instances (29.0% of the raw total).
Dropping OISD Big removes a further 252,324 rules (43.1% of the full list).
