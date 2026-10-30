# Blocklist stats

_Generated 2026-10-30 17:29:53 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 185,639 | 84,614 | 45.6% |
| HaGeZi Normal | 174,344 | 73,021 | 41.9% |
| AdAway | 6,540 | 3,448 | 52.7% |
| OISD Big | 234,966 | 149,903 | 63.8% |
| Dan Pollock | 12,971 | 9,863 | 76.0% |
| Peter Lowe | 7,156 | 3,897 | 54.5% |
| Dandelion Sprout | 480 | 301 | 62.7% |
| EasyList | 51,325 | 9,248 | 18.0% |
| EasyPrivacy | 56,402 | 26,115 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,458 | 1,371 | 94.0% |
| uBO Badware | 4,685 | 4,638 | 99.0% |
| uBO Quick Fixes | 221 | 210 | 95.0% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **739,945** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 739,945 |
| **DNSZeroList.txt** (all sources, deduped) | **498,413** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **348,510** |

Deduplication removed 241,532 duplicate rule instances (32.6% of the raw total).
Dropping OISD Big removes a further 149,903 rules (30.1% of the full list).
