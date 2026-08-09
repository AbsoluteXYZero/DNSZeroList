# Blocklist stats

_Generated 2026-08-09 12:31:43 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 164,256 | 56,738 | 34.5% |
| HaGeZi Normal | 181,366 | 82,694 | 45.6% |
| AdAway | 6,540 | 3,464 | 53.0% |
| OISD Big | 253,482 | 172,570 | 68.1% |
| Dan Pollock | 12,989 | 9,844 | 75.8% |
| Peter Lowe | 7,072 | 3,841 | 54.3% |
| Dandelion Sprout | 480 | 292 | 60.8% |
| EasyList | 62,805 | 9,328 | 14.9% |
| EasyPrivacy | 55,659 | 26,778 | 48.1% |
| uBO Ads | 1,769 | 1,725 | 97.5% |
| uBO Privacy | 1,393 | 1,314 | 94.3% |
| uBO Badware | 4,155 | 4,110 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,932 | 1,927 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **754,028** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 754,028 |
| **DNSZeroList.txt** (all sources, deduped) | **508,764** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **336,194** |

Deduplication removed 245,264 duplicate rule instances (32.5% of the raw total).
Dropping OISD Big removes a further 172,570 rules (33.9% of the full list).
