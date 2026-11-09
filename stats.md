# Blocklist stats

_Generated 2026-11-09 03:48:00 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 191,006 | 80,303 | 42.0% |
| HaGeZi Normal | 206,744 | 80,920 | 39.1% |
| AdAway | 6,540 | 3,439 | 52.6% |
| OISD Big | 231,858 | 136,381 | 58.8% |
| Dan Pollock | 12,971 | 9,844 | 75.9% |
| Peter Lowe | 7,152 | 3,894 | 54.4% |
| Dandelion Sprout | 490 | 304 | 62.0% |
| EasyList | 54,204 | 9,271 | 17.1% |
| EasyPrivacy | 56,545 | 26,249 | 46.4% |
| uBO Ads | 1,771 | 1,728 | 97.6% |
| uBO Privacy | 1,463 | 1,375 | 94.0% |
| uBO Badware | 4,731 | 4,675 | 98.8% |
| uBO Quick Fixes | 172 | 161 | 93.6% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **777,630** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 777,630 |
| **DNSZeroList.txt** (all sources, deduped) | **507,380** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **370,999** |

Deduplication removed 270,250 duplicate rule instances (34.8% of the raw total).
Dropping OISD Big removes a further 136,381 rules (26.9% of the full list).
