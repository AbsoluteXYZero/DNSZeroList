# Blocklist stats

_Generated 2026-10-10 03:31:03 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 181,688 | 78,664 | 43.3% |
| HaGeZi Normal | 158,980 | 62,318 | 39.2% |
| AdAway | 6,540 | 3,456 | 52.8% |
| OISD Big | 240,619 | 160,271 | 66.6% |
| Dan Pollock | 13,083 | 9,979 | 76.3% |
| Peter Lowe | 7,126 | 3,884 | 54.5% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 56,124 | 9,234 | 16.5% |
| EasyPrivacy | 56,262 | 26,001 | 46.2% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,444 | 1,361 | 94.3% |
| uBO Badware | 4,263 | 4,212 | 98.8% |
| uBO Quick Fixes | 160 | 151 | 94.4% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **730,523** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 730,523 |
| **DNSZeroList.txt** (all sources, deduped) | **491,447** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **331,176** |

Deduplication removed 239,076 duplicate rule instances (32.7% of the raw total).
Dropping OISD Big removes a further 160,271 rules (32.6% of the full list).
