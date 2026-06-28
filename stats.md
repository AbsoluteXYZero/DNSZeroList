# Blocklist stats

_Generated 2026-06-28 02:39:44 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 159,671 | 56,849 | 35.6% |
| HaGeZi Normal | 160,674 | 56,419 | 35.1% |
| AdAway | 6,540 | 3,534 | 54.0% |
| OISD Big | 490,075 | 403,454 | 82.3% |
| Dan Pollock | 12,891 | 9,646 | 74.8% |
| Peter Lowe | 7,046 | 3,833 | 54.4% |
| Dandelion Sprout | 480 | 281 | 58.5% |
| EasyList | 58,704 | 9,364 | 16.0% |
| EasyPrivacy | 55,426 | 26,653 | 48.1% |
| uBO Ads | 1,787 | 1,737 | 97.2% |
| uBO Privacy | 1,365 | 1,284 | 94.1% |
| uBO Badware | 4,149 | 4,104 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,925 | 1,921 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **960,862** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 960,862 |
| **DNSZeroList.txt** (all sources, deduped) | **710,042** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **306,588** |

Deduplication removed 250,820 duplicate rule instances (26.1% of the raw total).
Dropping OISD Big removes a further 403,454 rules (56.8% of the full list).
