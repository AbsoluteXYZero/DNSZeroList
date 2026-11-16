# Blocklist stats

_Generated 2026-11-16 03:57:33 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 192,134 | 79,973 | 41.6% |
| HaGeZi Normal | 223,869 | 95,558 | 42.7% |
| AdAway | 6,540 | 3,301 | 50.5% |
| OISD Big | 228,409 | 131,399 | 57.5% |
| Dan Pollock | 13,090 | 9,912 | 75.7% |
| Peter Lowe | 7,160 | 3,885 | 54.3% |
| Dandelion Sprout | 490 | 306 | 62.4% |
| EasyList | 53,809 | 9,260 | 17.2% |
| EasyPrivacy | 56,620 | 26,002 | 45.9% |
| uBO Ads | 1,766 | 1,722 | 97.5% |
| uBO Privacy | 1,471 | 1,379 | 93.7% |
| uBO Badware | 4,741 | 4,685 | 98.8% |
| uBO Quick Fixes | 172 | 161 | 93.6% |
| uBO Unbreak | 1,951 | 1,947 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **792,259** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 792,259 |
| **DNSZeroList.txt** (all sources, deduped) | **517,819** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **386,420** |

Deduplication removed 274,440 duplicate rule instances (34.6% of the raw total).
Dropping OISD Big removes a further 131,399 rules (25.4% of the full list).
