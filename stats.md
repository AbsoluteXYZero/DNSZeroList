# Blocklist stats

_Generated 2026-07-28 13:43:06 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 160,922 | 56,686 | 35.2% |
| HaGeZi Normal | 182,036 | 83,107 | 45.7% |
| AdAway | 6,540 | 3,464 | 53.0% |
| OISD Big | 335,874 | 254,177 | 75.7% |
| Dan Pollock | 12,963 | 9,810 | 75.7% |
| Peter Lowe | 7,058 | 3,830 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 59,625 | 9,335 | 15.7% |
| EasyPrivacy | 55,581 | 26,742 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,387 | 1,305 | 94.1% |
| uBO Badware | 4,186 | 4,139 | 98.9% |
| uBO Quick Fixes | 90 | 81 | 90.0% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **830,484** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 830,484 |
| **DNSZeroList.txt** (all sources, deduped) | **588,895** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **334,718** |

Deduplication removed 241,589 duplicate rule instances (29.1% of the raw total).
Dropping OISD Big removes a further 254,177 rules (43.2% of the full list).
