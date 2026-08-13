# Blocklist stats

_Generated 2026-08-13 01:12:05 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 155,268 | 56,994 | 36.7% |
| HaGeZi Normal | 181,366 | 84,732 | 46.7% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 251,980 | 171,333 | 68.0% |
| Dan Pollock | 13,001 | 9,849 | 75.8% |
| Peter Lowe | 7,082 | 3,844 | 54.3% |
| Dandelion Sprout | 480 | 291 | 60.6% |
| EasyList | 53,446 | 9,324 | 17.4% |
| EasyPrivacy | 55,688 | 26,786 | 48.1% |
| uBO Ads | 1,769 | 1,725 | 97.5% |
| uBO Privacy | 1,404 | 1,325 | 94.4% |
| uBO Badware | 4,155 | 4,110 | 98.9% |
| uBO Quick Fixes | 90 | 81 | 90.0% |
| uBO Unbreak | 1,933 | 1,928 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **734,239** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 734,239 |
| **DNSZeroList.txt** (all sources, deduped) | **500,495** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **329,162** |

Deduplication removed 233,744 duplicate rule instances (31.8% of the raw total).
Dropping OISD Big removes a further 171,333 rules (34.2% of the full list).
