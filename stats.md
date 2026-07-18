# Blocklist stats

_Generated 2026-07-18 12:54:57 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,440 | 56,894 | 35.9% |
| HaGeZi Normal | 177,816 | 79,742 | 44.8% |
| AdAway | 6,540 | 3,482 | 53.2% |
| OISD Big | 328,120 | 245,419 | 74.8% |
| Dan Pollock | 12,947 | 9,776 | 75.5% |
| Peter Lowe | 7,066 | 3,834 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 56,886 | 9,309 | 16.4% |
| EasyPrivacy | 55,524 | 26,693 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,381 | 1,299 | 94.1% |
| uBO Badware | 4,174 | 4,127 | 98.9% |
| uBO Quick Fixes | 95 | 85 | 89.5% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **813,211** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 813,211 |
| **DNSZeroList.txt** (all sources, deduped) | **575,960** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **330,541** |

Deduplication removed 237,251 duplicate rule instances (29.2% of the raw total).
Dropping OISD Big removes a further 245,419 rules (42.6% of the full list).
