# Blocklist stats

_Generated 2026-09-17 15:55:50 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 180,153 | 74,767 | 41.5% |
| HaGeZi Normal | 197,602 | 94,721 | 47.9% |
| AdAway | 6,540 | 3,458 | 52.9% |
| OISD Big | 246,598 | 166,921 | 67.7% |
| Dan Pollock | 13,075 | 9,924 | 75.9% |
| Peter Lowe | 7,152 | 3,891 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 56,951 | 9,235 | 16.2% |
| EasyPrivacy | 56,064 | 25,692 | 45.8% |
| uBO Ads | 1,763 | 1,719 | 97.5% |
| uBO Privacy | 1,435 | 1,354 | 94.4% |
| uBO Badware | 4,133 | 4,084 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,939 | 1,935 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **774,015** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 774,015 |
| **DNSZeroList.txt** (all sources, deduped) | **529,897** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **362,976** |

Deduplication removed 244,118 duplicate rule instances (31.5% of the raw total).
Dropping OISD Big removes a further 166,921 rules (31.5% of the full list).
