# Blocklist stats

_Generated 2026-10-09 17:45:43 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 181,580 | 79,119 | 43.6% |
| HaGeZi Normal | 158,769 | 62,413 | 39.3% |
| AdAway | 6,540 | 3,456 | 52.8% |
| OISD Big | 240,335 | 160,572 | 66.8% |
| Dan Pollock | 13,083 | 9,979 | 76.3% |
| Peter Lowe | 7,126 | 3,883 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 56,030 | 9,246 | 16.5% |
| EasyPrivacy | 56,261 | 26,000 | 46.2% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,444 | 1,361 | 94.3% |
| uBO Badware | 4,263 | 4,212 | 98.8% |
| uBO Quick Fixes | 160 | 151 | 94.4% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **729,825** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 729,825 |
| **DNSZeroList.txt** (all sources, deduped) | **491,755** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **331,183** |

Deduplication removed 238,070 duplicate rule instances (32.6% of the raw total).
Dropping OISD Big removes a further 160,572 rules (32.7% of the full list).
