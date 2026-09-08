# Blocklist stats

_Generated 2026-09-08 02:13:37 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,023 | 74,978 | 42.4% |
| HaGeZi Normal | 191,639 | 86,734 | 45.3% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 270,846 | 182,855 | 67.5% |
| Dan Pollock | 13,058 | 9,913 | 75.9% |
| Peter Lowe | 7,116 | 3,870 | 54.4% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 53,569 | 9,228 | 17.2% |
| EasyPrivacy | 55,990 | 25,663 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,432 | 1,349 | 94.2% |
| uBO Badware | 4,232 | 4,184 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,937 | 1,933 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **785,762** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 785,762 |
| **DNSZeroList.txt** (all sources, deduped) | **538,407** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **355,552** |

Deduplication removed 247,355 duplicate rule instances (31.5% of the raw total).
Dropping OISD Big removes a further 182,855 rules (34.0% of the full list).
