# Blocklist stats

_Generated 2026-11-04 19:08:18 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 188,528 | 87,889 | 46.6% |
| HaGeZi Normal | 195,087 | 76,477 | 39.2% |
| AdAway | 6,540 | 3,450 | 52.8% |
| OISD Big | 232,230 | 126,971 | 54.7% |
| Dan Pollock | 12,971 | 9,869 | 76.1% |
| Peter Lowe | 7,158 | 3,900 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 52,889 | 9,236 | 17.5% |
| EasyPrivacy | 56,436 | 26,155 | 46.3% |
| uBO Ads | 1,771 | 1,728 | 97.6% |
| uBO Privacy | 1,461 | 1,376 | 94.2% |
| uBO Badware | 4,721 | 4,665 | 98.8% |
| uBO Quick Fixes | 169 | 158 | 93.5% |
| uBO Unbreak | 1,945 | 1,941 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **762,423** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 762,423 |
| **DNSZeroList.txt** (all sources, deduped) | **501,888** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **374,917** |

Deduplication removed 260,535 duplicate rule instances (34.2% of the raw total).
Dropping OISD Big removes a further 126,971 rules (25.3% of the full list).
