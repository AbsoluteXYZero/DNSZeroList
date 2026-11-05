# Blocklist stats

_Generated 2026-11-05 19:15:40 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 189,838 | 90,620 | 47.7% |
| HaGeZi Normal | 177,949 | 78,388 | 44.1% |
| AdAway | 6,540 | 3,445 | 52.7% |
| OISD Big | 232,211 | 140,051 | 60.3% |
| Dan Pollock | 12,971 | 9,870 | 76.1% |
| Peter Lowe | 7,158 | 3,898 | 54.5% |
| Dandelion Sprout | 490 | 303 | 61.8% |
| EasyList | 53,096 | 9,254 | 17.4% |
| EasyPrivacy | 56,448 | 26,177 | 46.4% |
| uBO Ads | 1,771 | 1,728 | 97.6% |
| uBO Privacy | 1,461 | 1,374 | 94.0% |
| uBO Badware | 4,721 | 4,665 | 98.8% |
| uBO Quick Fixes | 169 | 158 | 93.5% |
| uBO Unbreak | 1,945 | 1,941 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **746,805** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 746,805 |
| **DNSZeroList.txt** (all sources, deduped) | **504,964** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **364,913** |

Deduplication removed 241,841 duplicate rule instances (32.4% of the raw total).
Dropping OISD Big removes a further 140,051 rules (27.7% of the full list).
