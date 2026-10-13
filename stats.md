# Blocklist stats

_Generated 2026-10-13 18:40:59 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 184,554 | 80,134 | 43.4% |
| HaGeZi Normal | 158,809 | 63,331 | 39.9% |
| AdAway | 6,540 | 3,456 | 52.8% |
| OISD Big | 238,000 | 158,975 | 66.8% |
| Dan Pollock | 13,084 | 9,973 | 76.2% |
| Peter Lowe | 7,130 | 3,886 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 57,209 | 9,236 | 16.1% |
| EasyPrivacy | 56,280 | 26,025 | 46.2% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,450 | 1,366 | 94.2% |
| uBO Badware | 4,266 | 4,216 | 98.8% |
| uBO Quick Fixes | 162 | 153 | 94.4% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **731,718** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 731,718 |
| **DNSZeroList.txt** (all sources, deduped) | **493,918** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **334,943** |

Deduplication removed 237,800 duplicate rule instances (32.5% of the raw total).
Dropping OISD Big removes a further 158,975 rules (32.2% of the full list).
