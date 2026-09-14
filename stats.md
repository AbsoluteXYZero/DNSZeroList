# Blocklist stats

_Generated 2026-09-14 17:17:28 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 179,457 | 74,938 | 41.8% |
| HaGeZi Normal | 180,765 | 79,635 | 44.1% |
| AdAway | 6,540 | 3,460 | 52.9% |
| OISD Big | 246,070 | 167,210 | 68.0% |
| Dan Pollock | 13,065 | 9,922 | 75.9% |
| Peter Lowe | 7,150 | 3,889 | 54.4% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 55,885 | 9,223 | 16.5% |
| EasyPrivacy | 56,037 | 25,684 | 45.8% |
| uBO Ads | 1,763 | 1,719 | 97.5% |
| uBO Privacy | 1,435 | 1,354 | 94.4% |
| uBO Badware | 4,126 | 4,078 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,937 | 1,933 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **754,840** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 754,840 |
| **DNSZeroList.txt** (all sources, deduped) | **513,505** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **346,295** |

Deduplication removed 241,335 duplicate rule instances (32.0% of the raw total).
Dropping OISD Big removes a further 167,210 rules (32.6% of the full list).
