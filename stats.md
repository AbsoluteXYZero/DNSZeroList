# Blocklist stats

_Generated 2026-07-11 01:51:24 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 156,124 | 56,898 | 36.4% |
| HaGeZi Normal | 160,351 | 62,591 | 39.0% |
| AdAway | 6,540 | 3,479 | 53.2% |
| OISD Big | 497,628 | 413,167 | 83.0% |
| Dan Pollock | 12,935 | 9,650 | 74.6% |
| Peter Lowe | 7,068 | 3,837 | 54.3% |
| Dandelion Sprout | 480 | 282 | 58.8% |
| EasyList | 54,744 | 9,309 | 17.0% |
| EasyPrivacy | 55,489 | 26,686 | 48.1% |
| uBO Ads | 1,786 | 1,738 | 97.3% |
| uBO Privacy | 1,378 | 1,296 | 94.0% |
| uBO Badware | 4,169 | 4,123 | 98.9% |
| uBO Quick Fixes | 94 | 85 | 90.4% |
| uBO Unbreak | 1,928 | 1,923 | 99.7% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **960,750** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 960,750 |
| **DNSZeroList.txt** (all sources, deduped) | **725,677** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **312,510** |

Deduplication removed 235,073 duplicate rule instances (24.5% of the raw total).
Dropping OISD Big removes a further 413,167 rules (56.9% of the full list).
