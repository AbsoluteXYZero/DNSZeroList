# Blocklist stats

_Generated 2026-08-02 01:55:52 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 162,095 | 56,725 | 35.0% |
| HaGeZi Normal | 181,066 | 82,035 | 45.3% |
| AdAway | 6,540 | 3,465 | 53.0% |
| OISD Big | 429,948 | 349,837 | 81.4% |
| Dan Pollock | 12,973 | 9,825 | 75.7% |
| Peter Lowe | 7,058 | 3,831 | 54.3% |
| Dandelion Sprout | 480 | 292 | 60.8% |
| EasyList | 60,724 | 9,339 | 15.4% |
| EasyPrivacy | 55,627 | 26,765 | 48.1% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,391 | 1,311 | 94.2% |
| uBO Badware | 4,268 | 4,222 | 98.9% |
| uBO Quick Fixes | 92 | 83 | 90.2% |
| uBO Unbreak | 1,932 | 1,927 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **926,001** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 926,001 |
| **DNSZeroList.txt** (all sources, deduped) | **684,149** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **334,312** |

Deduplication removed 241,852 duplicate rule instances (26.1% of the raw total).
Dropping OISD Big removes a further 349,837 rules (51.1% of the full list).
