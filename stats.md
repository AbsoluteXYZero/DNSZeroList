# Blocklist stats

_Generated 2026-09-08 15:42:28 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,252 | 74,982 | 42.3% |
| HaGeZi Normal | 191,781 | 89,185 | 46.5% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 270,105 | 184,600 | 68.3% |
| Dan Pollock | 13,058 | 9,913 | 75.9% |
| Peter Lowe | 7,116 | 3,870 | 54.4% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 53,762 | 9,213 | 17.1% |
| EasyPrivacy | 55,992 | 25,664 | 45.8% |
| uBO Ads | 1,770 | 1,727 | 97.6% |
| uBO Privacy | 1,432 | 1,350 | 94.3% |
| uBO Badware | 4,233 | 4,185 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,937 | 1,933 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **785,588** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 785,588 |
| **DNSZeroList.txt** (all sources, deduped) | **540,234** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **355,634** |

Deduplication removed 245,354 duplicate rule instances (31.2% of the raw total).
Dropping OISD Big removes a further 184,600 rules (34.2% of the full list).
