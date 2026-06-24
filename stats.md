# Blocklist stats

_Generated 2026-06-24 02:30:00 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,639 | 56,914 | 35.9% |
| HaGeZi Normal | 159,437 | 55,930 | 35.1% |
| AdAway | 6,540 | 3,534 | 54.0% |
| OISD Big | 489,537 | 403,112 | 82.3% |
| Dan Pollock | 12,884 | 9,642 | 74.8% |
| Peter Lowe | 7,048 | 3,834 | 54.4% |
| Dandelion Sprout | 480 | 278 | 57.9% |
| EasyList | 57,476 | 9,354 | 16.3% |
| EasyPrivacy | 55,400 | 26,635 | 48.1% |
| uBO Ads | 1,787 | 1,737 | 97.2% |
| uBO Privacy | 1,362 | 1,281 | 94.1% |
| uBO Badware | 4,152 | 4,104 | 98.8% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,924 | 1,920 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **956,793** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 956,793 |
| **DNSZeroList.txt** (all sources, deduped) | **708,411** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **305,299** |

Deduplication removed 248,382 duplicate rule instances (26.0% of the raw total).
Dropping OISD Big removes a further 403,112 rules (56.9% of the full list).
