# Blocklist stats

_Generated 2026-08-16 00:45:46 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 156,397 | 56,990 | 36.4% |
| HaGeZi Normal | 181,570 | 82,333 | 45.3% |
| AdAway | 6,540 | 3,462 | 52.9% |
| OISD Big | 267,710 | 185,691 | 69.4% |
| Dan Pollock | 13,008 | 9,857 | 75.8% |
| Peter Lowe | 7,074 | 3,842 | 54.3% |
| Dandelion Sprout | 480 | 294 | 61.3% |
| EasyList | 54,306 | 9,319 | 17.2% |
| EasyPrivacy | 55,934 | 26,787 | 47.9% |
| uBO Ads | 1,769 | 1,725 | 97.5% |
| uBO Privacy | 1,407 | 1,328 | 94.4% |
| uBO Badware | 4,165 | 4,121 | 98.9% |
| uBO Quick Fixes | 90 | 81 | 90.0% |
| uBO Unbreak | 1,934 | 1,929 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **752,421** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 752,421 |
| **DNSZeroList.txt** (all sources, deduped) | **514,476** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **328,785** |

Deduplication removed 237,945 duplicate rule instances (31.6% of the raw total).
Dropping OISD Big removes a further 185,691 rules (36.1% of the full list).
