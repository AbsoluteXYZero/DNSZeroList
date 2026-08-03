# Blocklist stats

_Generated 2026-08-03 14:18:37 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 162,480 | 56,715 | 34.9% |
| HaGeZi Normal | 182,177 | 82,368 | 45.2% |
| AdAway | 6,540 | 3,465 | 53.0% |
| OISD Big | 430,255 | 349,554 | 81.2% |
| Dan Pollock | 12,973 | 9,825 | 75.7% |
| Peter Lowe | 7,066 | 3,835 | 54.3% |
| Dandelion Sprout | 480 | 292 | 60.8% |
| EasyList | 61,106 | 9,343 | 15.3% |
| EasyPrivacy | 55,627 | 26,766 | 48.1% |
| uBO Ads | 1,768 | 1,724 | 97.5% |
| uBO Privacy | 1,391 | 1,311 | 94.2% |
| uBO Badware | 4,271 | 4,225 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,932 | 1,927 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **928,196** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 928,196 |
| **DNSZeroList.txt** (all sources, deduped) | **684,904** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **335,350** |

Deduplication removed 243,292 duplicate rule instances (26.2% of the raw total).
Dropping OISD Big removes a further 349,554 rules (51.0% of the full list).
