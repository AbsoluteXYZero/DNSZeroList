# Blocklist stats

_Generated 2026-07-05 02:11:51 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 155,042 | 57,003 | 36.8% |
| HaGeZi Normal | 154,264 | 56,635 | 36.7% |
| AdAway | 6,540 | 3,533 | 54.0% |
| OISD Big | 503,870 | 423,147 | 84.0% |
| Dan Pollock | 12,909 | 9,698 | 75.1% |
| Peter Lowe | 7,058 | 3,844 | 54.5% |
| Dandelion Sprout | 480 | 280 | 58.3% |
| EasyList | 53,804 | 9,330 | 17.3% |
| EasyPrivacy | 55,465 | 26,656 | 48.1% |
| uBO Ads | 1,787 | 1,738 | 97.3% |
| uBO Privacy | 1,372 | 1,290 | 94.0% |
| uBO Badware | 4,163 | 4,118 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,925 | 1,921 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **958,808** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 958,808 |
| **DNSZeroList.txt** (all sources, deduped) | **725,855** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **302,708** |

Deduplication removed 232,953 duplicate rule instances (24.3% of the raw total).
Dropping OISD Big removes a further 423,147 rules (58.3% of the full list).
