# Blocklist stats

_Generated 2026-08-05 13:45:43 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 163,040 | 56,668 | 34.8% |
| HaGeZi Normal | 183,005 | 82,601 | 45.1% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 434,482 | 352,831 | 81.2% |
| Dan Pollock | 12,981 | 9,833 | 75.7% |
| Peter Lowe | 7,068 | 3,838 | 54.3% |
| Dandelion Sprout | 480 | 292 | 60.8% |
| EasyList | 61,647 | 9,347 | 15.2% |
| EasyPrivacy | 55,645 | 26,773 | 48.1% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,391 | 1,311 | 94.2% |
| uBO Badware | 4,273 | 4,227 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,932 | 1,927 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **934,385** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 934,385 |
| **DNSZeroList.txt** (all sources, deduped) | **689,071** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **336,240** |

Deduplication removed 245,314 duplicate rule instances (26.3% of the raw total).
Dropping OISD Big removes a further 352,831 rules (51.2% of the full list).
