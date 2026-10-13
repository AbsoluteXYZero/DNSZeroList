# Blocklist stats

_Generated 2026-10-13 04:42:02 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 184,348 | 80,280 | 43.5% |
| HaGeZi Normal | 157,755 | 62,718 | 39.8% |
| AdAway | 6,540 | 3,458 | 52.9% |
| OISD Big | 237,840 | 158,972 | 66.8% |
| Dan Pollock | 13,084 | 9,973 | 76.2% |
| Peter Lowe | 7,130 | 3,886 | 54.5% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 56,989 | 9,232 | 16.2% |
| EasyPrivacy | 56,276 | 26,025 | 46.2% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,450 | 1,368 | 94.3% |
| uBO Badware | 4,264 | 4,214 | 98.8% |
| uBO Quick Fixes | 160 | 151 | 94.4% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **730,070** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 730,070 |
| **DNSZeroList.txt** (all sources, deduped) | **493,092** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **334,120** |

Deduplication removed 236,978 duplicate rule instances (32.5% of the raw total).
Dropping OISD Big removes a further 158,972 rules (32.2% of the full list).
