# Blocklist stats

_Generated 2026-07-21 01:51:41 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,794 | 56,825 | 35.8% |
| HaGeZi Normal | 178,595 | 81,881 | 45.8% |
| AdAway | 6,540 | 3,464 | 53.0% |
| OISD Big | 328,070 | 247,411 | 75.4% |
| Dan Pollock | 12,950 | 9,796 | 75.6% |
| Peter Lowe | 7,066 | 3,834 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 57,620 | 9,321 | 16.2% |
| EasyPrivacy | 55,543 | 26,734 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,383 | 1,301 | 94.1% |
| uBO Badware | 4,182 | 4,135 | 98.9% |
| uBO Quick Fixes | 96 | 86 | 89.6% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **815,061** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 815,061 |
| **DNSZeroList.txt** (all sources, deduped) | **578,846** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **331,435** |

Deduplication removed 236,215 duplicate rule instances (29.0% of the raw total).
Dropping OISD Big removes a further 247,411 rules (42.7% of the full list).
