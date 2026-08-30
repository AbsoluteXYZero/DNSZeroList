# Blocklist stats

_Generated 2026-08-30 15:45:25 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 179,141 | 75,034 | 41.9% |
| HaGeZi Normal | 191,135 | 86,200 | 45.1% |
| AdAway | 6,540 | 3,461 | 52.9% |
| OISD Big | 270,188 | 185,750 | 68.7% |
| Dan Pollock | 13,045 | 9,893 | 75.8% |
| Peter Lowe | 7,110 | 3,865 | 54.4% |
| Dandelion Sprout | 480 | 298 | 62.1% |
| EasyList | 55,828 | 9,219 | 16.5% |
| EasyPrivacy | 55,944 | 25,640 | 45.8% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,425 | 1,344 | 94.3% |
| uBO Badware | 4,208 | 4,161 | 98.9% |
| uBO Quick Fixes | 92 | 83 | 90.2% |
| uBO Unbreak | 1,936 | 1,932 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **788,880** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 788,880 |
| **DNSZeroList.txt** (all sources, deduped) | **540,441** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **354,691** |

Deduplication removed 248,439 duplicate rule instances (31.5% of the raw total).
Dropping OISD Big removes a further 185,750 rules (34.4% of the full list).
