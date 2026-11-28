# Blocklist stats

_Generated 2026-11-28 05:38:25 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 195,844 | 93,056 | 47.5% |
| HaGeZi Normal | 181,992 | 90,857 | 49.9% |
| AdAway | 6,540 | 3,443 | 52.6% |
| OISD Big | 221,656 | 136,651 | 61.7% |
| Dan Pollock | 13,117 | 9,988 | 76.1% |
| Peter Lowe | 7,164 | 3,887 | 54.3% |
| Dandelion Sprout | 490 | 306 | 62.4% |
| EasyList | 54,293 | 9,066 | 16.7% |
| EasyPrivacy | 56,846 | 26,237 | 46.2% |
| uBO Ads | 1,765 | 1,721 | 97.5% |
| uBO Privacy | 1,469 | 1,377 | 93.7% |
| uBO Badware | 4,739 | 4,684 | 98.8% |
| uBO Quick Fixes | 106 | 95 | 89.6% |
| uBO Unbreak | 1,949 | 1,945 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **748,006** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 748,006 |
| **DNSZeroList.txt** (all sources, deduped) | **509,427** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **372,776** |

Deduplication removed 238,579 duplicate rule instances (31.9% of the raw total).
Dropping OISD Big removes a further 136,651 rules (26.8% of the full list).
