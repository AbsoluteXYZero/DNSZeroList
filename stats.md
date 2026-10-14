# Blocklist stats

_Generated 2026-10-14 02:50:42 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 184,287 | 80,037 | 43.4% |
| HaGeZi Normal | 158,809 | 63,345 | 39.9% |
| AdAway | 6,540 | 3,456 | 52.8% |
| OISD Big | 237,758 | 158,645 | 66.7% |
| Dan Pollock | 13,084 | 9,973 | 76.2% |
| Peter Lowe | 7,130 | 3,886 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 57,324 | 9,239 | 16.1% |
| EasyPrivacy | 56,280 | 26,025 | 46.2% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,450 | 1,366 | 94.2% |
| uBO Badware | 4,266 | 4,216 | 98.8% |
| uBO Quick Fixes | 162 | 151 | 93.2% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **731,324** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 731,324 |
| **DNSZeroList.txt** (all sources, deduped) | **493,609** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **334,964** |

Deduplication removed 237,715 duplicate rule instances (32.5% of the raw total).
Dropping OISD Big removes a further 158,645 rules (32.1% of the full list).
