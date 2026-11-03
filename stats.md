# Blocklist stats

_Generated 2026-11-03 18:51:31 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 188,290 | 83,477 | 44.3% |
| HaGeZi Normal | 179,493 | 74,221 | 41.4% |
| AdAway | 6,540 | 3,451 | 52.8% |
| OISD Big | 232,202 | 147,511 | 63.5% |
| Dan Pollock | 12,971 | 9,867 | 76.1% |
| Peter Lowe | 7,158 | 3,899 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 52,677 | 9,237 | 17.5% |
| EasyPrivacy | 56,425 | 26,154 | 46.4% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,461 | 1,374 | 94.0% |
| uBO Badware | 4,719 | 4,664 | 98.8% |
| uBO Quick Fixes | 169 | 158 | 93.5% |
| uBO Unbreak | 1,945 | 1,941 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **746,342** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 746,342 |
| **DNSZeroList.txt** (all sources, deduped) | **499,551** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **352,040** |

Deduplication removed 246,791 duplicate rule instances (33.1% of the raw total).
Dropping OISD Big removes a further 147,511 rules (29.5% of the full list).
