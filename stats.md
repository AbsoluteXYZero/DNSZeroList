# Blocklist stats

_Generated 2026-06-22 16:30:51 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,223 | 56,934 | 36.0% |
| HaGeZi Normal | 158,821 | 57,109 | 36.0% |
| AdAway | 6,540 | 3,536 | 54.1% |
| OISD Big | 332,185 | 247,493 | 74.5% |
| Dan Pollock | 12,881 | 9,750 | 75.7% |
| Peter Lowe | 7,046 | 3,834 | 54.4% |
| Dandelion Sprout | 480 | 284 | 59.2% |
| EasyList | 57,067 | 9,334 | 16.4% |
| EasyPrivacy | 55,386 | 26,638 | 48.1% |
| uBO Ads | 1,786 | 1,736 | 97.2% |
| uBO Privacy | 1,362 | 1,281 | 94.1% |
| uBO Badware | 4,151 | 4,103 | 98.8% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,924 | 1,920 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **797,979** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 797,979 |
| **DNSZeroList.txt** (all sources, deduped) | **552,308** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **304,815** |

Deduplication removed 245,671 duplicate rule instances (30.8% of the raw total).
Dropping OISD Big removes a further 247,493 rules (44.8% of the full list).
