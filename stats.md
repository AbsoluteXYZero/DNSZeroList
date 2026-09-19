# Blocklist stats

_Generated 2026-09-19 15:04:34 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 180,864 | 74,688 | 41.3% |
| HaGeZi Normal | 199,411 | 95,730 | 48.0% |
| AdAway | 6,540 | 3,458 | 52.9% |
| OISD Big | 246,298 | 166,187 | 67.5% |
| Dan Pollock | 13,082 | 9,931 | 75.9% |
| Peter Lowe | 7,124 | 3,876 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 57,619 | 9,228 | 16.0% |
| EasyPrivacy | 56,095 | 25,709 | 45.8% |
| uBO Ads | 1,763 | 1,719 | 97.5% |
| uBO Privacy | 1,437 | 1,356 | 94.4% |
| uBO Badware | 4,142 | 4,092 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,939 | 1,935 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **776,924** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 776,924 |
| **DNSZeroList.txt** (all sources, deduped) | **530,959** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **364,772** |

Deduplication removed 245,965 duplicate rule instances (31.7% of the raw total).
Dropping OISD Big removes a further 166,187 rules (31.3% of the full list).
