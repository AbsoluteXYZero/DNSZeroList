# Blocklist stats

_Generated 2026-09-21 02:30:47 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 181,388 | 74,694 | 41.2% |
| HaGeZi Normal | 199,254 | 95,621 | 48.0% |
| AdAway | 6,540 | 3,459 | 52.9% |
| OISD Big | 246,510 | 166,413 | 67.5% |
| Dan Pollock | 13,082 | 9,932 | 75.9% |
| Peter Lowe | 7,126 | 3,877 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 58,116 | 9,218 | 15.9% |
| EasyPrivacy | 56,103 | 25,703 | 45.8% |
| uBO Ads | 1,775 | 1,731 | 97.5% |
| uBO Privacy | 1,437 | 1,357 | 94.4% |
| uBO Badware | 4,225 | 4,175 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,939 | 1,935 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **778,105** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 778,105 |
| **DNSZeroList.txt** (all sources, deduped) | **531,446** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **365,033** |

Deduplication removed 246,659 duplicate rule instances (31.7% of the raw total).
Dropping OISD Big removes a further 166,413 rules (31.3% of the full list).
