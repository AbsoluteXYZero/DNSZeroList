# Blocklist stats

_Generated 2026-11-26 06:05:28 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 195,049 | 93,025 | 47.7% |
| HaGeZi Normal | 184,283 | 90,424 | 49.1% |
| AdAway | 6,540 | 3,443 | 52.6% |
| OISD Big | 221,953 | 134,329 | 60.5% |
| Dan Pollock | 13,117 | 9,988 | 76.1% |
| Peter Lowe | 7,148 | 3,879 | 54.3% |
| Dandelion Sprout | 490 | 307 | 62.7% |
| EasyList | 53,777 | 9,295 | 17.3% |
| EasyPrivacy | 56,820 | 26,228 | 46.2% |
| uBO Ads | 1,765 | 1,721 | 97.5% |
| uBO Privacy | 1,467 | 1,375 | 93.7% |
| uBO Badware | 4,739 | 4,683 | 98.8% |
| uBO Quick Fixes | 106 | 95 | 89.6% |
| uBO Unbreak | 1,949 | 1,945 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **749,239** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 749,239 |
| **DNSZeroList.txt** (all sources, deduped) | **509,245** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **374,916** |

Deduplication removed 239,994 duplicate rule instances (32.0% of the raw total).
Dropping OISD Big removes a further 134,329 rules (26.4% of the full list).
