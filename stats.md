# Blocklist stats

_Generated 2026-06-25 02:32:07 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,958 | 56,959 | 35.8% |
| HaGeZi Normal | 159,442 | 56,154 | 35.2% |
| AdAway | 6,540 | 3,527 | 53.9% |
| OISD Big | 475,106 | 389,199 | 81.9% |
| Dan Pollock | 12,887 | 9,708 | 75.3% |
| Peter Lowe | 7,050 | 3,836 | 54.4% |
| Dandelion Sprout | 480 | 281 | 58.5% |
| EasyList | 57,767 | 9,357 | 16.2% |
| EasyPrivacy | 55,405 | 26,654 | 48.1% |
| uBO Ads | 1,787 | 1,737 | 97.2% |
| uBO Privacy | 1,362 | 1,281 | 94.1% |
| uBO Badware | 4,152 | 4,104 | 98.8% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,924 | 1,920 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **942,987** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 942,987 |
| **DNSZeroList.txt** (all sources, deduped) | **694,603** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **305,404** |

Deduplication removed 248,384 duplicate rule instances (26.3% of the raw total).
Dropping OISD Big removes a further 389,199 rules (56.0% of the full list).
