# Blocklist stats

_Generated 2026-06-26 14:06:03 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 159,215 | 56,858 | 35.7% |
| HaGeZi Normal | 160,559 | 56,416 | 35.1% |
| AdAway | 6,540 | 3,527 | 53.9% |
| OISD Big | 481,572 | 395,030 | 82.0% |
| Dan Pollock | 12,890 | 9,770 | 75.8% |
| Peter Lowe | 7,044 | 3,835 | 54.4% |
| Dandelion Sprout | 480 | 279 | 58.1% |
| EasyList | 58,258 | 9,360 | 16.1% |
| EasyPrivacy | 55,421 | 26,659 | 48.1% |
| uBO Ads | 1,787 | 1,737 | 97.2% |
| uBO Privacy | 1,363 | 1,282 | 94.1% |
| uBO Badware | 4,147 | 4,102 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,924 | 1,920 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **951,327** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 951,327 |
| **DNSZeroList.txt** (all sources, deduped) | **701,435** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **306,405** |

Deduplication removed 249,892 duplicate rule instances (26.3% of the raw total).
Dropping OISD Big removes a further 395,030 rules (56.3% of the full list).
