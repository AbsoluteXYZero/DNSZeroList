# Blocklist stats

_Generated 2026-09-06 02:04:50 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 180,484 | 74,954 | 41.5% |
| HaGeZi Normal | 192,739 | 87,032 | 45.2% |
| AdAway | 6,540 | 3,464 | 53.0% |
| OISD Big | 256,643 | 168,741 | 65.7% |
| Dan Pollock | 13,057 | 9,911 | 75.9% |
| Peter Lowe | 7,112 | 3,867 | 54.4% |
| Dandelion Sprout | 480 | 298 | 62.1% |
| EasyList | 57,076 | 9,227 | 16.2% |
| EasyPrivacy | 55,999 | 25,670 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,430 | 1,347 | 94.2% |
| uBO Badware | 4,229 | 4,181 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,937 | 1,933 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **779,624** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 779,624 |
| **DNSZeroList.txt** (all sources, deduped) | **525,211** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **356,470** |

Deduplication removed 254,413 duplicate rule instances (32.6% of the raw total).
Dropping OISD Big removes a further 168,741 rules (32.1% of the full list).
