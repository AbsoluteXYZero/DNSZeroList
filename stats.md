# Blocklist stats

_Generated 2026-09-26 15:26:05 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 183,208 | 75,423 | 41.2% |
| HaGeZi Normal | 164,641 | 80,955 | 49.2% |
| AdAway | 6,540 | 3,449 | 52.7% |
| OISD Big | 243,686 | 167,753 | 68.8% |
| Dan Pollock | 13,082 | 9,945 | 76.0% |
| Peter Lowe | 7,132 | 3,952 | 55.4% |
| Dandelion Sprout | 480 | 309 | 64.4% |
| EasyList | 59,824 | 9,238 | 15.4% |
| EasyPrivacy | 56,169 | 25,815 | 46.0% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,439 | 1,362 | 94.6% |
| uBO Badware | 4,227 | 4,177 | 98.8% |
| uBO Quick Fixes | 136 | 127 | 93.4% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 37 | 100.0% |
| **Sum (before dedup)** | **744,317** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 744,317 |
| **DNSZeroList.txt** (all sources, deduped) | **516,124** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **348,371** |

Deduplication removed 228,193 duplicate rule instances (30.7% of the raw total).
Dropping OISD Big removes a further 167,753 rules (32.5% of the full list).
