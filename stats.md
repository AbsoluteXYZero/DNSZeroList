# Blocklist stats

_Generated 2026-07-02 02:30:12 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 154,099 | 56,911 | 36.9% |
| HaGeZi Normal | 155,696 | 57,998 | 37.3% |
| AdAway | 6,540 | 3,534 | 54.0% |
| OISD Big | 326,254 | 247,219 | 75.8% |
| Dan Pollock | 12,908 | 9,758 | 75.6% |
| Peter Lowe | 7,064 | 3,845 | 54.4% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 52,890 | 9,321 | 17.6% |
| EasyPrivacy | 55,453 | 26,669 | 48.1% |
| uBO Ads | 1,787 | 1,737 | 97.2% |
| uBO Privacy | 1,372 | 1,290 | 94.0% |
| uBO Badware | 4,152 | 4,107 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,925 | 1,921 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **780,749** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 780,749 |
| **DNSZeroList.txt** (all sources, deduped) | **549,185** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **301,966** |

Deduplication removed 231,564 duplicate rule instances (29.7% of the raw total).
Dropping OISD Big removes a further 247,219 rules (45.0% of the full list).
