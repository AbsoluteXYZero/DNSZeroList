# Blocklist stats

_Generated 2026-08-15 12:19:58 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 156,010 | 56,991 | 36.5% |
| HaGeZi Normal | 181,570 | 82,516 | 45.4% |
| AdAway | 6,540 | 3,462 | 52.9% |
| OISD Big | 267,142 | 185,317 | 69.4% |
| Dan Pollock | 13,008 | 9,857 | 75.8% |
| Peter Lowe | 7,074 | 3,842 | 54.3% |
| Dandelion Sprout | 480 | 294 | 61.3% |
| EasyList | 54,156 | 9,324 | 17.2% |
| EasyPrivacy | 55,700 | 26,784 | 48.1% |
| uBO Ads | 1,769 | 1,725 | 97.5% |
| uBO Privacy | 1,407 | 1,328 | 94.4% |
| uBO Badware | 4,165 | 4,121 | 98.9% |
| uBO Quick Fixes | 90 | 81 | 90.0% |
| uBO Unbreak | 1,934 | 1,929 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **751,082** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 751,082 |
| **DNSZeroList.txt** (all sources, deduped) | **513,935** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **328,618** |

Deduplication removed 237,147 duplicate rule instances (31.6% of the raw total).
Dropping OISD Big removes a further 185,317 rules (36.1% of the full list).
