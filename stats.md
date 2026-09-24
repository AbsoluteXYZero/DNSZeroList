# Blocklist stats

_Generated 2026-09-24 16:11:19 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 182,567 | 75,446 | 41.3% |
| HaGeZi Normal | 164,176 | 80,430 | 49.0% |
| AdAway | 6,540 | 3,447 | 52.7% |
| OISD Big | 248,376 | 171,317 | 69.0% |
| Dan Pollock | 13,082 | 9,949 | 76.1% |
| Peter Lowe | 7,140 | 3,957 | 55.4% |
| Dandelion Sprout | 480 | 310 | 64.6% |
| EasyList | 59,215 | 9,231 | 15.6% |
| EasyPrivacy | 56,156 | 25,810 | 46.0% |
| uBO Ads | 1,776 | 1,732 | 97.5% |
| uBO Privacy | 1,437 | 1,360 | 94.6% |
| uBO Badware | 4,226 | 4,176 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 37 | 100.0% |
| **Sum (before dedup)** | **747,241** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 747,241 |
| **DNSZeroList.txt** (all sources, deduped) | **518,734** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **347,417** |

Deduplication removed 228,507 duplicate rule instances (30.6% of the raw total).
Dropping OISD Big removes a further 171,317 rules (33.0% of the full list).
