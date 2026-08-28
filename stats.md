# Blocklist stats

_Generated 2026-08-28 08:07:34 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 178,428 | 75,071 | 42.1% |
| HaGeZi Normal | 190,021 | 85,931 | 45.2% |
| AdAway | 6,540 | 3,461 | 52.9% |
| OISD Big | 267,428 | 183,404 | 68.6% |
| Dan Pollock | 13,044 | 9,892 | 75.8% |
| Peter Lowe | 7,072 | 3,842 | 54.3% |
| Dandelion Sprout | 480 | 296 | 61.7% |
| EasyList | 55,150 | 9,212 | 16.7% |
| EasyPrivacy | 55,930 | 25,634 | 45.8% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,425 | 1,344 | 94.3% |
| uBO Badware | 4,198 | 4,151 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,936 | 1,932 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **783,551** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 783,551 |
| **DNSZeroList.txt** (all sources, deduped) | **537,011** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **353,607** |

Deduplication removed 246,540 duplicate rule instances (31.5% of the raw total).
Dropping OISD Big removes a further 183,404 rules (34.2% of the full list).
