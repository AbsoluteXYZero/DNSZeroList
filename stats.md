# Blocklist stats

_Generated 2026-08-12 01:10:37 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 154,884 | 56,988 | 36.8% |
| HaGeZi Normal | 181,366 | 84,729 | 46.7% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 251,430 | 170,969 | 68.0% |
| Dan Pollock | 12,998 | 9,846 | 75.8% |
| Peter Lowe | 7,076 | 3,841 | 54.3% |
| Dandelion Sprout | 480 | 291 | 60.6% |
| EasyList | 53,107 | 9,340 | 17.6% |
| EasyPrivacy | 55,680 | 26,783 | 48.1% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,402 | 1,323 | 94.4% |
| uBO Badware | 4,155 | 4,110 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,933 | 1,928 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **732,951** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 732,951 |
| **DNSZeroList.txt** (all sources, deduped) | **499,767** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **328,798** |

Deduplication removed 233,184 duplicate rule instances (31.8% of the raw total).
Dropping OISD Big removes a further 170,969 rules (34.2% of the full list).
