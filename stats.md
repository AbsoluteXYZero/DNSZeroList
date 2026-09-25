# Blocklist stats

_Generated 2026-09-25 16:11:56 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 182,881 | 75,437 | 41.2% |
| HaGeZi Normal | 164,218 | 80,592 | 49.1% |
| AdAway | 6,540 | 3,448 | 52.7% |
| OISD Big | 244,086 | 168,129 | 68.9% |
| Dan Pollock | 13,082 | 9,946 | 76.0% |
| Peter Lowe | 7,132 | 3,952 | 55.4% |
| Dandelion Sprout | 480 | 309 | 64.4% |
| EasyList | 59,515 | 9,240 | 15.5% |
| EasyPrivacy | 56,165 | 25,814 | 46.0% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,437 | 1,360 | 94.6% |
| uBO Badware | 4,227 | 4,177 | 98.8% |
| uBO Quick Fixes | 136 | 127 | 93.4% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 37 | 100.0% |
| **Sum (before dedup)** | **743,652** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 743,652 |
| **DNSZeroList.txt** (all sources, deduped) | **515,829** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **347,700** |

Deduplication removed 227,823 duplicate rule instances (30.6% of the raw total).
Dropping OISD Big removes a further 168,129 rules (32.6% of the full list).
