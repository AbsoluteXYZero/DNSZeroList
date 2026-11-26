# Blocklist stats

_Generated 2026-11-26 20:43:59 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 195,314 | 93,051 | 47.6% |
| HaGeZi Normal | 180,372 | 89,321 | 49.5% |
| AdAway | 6,540 | 3,443 | 52.6% |
| OISD Big | 222,172 | 137,324 | 61.8% |
| Dan Pollock | 13,117 | 9,987 | 76.1% |
| Peter Lowe | 7,150 | 3,880 | 54.3% |
| Dandelion Sprout | 490 | 307 | 62.7% |
| EasyList | 54,004 | 9,272 | 17.2% |
| EasyPrivacy | 56,825 | 26,228 | 46.2% |
| uBO Ads | 1,765 | 1,721 | 97.5% |
| uBO Privacy | 1,467 | 1,375 | 93.7% |
| uBO Badware | 4,739 | 4,684 | 98.8% |
| uBO Quick Fixes | 106 | 95 | 89.6% |
| uBO Unbreak | 1,949 | 1,945 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **746,046** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 746,046 |
| **DNSZeroList.txt** (all sources, deduped) | **508,461** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **371,137** |

Deduplication removed 237,585 duplicate rule instances (31.8% of the raw total).
Dropping OISD Big removes a further 137,324 rules (27.0% of the full list).
