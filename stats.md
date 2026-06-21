# Blocklist stats

_Generated 2026-06-21 02:51:25 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,370 | 56,954 | 36.0% |
| HaGeZi Normal | 153,687 | 51,786 | 33.7% |
| AdAway | 6,540 | 3,535 | 54.1% |
| OISD Big | 477,685 | 393,084 | 82.3% |
| Dan Pollock | 12,880 | 9,722 | 75.5% |
| Peter Lowe | 7,040 | 3,831 | 54.4% |
| Dandelion Sprout | 480 | 283 | 59.0% |
| EasyList | 57,313 | 9,389 | 16.4% |
| EasyPrivacy | 55,378 | 26,618 | 48.1% |
| uBO Ads | 1,786 | 1,736 | 97.2% |
| uBO Privacy | 1,360 | 1,279 | 94.0% |
| uBO Badware | 4,150 | 4,102 | 98.8% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,924 | 1,920 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **938,720** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 938,720 |
| **DNSZeroList.txt** (all sources, deduped) | **692,838** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **299,754** |

Deduplication removed 245,882 duplicate rule instances (26.2% of the raw total).
Dropping OISD Big removes a further 393,084 rules (56.7% of the full list).
