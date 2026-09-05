# Blocklist stats

_Generated 2026-09-05 14:16:55 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 180,357 | 74,950 | 41.6% |
| HaGeZi Normal | 192,747 | 87,108 | 45.2% |
| AdAway | 6,540 | 3,464 | 53.0% |
| OISD Big | 256,763 | 168,929 | 65.8% |
| Dan Pollock | 13,057 | 9,911 | 75.9% |
| Peter Lowe | 7,112 | 3,867 | 54.4% |
| Dandelion Sprout | 480 | 298 | 62.1% |
| EasyList | 56,933 | 9,207 | 16.2% |
| EasyPrivacy | 55,997 | 25,670 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,430 | 1,347 | 94.2% |
| uBO Badware | 4,229 | 4,181 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,936 | 1,932 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **779,479** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 779,479 |
| **DNSZeroList.txt** (all sources, deduped) | **525,334** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **356,405** |

Deduplication removed 254,145 duplicate rule instances (32.6% of the raw total).
Dropping OISD Big removes a further 168,929 rules (32.2% of the full list).
