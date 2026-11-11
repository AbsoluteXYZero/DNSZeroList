# Blocklist stats

_Generated 2026-11-11 19:02:05 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 190,440 | 80,193 | 42.1% |
| HaGeZi Normal | 208,182 | 81,590 | 39.2% |
| AdAway | 6,540 | 3,442 | 52.6% |
| OISD Big | 226,386 | 132,802 | 58.7% |
| Dan Pollock | 13,090 | 9,950 | 76.0% |
| Peter Lowe | 7,156 | 3,879 | 54.2% |
| Dandelion Sprout | 490 | 306 | 62.4% |
| EasyList | 52,162 | 9,255 | 17.7% |
| EasyPrivacy | 56,569 | 26,251 | 46.4% |
| uBO Ads | 1,766 | 1,722 | 97.5% |
| uBO Privacy | 1,466 | 1,377 | 93.9% |
| uBO Badware | 4,734 | 4,678 | 98.8% |
| uBO Quick Fixes | 171 | 160 | 93.6% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **771,135** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 771,135 |
| **DNSZeroList.txt** (all sources, deduped) | **503,069** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **370,267** |

Deduplication removed 268,066 duplicate rule instances (34.8% of the raw total).
Dropping OISD Big removes a further 132,802 rules (26.4% of the full list).
