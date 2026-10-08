# Blocklist stats

_Generated 2026-10-08 18:12:35 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 179,496 | 77,112 | 43.0% |
| HaGeZi Normal | 158,505 | 62,235 | 39.3% |
| AdAway | 6,540 | 3,456 | 52.8% |
| OISD Big | 240,374 | 160,791 | 66.9% |
| Dan Pollock | 13,083 | 9,979 | 76.3% |
| Peter Lowe | 7,136 | 3,887 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 55,757 | 9,272 | 16.6% |
| EasyPrivacy | 56,245 | 25,754 | 45.8% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,444 | 1,362 | 94.3% |
| uBO Badware | 4,262 | 4,211 | 98.8% |
| uBO Quick Fixes | 156 | 147 | 94.2% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **727,232** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 727,232 |
| **DNSZeroList.txt** (all sources, deduped) | **489,396** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **328,605** |

Deduplication removed 237,836 duplicate rule instances (32.7% of the raw total).
Dropping OISD Big removes a further 160,791 rules (32.9% of the full list).
