# Blocklist stats

_Generated 2026-06-29 15:32:40 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 153,322 | 56,997 | 37.2% |
| HaGeZi Normal | 166,331 | 63,232 | 38.0% |
| AdAway | 6,540 | 3,528 | 53.9% |
| OISD Big | 488,966 | 402,143 | 82.2% |
| Dan Pollock | 12,891 | 9,606 | 74.5% |
| Peter Lowe | 7,064 | 3,845 | 54.4% |
| Dandelion Sprout | 480 | 280 | 58.3% |
| EasyList | 52,118 | 9,285 | 17.8% |
| EasyPrivacy | 55,440 | 26,665 | 48.1% |
| uBO Ads | 1,787 | 1,737 | 97.2% |
| uBO Privacy | 1,371 | 1,289 | 94.0% |
| uBO Badware | 4,149 | 4,104 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,925 | 1,921 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **952,513** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 952,513 |
| **DNSZeroList.txt** (all sources, deduped) | **714,626** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **312,483** |

Deduplication removed 237,887 duplicate rule instances (25.0% of the raw total).
Dropping OISD Big removes a further 402,143 rules (56.3% of the full list).
