# Blocklist stats

_Generated 2026-07-13 14:09:35 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 156,929 | 56,872 | 36.2% |
| HaGeZi Normal | 161,340 | 62,737 | 38.9% |
| AdAway | 6,540 | 3,479 | 53.2% |
| OISD Big | 508,823 | 424,074 | 83.3% |
| Dan Pollock | 12,935 | 9,794 | 75.7% |
| Peter Lowe | 7,078 | 3,844 | 54.3% |
| Dandelion Sprout | 480 | 282 | 58.8% |
| EasyList | 55,516 | 9,316 | 16.8% |
| EasyPrivacy | 55,500 | 26,690 | 48.1% |
| uBO Ads | 1,785 | 1,737 | 97.3% |
| uBO Privacy | 1,378 | 1,296 | 94.0% |
| uBO Badware | 4,169 | 4,123 | 98.9% |
| uBO Quick Fixes | 97 | 87 | 89.7% |
| uBO Unbreak | 1,927 | 1,922 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **974,534** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 974,534 |
| **DNSZeroList.txt** (all sources, deduped) | **737,622** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **313,548** |

Deduplication removed 236,912 duplicate rule instances (24.3% of the raw total).
Dropping OISD Big removes a further 424,074 rules (57.5% of the full list).
