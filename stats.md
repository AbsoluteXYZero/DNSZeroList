# Blocklist stats

_Generated 2026-09-01 15:48:10 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 179,168 | 74,996 | 41.9% |
| HaGeZi Normal | 190,425 | 85,613 | 45.0% |
| AdAway | 6,540 | 3,461 | 52.9% |
| OISD Big | 269,972 | 182,443 | 67.6% |
| Dan Pollock | 13,049 | 9,901 | 75.9% |
| Peter Lowe | 7,114 | 3,868 | 54.4% |
| Dandelion Sprout | 480 | 298 | 62.1% |
| EasyList | 55,809 | 9,213 | 16.5% |
| EasyPrivacy | 55,960 | 25,652 | 45.8% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,426 | 1,345 | 94.3% |
| uBO Badware | 4,223 | 4,176 | 98.9% |
| uBO Quick Fixes | 92 | 83 | 90.2% |
| uBO Unbreak | 1,936 | 1,932 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **788,002** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 788,002 |
| **DNSZeroList.txt** (all sources, deduped) | **536,332** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **353,889** |

Deduplication removed 251,670 duplicate rule instances (31.9% of the raw total).
Dropping OISD Big removes a further 182,443 rules (34.0% of the full list).
