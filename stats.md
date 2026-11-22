# Blocklist stats

_Generated 2026-11-22 18:51:37 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 192,456 | 89,869 | 46.7% |
| HaGeZi Normal | 233,475 | 92,995 | 39.8% |
| AdAway | 6,540 | 3,446 | 52.7% |
| OISD Big | 220,262 | 89,672 | 40.7% |
| Dan Pollock | 13,090 | 9,965 | 76.1% |
| Peter Lowe | 7,142 | 3,874 | 54.2% |
| Dandelion Sprout | 490 | 306 | 62.4% |
| EasyList | 54,298 | 9,265 | 17.1% |
| EasyPrivacy | 56,749 | 26,076 | 45.9% |
| uBO Ads | 1,765 | 1,721 | 97.5% |
| uBO Privacy | 1,467 | 1,376 | 93.8% |
| uBO Badware | 4,737 | 4,681 | 98.8% |
| uBO Quick Fixes | 106 | 95 | 89.6% |
| uBO Unbreak | 1,949 | 1,945 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **794,562** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 794,562 |
| **DNSZeroList.txt** (all sources, deduped) | **508,279** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **418,607** |

Deduplication removed 286,283 duplicate rule instances (36.0% of the raw total).
Dropping OISD Big removes a further 89,672 rules (17.6% of the full list).
