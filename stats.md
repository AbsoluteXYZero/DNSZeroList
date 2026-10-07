# Blocklist stats

_Generated 2026-10-07 18:10:18 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 179,207 | 77,102 | 43.0% |
| HaGeZi Normal | 161,748 | 62,432 | 38.6% |
| AdAway | 6,540 | 3,456 | 52.8% |
| OISD Big | 240,400 | 159,335 | 66.3% |
| Dan Pollock | 13,083 | 9,979 | 76.3% |
| Peter Lowe | 7,136 | 3,888 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 55,442 | 9,232 | 16.7% |
| EasyPrivacy | 56,238 | 25,750 | 45.8% |
| uBO Ads | 1,777 | 1,734 | 97.6% |
| uBO Privacy | 1,445 | 1,363 | 94.3% |
| uBO Badware | 4,262 | 4,211 | 98.8% |
| uBO Quick Fixes | 154 | 145 | 94.2% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **729,890** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 729,890 |
| **DNSZeroList.txt** (all sources, deduped) | **489,339** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **330,004** |

Deduplication removed 240,551 duplicate rule instances (33.0% of the raw total).
Dropping OISD Big removes a further 159,335 rules (32.6% of the full list).
