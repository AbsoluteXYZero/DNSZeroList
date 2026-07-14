# Blocklist stats

_Generated 2026-07-14 01:43:32 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 157,097 | 56,864 | 36.2% |
| HaGeZi Normal | 161,434 | 63,199 | 39.1% |
| AdAway | 6,540 | 3,479 | 53.2% |
| OISD Big | 508,458 | 424,055 | 83.4% |
| Dan Pollock | 12,939 | 9,799 | 75.7% |
| Peter Lowe | 7,078 | 3,845 | 54.3% |
| Dandelion Sprout | 480 | 283 | 59.0% |
| EasyList | 55,663 | 9,309 | 16.7% |
| EasyPrivacy | 55,504 | 26,690 | 48.1% |
| uBO Ads | 1,785 | 1,737 | 97.3% |
| uBO Privacy | 1,378 | 1,296 | 94.0% |
| uBO Badware | 4,169 | 4,123 | 98.9% |
| uBO Quick Fixes | 97 | 87 | 89.7% |
| uBO Unbreak | 1,927 | 1,922 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **974,586** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 974,586 |
| **DNSZeroList.txt** (all sources, deduped) | **737,767** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **313,712** |

Deduplication removed 236,819 duplicate rule instances (24.3% of the raw total).
Dropping OISD Big removes a further 424,055 rules (57.5% of the full list).
