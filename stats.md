# Blocklist stats

_Generated 2026-08-22 00:43:01 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,903 | 75,246 | 42.3% |
| HaGeZi Normal | 187,763 | 84,589 | 45.1% |
| AdAway | 6,540 | 3,461 | 52.9% |
| OISD Big | 268,924 | 185,692 | 69.0% |
| Dan Pollock | 13,029 | 9,877 | 75.8% |
| Peter Lowe | 7,064 | 3,838 | 54.3% |
| Dandelion Sprout | 480 | 296 | 61.7% |
| EasyList | 54,563 | 9,315 | 17.1% |
| EasyPrivacy | 55,877 | 25,613 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,424 | 1,343 | 94.3% |
| uBO Badware | 4,173 | 4,126 | 98.9% |
| uBO Quick Fixes | 89 | 80 | 89.9% |
| uBO Unbreak | 1,935 | 1,931 | 99.8% |
| uBO Resource Abuse | 38 | 36 | 94.7% |
| **Sum (before dedup)** | **781,572** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 781,572 |
| **DNSZeroList.txt** (all sources, deduped) | **537,347** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **351,655** |

Deduplication removed 244,225 duplicate rule instances (31.2% of the raw total).
Dropping OISD Big removes a further 185,692 rules (34.6% of the full list).
