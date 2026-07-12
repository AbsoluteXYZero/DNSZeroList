# Blocklist stats

_Generated 2026-07-12 01:53:43 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 156,457 | 56,900 | 36.4% |
| HaGeZi Normal | 160,709 | 62,637 | 39.0% |
| AdAway | 6,540 | 3,478 | 53.2% |
| OISD Big | 503,369 | 418,824 | 83.2% |
| Dan Pollock | 12,935 | 9,722 | 75.2% |
| Peter Lowe | 7,078 | 3,844 | 54.3% |
| Dandelion Sprout | 480 | 279 | 58.1% |
| EasyList | 55,063 | 9,307 | 16.9% |
| EasyPrivacy | 55,490 | 26,687 | 48.1% |
| uBO Ads | 1,786 | 1,738 | 97.3% |
| uBO Privacy | 1,377 | 1,295 | 94.0% |
| uBO Badware | 4,169 | 4,123 | 98.9% |
| uBO Quick Fixes | 97 | 87 | 89.7% |
| uBO Unbreak | 1,928 | 1,923 | 99.7% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **967,514** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 967,514 |
| **DNSZeroList.txt** (all sources, deduped) | **731,723** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **312,899** |

Deduplication removed 235,791 duplicate rule instances (24.4% of the raw total).
Dropping OISD Big removes a further 418,824 rules (57.2% of the full list).
