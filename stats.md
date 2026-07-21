# Blocklist stats

_Generated 2026-07-21 13:19:40 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,937 | 56,788 | 35.7% |
| HaGeZi Normal | 178,942 | 82,071 | 45.9% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 329,005 | 248,403 | 75.5% |
| Dan Pollock | 12,950 | 9,796 | 75.6% |
| Peter Lowe | 7,068 | 3,835 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 57,749 | 9,314 | 16.1% |
| EasyPrivacy | 55,542 | 26,732 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,383 | 1,301 | 94.1% |
| uBO Badware | 4,185 | 4,138 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **816,616** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 816,616 |
| **DNSZeroList.txt** (all sources, deduped) | **580,069** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **331,666** |

Deduplication removed 236,547 duplicate rule instances (29.0% of the raw total).
Dropping OISD Big removes a further 248,403 rules (42.8% of the full list).
