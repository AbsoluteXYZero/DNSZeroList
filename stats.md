# Blocklist stats

_Generated 2026-09-18 02:22:42 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 180,344 | 74,766 | 41.5% |
| HaGeZi Normal | 197,602 | 94,721 | 47.9% |
| AdAway | 6,540 | 3,458 | 52.9% |
| OISD Big | 246,977 | 167,252 | 67.7% |
| Dan Pollock | 13,078 | 9,927 | 75.9% |
| Peter Lowe | 7,152 | 3,891 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 57,110 | 9,214 | 16.1% |
| EasyPrivacy | 56,069 | 25,692 | 45.8% |
| uBO Ads | 1,763 | 1,719 | 97.5% |
| uBO Privacy | 1,435 | 1,354 | 94.4% |
| uBO Badware | 4,134 | 4,085 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,939 | 1,935 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **774,753** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 774,753 |
| **DNSZeroList.txt** (all sources, deduped) | **530,402** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **363,150** |

Deduplication removed 244,351 duplicate rule instances (31.5% of the raw total).
Dropping OISD Big removes a further 167,252 rules (31.5% of the full list).
