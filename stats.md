# Blocklist stats

_Generated 2026-08-25 12:29:57 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,614 | 75,108 | 42.3% |
| HaGeZi Normal | 189,012 | 85,506 | 45.2% |
| AdAway | 6,540 | 3,461 | 52.9% |
| OISD Big | 268,917 | 185,160 | 68.9% |
| Dan Pollock | 13,031 | 9,879 | 75.8% |
| Peter Lowe | 7,068 | 3,840 | 54.3% |
| Dandelion Sprout | 480 | 296 | 61.7% |
| EasyList | 54,397 | 9,206 | 16.9% |
| EasyPrivacy | 55,911 | 25,632 | 45.8% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,425 | 1,344 | 94.3% |
| uBO Badware | 4,186 | 4,139 | 98.9% |
| uBO Quick Fixes | 90 | 81 | 90.0% |
| uBO Unbreak | 1,935 | 1,931 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **782,414** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 782,414 |
| **DNSZeroList.txt** (all sources, deduped) | **537,614** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **352,454** |

Deduplication removed 244,800 duplicate rule instances (31.3% of the raw total).
Dropping OISD Big removes a further 185,160 rules (34.4% of the full list).
