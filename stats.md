# Blocklist stats

_Generated 2026-08-03 01:58:46 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 162,352 | 56,742 | 34.9% |
| HaGeZi Normal | 181,396 | 81,959 | 45.2% |
| AdAway | 6,540 | 3,466 | 53.0% |
| OISD Big | 430,096 | 349,469 | 81.3% |
| Dan Pollock | 12,973 | 9,825 | 75.7% |
| Peter Lowe | 7,058 | 3,831 | 54.3% |
| Dandelion Sprout | 480 | 292 | 60.8% |
| EasyList | 60,977 | 9,342 | 15.3% |
| EasyPrivacy | 55,627 | 26,765 | 48.1% |
| uBO Ads | 1,768 | 1,724 | 97.5% |
| uBO Privacy | 1,391 | 1,311 | 94.2% |
| uBO Badware | 4,271 | 4,225 | 98.9% |
| uBO Quick Fixes | 92 | 83 | 90.2% |
| uBO Unbreak | 1,932 | 1,927 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **926,990** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 926,990 |
| **DNSZeroList.txt** (all sources, deduped) | **684,400** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **334,931** |

Deduplication removed 242,590 duplicate rule instances (26.2% of the raw total).
Dropping OISD Big removes a further 349,469 rules (51.1% of the full list).
