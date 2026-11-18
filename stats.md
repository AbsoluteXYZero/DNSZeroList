# Blocklist stats

_Generated 2026-11-18 19:46:21 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 191,287 | 90,122 | 47.1% |
| HaGeZi Normal | 188,169 | 80,787 | 42.9% |
| AdAway | 6,540 | 3,445 | 52.7% |
| OISD Big | 229,491 | 130,138 | 56.7% |
| Dan Pollock | 13,090 | 9,943 | 76.0% |
| Peter Lowe | 7,168 | 3,888 | 54.2% |
| Dandelion Sprout | 490 | 304 | 62.0% |
| EasyList | 52,900 | 9,273 | 17.5% |
| EasyPrivacy | 56,684 | 26,055 | 46.0% |
| uBO Ads | 1,765 | 1,721 | 97.5% |
| uBO Privacy | 1,473 | 1,381 | 93.8% |
| uBO Badware | 4,744 | 4,688 | 98.8% |
| uBO Quick Fixes | 173 | 162 | 93.6% |
| uBO Unbreak | 1,951 | 1,947 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **755,962** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 755,962 |
| **DNSZeroList.txt** (all sources, deduped) | **503,686** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **373,548** |

Deduplication removed 252,276 duplicate rule instances (33.4% of the raw total).
Dropping OISD Big removes a further 130,138 rules (25.8% of the full list).
