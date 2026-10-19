# Blocklist stats

_Generated 2026-10-19 02:31:54 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 186,320 | 79,651 | 42.7% |
| HaGeZi Normal | 166,141 | 68,032 | 40.9% |
| AdAway | 6,540 | 3,450 | 52.8% |
| OISD Big | 234,618 | 154,725 | 65.9% |
| Dan Pollock | 13,085 | 9,970 | 76.2% |
| Peter Lowe | 7,170 | 3,901 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 59,008 | 9,236 | 15.7% |
| EasyPrivacy | 56,312 | 26,033 | 46.2% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,451 | 1,366 | 94.1% |
| uBO Badware | 4,271 | 4,221 | 98.8% |
| uBO Quick Fixes | 211 | 200 | 94.8% |
| uBO Unbreak | 1,944 | 1,940 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **739,363** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 739,363 |
| **DNSZeroList.txt** (all sources, deduped) | **496,758** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **342,033** |

Deduplication removed 242,605 duplicate rule instances (32.8% of the raw total).
Dropping OISD Big removes a further 154,725 rules (31.1% of the full list).
