# Blocklist stats

_Generated 2026-07-29 01:48:44 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 161,063 | 56,711 | 35.2% |
| HaGeZi Normal | 182,128 | 83,038 | 45.6% |
| AdAway | 6,540 | 3,464 | 53.0% |
| OISD Big | 337,298 | 254,907 | 75.6% |
| Dan Pollock | 12,963 | 9,810 | 75.7% |
| Peter Lowe | 7,058 | 3,830 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 59,757 | 9,342 | 15.6% |
| EasyPrivacy | 55,595 | 26,748 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,387 | 1,305 | 94.1% |
| uBO Badware | 4,186 | 4,139 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **832,288** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 832,288 |
| **DNSZeroList.txt** (all sources, deduped) | **589,826** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **334,919** |

Deduplication removed 242,462 duplicate rule instances (29.1% of the raw total).
Dropping OISD Big removes a further 254,907 rules (43.2% of the full list).
