# Blocklist stats

_Generated 2026-10-05 22:24:46 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 178,674 | 77,312 | 43.3% |
| HaGeZi Normal | 173,200 | 61,898 | 35.7% |
| AdAway | 6,540 | 3,458 | 52.9% |
| OISD Big | 240,963 | 147,814 | 61.3% |
| Dan Pollock | 13,083 | 9,981 | 76.3% |
| Peter Lowe | 7,136 | 3,887 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 54,930 | 9,215 | 16.8% |
| EasyPrivacy | 56,228 | 25,746 | 45.8% |
| uBO Ads | 1,777 | 1,734 | 97.6% |
| uBO Privacy | 1,445 | 1,363 | 94.3% |
| uBO Badware | 4,253 | 4,202 | 98.8% |
| uBO Quick Fixes | 148 | 139 | 93.9% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **740,834** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 740,834 |
| **DNSZeroList.txt** (all sources, deduped) | **489,176** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **341,362** |

Deduplication removed 251,658 duplicate rule instances (34.0% of the raw total).
Dropping OISD Big removes a further 147,814 rules (30.2% of the full list).
