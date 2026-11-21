# Blocklist stats

_Generated 2026-11-21 18:28:58 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 192,079 | 89,876 | 46.8% |
| HaGeZi Normal | 195,083 | 90,369 | 46.3% |
| AdAway | 6,540 | 3,444 | 52.7% |
| OISD Big | 224,142 | 129,091 | 57.6% |
| Dan Pollock | 13,090 | 9,961 | 76.1% |
| Peter Lowe | 7,142 | 3,876 | 54.3% |
| Dandelion Sprout | 490 | 306 | 62.4% |
| EasyList | 53,944 | 9,269 | 17.2% |
| EasyPrivacy | 56,732 | 26,071 | 46.0% |
| uBO Ads | 1,765 | 1,721 | 97.5% |
| uBO Privacy | 1,467 | 1,376 | 93.8% |
| uBO Badware | 4,737 | 4,681 | 98.8% |
| uBO Quick Fixes | 172 | 161 | 93.6% |
| uBO Unbreak | 1,949 | 1,945 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **759,368** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 759,368 |
| **DNSZeroList.txt** (all sources, deduped) | **509,456** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **380,365** |

Deduplication removed 249,912 duplicate rule instances (32.9% of the raw total).
Dropping OISD Big removes a further 129,091 rules (25.3% of the full list).
