# Blocklist stats

_Generated 2026-09-15 02:36:59 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 179,634 | 74,942 | 41.7% |
| HaGeZi Normal | 180,765 | 79,639 | 44.1% |
| AdAway | 6,540 | 3,460 | 52.9% |
| OISD Big | 246,373 | 167,440 | 68.0% |
| Dan Pollock | 13,069 | 9,926 | 76.0% |
| Peter Lowe | 7,150 | 3,889 | 54.4% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 56,038 | 9,208 | 16.4% |
| EasyPrivacy | 56,040 | 25,684 | 45.8% |
| uBO Ads | 1,763 | 1,719 | 97.5% |
| uBO Privacy | 1,435 | 1,354 | 94.4% |
| uBO Badware | 4,126 | 4,078 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,937 | 1,933 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **755,480** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 755,480 |
| **DNSZeroList.txt** (all sources, deduped) | **513,901** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **346,461** |

Deduplication removed 241,579 duplicate rule instances (32.0% of the raw total).
Dropping OISD Big removes a further 167,440 rules (32.6% of the full list).
