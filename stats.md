# Blocklist stats

_Generated 2026-11-06 04:22:19 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 189,976 | 90,469 | 47.6% |
| HaGeZi Normal | 177,920 | 78,193 | 43.9% |
| AdAway | 6,540 | 3,444 | 52.7% |
| OISD Big | 232,556 | 140,117 | 60.3% |
| Dan Pollock | 12,971 | 9,857 | 76.0% |
| Peter Lowe | 7,160 | 3,899 | 54.5% |
| Dandelion Sprout | 490 | 303 | 61.8% |
| EasyList | 53,210 | 9,238 | 17.4% |
| EasyPrivacy | 56,451 | 26,177 | 46.4% |
| uBO Ads | 1,771 | 1,728 | 97.6% |
| uBO Privacy | 1,461 | 1,374 | 94.0% |
| uBO Badware | 4,720 | 4,664 | 98.8% |
| uBO Quick Fixes | 169 | 158 | 93.5% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **747,378** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 747,378 |
| **DNSZeroList.txt** (all sources, deduped) | **504,980** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **364,863** |

Deduplication removed 242,398 duplicate rule instances (32.4% of the raw total).
Dropping OISD Big removes a further 140,117 rules (27.7% of the full list).
