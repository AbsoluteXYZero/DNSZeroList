# Blocklist stats

_Generated 2026-11-13 04:15:54 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 191,008 | 80,074 | 41.9% |
| HaGeZi Normal | 209,073 | 81,933 | 39.2% |
| AdAway | 6,540 | 3,441 | 52.6% |
| OISD Big | 227,854 | 132,220 | 58.0% |
| Dan Pollock | 13,090 | 9,950 | 76.0% |
| Peter Lowe | 7,158 | 3,880 | 54.2% |
| Dandelion Sprout | 490 | 306 | 62.4% |
| EasyList | 52,695 | 9,247 | 17.5% |
| EasyPrivacy | 56,588 | 26,008 | 46.0% |
| uBO Ads | 1,766 | 1,722 | 97.5% |
| uBO Privacy | 1,467 | 1,377 | 93.9% |
| uBO Badware | 4,737 | 4,681 | 98.8% |
| uBO Quick Fixes | 172 | 161 | 93.6% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **774,621** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 774,621 |
| **DNSZeroList.txt** (all sources, deduped) | **503,334** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **371,114** |

Deduplication removed 271,287 duplicate rule instances (35.0% of the raw total).
Dropping OISD Big removes a further 132,220 rules (26.3% of the full list).
