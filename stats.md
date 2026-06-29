# Blocklist stats

_Generated 2026-06-29 02:40:27 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 159,988 | 56,886 | 35.6% |
| HaGeZi Normal | 161,059 | 57,184 | 35.5% |
| AdAway | 6,540 | 3,522 | 53.9% |
| OISD Big | 484,582 | 398,388 | 82.2% |
| Dan Pollock | 12,891 | 9,613 | 74.6% |
| Peter Lowe | 7,064 | 3,852 | 54.5% |
| Dandelion Sprout | 480 | 282 | 58.8% |
| EasyList | 59,004 | 9,358 | 15.9% |
| EasyPrivacy | 55,438 | 26,680 | 48.1% |
| uBO Ads | 1,787 | 1,737 | 97.2% |
| uBO Privacy | 1,368 | 1,287 | 94.1% |
| uBO Badware | 4,149 | 4,104 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,925 | 1,921 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **956,404** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 956,404 |
| **DNSZeroList.txt** (all sources, deduped) | **705,511** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **307,123** |

Deduplication removed 250,893 duplicate rule instances (26.2% of the raw total).
Dropping OISD Big removes a further 398,388 rules (56.5% of the full list).
