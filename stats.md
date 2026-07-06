# Blocklist stats

_Generated 2026-07-06 15:14:13 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 154,693 | 57,015 | 36.9% |
| HaGeZi Normal | 157,467 | 57,944 | 36.8% |
| AdAway | 6,540 | 3,533 | 54.0% |
| OISD Big | 497,058 | 413,708 | 83.2% |
| Dan Pollock | 12,909 | 9,713 | 75.2% |
| Peter Lowe | 7,058 | 3,845 | 54.5% |
| Dandelion Sprout | 480 | 278 | 57.9% |
| EasyList | 53,372 | 9,281 | 17.4% |
| EasyPrivacy | 55,468 | 26,683 | 48.1% |
| uBO Ads | 1,787 | 1,738 | 97.3% |
| uBO Privacy | 1,372 | 1,290 | 94.0% |
| uBO Badware | 4,163 | 4,118 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,925 | 1,921 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **954,421** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 954,421 |
| **DNSZeroList.txt** (all sources, deduped) | **719,956** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **306,248** |

Deduplication removed 234,465 duplicate rule instances (24.6% of the raw total).
Dropping OISD Big removes a further 413,708 rules (57.5% of the full list).
