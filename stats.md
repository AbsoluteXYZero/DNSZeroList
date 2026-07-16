# Blocklist stats

_Generated 2026-07-16 13:23:24 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 157,846 | 56,908 | 36.1% |
| HaGeZi Normal | 162,129 | 64,770 | 39.9% |
| AdAway | 6,540 | 3,483 | 53.3% |
| OISD Big | 324,027 | 241,910 | 74.7% |
| Dan Pollock | 12,943 | 9,770 | 75.5% |
| Peter Lowe | 7,082 | 3,844 | 54.3% |
| Dandelion Sprout | 480 | 290 | 60.4% |
| EasyList | 56,335 | 9,319 | 16.5% |
| EasyPrivacy | 55,517 | 26,694 | 48.1% |
| uBO Ads | 1,775 | 1,729 | 97.4% |
| uBO Privacy | 1,380 | 1,298 | 94.1% |
| uBO Badware | 4,173 | 4,127 | 98.9% |
| uBO Quick Fixes | 96 | 86 | 89.6% |
| uBO Unbreak | 1,928 | 1,923 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **792,288** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 792,288 |
| **DNSZeroList.txt** (all sources, deduped) | **556,679** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **314,769** |

Deduplication removed 235,609 duplicate rule instances (29.7% of the raw total).
Dropping OISD Big removes a further 241,910 rules (43.5% of the full list).
