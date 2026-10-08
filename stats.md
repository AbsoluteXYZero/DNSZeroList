# Blocklist stats

_Generated 2026-10-08 03:42:33 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 179,333 | 77,101 | 43.0% |
| HaGeZi Normal | 161,748 | 62,452 | 38.6% |
| AdAway | 6,540 | 3,456 | 52.8% |
| OISD Big | 240,077 | 159,029 | 66.2% |
| Dan Pollock | 13,083 | 9,979 | 76.3% |
| Peter Lowe | 7,136 | 3,887 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 55,555 | 9,230 | 16.6% |
| EasyPrivacy | 56,240 | 25,751 | 45.8% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,443 | 1,361 | 94.3% |
| uBO Badware | 4,262 | 4,211 | 98.8% |
| uBO Quick Fixes | 154 | 145 | 94.2% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **729,805** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 729,805 |
| **DNSZeroList.txt** (all sources, deduped) | **489,147** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **330,118** |

Deduplication removed 240,658 duplicate rule instances (33.0% of the raw total).
Dropping OISD Big removes a further 159,029 rules (32.5% of the full list).
