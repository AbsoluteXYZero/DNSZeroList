# Blocklist stats

_Generated 2026-09-23 02:33:27 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 182,068 | 74,589 | 41.0% |
| HaGeZi Normal | 201,296 | 96,561 | 48.0% |
| AdAway | 6,540 | 3,454 | 52.8% |
| OISD Big | 246,775 | 166,157 | 67.3% |
| Dan Pollock | 13,082 | 9,931 | 75.9% |
| Peter Lowe | 7,140 | 3,887 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 58,736 | 9,222 | 15.7% |
| EasyPrivacy | 56,145 | 25,710 | 45.8% |
| uBO Ads | 1,775 | 1,731 | 97.5% |
| uBO Privacy | 1,438 | 1,357 | 94.4% |
| uBO Badware | 4,226 | 4,176 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,939 | 1,935 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **781,770** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 781,770 |
| **DNSZeroList.txt** (all sources, deduped) | **533,013** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **366,856** |

Deduplication removed 248,757 duplicate rule instances (31.8% of the raw total).
Dropping OISD Big removes a further 166,157 rules (31.2% of the full list).
