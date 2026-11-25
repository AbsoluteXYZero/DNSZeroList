# Blocklist stats

_Generated 2026-11-25 20:52:26 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 194,922 | 93,020 | 47.7% |
| HaGeZi Normal | 190,373 | 90,515 | 47.5% |
| AdAway | 6,540 | 3,443 | 52.6% |
| OISD Big | 221,797 | 128,168 | 57.8% |
| Dan Pollock | 13,117 | 9,989 | 76.2% |
| Peter Lowe | 7,148 | 3,879 | 54.3% |
| Dandelion Sprout | 490 | 307 | 62.7% |
| EasyList | 53,637 | 9,274 | 17.3% |
| EasyPrivacy | 56,795 | 26,206 | 46.1% |
| uBO Ads | 1,765 | 1,721 | 97.5% |
| uBO Privacy | 1,467 | 1,375 | 93.7% |
| uBO Badware | 4,739 | 4,683 | 98.8% |
| uBO Quick Fixes | 106 | 95 | 89.6% |
| uBO Unbreak | 1,949 | 1,945 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **754,881** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 754,881 |
| **DNSZeroList.txt** (all sources, deduped) | **509,060** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **380,892** |

Deduplication removed 245,821 duplicate rule instances (32.6% of the raw total).
Dropping OISD Big removes a further 128,168 rules (25.2% of the full list).
