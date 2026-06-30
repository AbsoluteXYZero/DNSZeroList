# Blocklist stats

_Generated 2026-06-30 13:59:22 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 153,594 | 56,901 | 37.0% |
| HaGeZi Normal | 161,556 | 64,289 | 39.8% |
| AdAway | 6,540 | 3,532 | 54.0% |
| OISD Big | 333,038 | 252,223 | 75.7% |
| Dan Pollock | 12,899 | 9,654 | 74.8% |
| Peter Lowe | 7,064 | 3,845 | 54.4% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 52,415 | 9,296 | 17.7% |
| EasyPrivacy | 55,443 | 26,667 | 48.1% |
| uBO Ads | 1,787 | 1,737 | 97.2% |
| uBO Privacy | 1,372 | 1,290 | 94.0% |
| uBO Badware | 4,150 | 4,105 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,925 | 1,921 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **792,392** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 792,392 |
| **DNSZeroList.txt** (all sources, deduped) | **559,814** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **307,591** |

Deduplication removed 232,578 duplicate rule instances (29.4% of the raw total).
Dropping OISD Big removes a further 252,223 rules (45.1% of the full list).
