# Blocklist stats

_Generated 2026-11-05 04:24:27 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 188,622 | 87,894 | 46.6% |
| HaGeZi Normal | 195,087 | 76,474 | 39.2% |
| AdAway | 6,540 | 3,445 | 52.7% |
| OISD Big | 232,370 | 127,060 | 54.7% |
| Dan Pollock | 12,971 | 9,869 | 76.1% |
| Peter Lowe | 7,158 | 3,900 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 52,972 | 9,235 | 17.4% |
| EasyPrivacy | 56,447 | 26,163 | 46.3% |
| uBO Ads | 1,771 | 1,728 | 97.6% |
| uBO Privacy | 1,461 | 1,376 | 94.2% |
| uBO Badware | 4,721 | 4,665 | 98.8% |
| uBO Quick Fixes | 169 | 158 | 93.5% |
| uBO Unbreak | 1,945 | 1,941 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **762,751** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 762,751 |
| **DNSZeroList.txt** (all sources, deduped) | **502,075** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **375,015** |

Deduplication removed 260,676 duplicate rule instances (34.2% of the raw total).
Dropping OISD Big removes a further 127,060 rules (25.3% of the full list).
