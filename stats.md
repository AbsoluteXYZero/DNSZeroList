# Blocklist stats

_Generated 2026-09-01 02:46:31 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 178,960 | 75,011 | 41.9% |
| HaGeZi Normal | 191,539 | 86,663 | 45.2% |
| AdAway | 6,540 | 3,461 | 52.9% |
| OISD Big | 270,478 | 186,105 | 68.8% |
| Dan Pollock | 13,049 | 9,897 | 75.8% |
| Peter Lowe | 7,114 | 3,868 | 54.4% |
| Dandelion Sprout | 480 | 298 | 62.1% |
| EasyList | 55,631 | 9,233 | 16.6% |
| EasyPrivacy | 55,951 | 25,642 | 45.8% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,425 | 1,344 | 94.3% |
| uBO Badware | 4,215 | 4,168 | 98.9% |
| uBO Quick Fixes | 92 | 83 | 90.2% |
| uBO Unbreak | 1,936 | 1,932 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **789,218** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 789,218 |
| **DNSZeroList.txt** (all sources, deduped) | **541,307** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **355,202** |

Deduplication removed 247,911 duplicate rule instances (31.4% of the raw total).
Dropping OISD Big removes a further 186,105 rules (34.4% of the full list).
