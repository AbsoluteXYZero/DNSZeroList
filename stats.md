# Blocklist stats

_Generated 2026-10-22 16:20:23 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 190,801 | 81,487 | 42.7% |
| HaGeZi Normal | 171,250 | 70,208 | 41.0% |
| AdAway | 6,540 | 3,447 | 52.7% |
| OISD Big | 234,863 | 153,281 | 65.3% |
| Dan Pollock | 13,085 | 9,966 | 76.2% |
| Peter Lowe | 7,178 | 3,906 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 60,199 | 9,237 | 15.3% |
| EasyPrivacy | 56,360 | 26,099 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,451 | 1,366 | 94.1% |
| uBO Badware | 4,850 | 4,800 | 99.0% |
| uBO Quick Fixes | 220 | 209 | 95.0% |
| uBO Unbreak | 1,943 | 1,939 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **751,032** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 751,032 |
| **DNSZeroList.txt** (all sources, deduped) | **502,700** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **349,419** |

Deduplication removed 248,332 duplicate rule instances (33.1% of the raw total).
Dropping OISD Big removes a further 153,281 rules (30.5% of the full list).
