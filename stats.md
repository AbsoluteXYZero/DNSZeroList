# Blocklist stats

_Generated 2026-08-20 12:28:58 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,505 | 75,252 | 42.4% |
| HaGeZi Normal | 187,031 | 84,830 | 45.4% |
| AdAway | 6,540 | 3,459 | 52.9% |
| OISD Big | 268,441 | 185,300 | 69.0% |
| Dan Pollock | 13,018 | 9,864 | 75.8% |
| Peter Lowe | 7,076 | 3,844 | 54.3% |
| Dandelion Sprout | 480 | 293 | 61.0% |
| EasyList | 54,190 | 9,314 | 17.2% |
| EasyPrivacy | 55,850 | 25,605 | 45.8% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,408 | 1,329 | 94.4% |
| uBO Badware | 4,172 | 4,126 | 98.9% |
| uBO Quick Fixes | 89 | 80 | 89.9% |
| uBO Unbreak | 1,935 | 1,930 | 99.7% |
| uBO Resource Abuse | 38 | 36 | 94.7% |
| **Sum (before dedup)** | **779,543** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 779,543 |
| **DNSZeroList.txt** (all sources, deduped) | **536,726** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **351,426** |

Deduplication removed 242,817 duplicate rule instances (31.1% of the raw total).
Dropping OISD Big removes a further 185,300 rules (34.5% of the full list).
