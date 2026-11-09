# Blocklist stats

_Generated 2026-11-09 21:46:04 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 188,229 | 80,011 | 42.5% |
| HaGeZi Normal | 207,196 | 81,311 | 39.2% |
| AdAway | 6,540 | 3,436 | 52.5% |
| OISD Big | 232,081 | 137,291 | 59.2% |
| Dan Pollock | 12,971 | 9,840 | 75.9% |
| Peter Lowe | 7,152 | 3,875 | 54.2% |
| Dandelion Sprout | 490 | 304 | 62.0% |
| EasyList | 51,409 | 9,270 | 18.0% |
| EasyPrivacy | 56,558 | 26,247 | 46.4% |
| uBO Ads | 1,766 | 1,722 | 97.5% |
| uBO Privacy | 1,464 | 1,375 | 93.9% |
| uBO Badware | 4,732 | 4,676 | 98.8% |
| uBO Quick Fixes | 171 | 160 | 93.6% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **772,742** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 772,742 |
| **DNSZeroList.txt** (all sources, deduped) | **505,859** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **368,568** |

Deduplication removed 266,883 duplicate rule instances (34.5% of the raw total).
Dropping OISD Big removes a further 137,291 rules (27.1% of the full list).
