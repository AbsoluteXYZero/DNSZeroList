# Blocklist stats

_Generated 2026-10-24 15:05:48 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 191,497 | 81,390 | 42.5% |
| HaGeZi Normal | 172,193 | 71,507 | 41.5% |
| AdAway | 6,540 | 3,446 | 52.7% |
| OISD Big | 235,989 | 153,609 | 65.1% |
| Dan Pollock | 12,971 | 9,859 | 76.0% |
| Peter Lowe | 7,158 | 3,896 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 60,873 | 9,246 | 15.2% |
| EasyPrivacy | 56,368 | 26,081 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,453 | 1,366 | 94.0% |
| uBO Badware | 4,852 | 4,802 | 99.0% |
| uBO Quick Fixes | 220 | 209 | 95.0% |
| uBO Unbreak | 1,944 | 1,940 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **754,350** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 754,350 |
| **DNSZeroList.txt** (all sources, deduped) | **504,918** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **351,309** |

Deduplication removed 249,432 duplicate rule instances (33.1% of the raw total).
Dropping OISD Big removes a further 153,609 rules (30.4% of the full list).
