# Blocklist stats

_Generated 2026-08-21 12:28:30 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,784 | 75,277 | 42.3% |
| HaGeZi Normal | 187,244 | 84,882 | 45.3% |
| AdAway | 6,540 | 3,460 | 52.9% |
| OISD Big | 268,505 | 185,425 | 69.1% |
| Dan Pollock | 13,022 | 9,869 | 75.8% |
| Peter Lowe | 7,064 | 3,838 | 54.3% |
| Dandelion Sprout | 480 | 295 | 61.5% |
| EasyList | 54,471 | 9,334 | 17.1% |
| EasyPrivacy | 55,871 | 25,617 | 45.9% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,409 | 1,329 | 94.3% |
| uBO Badware | 4,173 | 4,126 | 98.9% |
| uBO Quick Fixes | 89 | 80 | 89.9% |
| uBO Unbreak | 1,935 | 1,930 | 99.7% |
| uBO Resource Abuse | 38 | 36 | 94.7% |
| **Sum (before dedup)** | **780,395** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 780,395 |
| **DNSZeroList.txt** (all sources, deduped) | **537,144** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **351,719** |

Deduplication removed 243,251 duplicate rule instances (31.2% of the raw total).
Dropping OISD Big removes a further 185,425 rules (34.5% of the full list).
