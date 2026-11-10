# Blocklist stats

_Generated 2026-11-10 05:22:10 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 188,364 | 80,046 | 42.5% |
| HaGeZi Normal | 206,820 | 81,528 | 39.4% |
| AdAway | 6,540 | 3,437 | 52.6% |
| OISD Big | 228,689 | 134,890 | 59.0% |
| Dan Pollock | 12,971 | 9,839 | 75.9% |
| Peter Lowe | 7,152 | 3,875 | 54.2% |
| Dandelion Sprout | 490 | 304 | 62.0% |
| EasyList | 51,528 | 9,264 | 18.0% |
| EasyPrivacy | 56,559 | 26,249 | 46.4% |
| uBO Ads | 1,766 | 1,722 | 97.5% |
| uBO Privacy | 1,464 | 1,375 | 93.9% |
| uBO Badware | 4,732 | 4,676 | 98.8% |
| uBO Quick Fixes | 171 | 160 | 93.6% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **769,229** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 769,229 |
| **DNSZeroList.txt** (all sources, deduped) | **503,086** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **368,196** |

Deduplication removed 266,143 duplicate rule instances (34.6% of the raw total).
Dropping OISD Big removes a further 134,890 rules (26.8% of the full list).
