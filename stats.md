# Blocklist stats

_Generated 2026-10-15 02:29:34 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 184,643 | 79,950 | 43.3% |
| HaGeZi Normal | 159,810 | 63,814 | 39.9% |
| AdAway | 6,540 | 3,449 | 52.7% |
| OISD Big | 238,080 | 158,914 | 66.7% |
| Dan Pollock | 13,084 | 9,972 | 76.2% |
| Peter Lowe | 7,130 | 3,884 | 54.5% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 57,664 | 9,235 | 16.0% |
| EasyPrivacy | 56,290 | 26,029 | 46.2% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,450 | 1,366 | 94.2% |
| uBO Badware | 4,266 | 4,216 | 98.8% |
| uBO Quick Fixes | 183 | 172 | 94.0% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **733,374** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 733,374 |
| **DNSZeroList.txt** (all sources, deduped) | **494,612** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **335,698** |

Deduplication removed 238,762 duplicate rule instances (32.6% of the raw total).
Dropping OISD Big removes a further 158,914 rules (32.1% of the full list).
