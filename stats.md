# Blocklist stats

_Generated 2026-11-19 05:11:21 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 191,446 | 90,120 | 47.1% |
| HaGeZi Normal | 176,302 | 71,548 | 40.6% |
| AdAway | 6,540 | 3,446 | 52.7% |
| OISD Big | 229,803 | 133,040 | 57.9% |
| Dan Pollock | 13,090 | 9,963 | 76.1% |
| Peter Lowe | 7,168 | 3,889 | 54.3% |
| Dandelion Sprout | 490 | 307 | 62.7% |
| EasyList | 53,040 | 9,264 | 17.5% |
| EasyPrivacy | 56,697 | 26,062 | 46.0% |
| uBO Ads | 1,765 | 1,721 | 97.5% |
| uBO Privacy | 1,473 | 1,381 | 93.8% |
| uBO Badware | 4,744 | 4,688 | 98.8% |
| uBO Quick Fixes | 173 | 162 | 93.6% |
| uBO Unbreak | 1,951 | 1,947 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **744,719** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 744,719 |
| **DNSZeroList.txt** (all sources, deduped) | **494,809** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **361,769** |

Deduplication removed 249,910 duplicate rule instances (33.6% of the raw total).
Dropping OISD Big removes a further 133,040 rules (26.9% of the full list).
