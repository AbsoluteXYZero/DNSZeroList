# Blocklist stats

_Generated 2026-08-08 00:58:25 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 163,796 | 56,712 | 34.6% |
| HaGeZi Normal | 182,616 | 82,434 | 45.1% |
| AdAway | 6,540 | 3,464 | 53.0% |
| OISD Big | 436,130 | 354,274 | 81.2% |
| Dan Pollock | 12,988 | 9,841 | 75.8% |
| Peter Lowe | 7,068 | 3,840 | 54.3% |
| Dandelion Sprout | 480 | 292 | 60.8% |
| EasyList | 62,348 | 9,329 | 15.0% |
| EasyPrivacy | 55,654 | 26,774 | 48.1% |
| uBO Ads | 1,769 | 1,725 | 97.5% |
| uBO Privacy | 1,391 | 1,312 | 94.3% |
| uBO Badware | 4,155 | 4,110 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,932 | 1,927 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **936,997** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 936,997 |
| **DNSZeroList.txt** (all sources, deduped) | **690,896** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **336,622** |

Deduplication removed 246,101 duplicate rule instances (26.3% of the raw total).
Dropping OISD Big removes a further 354,274 rules (51.3% of the full list).
