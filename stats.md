# Blocklist stats

_Generated 2026-10-16 02:23:58 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 185,259 | 79,843 | 43.1% |
| HaGeZi Normal | 162,803 | 66,282 | 40.7% |
| AdAway | 6,540 | 3,449 | 52.7% |
| OISD Big | 236,186 | 157,817 | 66.8% |
| Dan Pollock | 13,085 | 9,971 | 76.2% |
| Peter Lowe | 7,130 | 3,881 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 57,990 | 9,234 | 15.9% |
| EasyPrivacy | 56,293 | 26,028 | 46.2% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,450 | 1,366 | 94.2% |
| uBO Badware | 4,266 | 4,216 | 98.8% |
| uBO Quick Fixes | 185 | 174 | 94.1% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **735,421** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 735,421 |
| **DNSZeroList.txt** (all sources, deduped) | **496,460** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **338,643** |

Deduplication removed 238,961 duplicate rule instances (32.5% of the raw total).
Dropping OISD Big removes a further 157,817 rules (31.8% of the full list).
