# Blocklist stats

_Generated 2026-10-22 02:36:13 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 190,581 | 81,708 | 42.9% |
| HaGeZi Normal | 170,357 | 69,880 | 41.0% |
| AdAway | 6,540 | 3,447 | 52.7% |
| OISD Big | 234,382 | 153,275 | 65.4% |
| Dan Pollock | 13,085 | 9,966 | 76.2% |
| Peter Lowe | 7,176 | 3,905 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 59,996 | 9,238 | 15.4% |
| EasyPrivacy | 56,351 | 26,098 | 46.3% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,451 | 1,366 | 94.1% |
| uBO Badware | 4,850 | 4,800 | 99.0% |
| uBO Quick Fixes | 215 | 204 | 94.9% |
| uBO Unbreak | 1,943 | 1,939 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **749,220** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 749,220 |
| **DNSZeroList.txt** (all sources, deduped) | **502,087** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **348,812** |

Deduplication removed 247,133 duplicate rule instances (33.0% of the raw total).
Dropping OISD Big removes a further 153,275 rules (30.5% of the full list).
