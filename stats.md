# Blocklist stats

_Generated 2026-10-12 20:38:02 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 184,238 | 80,277 | 43.6% |
| HaGeZi Normal | 157,755 | 62,718 | 39.8% |
| AdAway | 6,540 | 3,458 | 52.9% |
| OISD Big | 237,859 | 159,093 | 66.9% |
| Dan Pollock | 13,083 | 9,972 | 76.2% |
| Peter Lowe | 7,130 | 3,886 | 54.5% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 56,887 | 9,233 | 16.2% |
| EasyPrivacy | 56,275 | 26,025 | 46.2% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,450 | 1,368 | 94.3% |
| uBO Badware | 4,264 | 4,214 | 98.8% |
| uBO Quick Fixes | 160 | 151 | 94.4% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **729,875** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 729,875 |
| **DNSZeroList.txt** (all sources, deduped) | **493,106** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **334,013** |

Deduplication removed 236,769 duplicate rule instances (32.4% of the raw total).
Dropping OISD Big removes a further 159,093 rules (32.3% of the full list).
