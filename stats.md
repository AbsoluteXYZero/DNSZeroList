# Blocklist stats

_Generated 2026-09-02 02:07:17 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 179,300 | 75,022 | 41.8% |
| HaGeZi Normal | 190,371 | 85,462 | 44.9% |
| AdAway | 6,540 | 3,461 | 52.9% |
| OISD Big | 270,256 | 182,515 | 67.5% |
| Dan Pollock | 13,051 | 9,902 | 75.9% |
| Peter Lowe | 7,114 | 3,867 | 54.4% |
| Dandelion Sprout | 480 | 298 | 62.1% |
| EasyList | 55,944 | 9,225 | 16.5% |
| EasyPrivacy | 55,962 | 25,651 | 45.8% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,426 | 1,345 | 94.3% |
| uBO Badware | 4,223 | 4,176 | 98.9% |
| uBO Quick Fixes | 92 | 83 | 90.2% |
| uBO Unbreak | 1,936 | 1,932 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **788,503** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 788,503 |
| **DNSZeroList.txt** (all sources, deduped) | **536,424** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **353,909** |

Deduplication removed 252,079 duplicate rule instances (32.0% of the raw total).
Dropping OISD Big removes a further 182,515 rules (34.0% of the full list).
