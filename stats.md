# Blocklist stats

_Generated 2026-11-24 21:45:28 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 194,547 | 93,031 | 47.8% |
| HaGeZi Normal | 191,463 | 91,832 | 48.0% |
| AdAway | 6,540 | 3,442 | 52.6% |
| OISD Big | 221,277 | 127,818 | 57.8% |
| Dan Pollock | 13,116 | 9,977 | 76.1% |
| Peter Lowe | 7,146 | 3,878 | 54.3% |
| Dandelion Sprout | 490 | 306 | 62.4% |
| EasyList | 53,289 | 9,283 | 17.4% |
| EasyPrivacy | 56,783 | 26,201 | 46.1% |
| uBO Ads | 1,765 | 1,721 | 97.5% |
| uBO Privacy | 1,467 | 1,375 | 93.7% |
| uBO Badware | 4,739 | 4,683 | 98.8% |
| uBO Quick Fixes | 106 | 95 | 89.6% |
| uBO Unbreak | 1,949 | 1,945 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **754,713** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 754,713 |
| **DNSZeroList.txt** (all sources, deduped) | **509,726** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **381,908** |

Deduplication removed 244,987 duplicate rule instances (32.5% of the raw total).
Dropping OISD Big removes a further 127,818 rules (25.1% of the full list).
