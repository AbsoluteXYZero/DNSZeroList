# Blocklist stats

_Generated 2026-06-20 13:42:20 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,206 | 56,962 | 36.0% |
| HaGeZi Normal | 158,411 | 52,917 | 33.4% |
| AdAway | 6,540 | 3,536 | 54.1% |
| OISD Big | 580,137 | 492,380 | 84.9% |
| Dan Pollock | 12,879 | 9,729 | 75.5% |
| Peter Lowe | 7,040 | 3,830 | 54.4% |
| Dandelion Sprout | 480 | 278 | 57.9% |
| EasyList | 57,153 | 9,386 | 16.4% |
| EasyPrivacy | 55,378 | 26,618 | 48.1% |
| uBO Ads | 1,786 | 1,736 | 97.2% |
| uBO Privacy | 1,358 | 1,278 | 94.1% |
| uBO Badware | 4,148 | 4,100 | 98.8% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,924 | 1,920 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **1,045,567** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 1,045,567 |
| **DNSZeroList.txt** (all sources, deduped) | **796,306** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **303,926** |

Deduplication removed 249,261 duplicate rule instances (23.8% of the raw total).
Dropping OISD Big removes a further 492,380 rules (61.8% of the full list).
