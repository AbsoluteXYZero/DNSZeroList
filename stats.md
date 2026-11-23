# Blocklist stats

_Generated 2026-11-23 04:53:31 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 190,831 | 89,953 | 47.1% |
| HaGeZi Normal | 177,323 | 87,734 | 49.5% |
| AdAway | 6,540 | 3,443 | 52.6% |
| OISD Big | 220,475 | 137,607 | 62.4% |
| Dan Pollock | 13,116 | 9,989 | 76.2% |
| Peter Lowe | 7,146 | 3,877 | 54.3% |
| Dandelion Sprout | 490 | 308 | 62.9% |
| EasyList | 52,658 | 9,262 | 17.6% |
| EasyPrivacy | 56,776 | 26,099 | 46.0% |
| uBO Ads | 1,765 | 1,721 | 97.5% |
| uBO Privacy | 1,467 | 1,375 | 93.7% |
| uBO Badware | 4,738 | 4,682 | 98.8% |
| uBO Quick Fixes | 106 | 95 | 89.6% |
| uBO Unbreak | 1,949 | 1,945 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **735,416** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 735,416 |
| **DNSZeroList.txt** (all sources, deduped) | **501,803** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **364,196** |

Deduplication removed 233,613 duplicate rule instances (31.8% of the raw total).
Dropping OISD Big removes a further 137,607 rules (27.4% of the full list).
