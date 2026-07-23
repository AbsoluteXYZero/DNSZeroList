# Blocklist stats

_Generated 2026-07-23 01:57:48 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 159,390 | 56,782 | 35.6% |
| HaGeZi Normal | 179,537 | 82,212 | 45.8% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 330,990 | 250,149 | 75.6% |
| Dan Pollock | 12,958 | 9,804 | 75.7% |
| Peter Lowe | 7,068 | 3,835 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 58,183 | 9,322 | 16.0% |
| EasyPrivacy | 55,554 | 26,735 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,384 | 1,302 | 94.1% |
| uBO Badware | 4,184 | 4,137 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **820,103** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 820,103 |
| **DNSZeroList.txt** (all sources, deduped) | **582,435** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **332,286** |

Deduplication removed 237,668 duplicate rule instances (29.0% of the raw total).
Dropping OISD Big removes a further 250,149 rules (42.9% of the full list).
