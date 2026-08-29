# Blocklist stats

_Generated 2026-08-29 04:54:10 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 178,696 | 75,049 | 42.0% |
| HaGeZi Normal | 190,338 | 86,006 | 45.2% |
| AdAway | 6,540 | 3,461 | 52.9% |
| OISD Big | 269,086 | 184,971 | 68.7% |
| Dan Pollock | 13,045 | 9,893 | 75.8% |
| Peter Lowe | 7,074 | 3,844 | 54.3% |
| Dandelion Sprout | 480 | 298 | 62.1% |
| EasyList | 55,394 | 9,206 | 16.6% |
| EasyPrivacy | 55,934 | 25,634 | 45.8% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,425 | 1,344 | 94.3% |
| uBO Badware | 4,199 | 4,152 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,936 | 1,932 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **786,046** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 786,046 |
| **DNSZeroList.txt** (all sources, deduped) | **538,936** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **353,965** |

Deduplication removed 247,110 duplicate rule instances (31.4% of the raw total).
Dropping OISD Big removes a further 184,971 rules (34.3% of the full list).
