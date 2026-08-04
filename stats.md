# Blocklist stats

_Generated 2026-08-04 13:50:04 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 162,745 | 56,679 | 34.8% |
| HaGeZi Normal | 182,920 | 82,651 | 45.2% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 433,316 | 351,905 | 81.2% |
| Dan Pollock | 12,978 | 9,830 | 75.7% |
| Peter Lowe | 7,068 | 3,838 | 54.3% |
| Dandelion Sprout | 480 | 292 | 60.8% |
| EasyList | 61,358 | 9,343 | 15.2% |
| EasyPrivacy | 55,635 | 26,768 | 48.1% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,391 | 1,311 | 94.2% |
| uBO Badware | 4,273 | 4,227 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,932 | 1,927 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **932,537** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 932,537 |
| **DNSZeroList.txt** (all sources, deduped) | **687,906** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **336,001** |

Deduplication removed 244,631 duplicate rule instances (26.2% of the raw total).
Dropping OISD Big removes a further 351,905 rules (51.2% of the full list).
