# Blocklist stats

_Generated 2026-07-07 14:10:07 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 154,986 | 56,984 | 36.8% |
| HaGeZi Normal | 161,630 | 63,741 | 39.4% |
| AdAway | 6,540 | 3,534 | 54.0% |
| OISD Big | 327,571 | 245,417 | 74.9% |
| Dan Pollock | 12,915 | 9,754 | 75.5% |
| Peter Lowe | 7,060 | 3,837 | 54.3% |
| Dandelion Sprout | 480 | 284 | 59.2% |
| EasyList | 53,668 | 9,302 | 17.3% |
| EasyPrivacy | 55,470 | 26,684 | 48.1% |
| uBO Ads | 1,787 | 1,738 | 97.3% |
| uBO Privacy | 1,374 | 1,292 | 94.0% |
| uBO Badware | 4,166 | 4,121 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,925 | 1,920 | 99.7% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **789,701** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 789,701 |
| **DNSZeroList.txt** (all sources, deduped) | **556,412** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **310,995** |

Deduplication removed 233,289 duplicate rule instances (29.5% of the raw total).
Dropping OISD Big removes a further 245,417 rules (44.1% of the full list).
