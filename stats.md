# Blocklist stats

_Generated 2026-10-26 02:26:36 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 192,039 | 81,340 | 42.4% |
| HaGeZi Normal | 178,832 | 74,209 | 41.5% |
| AdAway | 6,540 | 3,449 | 52.7% |
| OISD Big | 233,655 | 148,166 | 63.4% |
| Dan Pollock | 12,971 | 9,858 | 76.0% |
| Peter Lowe | 7,158 | 3,896 | 54.4% |
| Dandelion Sprout | 480 | 301 | 62.7% |
| EasyList | 61,384 | 9,241 | 15.1% |
| EasyPrivacy | 56,370 | 26,079 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,454 | 1,368 | 94.1% |
| uBO Badware | 4,855 | 4,805 | 99.0% |
| uBO Quick Fixes | 221 | 210 | 95.0% |
| uBO Unbreak | 1,944 | 1,940 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **759,715** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 759,715 |
| **DNSZeroList.txt** (all sources, deduped) | **506,169** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **358,003** |

Deduplication removed 253,546 duplicate rule instances (33.4% of the raw total).
Dropping OISD Big removes a further 148,166 rules (29.3% of the full list).
