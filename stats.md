# Blocklist stats

_Generated 2026-10-06 03:59:52 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 178,724 | 77,315 | 43.3% |
| HaGeZi Normal | 173,200 | 61,946 | 35.8% |
| AdAway | 6,540 | 3,458 | 52.9% |
| OISD Big | 240,506 | 147,364 | 61.3% |
| Dan Pollock | 13,083 | 9,981 | 76.3% |
| Peter Lowe | 7,136 | 3,887 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 54,995 | 9,234 | 16.8% |
| EasyPrivacy | 56,230 | 25,747 | 45.8% |
| uBO Ads | 1,777 | 1,734 | 97.6% |
| uBO Privacy | 1,445 | 1,363 | 94.3% |
| uBO Badware | 4,253 | 4,202 | 98.8% |
| uBO Quick Fixes | 148 | 139 | 93.9% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **740,494** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 740,494 |
| **DNSZeroList.txt** (all sources, deduped) | **488,794** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **341,430** |

Deduplication removed 251,700 duplicate rule instances (34.0% of the raw total).
Dropping OISD Big removes a further 147,364 rules (30.1% of the full list).
