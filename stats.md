# Blocklist stats

_Generated 2026-11-07 03:51:17 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 190,283 | 90,482 | 47.6% |
| HaGeZi Normal | 171,417 | 70,783 | 41.3% |
| AdAway | 6,540 | 3,454 | 52.8% |
| OISD Big | 232,503 | 138,314 | 59.5% |
| Dan Pollock | 12,971 | 9,862 | 76.0% |
| Peter Lowe | 7,150 | 3,899 | 54.5% |
| Dandelion Sprout | 490 | 303 | 61.8% |
| EasyList | 53,515 | 9,251 | 17.3% |
| EasyPrivacy | 56,454 | 26,189 | 46.4% |
| uBO Ads | 1,771 | 1,728 | 97.6% |
| uBO Privacy | 1,463 | 1,375 | 94.0% |
| uBO Badware | 4,723 | 4,667 | 98.8% |
| uBO Quick Fixes | 169 | 158 | 93.5% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **741,432** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 741,432 |
| **DNSZeroList.txt** (all sources, deduped) | **497,580** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **359,266** |

Deduplication removed 243,852 duplicate rule instances (32.9% of the raw total).
Dropping OISD Big removes a further 138,314 rules (27.8% of the full list).
