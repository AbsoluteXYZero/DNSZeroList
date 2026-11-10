# Blocklist stats

_Generated 2026-11-10 19:05:27 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 188,617 | 80,047 | 42.4% |
| HaGeZi Normal | 207,301 | 82,150 | 39.6% |
| AdAway | 6,540 | 3,438 | 52.6% |
| OISD Big | 226,125 | 132,957 | 58.8% |
| Dan Pollock | 12,971 | 9,839 | 75.9% |
| Peter Lowe | 7,152 | 3,875 | 54.2% |
| Dandelion Sprout | 490 | 304 | 62.0% |
| EasyList | 51,760 | 9,254 | 17.9% |
| EasyPrivacy | 56,563 | 26,250 | 46.4% |
| uBO Ads | 1,766 | 1,722 | 97.5% |
| uBO Privacy | 1,464 | 1,375 | 93.9% |
| uBO Badware | 4,732 | 4,676 | 98.8% |
| uBO Quick Fixes | 171 | 160 | 93.6% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **767,635** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 767,635 |
| **DNSZeroList.txt** (all sources, deduped) | **501,724** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **368,767** |

Deduplication removed 265,911 duplicate rule instances (34.6% of the raw total).
Dropping OISD Big removes a further 132,957 rules (26.5% of the full list).
