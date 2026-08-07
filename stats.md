# Blocklist stats

_Generated 2026-08-07 02:11:04 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 163,481 | 56,714 | 34.7% |
| HaGeZi Normal | 182,671 | 82,391 | 45.1% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 435,162 | 353,396 | 81.2% |
| Dan Pollock | 12,988 | 9,840 | 75.8% |
| Peter Lowe | 7,068 | 3,838 | 54.3% |
| Dandelion Sprout | 480 | 292 | 60.8% |
| EasyList | 62,083 | 9,365 | 15.1% |
| EasyPrivacy | 55,651 | 26,773 | 48.1% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,391 | 1,312 | 94.3% |
| uBO Badware | 4,274 | 4,228 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,932 | 1,927 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **935,622** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 935,622 |
| **DNSZeroList.txt** (all sources, deduped) | **689,864** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **336,468** |

Deduplication removed 245,758 duplicate rule instances (26.3% of the raw total).
Dropping OISD Big removes a further 353,396 rules (51.2% of the full list).
