# Blocklist stats

_Generated 2026-08-24 00:44:48 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 178,168 | 75,196 | 42.2% |
| HaGeZi Normal | 188,380 | 84,995 | 45.1% |
| AdAway | 6,540 | 3,462 | 52.9% |
| OISD Big | 268,171 | 184,757 | 68.9% |
| Dan Pollock | 13,030 | 9,878 | 75.8% |
| Peter Lowe | 7,066 | 3,839 | 54.3% |
| Dandelion Sprout | 480 | 296 | 61.7% |
| EasyList | 55,118 | 9,344 | 17.0% |
| EasyPrivacy | 55,885 | 25,616 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,424 | 1,343 | 94.3% |
| uBO Badware | 4,181 | 4,134 | 98.9% |
| uBO Quick Fixes | 89 | 80 | 89.9% |
| uBO Unbreak | 1,935 | 1,931 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **782,274** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 782,274 |
| **DNSZeroList.txt** (all sources, deduped) | **537,234** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **352,477** |

Deduplication removed 245,040 duplicate rule instances (31.3% of the raw total).
Dropping OISD Big removes a further 184,757 rules (34.4% of the full list).
