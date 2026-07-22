# Blocklist stats

_Generated 2026-07-22 01:50:29 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 159,088 | 56,789 | 35.7% |
| HaGeZi Normal | 179,094 | 82,085 | 45.8% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 330,222 | 249,609 | 75.6% |
| Dan Pollock | 12,953 | 9,799 | 75.7% |
| Peter Lowe | 7,068 | 3,835 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 57,902 | 9,324 | 16.1% |
| EasyPrivacy | 55,547 | 26,732 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,383 | 1,301 | 94.1% |
| uBO Badware | 4,185 | 4,138 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **818,297** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 818,297 |
| **DNSZeroList.txt** (all sources, deduped) | **581,464** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **331,855** |

Deduplication removed 236,833 duplicate rule instances (28.9% of the raw total).
Dropping OISD Big removes a further 249,609 rules (42.9% of the full list).
