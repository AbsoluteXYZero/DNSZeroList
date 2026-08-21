# Blocklist stats

_Generated 2026-08-21 00:46:36 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,654 | 75,283 | 42.4% |
| HaGeZi Normal | 187,069 | 84,876 | 45.4% |
| AdAway | 6,540 | 3,460 | 52.9% |
| OISD Big | 268,336 | 185,284 | 69.0% |
| Dan Pollock | 13,019 | 9,865 | 75.8% |
| Peter Lowe | 7,076 | 3,844 | 54.3% |
| Dandelion Sprout | 480 | 295 | 61.5% |
| EasyList | 54,331 | 9,314 | 17.1% |
| EasyPrivacy | 55,869 | 25,616 | 45.9% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,409 | 1,330 | 94.4% |
| uBO Badware | 4,172 | 4,125 | 98.9% |
| uBO Quick Fixes | 89 | 80 | 89.9% |
| uBO Unbreak | 1,935 | 1,930 | 99.7% |
| uBO Resource Abuse | 38 | 36 | 94.7% |
| **Sum (before dedup)** | **779,787** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 779,787 |
| **DNSZeroList.txt** (all sources, deduped) | **536,875** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **351,591** |

Deduplication removed 242,912 duplicate rule instances (31.2% of the raw total).
Dropping OISD Big removes a further 185,284 rules (34.5% of the full list).
