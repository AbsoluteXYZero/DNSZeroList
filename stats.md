# Blocklist stats

_Generated 2026-10-18 02:16:25 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 185,954 | 79,696 | 42.9% |
| HaGeZi Normal | 165,192 | 67,853 | 41.1% |
| AdAway | 6,540 | 3,450 | 52.8% |
| OISD Big | 234,434 | 155,348 | 66.3% |
| Dan Pollock | 13,085 | 9,970 | 76.2% |
| Peter Lowe | 7,170 | 3,901 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 58,680 | 9,261 | 15.8% |
| EasyPrivacy | 56,307 | 26,031 | 46.2% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,452 | 1,367 | 94.1% |
| uBO Badware | 4,268 | 4,218 | 98.8% |
| uBO Quick Fixes | 185 | 174 | 94.1% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **737,500** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 737,500 |
| **DNSZeroList.txt** (all sources, deduped) | **496,273** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **340,925** |

Deduplication removed 241,227 duplicate rule instances (32.7% of the raw total).
Dropping OISD Big removes a further 155,348 rules (31.3% of the full list).
