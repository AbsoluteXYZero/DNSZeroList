# Blocklist stats

_Generated 2026-08-27 21:28:22 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 178,285 | 75,061 | 42.1% |
| HaGeZi Normal | 190,021 | 85,918 | 45.2% |
| AdAway | 6,540 | 3,461 | 52.9% |
| OISD Big | 266,940 | 182,943 | 68.5% |
| Dan Pollock | 13,038 | 9,886 | 75.8% |
| Peter Lowe | 7,072 | 3,842 | 54.3% |
| Dandelion Sprout | 480 | 296 | 61.7% |
| EasyList | 55,032 | 9,222 | 16.8% |
| EasyPrivacy | 55,928 | 25,635 | 45.8% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,425 | 1,344 | 94.3% |
| uBO Badware | 4,196 | 4,149 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,936 | 1,932 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **782,792** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 782,792 |
| **DNSZeroList.txt** (all sources, deduped) | **536,412** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **353,469** |

Deduplication removed 246,380 duplicate rule instances (31.5% of the raw total).
Dropping OISD Big removes a further 182,943 rules (34.1% of the full list).
