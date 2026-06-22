# Blocklist stats

_Generated 2026-06-22 02:54:05 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,692 | 56,952 | 35.9% |
| HaGeZi Normal | 158,993 | 55,649 | 35.0% |
| AdAway | 6,540 | 3,535 | 54.1% |
| OISD Big | 496,811 | 410,802 | 82.7% |
| Dan Pollock | 12,881 | 9,727 | 75.5% |
| Peter Lowe | 7,040 | 3,830 | 54.4% |
| Dandelion Sprout | 480 | 280 | 58.3% |
| EasyList | 57,617 | 9,383 | 16.3% |
| EasyPrivacy | 55,386 | 26,629 | 48.1% |
| uBO Ads | 1,786 | 1,736 | 97.2% |
| uBO Privacy | 1,362 | 1,281 | 94.1% |
| uBO Badware | 4,150 | 4,102 | 98.8% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,924 | 1,920 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **963,789** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 963,789 |
| **DNSZeroList.txt** (all sources, deduped) | **715,974** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **305,172** |

Deduplication removed 247,815 duplicate rule instances (25.7% of the raw total).
Dropping OISD Big removes a further 410,802 rules (57.4% of the full list).
