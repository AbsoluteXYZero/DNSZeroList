# Blocklist stats

_Generated 2026-11-19 19:46:12 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 191,666 | 90,117 | 47.0% |
| HaGeZi Normal | 177,101 | 72,185 | 40.8% |
| AdAway | 6,540 | 3,447 | 52.7% |
| OISD Big | 231,548 | 134,675 | 58.2% |
| Dan Pollock | 13,090 | 9,963 | 76.1% |
| Peter Lowe | 7,168 | 3,889 | 54.3% |
| Dandelion Sprout | 490 | 307 | 62.7% |
| EasyList | 53,261 | 9,272 | 17.4% |
| EasyPrivacy | 56,706 | 26,065 | 46.0% |
| uBO Ads | 1,765 | 1,721 | 97.5% |
| uBO Privacy | 1,467 | 1,375 | 93.7% |
| uBO Badware | 4,737 | 4,681 | 98.8% |
| uBO Quick Fixes | 172 | 161 | 93.6% |
| uBO Unbreak | 1,951 | 1,947 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **747,699** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 747,699 |
| **DNSZeroList.txt** (all sources, deduped) | **497,251** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **362,576** |

Deduplication removed 250,448 duplicate rule instances (33.5% of the raw total).
Dropping OISD Big removes a further 134,675 rules (27.1% of the full list).
