# Blocklist stats

_Generated 2026-06-20 01:31:05 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,050 | 56,577 | 35.8% |
| HaGeZi Normal | 158,455 | 53,378 | 33.7% |
| AdAway | 6,540 | 3,528 | 53.9% |
| OISD Big | 425,574 | 338,264 | 79.5% |
| Dan Pollock | 12,879 | 9,743 | 75.7% |
| Peter Lowe | 7,040 | 3,831 | 54.4% |
| Dandelion Sprout | 480 | 283 | 59.0% |
| EasyList | 56,995 | 9,374 | 16.4% |
| EasyPrivacy | 55,376 | 26,621 | 48.1% |
| uBO Ads | 1,786 | 1,736 | 97.2% |
| uBO Privacy | 1,358 | 1,278 | 94.1% |
| uBO Badware | 4,148 | 4,100 | 98.8% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,924 | 1,920 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **890,732** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 890,732 |
| **DNSZeroList.txt** (all sources, deduped) | **641,628** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **303,364** |

Deduplication removed 249,104 duplicate rule instances (28.0% of the raw total).
Dropping OISD Big removes a further 338,264 rules (52.7% of the full list).
