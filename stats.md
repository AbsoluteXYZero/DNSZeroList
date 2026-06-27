# Blocklist stats

_Generated 2026-06-27 13:14:07 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 159,515 | 56,813 | 35.6% |
| HaGeZi Normal | 160,626 | 57,517 | 35.8% |
| AdAway | 6,540 | 3,534 | 54.0% |
| OISD Big | 335,510 | 249,913 | 74.5% |
| Dan Pollock | 12,891 | 9,658 | 74.9% |
| Peter Lowe | 7,046 | 3,833 | 54.4% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 58,540 | 9,349 | 16.0% |
| EasyPrivacy | 55,426 | 26,656 | 48.1% |
| uBO Ads | 1,787 | 1,737 | 97.2% |
| uBO Privacy | 1,364 | 1,283 | 94.1% |
| uBO Badware | 4,149 | 4,104 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,925 | 1,921 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **805,926** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 805,926 |
| **DNSZeroList.txt** (all sources, deduped) | **556,443** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **306,530** |

Deduplication removed 249,483 duplicate rule instances (31.0% of the raw total).
Dropping OISD Big removes a further 249,913 rules (44.9% of the full list).
