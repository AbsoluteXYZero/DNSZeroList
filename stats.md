# Blocklist stats

_Generated 2026-11-27 05:57:03 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 195,445 | 93,058 | 47.6% |
| HaGeZi Normal | 184,355 | 93,243 | 50.6% |
| AdAway | 6,540 | 3,443 | 52.6% |
| OISD Big | 222,340 | 137,395 | 61.8% |
| Dan Pollock | 13,117 | 9,987 | 76.1% |
| Peter Lowe | 7,152 | 3,881 | 54.3% |
| Dandelion Sprout | 490 | 307 | 62.7% |
| EasyList | 54,148 | 9,294 | 17.2% |
| EasyPrivacy | 56,828 | 26,230 | 46.2% |
| uBO Ads | 1,765 | 1,721 | 97.5% |
| uBO Privacy | 1,467 | 1,375 | 93.7% |
| uBO Badware | 4,739 | 4,684 | 98.8% |
| uBO Quick Fixes | 106 | 95 | 89.6% |
| uBO Unbreak | 1,949 | 1,945 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **750,477** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 750,477 |
| **DNSZeroList.txt** (all sources, deduped) | **512,575** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **375,180** |

Deduplication removed 237,902 duplicate rule instances (31.7% of the raw total).
Dropping OISD Big removes a further 137,395 rules (26.8% of the full list).
