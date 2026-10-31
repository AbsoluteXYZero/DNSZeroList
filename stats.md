# Blocklist stats

_Generated 2026-10-31 16:33:40 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 186,019 | 84,448 | 45.4% |
| HaGeZi Normal | 175,278 | 73,407 | 41.9% |
| AdAway | 6,540 | 3,448 | 52.7% |
| OISD Big | 235,370 | 150,074 | 63.8% |
| Dan Pollock | 12,971 | 9,864 | 76.0% |
| Peter Lowe | 7,156 | 3,897 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 51,673 | 9,236 | 17.9% |
| EasyPrivacy | 56,410 | 26,115 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,458 | 1,371 | 94.0% |
| uBO Badware | 4,686 | 4,629 | 98.8% |
| uBO Quick Fixes | 222 | 211 | 95.0% |
| uBO Unbreak | 1,947 | 1,943 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **742,022** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 742,022 |
| **DNSZeroList.txt** (all sources, deduped) | **499,316** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **349,242** |

Deduplication removed 242,706 duplicate rule instances (32.7% of the raw total).
Dropping OISD Big removes a further 150,074 rules (30.1% of the full list).
