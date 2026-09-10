# Blocklist stats

_Generated 2026-09-10 15:33:04 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,994 | 74,910 | 42.1% |
| HaGeZi Normal | 181,641 | 78,645 | 43.3% |
| AdAway | 6,540 | 3,472 | 53.1% |
| OISD Big | 247,748 | 167,793 | 67.7% |
| Dan Pollock | 13,063 | 9,919 | 75.9% |
| Peter Lowe | 7,116 | 3,868 | 54.4% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 54,467 | 9,215 | 16.9% |
| EasyPrivacy | 56,002 | 25,669 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,432 | 1,351 | 94.3% |
| uBO Badware | 4,236 | 4,187 | 98.8% |
| uBO Quick Fixes | 94 | 85 | 90.4% |
| uBO Unbreak | 1,937 | 1,933 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **754,557** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 754,557 |
| **DNSZeroList.txt** (all sources, deduped) | **513,330** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **345,537** |

Deduplication removed 241,227 duplicate rule instances (32.0% of the raw total).
Dropping OISD Big removes a further 167,793 rules (32.7% of the full list).
