# Blocklist stats

_Generated 2026-08-25 00:44:19 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,458 | 75,178 | 42.4% |
| HaGeZi Normal | 188,418 | 85,237 | 45.2% |
| AdAway | 6,540 | 3,462 | 52.9% |
| OISD Big | 268,977 | 185,340 | 68.9% |
| Dan Pollock | 13,031 | 9,879 | 75.8% |
| Peter Lowe | 7,066 | 3,839 | 54.3% |
| Dandelion Sprout | 480 | 296 | 61.7% |
| EasyList | 54,247 | 9,202 | 17.0% |
| EasyPrivacy | 55,906 | 25,627 | 45.8% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,424 | 1,343 | 94.3% |
| uBO Badware | 4,183 | 4,136 | 98.9% |
| uBO Quick Fixes | 89 | 80 | 89.9% |
| uBO Unbreak | 1,935 | 1,931 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **781,562** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 781,562 |
| **DNSZeroList.txt** (all sources, deduped) | **537,372** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **352,032** |

Deduplication removed 244,190 duplicate rule instances (31.2% of the raw total).
Dropping OISD Big removes a further 185,340 rules (34.5% of the full list).
