# Blocklist stats

_Generated 2026-06-28 13:19:38 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 159,820 | 56,826 | 35.6% |
| HaGeZi Normal | 160,626 | 57,515 | 35.8% |
| AdAway | 6,540 | 3,534 | 54.0% |
| OISD Big | 335,528 | 249,931 | 74.5% |
| Dan Pollock | 12,891 | 9,658 | 74.9% |
| Peter Lowe | 7,046 | 3,833 | 54.4% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 58,837 | 9,354 | 15.9% |
| EasyPrivacy | 55,435 | 26,662 | 48.1% |
| uBO Ads | 1,787 | 1,737 | 97.2% |
| uBO Privacy | 1,365 | 1,284 | 94.1% |
| uBO Badware | 4,149 | 4,104 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,925 | 1,921 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **806,558** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 806,558 |
| **DNSZeroList.txt** (all sources, deduped) | **556,779** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **306,848** |

Deduplication removed 249,779 duplicate rule instances (31.0% of the raw total).
Dropping OISD Big removes a further 249,931 rules (44.9% of the full list).
