# Blocklist stats

_Generated 2026-11-14 04:12:20 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 191,429 | 80,072 | 41.8% |
| HaGeZi Normal | 211,014 | 82,972 | 39.3% |
| AdAway | 6,540 | 3,441 | 52.6% |
| OISD Big | 227,968 | 131,755 | 57.8% |
| Dan Pollock | 13,090 | 9,950 | 76.0% |
| Peter Lowe | 7,156 | 3,879 | 54.2% |
| Dandelion Sprout | 490 | 306 | 62.4% |
| EasyList | 53,107 | 9,250 | 17.4% |
| EasyPrivacy | 56,611 | 26,016 | 46.0% |
| uBO Ads | 1,766 | 1,722 | 97.5% |
| uBO Privacy | 1,469 | 1,378 | 93.8% |
| uBO Badware | 4,737 | 4,681 | 98.8% |
| uBO Quick Fixes | 172 | 161 | 93.6% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **777,532** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 777,532 |
| **DNSZeroList.txt** (all sources, deduped) | **504,595** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **372,840** |

Deduplication removed 272,937 duplicate rule instances (35.1% of the raw total).
Dropping OISD Big removes a further 131,755 rules (26.1% of the full list).
