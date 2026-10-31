# Blocklist stats

_Generated 2026-10-31 03:25:44 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 185,803 | 84,615 | 45.5% |
| HaGeZi Normal | 174,344 | 73,040 | 41.9% |
| AdAway | 6,540 | 3,448 | 52.7% |
| OISD Big | 235,098 | 149,982 | 63.8% |
| Dan Pollock | 12,971 | 9,863 | 76.0% |
| Peter Lowe | 7,156 | 3,897 | 54.5% |
| Dandelion Sprout | 480 | 301 | 62.7% |
| EasyList | 51,479 | 9,246 | 18.0% |
| EasyPrivacy | 56,404 | 26,115 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,458 | 1,371 | 94.0% |
| uBO Badware | 4,685 | 4,638 | 99.0% |
| uBO Quick Fixes | 221 | 210 | 95.0% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **740,397** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 740,397 |
| **DNSZeroList.txt** (all sources, deduped) | **498,650** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **348,668** |

Deduplication removed 241,747 duplicate rule instances (32.7% of the raw total).
Dropping OISD Big removes a further 149,982 rules (30.1% of the full list).
