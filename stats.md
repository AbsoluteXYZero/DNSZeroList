# Blocklist stats

_Generated 2026-10-11 17:05:03 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 182,151 | 78,656 | 43.2% |
| HaGeZi Normal | 157,685 | 62,515 | 39.6% |
| AdAway | 6,540 | 3,458 | 52.9% |
| OISD Big | 237,471 | 159,073 | 67.0% |
| Dan Pollock | 13,083 | 9,972 | 76.2% |
| Peter Lowe | 7,128 | 3,885 | 54.5% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 56,560 | 9,235 | 16.3% |
| EasyPrivacy | 56,272 | 26,007 | 46.2% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,448 | 1,365 | 94.3% |
| uBO Badware | 4,264 | 4,214 | 98.8% |
| uBO Quick Fixes | 160 | 151 | 94.4% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **726,996** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 726,996 |
| **DNSZeroList.txt** (all sources, deduped) | **490,716** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **331,643** |

Deduplication removed 236,280 duplicate rule instances (32.5% of the raw total).
Dropping OISD Big removes a further 159,073 rules (32.4% of the full list).
