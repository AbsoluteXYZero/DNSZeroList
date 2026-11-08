# Blocklist stats

_Generated 2026-11-08 03:33:23 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 190,603 | 80,296 | 42.1% |
| HaGeZi Normal | 206,011 | 80,367 | 39.0% |
| AdAway | 6,540 | 3,438 | 52.6% |
| OISD Big | 232,176 | 137,086 | 59.0% |
| Dan Pollock | 12,971 | 9,845 | 75.9% |
| Peter Lowe | 7,152 | 3,894 | 54.4% |
| Dandelion Sprout | 490 | 304 | 62.0% |
| EasyList | 53,838 | 9,267 | 17.2% |
| EasyPrivacy | 56,456 | 26,180 | 46.4% |
| uBO Ads | 1,771 | 1,728 | 97.6% |
| uBO Privacy | 1,463 | 1,375 | 94.0% |
| uBO Badware | 4,730 | 4,674 | 98.8% |
| uBO Quick Fixes | 172 | 161 | 93.6% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **776,356** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 776,356 |
| **DNSZeroList.txt** (all sources, deduped) | **506,951** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **369,865** |

Deduplication removed 269,405 duplicate rule instances (34.7% of the raw total).
Dropping OISD Big removes a further 137,086 rules (27.0% of the full list).
