# Blocklist stats

_Generated 2026-11-23 23:06:13 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 194,194 | 93,014 | 47.9% |
| HaGeZi Normal | 180,109 | 90,195 | 50.1% |
| AdAway | 6,540 | 3,443 | 52.6% |
| OISD Big | 220,892 | 136,878 | 62.0% |
| Dan Pollock | 13,116 | 9,989 | 76.2% |
| Peter Lowe | 7,146 | 3,877 | 54.3% |
| Dandelion Sprout | 490 | 308 | 62.9% |
| EasyList | 52,935 | 9,271 | 17.5% |
| EasyPrivacy | 56,781 | 26,202 | 46.1% |
| uBO Ads | 1,765 | 1,721 | 97.5% |
| uBO Privacy | 1,467 | 1,376 | 93.8% |
| uBO Badware | 4,739 | 4,683 | 98.8% |
| uBO Quick Fixes | 106 | 95 | 89.6% |
| uBO Unbreak | 1,949 | 1,945 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **742,265** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 742,265 |
| **DNSZeroList.txt** (all sources, deduped) | **507,564** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **370,686** |

Deduplication removed 234,701 duplicate rule instances (31.6% of the raw total).
Dropping OISD Big removes a further 136,878 rules (27.0% of the full list).
