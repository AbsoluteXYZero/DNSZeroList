# Blocklist stats

_Generated 2026-06-23 14:30:29 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,493 | 57,733 | 36.4% |
| HaGeZi Normal | 145,421 | 54,735 | 37.6% |
| AdAway | 6,540 | 3,534 | 54.0% |
| OISD Big | 489,116 | 406,720 | 83.2% |
| Dan Pollock | 12,882 | 9,655 | 74.9% |
| Peter Lowe | 7,048 | 3,887 | 55.2% |
| Dandelion Sprout | 480 | 284 | 59.2% |
| EasyList | 57,340 | 9,355 | 16.3% |
| EasyPrivacy | 55,398 | 26,740 | 48.3% |
| uBO Ads | 1,787 | 1,737 | 97.2% |
| uBO Privacy | 1,362 | 1,285 | 94.3% |
| uBO Badware | 4,152 | 4,104 | 98.8% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,924 | 1,920 | 99.8% |
| uBO Resource Abuse | 36 | 36 | 100.0% |
| **Sum (before dedup)** | **942,070** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 942,070 |
| **DNSZeroList.txt** (all sources, deduped) | **706,716** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **299,996** |

Deduplication removed 235,354 duplicate rule instances (25.0% of the raw total).
Dropping OISD Big removes a further 406,720 rules (57.6% of the full list).
