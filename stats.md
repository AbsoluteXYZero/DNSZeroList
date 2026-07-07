# Blocklist stats

_Generated 2026-07-07 02:12:11 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 154,823 | 56,996 | 36.8% |
| HaGeZi Normal | 161,835 | 63,857 | 39.5% |
| AdAway | 6,540 | 3,534 | 54.0% |
| OISD Big | 327,208 | 245,050 | 74.9% |
| Dan Pollock | 12,915 | 9,754 | 75.5% |
| Peter Lowe | 7,058 | 3,835 | 54.3% |
| Dandelion Sprout | 480 | 284 | 59.2% |
| EasyList | 53,515 | 9,303 | 17.4% |
| EasyPrivacy | 55,469 | 26,684 | 48.1% |
| uBO Ads | 1,787 | 1,738 | 97.3% |
| uBO Privacy | 1,372 | 1,290 | 94.0% |
| uBO Badware | 4,164 | 4,119 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,925 | 1,920 | 99.7% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **789,220** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 789,220 |
| **DNSZeroList.txt** (all sources, deduped) | **556,027** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **310,977** |

Deduplication removed 233,193 duplicate rule instances (29.5% of the raw total).
Dropping OISD Big removes a further 245,050 rules (44.1% of the full list).
