# Blocklist stats

_Generated 2026-11-18 05:15:44 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 191,070 | 90,163 | 47.2% |
| HaGeZi Normal | 187,101 | 80,231 | 42.9% |
| AdAway | 6,540 | 3,445 | 52.7% |
| OISD Big | 229,314 | 130,301 | 56.8% |
| Dan Pollock | 13,090 | 9,943 | 76.0% |
| Peter Lowe | 7,164 | 3,886 | 54.2% |
| Dandelion Sprout | 490 | 304 | 62.0% |
| EasyList | 52,683 | 9,261 | 17.6% |
| EasyPrivacy | 56,661 | 26,039 | 46.0% |
| uBO Ads | 1,766 | 1,722 | 97.5% |
| uBO Privacy | 1,471 | 1,379 | 93.7% |
| uBO Badware | 4,744 | 4,688 | 98.8% |
| uBO Quick Fixes | 173 | 162 | 93.6% |
| uBO Unbreak | 1,951 | 1,947 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **754,255** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 754,255 |
| **DNSZeroList.txt** (all sources, deduped) | **502,830** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **372,529** |

Deduplication removed 251,425 duplicate rule instances (33.3% of the raw total).
Dropping OISD Big removes a further 130,301 rules (25.9% of the full list).
