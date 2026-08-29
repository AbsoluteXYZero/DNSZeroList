# Blocklist stats

_Generated 2026-08-29 15:57:47 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 178,821 | 75,027 | 42.0% |
| HaGeZi Normal | 190,873 | 86,188 | 45.2% |
| AdAway | 6,540 | 3,461 | 52.9% |
| OISD Big | 269,577 | 185,307 | 68.7% |
| Dan Pollock | 13,045 | 9,893 | 75.8% |
| Peter Lowe | 7,092 | 3,857 | 54.4% |
| Dandelion Sprout | 480 | 298 | 62.1% |
| EasyList | 55,528 | 9,220 | 16.6% |
| EasyPrivacy | 55,935 | 25,635 | 45.8% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,425 | 1,344 | 94.3% |
| uBO Badware | 4,199 | 4,152 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,936 | 1,932 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **787,350** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 787,350 |
| **DNSZeroList.txt** (all sources, deduped) | **539,652** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **354,345** |

Deduplication removed 247,698 duplicate rule instances (31.5% of the raw total).
Dropping OISD Big removes a further 185,307 rules (34.3% of the full list).
