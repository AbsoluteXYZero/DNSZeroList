# Blocklist stats

_Generated 2026-09-24 02:22:53 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 182,392 | 75,562 | 41.4% |
| HaGeZi Normal | 162,636 | 80,177 | 49.3% |
| AdAway | 6,540 | 3,454 | 52.8% |
| OISD Big | 248,431 | 172,318 | 69.4% |
| Dan Pollock | 13,082 | 9,938 | 76.0% |
| Peter Lowe | 7,140 | 3,955 | 55.4% |
| Dandelion Sprout | 480 | 311 | 64.8% |
| EasyList | 59,046 | 9,223 | 15.6% |
| EasyPrivacy | 56,154 | 25,806 | 46.0% |
| uBO Ads | 1,776 | 1,732 | 97.5% |
| uBO Privacy | 1,437 | 1,360 | 94.6% |
| uBO Badware | 4,226 | 4,176 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 37 | 100.0% |
| **Sum (before dedup)** | **745,410** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 745,410 |
| **DNSZeroList.txt** (all sources, deduped) | **518,440** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **346,122** |

Deduplication removed 226,970 duplicate rule instances (30.4% of the raw total).
Dropping OISD Big removes a further 172,318 rules (33.2% of the full list).
