# Blocklist stats

_Generated 2026-07-22 13:23:38 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 159,246 | 56,782 | 35.7% |
| HaGeZi Normal | 179,383 | 82,203 | 45.8% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 330,331 | 249,531 | 75.5% |
| Dan Pollock | 12,953 | 9,799 | 75.7% |
| Peter Lowe | 7,068 | 3,835 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 58,040 | 9,317 | 16.1% |
| EasyPrivacy | 55,547 | 26,732 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,383 | 1,301 | 94.1% |
| uBO Badware | 4,185 | 4,138 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **818,991** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 818,991 |
| **DNSZeroList.txt** (all sources, deduped) | **581,648** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **332,117** |

Deduplication removed 237,343 duplicate rule instances (29.0% of the raw total).
Dropping OISD Big removes a further 249,531 rules (42.9% of the full list).
