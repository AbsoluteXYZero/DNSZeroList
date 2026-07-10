# Blocklist stats

_Generated 2026-07-10 14:02:54 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 155,961 | 56,910 | 36.5% |
| HaGeZi Normal | 160,524 | 63,665 | 39.7% |
| AdAway | 6,540 | 3,479 | 53.2% |
| OISD Big | 328,962 | 245,465 | 74.6% |
| Dan Pollock | 12,931 | 9,668 | 74.8% |
| Peter Lowe | 7,068 | 3,838 | 54.3% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 54,592 | 9,310 | 17.1% |
| EasyPrivacy | 55,485 | 26,686 | 48.1% |
| uBO Ads | 1,786 | 1,738 | 97.3% |
| uBO Privacy | 1,377 | 1,295 | 94.0% |
| uBO Badware | 4,169 | 4,123 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,927 | 1,922 | 99.7% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **791,931** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 791,931 |
| **DNSZeroList.txt** (all sources, deduped) | **558,075** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **312,610** |

Deduplication removed 233,856 duplicate rule instances (29.5% of the raw total).
Dropping OISD Big removes a further 245,465 rules (44.0% of the full list).
