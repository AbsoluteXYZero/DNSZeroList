# Blocklist stats

_Generated 2026-10-09 03:48:07 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 179,650 | 77,105 | 42.9% |
| HaGeZi Normal | 158,505 | 62,251 | 39.3% |
| AdAway | 6,540 | 3,456 | 52.8% |
| OISD Big | 240,080 | 160,336 | 66.8% |
| Dan Pollock | 13,083 | 9,979 | 76.3% |
| Peter Lowe | 7,136 | 3,887 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 55,865 | 9,242 | 16.5% |
| EasyPrivacy | 56,256 | 25,762 | 45.8% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,444 | 1,362 | 94.3% |
| uBO Badware | 4,262 | 4,211 | 98.8% |
| uBO Quick Fixes | 156 | 147 | 94.2% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **727,211** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 727,211 |
| **DNSZeroList.txt** (all sources, deduped) | **489,062** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **328,726** |

Deduplication removed 238,149 duplicate rule instances (32.7% of the raw total).
Dropping OISD Big removes a further 160,336 rules (32.8% of the full list).
