# Blocklist stats

_Generated 2026-10-11 03:03:58 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 181,970 | 78,632 | 43.2% |
| HaGeZi Normal | 159,965 | 62,692 | 39.2% |
| AdAway | 6,540 | 3,456 | 52.8% |
| OISD Big | 237,581 | 159,248 | 67.0% |
| Dan Pollock | 13,083 | 9,972 | 76.2% |
| Peter Lowe | 7,128 | 3,885 | 54.5% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 56,397 | 9,238 | 16.4% |
| EasyPrivacy | 56,268 | 26,004 | 46.2% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,445 | 1,362 | 94.3% |
| uBO Badware | 4,264 | 4,213 | 98.8% |
| uBO Quick Fixes | 160 | 151 | 94.4% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **729,035** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 729,035 |
| **DNSZeroList.txt** (all sources, deduped) | **490,887** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **331,639** |

Deduplication removed 238,148 duplicate rule instances (32.7% of the raw total).
Dropping OISD Big removes a further 159,248 rules (32.4% of the full list).
