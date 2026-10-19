# Blocklist stats

_Generated 2026-10-19 18:00:18 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 188,420 | 81,530 | 43.3% |
| HaGeZi Normal | 167,139 | 68,557 | 41.0% |
| AdAway | 6,540 | 3,450 | 52.8% |
| OISD Big | 234,571 | 154,455 | 65.8% |
| Dan Pollock | 13,085 | 9,971 | 76.2% |
| Peter Lowe | 7,170 | 3,901 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 59,229 | 9,263 | 15.6% |
| EasyPrivacy | 56,328 | 26,078 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,451 | 1,366 | 94.1% |
| uBO Badware | 4,283 | 4,233 | 98.8% |
| uBO Quick Fixes | 211 | 200 | 94.8% |
| uBO Unbreak | 1,944 | 1,940 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **742,663** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 742,663 |
| **DNSZeroList.txt** (all sources, deduped) | **499,269** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **344,814** |

Deduplication removed 243,394 duplicate rule instances (32.8% of the raw total).
Dropping OISD Big removes a further 154,455 rules (30.9% of the full list).
