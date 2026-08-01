# Blocklist stats

_Generated 2026-08-01 12:59:21 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 161,962 | 56,709 | 35.0% |
| HaGeZi Normal | 181,161 | 82,293 | 45.4% |
| AdAway | 6,540 | 3,465 | 53.0% |
| OISD Big | 331,350 | 251,385 | 75.9% |
| Dan Pollock | 12,972 | 9,822 | 75.7% |
| Peter Lowe | 7,058 | 3,831 | 54.3% |
| Dandelion Sprout | 480 | 292 | 60.8% |
| EasyList | 60,582 | 9,325 | 15.4% |
| EasyPrivacy | 55,627 | 26,765 | 48.1% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,391 | 1,311 | 94.2% |
| uBO Badware | 4,268 | 4,222 | 98.9% |
| uBO Quick Fixes | 92 | 83 | 90.2% |
| uBO Unbreak | 1,932 | 1,927 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **827,222** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 827,222 |
| **DNSZeroList.txt** (all sources, deduped) | **585,558** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **334,173** |

Deduplication removed 241,664 duplicate rule instances (29.2% of the raw total).
Dropping OISD Big removes a further 251,385 rules (42.9% of the full list).
