# Blocklist stats

_Generated 2026-08-11 01:03:05 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 154,536 | 56,986 | 36.9% |
| HaGeZi Normal | 181,366 | 84,730 | 46.7% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 251,161 | 170,898 | 68.0% |
| Dan Pollock | 12,991 | 9,839 | 75.7% |
| Peter Lowe | 7,074 | 3,841 | 54.3% |
| Dandelion Sprout | 480 | 291 | 60.6% |
| EasyList | 52,761 | 9,321 | 17.7% |
| EasyPrivacy | 55,671 | 26,782 | 48.1% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,399 | 1,320 | 94.4% |
| uBO Badware | 4,155 | 4,110 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,933 | 1,928 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **731,967** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 731,967 |
| **DNSZeroList.txt** (all sources, deduped) | **499,316** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **328,418** |

Deduplication removed 232,651 duplicate rule instances (31.8% of the raw total).
Dropping OISD Big removes a further 170,898 rules (34.2% of the full list).
