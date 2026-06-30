# Blocklist stats

_Generated 2026-06-30 02:35:04 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 153,443 | 56,967 | 37.1% |
| HaGeZi Normal | 166,478 | 64,250 | 38.6% |
| AdAway | 6,540 | 3,528 | 53.9% |
| OISD Big | 336,212 | 250,420 | 74.5% |
| Dan Pollock | 12,898 | 9,654 | 74.8% |
| Peter Lowe | 7,064 | 3,844 | 54.4% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 52,263 | 9,313 | 17.8% |
| EasyPrivacy | 55,440 | 26,667 | 48.1% |
| uBO Ads | 1,787 | 1,737 | 97.2% |
| uBO Privacy | 1,372 | 1,290 | 94.0% |
| uBO Badware | 4,150 | 4,105 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,925 | 1,921 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **800,181** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 800,181 |
| **DNSZeroList.txt** (all sources, deduped) | **563,059** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **312,639** |

Deduplication removed 237,122 duplicate rule instances (29.6% of the raw total).
Dropping OISD Big removes a further 250,420 rules (44.5% of the full list).
