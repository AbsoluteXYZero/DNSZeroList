# Blocklist stats

_Generated 2026-09-25 02:39:13 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 182,724 | 75,446 | 41.3% |
| HaGeZi Normal | 164,176 | 80,430 | 49.0% |
| AdAway | 6,540 | 3,447 | 52.7% |
| OISD Big | 248,533 | 171,417 | 69.0% |
| Dan Pollock | 13,082 | 9,949 | 76.1% |
| Peter Lowe | 7,140 | 3,957 | 55.4% |
| Dandelion Sprout | 480 | 310 | 64.6% |
| EasyList | 59,355 | 9,224 | 15.5% |
| EasyPrivacy | 56,160 | 25,810 | 46.0% |
| uBO Ads | 1,776 | 1,732 | 97.5% |
| uBO Privacy | 1,437 | 1,360 | 94.6% |
| uBO Badware | 4,226 | 4,176 | 98.8% |
| uBO Quick Fixes | 114 | 105 | 92.1% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 37 | 100.0% |
| **Sum (before dedup)** | **747,720** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 747,720 |
| **DNSZeroList.txt** (all sources, deduped) | **519,003** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **347,586** |

Deduplication removed 228,717 duplicate rule instances (30.6% of the raw total).
Dropping OISD Big removes a further 171,417 rules (33.0% of the full list).
