# Blocklist stats

_Generated 2026-06-21 13:50:44 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,526 | 56,959 | 35.9% |
| HaGeZi Normal | 158,833 | 55,973 | 35.2% |
| AdAway | 6,540 | 3,535 | 54.1% |
| OISD Big | 496,452 | 410,848 | 82.8% |
| Dan Pollock | 12,880 | 9,732 | 75.6% |
| Peter Lowe | 7,040 | 3,831 | 54.4% |
| Dandelion Sprout | 480 | 280 | 58.3% |
| EasyList | 57,458 | 9,382 | 16.3% |
| EasyPrivacy | 55,385 | 26,630 | 48.1% |
| uBO Ads | 1,786 | 1,736 | 97.2% |
| uBO Privacy | 1,361 | 1,280 | 94.0% |
| uBO Badware | 4,150 | 4,102 | 98.8% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,924 | 1,920 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **962,942** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 962,942 |
| **DNSZeroList.txt** (all sources, deduped) | **715,804** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **304,956** |

Deduplication removed 247,138 duplicate rule instances (25.7% of the raw total).
Dropping OISD Big removes a further 410,848 rules (57.4% of the full list).
