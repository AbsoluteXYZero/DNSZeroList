# Blocklist stats

_Generated 2026-07-14 13:12:13 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 157,263 | 56,840 | 36.1% |
| HaGeZi Normal | 161,772 | 63,302 | 39.1% |
| AdAway | 6,540 | 3,478 | 53.2% |
| OISD Big | 517,219 | 432,680 | 83.7% |
| Dan Pollock | 12,939 | 9,746 | 75.3% |
| Peter Lowe | 7,078 | 3,843 | 54.3% |
| Dandelion Sprout | 480 | 279 | 58.1% |
| EasyList | 55,803 | 9,297 | 16.7% |
| EasyPrivacy | 55,504 | 26,692 | 48.1% |
| uBO Ads | 1,785 | 1,737 | 97.3% |
| uBO Privacy | 1,379 | 1,297 | 94.1% |
| uBO Badware | 4,169 | 4,123 | 98.9% |
| uBO Quick Fixes | 97 | 87 | 89.7% |
| uBO Unbreak | 1,927 | 1,922 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **983,992** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 983,992 |
| **DNSZeroList.txt** (all sources, deduped) | **746,616** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **313,936** |

Deduplication removed 237,376 duplicate rule instances (24.1% of the raw total).
Dropping OISD Big removes a further 432,680 rules (58.0% of the full list).
