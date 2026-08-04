# Blocklist stats

_Generated 2026-08-04 01:44:37 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 162,609 | 56,728 | 34.9% |
| HaGeZi Normal | 182,514 | 82,466 | 45.2% |
| AdAway | 6,540 | 3,465 | 53.0% |
| OISD Big | 433,102 | 351,750 | 81.2% |
| Dan Pollock | 12,978 | 9,831 | 75.8% |
| Peter Lowe | 7,066 | 3,837 | 54.3% |
| Dandelion Sprout | 480 | 292 | 60.8% |
| EasyList | 61,213 | 9,329 | 15.2% |
| EasyPrivacy | 55,635 | 26,768 | 48.1% |
| uBO Ads | 1,768 | 1,724 | 97.5% |
| uBO Privacy | 1,391 | 1,311 | 94.2% |
| uBO Badware | 4,271 | 4,225 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,932 | 1,927 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **931,629** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 931,629 |
| **DNSZeroList.txt** (all sources, deduped) | **687,420** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **335,670** |

Deduplication removed 244,209 duplicate rule instances (26.2% of the raw total).
Dropping OISD Big removes a further 351,750 rules (51.2% of the full list).
