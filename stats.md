# Blocklist stats

_Generated 2026-10-25 15:18:16 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 191,854 | 81,393 | 42.4% |
| HaGeZi Normal | 172,193 | 71,608 | 41.6% |
| AdAway | 6,540 | 3,448 | 52.7% |
| OISD Big | 233,879 | 151,959 | 65.0% |
| Dan Pollock | 12,971 | 9,858 | 76.0% |
| Peter Lowe | 7,158 | 3,896 | 54.4% |
| Dandelion Sprout | 480 | 301 | 62.7% |
| EasyList | 61,226 | 9,254 | 15.1% |
| EasyPrivacy | 56,368 | 26,079 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,453 | 1,366 | 94.0% |
| uBO Badware | 4,855 | 4,805 | 99.0% |
| uBO Quick Fixes | 221 | 210 | 95.0% |
| uBO Unbreak | 1,944 | 1,940 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **752,954** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 752,954 |
| **DNSZeroList.txt** (all sources, deduped) | **503,632** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **351,673** |

Deduplication removed 249,322 duplicate rule instances (33.1% of the raw total).
Dropping OISD Big removes a further 151,959 rules (30.2% of the full list).
