# Blocklist stats

_Generated 2026-10-16 15:49:01 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 185,446 | 79,753 | 43.0% |
| HaGeZi Normal | 164,067 | 67,066 | 40.9% |
| AdAway | 6,540 | 3,449 | 52.7% |
| OISD Big | 235,822 | 156,740 | 66.5% |
| Dan Pollock | 13,085 | 9,969 | 76.2% |
| Peter Lowe | 7,170 | 3,909 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 58,187 | 9,252 | 15.9% |
| EasyPrivacy | 56,302 | 26,033 | 46.2% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,451 | 1,366 | 94.1% |
| uBO Badware | 4,266 | 4,216 | 98.8% |
| uBO Quick Fixes | 185 | 174 | 94.1% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **736,755** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 736,755 |
| **DNSZeroList.txt** (all sources, deduped) | **496,615** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **339,875** |

Deduplication removed 240,140 duplicate rule instances (32.6% of the raw total).
Dropping OISD Big removes a further 156,740 rules (31.6% of the full list).
