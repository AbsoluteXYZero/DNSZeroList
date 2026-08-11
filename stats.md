# Blocklist stats

_Generated 2026-08-11 12:42:46 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 154,721 | 56,999 | 36.8% |
| HaGeZi Normal | 181,366 | 84,728 | 46.7% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 251,324 | 171,012 | 68.0% |
| Dan Pollock | 12,991 | 9,839 | 75.7% |
| Peter Lowe | 7,076 | 3,842 | 54.3% |
| Dandelion Sprout | 480 | 291 | 60.6% |
| EasyList | 52,924 | 9,315 | 17.6% |
| EasyPrivacy | 55,673 | 26,782 | 48.1% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,400 | 1,321 | 94.4% |
| uBO Badware | 4,155 | 4,110 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,933 | 1,928 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **732,483** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 732,483 |
| **DNSZeroList.txt** (all sources, deduped) | **499,609** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **328,597** |

Deduplication removed 232,874 duplicate rule instances (31.8% of the raw total).
Dropping OISD Big removes a further 171,012 rules (34.2% of the full list).
