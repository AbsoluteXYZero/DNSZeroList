# Blocklist stats

_Generated 2026-11-11 03:53:42 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 188,765 | 80,038 | 42.4% |
| HaGeZi Normal | 207,081 | 81,728 | 39.5% |
| AdAway | 6,540 | 3,438 | 52.6% |
| OISD Big | 226,269 | 132,876 | 58.7% |
| Dan Pollock | 12,971 | 9,839 | 75.9% |
| Peter Lowe | 7,154 | 3,877 | 54.2% |
| Dandelion Sprout | 490 | 304 | 62.0% |
| EasyList | 51,908 | 9,265 | 17.8% |
| EasyPrivacy | 56,566 | 26,250 | 46.4% |
| uBO Ads | 1,766 | 1,722 | 97.5% |
| uBO Privacy | 1,464 | 1,375 | 93.9% |
| uBO Badware | 4,732 | 4,676 | 98.8% |
| uBO Quick Fixes | 171 | 160 | 93.6% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **767,860** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 767,860 |
| **DNSZeroList.txt** (all sources, deduped) | **501,429** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **368,553** |

Deduplication removed 266,431 duplicate rule instances (34.7% of the raw total).
Dropping OISD Big removes a further 132,876 rules (26.5% of the full list).
