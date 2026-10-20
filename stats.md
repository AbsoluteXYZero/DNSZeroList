# Blocklist stats

_Generated 2026-10-20 02:44:43 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 188,560 | 81,408 | 43.2% |
| HaGeZi Normal | 167,139 | 68,556 | 41.0% |
| AdAway | 6,540 | 3,450 | 52.8% |
| OISD Big | 235,043 | 154,669 | 65.8% |
| Dan Pollock | 13,085 | 9,971 | 76.2% |
| Peter Lowe | 7,172 | 3,903 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 59,349 | 9,247 | 15.6% |
| EasyPrivacy | 56,329 | 26,077 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,451 | 1,366 | 94.1% |
| uBO Badware | 4,283 | 4,233 | 98.8% |
| uBO Quick Fixes | 211 | 200 | 94.8% |
| uBO Unbreak | 1,944 | 1,940 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **743,398** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 743,398 |
| **DNSZeroList.txt** (all sources, deduped) | **499,607** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **344,938** |

Deduplication removed 243,791 duplicate rule instances (32.8% of the raw total).
Dropping OISD Big removes a further 154,669 rules (31.0% of the full list).
