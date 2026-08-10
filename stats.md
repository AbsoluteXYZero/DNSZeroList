# Blocklist stats

_Generated 2026-08-10 01:03:46 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 164,416 | 56,736 | 34.5% |
| HaGeZi Normal | 181,366 | 82,694 | 45.6% |
| AdAway | 6,540 | 3,464 | 53.0% |
| OISD Big | 253,454 | 172,328 | 68.0% |
| Dan Pollock | 12,989 | 9,844 | 75.8% |
| Peter Lowe | 7,072 | 3,841 | 54.3% |
| Dandelion Sprout | 480 | 292 | 60.8% |
| EasyList | 62,968 | 9,331 | 14.8% |
| EasyPrivacy | 55,659 | 26,778 | 48.1% |
| uBO Ads | 1,769 | 1,725 | 97.5% |
| uBO Privacy | 1,393 | 1,314 | 94.3% |
| uBO Badware | 4,155 | 4,110 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,932 | 1,927 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **754,323** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 754,323 |
| **DNSZeroList.txt** (all sources, deduped) | **508,684** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **336,356** |

Deduplication removed 245,639 duplicate rule instances (32.6% of the raw total).
Dropping OISD Big removes a further 172,328 rules (33.9% of the full list).
