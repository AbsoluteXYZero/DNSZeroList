# Blocklist stats

_Generated 2026-08-09 01:02:02 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 164,106 | 56,713 | 34.6% |
| HaGeZi Normal | 182,277 | 83,367 | 45.7% |
| AdAway | 6,540 | 3,464 | 53.0% |
| OISD Big | 253,285 | 172,370 | 68.1% |
| Dan Pollock | 12,989 | 9,844 | 75.8% |
| Peter Lowe | 7,072 | 3,841 | 54.3% |
| Dandelion Sprout | 480 | 292 | 60.8% |
| EasyList | 62,656 | 9,329 | 14.9% |
| EasyPrivacy | 55,657 | 26,774 | 48.1% |
| uBO Ads | 1,769 | 1,725 | 97.5% |
| uBO Privacy | 1,392 | 1,313 | 94.3% |
| uBO Badware | 4,155 | 4,110 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,932 | 1,927 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **754,440** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 754,440 |
| **DNSZeroList.txt** (all sources, deduped) | **509,139** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **336,769** |

Deduplication removed 245,301 duplicate rule instances (32.5% of the raw total).
Dropping OISD Big removes a further 172,370 rules (33.9% of the full list).
