# Blocklist stats

_Generated 2026-08-26 00:45:16 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,767 | 75,119 | 42.3% |
| HaGeZi Normal | 189,012 | 85,624 | 45.3% |
| AdAway | 6,540 | 3,461 | 52.9% |
| OISD Big | 267,481 | 183,833 | 68.7% |
| Dan Pollock | 13,036 | 9,884 | 75.8% |
| Peter Lowe | 7,068 | 3,840 | 54.3% |
| Dandelion Sprout | 480 | 296 | 61.7% |
| EasyList | 54,530 | 9,202 | 16.9% |
| EasyPrivacy | 55,916 | 25,631 | 45.8% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,425 | 1,344 | 94.3% |
| uBO Badware | 4,188 | 4,141 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,935 | 1,931 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **781,277** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 781,277 |
| **DNSZeroList.txt** (all sources, deduped) | **536,443** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **352,610** |

Deduplication removed 244,834 duplicate rule instances (31.3% of the raw total).
Dropping OISD Big removes a further 183,833 rules (34.3% of the full list).
