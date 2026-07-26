# Blocklist stats

_Generated 2026-07-26 01:56:51 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 160,248 | 56,747 | 35.4% |
| HaGeZi Normal | 180,714 | 82,571 | 45.7% |
| AdAway | 6,540 | 3,464 | 53.0% |
| OISD Big | 334,002 | 252,669 | 75.6% |
| Dan Pollock | 12,961 | 9,807 | 75.7% |
| Peter Lowe | 7,058 | 3,830 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 58,980 | 9,325 | 15.8% |
| EasyPrivacy | 55,565 | 26,738 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,385 | 1,303 | 94.1% |
| uBO Badware | 4,185 | 4,138 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **825,953** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 825,953 |
| **DNSZeroList.txt** (all sources, deduped) | **586,174** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **333,505** |

Deduplication removed 239,779 duplicate rule instances (29.0% of the raw total).
Dropping OISD Big removes a further 252,669 rules (43.1% of the full list).
