# Blocklist stats

_Generated 2026-09-02 15:40:45 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 179,496 | 75,002 | 41.8% |
| HaGeZi Normal | 190,507 | 85,455 | 44.9% |
| AdAway | 6,540 | 3,461 | 52.9% |
| OISD Big | 270,288 | 182,710 | 67.6% |
| Dan Pollock | 13,051 | 9,902 | 75.9% |
| Peter Lowe | 7,118 | 3,869 | 54.4% |
| Dandelion Sprout | 480 | 298 | 62.1% |
| EasyList | 56,121 | 9,206 | 16.4% |
| EasyPrivacy | 55,966 | 25,657 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,427 | 1,346 | 94.3% |
| uBO Badware | 4,224 | 4,177 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,936 | 1,932 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **789,052** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 789,052 |
| **DNSZeroList.txt** (all sources, deduped) | **536,739** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **354,029** |

Deduplication removed 252,313 duplicate rule instances (32.0% of the raw total).
Dropping OISD Big removes a further 182,710 rules (34.0% of the full list).
