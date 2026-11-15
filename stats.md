# Blocklist stats

_Generated 2026-11-15 18:16:21 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 192,018 | 79,973 | 41.6% |
| HaGeZi Normal | 223,018 | 94,821 | 42.5% |
| AdAway | 6,540 | 3,301 | 50.5% |
| OISD Big | 228,090 | 131,185 | 57.5% |
| Dan Pollock | 13,090 | 9,912 | 75.7% |
| Peter Lowe | 7,160 | 3,885 | 54.3% |
| Dandelion Sprout | 490 | 306 | 62.4% |
| EasyList | 53,679 | 9,252 | 17.2% |
| EasyPrivacy | 56,618 | 26,002 | 45.9% |
| uBO Ads | 1,766 | 1,722 | 97.5% |
| uBO Privacy | 1,469 | 1,377 | 93.7% |
| uBO Badware | 4,741 | 4,685 | 98.8% |
| uBO Quick Fixes | 172 | 161 | 93.6% |
| uBO Unbreak | 1,951 | 1,947 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **790,839** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 790,839 |
| **DNSZeroList.txt** (all sources, deduped) | **516,728** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **385,543** |

Deduplication removed 274,111 duplicate rule instances (34.7% of the raw total).
Dropping OISD Big removes a further 131,185 rules (25.4% of the full list).
