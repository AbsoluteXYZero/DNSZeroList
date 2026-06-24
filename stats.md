# Blocklist stats

_Generated 2026-06-24 14:09:50 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,809 | 56,948 | 35.9% |
| HaGeZi Normal | 159,417 | 56,125 | 35.2% |
| AdAway | 6,540 | 3,528 | 53.9% |
| OISD Big | 468,436 | 382,312 | 81.6% |
| Dan Pollock | 12,884 | 9,657 | 75.0% |
| Peter Lowe | 7,048 | 3,834 | 54.4% |
| Dandelion Sprout | 480 | 277 | 57.7% |
| EasyList | 57,618 | 9,352 | 16.2% |
| EasyPrivacy | 55,402 | 26,649 | 48.1% |
| uBO Ads | 1,787 | 1,737 | 97.2% |
| uBO Privacy | 1,362 | 1,281 | 94.1% |
| uBO Badware | 4,152 | 4,104 | 98.8% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,924 | 1,920 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **935,986** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 935,986 |
| **DNSZeroList.txt** (all sources, deduped) | **687,689** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **305,377** |

Deduplication removed 248,297 duplicate rule instances (26.5% of the raw total).
Dropping OISD Big removes a further 382,312 rules (55.6% of the full list).
