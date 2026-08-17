# Blocklist stats

_Generated 2026-08-17 12:24:49 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 155,429 | 56,983 | 36.7% |
| HaGeZi Normal | 183,588 | 83,657 | 45.6% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 269,446 | 186,675 | 69.3% |
| Dan Pollock | 13,009 | 9,855 | 75.8% |
| Peter Lowe | 7,074 | 3,842 | 54.3% |
| Dandelion Sprout | 480 | 294 | 61.3% |
| EasyList | 53,352 | 9,313 | 17.5% |
| EasyPrivacy | 55,840 | 26,766 | 47.9% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,407 | 1,328 | 94.4% |
| uBO Badware | 4,167 | 4,123 | 98.9% |
| uBO Quick Fixes | 90 | 81 | 90.0% |
| uBO Unbreak | 1,934 | 1,929 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **754,163** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 754,163 |
| **DNSZeroList.txt** (all sources, deduped) | **516,342** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **329,667** |

Deduplication removed 237,821 duplicate rule instances (31.5% of the raw total).
Dropping OISD Big removes a further 186,675 rules (36.2% of the full list).
