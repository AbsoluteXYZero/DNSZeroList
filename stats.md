# Blocklist stats

_Generated 2026-07-17 13:07:57 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,153 | 56,906 | 36.0% |
| HaGeZi Normal | 176,945 | 79,111 | 44.7% |
| AdAway | 6,540 | 3,483 | 53.3% |
| OISD Big | 324,621 | 242,094 | 74.6% |
| Dan Pollock | 12,944 | 9,773 | 75.5% |
| Peter Lowe | 7,066 | 3,836 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 56,608 | 9,306 | 16.4% |
| EasyPrivacy | 55,521 | 26,694 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,380 | 1,298 | 94.1% |
| uBO Badware | 4,173 | 4,126 | 98.9% |
| uBO Quick Fixes | 96 | 86 | 89.6% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **808,269** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 808,269 |
| **DNSZeroList.txt** (all sources, deduped) | **571,704** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **329,610** |

Deduplication removed 236,565 duplicate rule instances (29.3% of the raw total).
Dropping OISD Big removes a further 242,094 rules (42.3% of the full list).
