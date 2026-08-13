# Blocklist stats

_Generated 2026-08-13 12:49:10 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 155,447 | 57,007 | 36.7% |
| HaGeZi Normal | 181,366 | 84,696 | 46.7% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 265,786 | 185,046 | 69.6% |
| Dan Pollock | 13,006 | 9,850 | 75.7% |
| Peter Lowe | 7,082 | 3,844 | 54.3% |
| Dandelion Sprout | 480 | 290 | 60.4% |
| EasyList | 53,609 | 9,316 | 17.4% |
| EasyPrivacy | 55,690 | 26,788 | 48.1% |
| uBO Ads | 1,769 | 1,725 | 97.5% |
| uBO Privacy | 1,404 | 1,325 | 94.4% |
| uBO Badware | 4,156 | 4,111 | 98.9% |
| uBO Quick Fixes | 90 | 81 | 90.0% |
| uBO Unbreak | 1,933 | 1,928 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **748,395** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 748,395 |
| **DNSZeroList.txt** (all sources, deduped) | **514,383** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **329,337** |

Deduplication removed 234,012 duplicate rule instances (31.3% of the raw total).
Dropping OISD Big removes a further 185,046 rules (36.0% of the full list).
