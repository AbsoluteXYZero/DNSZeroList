# Blocklist stats

_Generated 2026-07-13 01:56:16 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 156,780 | 56,905 | 36.3% |
| HaGeZi Normal | 160,555 | 63,778 | 39.7% |
| AdAway | 6,540 | 3,479 | 53.2% |
| OISD Big | 328,583 | 245,623 | 74.8% |
| Dan Pollock | 12,935 | 9,811 | 75.8% |
| Peter Lowe | 7,078 | 3,844 | 54.3% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 55,369 | 9,306 | 16.8% |
| EasyPrivacy | 55,498 | 26,691 | 48.1% |
| uBO Ads | 1,786 | 1,738 | 97.3% |
| uBO Privacy | 1,377 | 1,295 | 94.0% |
| uBO Badware | 4,169 | 4,123 | 98.9% |
| uBO Quick Fixes | 97 | 87 | 89.7% |
| uBO Unbreak | 1,927 | 1,922 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **793,211** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 793,211 |
| **DNSZeroList.txt** (all sources, deduped) | **558,413** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **312,790** |

Deduplication removed 234,798 duplicate rule instances (29.6% of the raw total).
Dropping OISD Big removes a further 245,623 rules (44.0% of the full list).
