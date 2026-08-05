# Blocklist stats

_Generated 2026-08-05 01:46:32 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 162,895 | 56,683 | 34.8% |
| HaGeZi Normal | 182,950 | 82,560 | 45.1% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 433,929 | 352,429 | 81.2% |
| Dan Pollock | 12,979 | 9,831 | 75.7% |
| Peter Lowe | 7,068 | 3,838 | 54.3% |
| Dandelion Sprout | 480 | 292 | 60.8% |
| EasyList | 61,503 | 9,347 | 15.2% |
| EasyPrivacy | 55,641 | 26,769 | 48.1% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,391 | 1,311 | 94.2% |
| uBO Badware | 4,273 | 4,227 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,932 | 1,927 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **933,482** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 933,482 |
| **DNSZeroList.txt** (all sources, deduped) | **688,498** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **336,069** |

Deduplication removed 244,984 duplicate rule instances (26.2% of the raw total).
Dropping OISD Big removes a further 352,429 rules (51.2% of the full list).
