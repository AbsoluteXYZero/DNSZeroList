# Blocklist stats

_Generated 2026-09-13 02:15:43 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 178,853 | 74,957 | 41.9% |
| HaGeZi Normal | 180,141 | 79,706 | 44.2% |
| AdAway | 6,540 | 3,458 | 52.9% |
| OISD Big | 245,269 | 166,734 | 68.0% |
| Dan Pollock | 13,064 | 9,921 | 75.9% |
| Peter Lowe | 7,150 | 3,886 | 54.3% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 55,307 | 9,234 | 16.7% |
| EasyPrivacy | 56,027 | 25,685 | 45.8% |
| uBO Ads | 1,764 | 1,720 | 97.5% |
| uBO Privacy | 1,433 | 1,352 | 94.3% |
| uBO Badware | 4,239 | 4,189 | 98.8% |
| uBO Quick Fixes | 94 | 85 | 90.4% |
| uBO Unbreak | 1,935 | 1,931 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **752,333** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 752,333 |
| **DNSZeroList.txt** (all sources, deduped) | **512,566** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **345,832** |

Deduplication removed 239,767 duplicate rule instances (31.9% of the raw total).
Dropping OISD Big removes a further 166,734 rules (32.5% of the full list).
