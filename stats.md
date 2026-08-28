# Blocklist stats

_Generated 2026-08-28 21:36:13 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 178,608 | 75,042 | 42.0% |
| HaGeZi Normal | 190,338 | 86,008 | 45.2% |
| AdAway | 6,540 | 3,461 | 52.9% |
| OISD Big | 267,709 | 183,596 | 68.6% |
| Dan Pollock | 13,044 | 9,892 | 75.8% |
| Peter Lowe | 7,074 | 3,844 | 54.3% |
| Dandelion Sprout | 480 | 297 | 61.9% |
| EasyList | 55,315 | 9,206 | 16.6% |
| EasyPrivacy | 55,932 | 25,634 | 45.8% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,425 | 1,344 | 94.3% |
| uBO Badware | 4,199 | 4,152 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,936 | 1,932 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **784,499** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 784,499 |
| **DNSZeroList.txt** (all sources, deduped) | **537,472** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **353,876** |

Deduplication removed 247,027 duplicate rule instances (31.5% of the raw total).
Dropping OISD Big removes a further 183,596 rules (34.2% of the full list).
