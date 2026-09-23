# Blocklist stats

_Generated 2026-09-23 15:49:33 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 182,238 | 75,556 | 41.5% |
| HaGeZi Normal | 162,618 | 80,238 | 49.3% |
| AdAway | 6,540 | 3,454 | 52.8% |
| OISD Big | 247,430 | 171,400 | 69.3% |
| Dan Pollock | 13,082 | 9,938 | 76.0% |
| Peter Lowe | 7,140 | 3,955 | 55.4% |
| Dandelion Sprout | 480 | 312 | 65.0% |
| EasyList | 58,915 | 9,227 | 15.7% |
| EasyPrivacy | 56,150 | 25,807 | 46.0% |
| uBO Ads | 1,776 | 1,732 | 97.5% |
| uBO Privacy | 1,437 | 1,360 | 94.6% |
| uBO Badware | 4,226 | 4,176 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 37 | 100.0% |
| **Sum (before dedup)** | **744,102** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 744,102 |
| **DNSZeroList.txt** (all sources, deduped) | **517,377** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **345,977** |

Deduplication removed 226,725 duplicate rule instances (30.5% of the raw total).
Dropping OISD Big removes a further 171,400 rules (33.1% of the full list).
