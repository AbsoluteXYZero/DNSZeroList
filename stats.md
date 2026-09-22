# Blocklist stats

_Generated 2026-09-22 15:58:57 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 181,905 | 74,587 | 41.0% |
| HaGeZi Normal | 201,296 | 96,563 | 48.0% |
| AdAway | 6,540 | 3,454 | 52.8% |
| OISD Big | 246,458 | 165,918 | 67.3% |
| Dan Pollock | 13,082 | 9,931 | 75.9% |
| Peter Lowe | 7,134 | 3,883 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 58,607 | 9,241 | 15.8% |
| EasyPrivacy | 56,137 | 25,710 | 45.8% |
| uBO Ads | 1,775 | 1,731 | 97.5% |
| uBO Privacy | 1,438 | 1,357 | 94.4% |
| uBO Badware | 4,226 | 4,176 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,939 | 1,935 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **781,147** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 781,147 |
| **DNSZeroList.txt** (all sources, deduped) | **532,628** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **366,710** |

Deduplication removed 248,519 duplicate rule instances (31.8% of the raw total).
Dropping OISD Big removes a further 165,918 rules (31.2% of the full list).
