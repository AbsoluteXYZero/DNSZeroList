# Blocklist stats

_Generated 2026-11-13 18:58:41 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 191,253 | 80,078 | 41.9% |
| HaGeZi Normal | 210,139 | 82,426 | 39.2% |
| AdAway | 6,540 | 3,441 | 52.6% |
| OISD Big | 228,130 | 132,154 | 57.9% |
| Dan Pollock | 13,090 | 9,950 | 76.0% |
| Peter Lowe | 7,156 | 3,879 | 54.2% |
| Dandelion Sprout | 490 | 306 | 62.4% |
| EasyList | 52,955 | 9,264 | 17.5% |
| EasyPrivacy | 56,591 | 26,008 | 46.0% |
| uBO Ads | 1,766 | 1,722 | 97.5% |
| uBO Privacy | 1,469 | 1,378 | 93.8% |
| uBO Badware | 4,738 | 4,682 | 98.8% |
| uBO Quick Fixes | 172 | 161 | 93.6% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **776,472** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 776,472 |
| **DNSZeroList.txt** (all sources, deduped) | **504,211** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **372,057** |

Deduplication removed 272,261 duplicate rule instances (35.1% of the raw total).
Dropping OISD Big removes a further 132,154 rules (26.2% of the full list).
