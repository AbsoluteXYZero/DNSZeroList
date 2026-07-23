# Blocklist stats

_Generated 2026-07-23 13:26:53 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 159,542 | 56,780 | 35.6% |
| HaGeZi Normal | 179,766 | 82,344 | 45.8% |
| AdAway | 6,540 | 3,462 | 52.9% |
| OISD Big | 331,501 | 250,597 | 75.6% |
| Dan Pollock | 12,958 | 9,804 | 75.7% |
| Peter Lowe | 7,068 | 3,835 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 58,307 | 9,319 | 16.0% |
| EasyPrivacy | 55,556 | 26,736 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,384 | 1,302 | 94.1% |
| uBO Badware | 4,184 | 4,137 | 98.9% |
| uBO Quick Fixes | 94 | 85 | 90.4% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **821,122** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 821,122 |
| **DNSZeroList.txt** (all sources, deduped) | **583,124** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **332,527** |

Deduplication removed 237,998 duplicate rule instances (29.0% of the raw total).
Dropping OISD Big removes a further 250,597 rules (43.0% of the full list).
