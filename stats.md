# Blocklist stats

_Generated 2026-11-07 17:12:34 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 190,465 | 80,962 | 42.5% |
| HaGeZi Normal | 196,068 | 76,918 | 39.2% |
| AdAway | 6,540 | 3,349 | 51.2% |
| OISD Big | 232,466 | 139,861 | 60.2% |
| Dan Pollock | 12,971 | 9,837 | 75.8% |
| Peter Lowe | 7,150 | 3,938 | 55.1% |
| Dandelion Sprout | 490 | 307 | 62.7% |
| EasyList | 53,692 | 9,252 | 17.2% |
| EasyPrivacy | 56,454 | 26,185 | 46.4% |
| uBO Ads | 1,771 | 1,728 | 97.6% |
| uBO Privacy | 1,463 | 1,375 | 94.0% |
| uBO Badware | 4,729 | 4,673 | 98.8% |
| uBO Quick Fixes | 172 | 161 | 93.6% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **766,414** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 766,414 |
| **DNSZeroList.txt** (all sources, deduped) | **503,804** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **363,943** |

Deduplication removed 262,610 duplicate rule instances (34.3% of the raw total).
Dropping OISD Big removes a further 139,861 rules (27.8% of the full list).
