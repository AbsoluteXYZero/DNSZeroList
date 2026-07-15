# Blocklist stats

_Generated 2026-07-15 01:29:26 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 157,438 | 56,863 | 36.1% |
| HaGeZi Normal | 161,970 | 64,513 | 39.8% |
| AdAway | 6,540 | 3,478 | 53.2% |
| OISD Big | 330,053 | 246,586 | 74.7% |
| Dan Pollock | 12,939 | 9,763 | 75.5% |
| Peter Lowe | 7,080 | 3,845 | 54.3% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 55,980 | 9,313 | 16.6% |
| EasyPrivacy | 55,508 | 26,692 | 48.1% |
| uBO Ads | 1,785 | 1,737 | 97.3% |
| uBO Privacy | 1,379 | 1,297 | 94.1% |
| uBO Badware | 4,169 | 4,123 | 98.9% |
| uBO Quick Fixes | 97 | 87 | 89.7% |
| uBO Unbreak | 1,927 | 1,922 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **797,382** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 797,382 |
| **DNSZeroList.txt** (all sources, deduped) | **560,768** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **314,182** |

Deduplication removed 236,614 duplicate rule instances (29.7% of the raw total).
Dropping OISD Big removes a further 246,586 rules (44.0% of the full list).
