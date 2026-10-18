# Blocklist stats

_Generated 2026-10-18 15:07:43 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 186,155 | 79,643 | 42.8% |
| HaGeZi Normal | 166,141 | 68,035 | 41.0% |
| AdAway | 6,540 | 3,450 | 52.8% |
| OISD Big | 234,278 | 154,495 | 65.9% |
| Dan Pollock | 13,085 | 9,970 | 76.2% |
| Peter Lowe | 7,170 | 3,901 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 58,861 | 9,242 | 15.7% |
| EasyPrivacy | 56,309 | 26,033 | 46.2% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,451 | 1,366 | 94.1% |
| uBO Badware | 4,269 | 4,219 | 98.8% |
| uBO Quick Fixes | 211 | 200 | 94.8% |
| uBO Unbreak | 1,944 | 1,940 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **738,706** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 738,706 |
| **DNSZeroList.txt** (all sources, deduped) | **496,372** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **341,877** |

Deduplication removed 242,334 duplicate rule instances (32.8% of the raw total).
Dropping OISD Big removes a further 154,495 rules (31.1% of the full list).
