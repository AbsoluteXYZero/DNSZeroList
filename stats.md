# Blocklist stats

_Generated 2026-09-27 16:04:51 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 183,519 | 75,436 | 41.1% |
| HaGeZi Normal | 164,796 | 81,041 | 49.2% |
| AdAway | 6,540 | 3,451 | 52.8% |
| OISD Big | 243,731 | 167,646 | 68.8% |
| Dan Pollock | 13,082 | 9,945 | 76.0% |
| Peter Lowe | 7,134 | 3,953 | 55.4% |
| Dandelion Sprout | 480 | 309 | 64.4% |
| EasyList | 60,126 | 9,245 | 15.4% |
| EasyPrivacy | 56,174 | 25,817 | 46.0% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,442 | 1,365 | 94.7% |
| uBO Badware | 4,236 | 4,186 | 98.8% |
| uBO Quick Fixes | 142 | 133 | 93.7% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 37 | 100.0% |
| **Sum (before dedup)** | **745,155** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 745,155 |
| **DNSZeroList.txt** (all sources, deduped) | **516,436** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **348,790** |

Deduplication removed 228,719 duplicate rule instances (30.7% of the raw total).
Dropping OISD Big removes a further 167,646 rules (32.5% of the full list).
