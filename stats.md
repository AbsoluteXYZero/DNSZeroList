# Blocklist stats

_Generated 2026-11-03 04:41:56 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 188,166 | 85,497 | 45.4% |
| HaGeZi Normal | 176,107 | 73,899 | 42.0% |
| AdAway | 6,540 | 3,451 | 52.8% |
| OISD Big | 232,131 | 147,473 | 63.5% |
| Dan Pollock | 12,971 | 9,867 | 76.1% |
| Peter Lowe | 7,158 | 3,898 | 54.5% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 52,560 | 9,234 | 17.6% |
| EasyPrivacy | 56,423 | 26,152 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,460 | 1,373 | 94.0% |
| uBO Badware | 4,719 | 4,663 | 98.8% |
| uBO Quick Fixes | 168 | 157 | 93.5% |
| uBO Unbreak | 1,945 | 1,941 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **742,640** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 742,640 |
| **DNSZeroList.txt** (all sources, deduped) | **499,122** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **351,649** |

Deduplication removed 243,518 duplicate rule instances (32.8% of the raw total).
Dropping OISD Big removes a further 147,473 rules (29.5% of the full list).
