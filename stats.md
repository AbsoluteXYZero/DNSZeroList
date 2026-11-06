# Blocklist stats

_Generated 2026-11-06 18:42:29 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 190,137 | 90,478 | 47.6% |
| HaGeZi Normal | 171,417 | 70,777 | 41.3% |
| AdAway | 6,540 | 3,454 | 52.8% |
| OISD Big | 232,734 | 138,704 | 59.6% |
| Dan Pollock | 12,971 | 9,862 | 76.0% |
| Peter Lowe | 7,150 | 3,899 | 54.5% |
| Dandelion Sprout | 490 | 303 | 61.8% |
| EasyList | 53,408 | 9,284 | 17.4% |
| EasyPrivacy | 56,454 | 26,189 | 46.4% |
| uBO Ads | 1,771 | 1,728 | 97.6% |
| uBO Privacy | 1,463 | 1,375 | 94.0% |
| uBO Badware | 4,723 | 4,667 | 98.8% |
| uBO Quick Fixes | 169 | 158 | 93.5% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **741,410** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 741,410 |
| **DNSZeroList.txt** (all sources, deduped) | **497,859** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **359,155** |

Deduplication removed 243,551 duplicate rule instances (32.8% of the raw total).
Dropping OISD Big removes a further 138,704 rules (27.9% of the full list).
