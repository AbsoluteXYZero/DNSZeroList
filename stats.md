# Blocklist stats

_Generated 2026-09-11 15:34:31 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 178,340 | 74,950 | 42.0% |
| HaGeZi Normal | 180,051 | 78,324 | 43.5% |
| AdAway | 6,540 | 3,472 | 53.1% |
| OISD Big | 246,959 | 167,139 | 67.7% |
| Dan Pollock | 13,064 | 9,921 | 75.9% |
| Peter Lowe | 7,138 | 3,879 | 54.3% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 54,788 | 9,210 | 16.8% |
| EasyPrivacy | 56,007 | 25,672 | 45.8% |
| uBO Ads | 1,768 | 1,724 | 97.5% |
| uBO Privacy | 1,433 | 1,352 | 94.3% |
| uBO Badware | 4,239 | 4,189 | 98.8% |
| uBO Quick Fixes | 94 | 85 | 90.4% |
| uBO Unbreak | 1,935 | 1,931 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **752,873** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 752,873 |
| **DNSZeroList.txt** (all sources, deduped) | **512,501** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **345,362** |

Deduplication removed 240,372 duplicate rule instances (31.9% of the raw total).
Dropping OISD Big removes a further 167,139 rules (32.6% of the full list).
