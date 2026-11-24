# Blocklist stats

_Generated 2026-11-24 07:42:42 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 194,327 | 93,002 | 47.9% |
| HaGeZi Normal | 180,356 | 90,118 | 50.0% |
| AdAway | 6,540 | 3,443 | 52.6% |
| OISD Big | 220,984 | 136,927 | 62.0% |
| Dan Pollock | 13,116 | 9,989 | 76.2% |
| Peter Lowe | 7,146 | 3,878 | 54.3% |
| Dandelion Sprout | 490 | 307 | 62.7% |
| EasyList | 53,077 | 9,283 | 17.5% |
| EasyPrivacy | 56,783 | 26,202 | 46.1% |
| uBO Ads | 1,765 | 1,721 | 97.5% |
| uBO Privacy | 1,467 | 1,376 | 93.8% |
| uBO Badware | 4,739 | 4,683 | 98.8% |
| uBO Quick Fixes | 106 | 95 | 89.6% |
| uBO Unbreak | 1,949 | 1,945 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **742,881** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 742,881 |
| **DNSZeroList.txt** (all sources, deduped) | **507,608** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **370,681** |

Deduplication removed 235,273 duplicate rule instances (31.7% of the raw total).
Dropping OISD Big removes a further 136,927 rules (27.0% of the full list).
