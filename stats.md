# Blocklist stats

_Generated 2026-07-30 13:29:44 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 161,446 | 56,695 | 35.1% |
| HaGeZi Normal | 180,483 | 81,794 | 45.3% |
| AdAway | 6,540 | 3,464 | 53.0% |
| OISD Big | 336,379 | 255,097 | 75.8% |
| Dan Pollock | 12,971 | 9,820 | 75.7% |
| Peter Lowe | 7,058 | 3,830 | 54.3% |
| Dandelion Sprout | 480 | 290 | 60.4% |
| EasyList | 60,111 | 9,336 | 15.5% |
| EasyPrivacy | 55,615 | 26,761 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,388 | 1,308 | 94.2% |
| uBO Badware | 4,186 | 4,140 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **830,490** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 830,490 |
| **DNSZeroList.txt** (all sources, deduped) | **588,436** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **333,339** |

Deduplication removed 242,054 duplicate rule instances (29.1% of the raw total).
Dropping OISD Big removes a further 255,097 rules (43.4% of the full list).
