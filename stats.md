# Blocklist stats

_Generated 2026-06-25 14:06:46 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 159,144 | 56,884 | 35.7% |
| HaGeZi Normal | 159,940 | 57,960 | 36.2% |
| AdAway | 6,540 | 3,520 | 53.8% |
| OISD Big | 333,130 | 248,800 | 74.7% |
| Dan Pollock | 12,887 | 9,734 | 75.5% |
| Peter Lowe | 7,050 | 3,837 | 54.4% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 57,943 | 9,355 | 16.1% |
| EasyPrivacy | 55,414 | 26,670 | 48.1% |
| uBO Ads | 1,787 | 1,737 | 97.2% |
| uBO Privacy | 1,362 | 1,281 | 94.1% |
| uBO Badware | 4,145 | 4,100 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,924 | 1,920 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **801,873** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 801,873 |
| **DNSZeroList.txt** (all sources, deduped) | **554,636** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **305,836** |

Deduplication removed 247,237 duplicate rule instances (30.8% of the raw total).
Dropping OISD Big removes a further 248,800 rules (44.9% of the full list).
