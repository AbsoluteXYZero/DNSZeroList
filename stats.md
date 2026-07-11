# Blocklist stats

_Generated 2026-07-11 12:58:39 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 156,281 | 56,910 | 36.4% |
| HaGeZi Normal | 160,127 | 63,719 | 39.8% |
| AdAway | 6,540 | 3,479 | 53.2% |
| OISD Big | 328,815 | 246,097 | 74.8% |
| Dan Pollock | 12,935 | 9,755 | 75.4% |
| Peter Lowe | 7,068 | 3,838 | 54.3% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 54,879 | 9,292 | 16.9% |
| EasyPrivacy | 55,488 | 26,686 | 48.1% |
| uBO Ads | 1,786 | 1,738 | 97.3% |
| uBO Privacy | 1,377 | 1,295 | 94.0% |
| uBO Badware | 4,169 | 4,123 | 98.9% |
| uBO Quick Fixes | 95 | 86 | 90.5% |
| uBO Unbreak | 1,928 | 1,923 | 99.7% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **792,004** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 792,004 |
| **DNSZeroList.txt** (all sources, deduped) | **558,344** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **312,247** |

Deduplication removed 233,660 duplicate rule instances (29.5% of the raw total).
Dropping OISD Big removes a further 246,097 rules (44.1% of the full list).
