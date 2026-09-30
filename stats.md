# Blocklist stats

_Generated 2026-09-30 03:09:21 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 176,740 | 74,589 | 42.2% |
| HaGeZi Normal | 199,685 | 97,916 | 49.0% |
| AdAway | 6,540 | 3,449 | 52.7% |
| OISD Big | 244,205 | 163,198 | 66.8% |
| Dan Pollock | 13,082 | 9,928 | 75.9% |
| Peter Lowe | 7,134 | 3,883 | 54.4% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 53,143 | 9,227 | 17.4% |
| EasyPrivacy | 56,186 | 25,727 | 45.8% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,442 | 1,361 | 94.4% |
| uBO Badware | 4,247 | 4,197 | 98.8% |
| uBO Quick Fixes | 144 | 135 | 93.8% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **766,781** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 766,781 |
| **DNSZeroList.txt** (all sources, deduped) | **526,565** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **363,367** |

Deduplication removed 240,216 duplicate rule instances (31.3% of the raw total).
Dropping OISD Big removes a further 163,198 rules (31.0% of the full list).
