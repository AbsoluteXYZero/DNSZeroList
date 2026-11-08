# Blocklist stats

_Generated 2026-11-08 17:25:01 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 190,797 | 80,297 | 42.1% |
| HaGeZi Normal | 206,744 | 80,907 | 39.1% |
| AdAway | 6,540 | 3,439 | 52.6% |
| OISD Big | 232,115 | 136,794 | 58.9% |
| Dan Pollock | 12,971 | 9,844 | 75.9% |
| Peter Lowe | 7,152 | 3,894 | 54.4% |
| Dandelion Sprout | 490 | 304 | 62.0% |
| EasyList | 54,051 | 9,296 | 17.2% |
| EasyPrivacy | 56,461 | 26,181 | 46.4% |
| uBO Ads | 1,771 | 1,728 | 97.6% |
| uBO Privacy | 1,463 | 1,375 | 94.0% |
| uBO Badware | 4,731 | 4,675 | 98.8% |
| uBO Quick Fixes | 172 | 161 | 93.6% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **777,441** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 777,441 |
| **DNSZeroList.txt** (all sources, deduped) | **507,545** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **370,751** |

Deduplication removed 269,896 duplicate rule instances (34.7% of the raw total).
Dropping OISD Big removes a further 136,794 rules (27.0% of the full list).
