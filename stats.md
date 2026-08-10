# Blocklist stats

_Generated 2026-08-10 12:47:35 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 154,340 | 56,976 | 36.9% |
| HaGeZi Normal | 181,366 | 84,581 | 46.6% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 251,486 | 171,083 | 68.0% |
| Dan Pollock | 12,989 | 9,837 | 75.7% |
| Peter Lowe | 7,072 | 3,839 | 54.3% |
| Dandelion Sprout | 480 | 291 | 60.6% |
| EasyList | 52,594 | 9,336 | 17.8% |
| EasyPrivacy | 55,666 | 26,782 | 48.1% |
| uBO Ads | 1,769 | 1,725 | 97.5% |
| uBO Privacy | 1,396 | 1,317 | 94.3% |
| uBO Badware | 4,155 | 4,110 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,932 | 1,927 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **731,915** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 731,915 |
| **DNSZeroList.txt** (all sources, deduped) | **499,314** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **328,231** |

Deduplication removed 232,601 duplicate rule instances (31.8% of the raw total).
Dropping OISD Big removes a further 171,083 rules (34.3% of the full list).
