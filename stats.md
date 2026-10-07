# Blocklist stats

_Generated 2026-10-07 03:27:50 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 179,035 | 77,143 | 43.1% |
| HaGeZi Normal | 161,287 | 62,016 | 38.5% |
| AdAway | 6,540 | 3,456 | 52.8% |
| OISD Big | 240,407 | 159,503 | 66.3% |
| Dan Pollock | 13,083 | 9,980 | 76.3% |
| Peter Lowe | 7,136 | 3,887 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 55,276 | 9,224 | 16.7% |
| EasyPrivacy | 56,233 | 25,748 | 45.8% |
| uBO Ads | 1,777 | 1,734 | 97.6% |
| uBO Privacy | 1,445 | 1,363 | 94.3% |
| uBO Badware | 4,261 | 4,210 | 98.8% |
| uBO Quick Fixes | 152 | 143 | 94.1% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **729,089** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 729,089 |
| **DNSZeroList.txt** (all sources, deduped) | **488,901** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **329,398** |

Deduplication removed 240,188 duplicate rule instances (32.9% of the raw total).
Dropping OISD Big removes a further 159,503 rules (32.6% of the full list).
