# Blocklist stats

_Generated 2026-07-01 14:12:18 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 153,948 | 56,879 | 36.9% |
| HaGeZi Normal | 155,866 | 58,132 | 37.3% |
| AdAway | 6,540 | 3,532 | 54.0% |
| OISD Big | 334,138 | 253,252 | 75.8% |
| Dan Pollock | 12,904 | 9,733 | 75.4% |
| Peter Lowe | 7,064 | 3,845 | 54.4% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 52,739 | 9,314 | 17.7% |
| EasyPrivacy | 55,451 | 26,675 | 48.1% |
| uBO Ads | 1,787 | 1,736 | 97.1% |
| uBO Privacy | 1,372 | 1,290 | 94.0% |
| uBO Badware | 4,152 | 4,107 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,925 | 1,921 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **788,495** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 788,495 |
| **DNSZeroList.txt** (all sources, deduped) | **555,165** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **301,913** |

Deduplication removed 233,330 duplicate rule instances (29.6% of the raw total).
Dropping OISD Big removes a further 253,252 rules (45.6% of the full list).
