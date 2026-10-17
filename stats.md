# Blocklist stats

_Generated 2026-10-17 14:42:08 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 185,803 | 79,694 | 42.9% |
| HaGeZi Normal | 164,947 | 67,816 | 41.1% |
| AdAway | 6,540 | 3,450 | 52.8% |
| OISD Big | 234,173 | 155,196 | 66.3% |
| Dan Pollock | 13,085 | 9,970 | 76.2% |
| Peter Lowe | 7,170 | 3,901 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 58,513 | 9,238 | 15.8% |
| EasyPrivacy | 56,307 | 26,034 | 46.2% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,451 | 1,366 | 94.1% |
| uBO Badware | 4,266 | 4,216 | 98.8% |
| uBO Quick Fixes | 185 | 174 | 94.1% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **736,673** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 736,673 |
| **DNSZeroList.txt** (all sources, deduped) | **495,905** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **340,709** |

Deduplication removed 240,768 duplicate rule instances (32.7% of the raw total).
Dropping OISD Big removes a further 155,196 rules (31.3% of the full list).
