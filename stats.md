# Blocklist stats

_Generated 2026-09-15 15:56:45 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 179,820 | 74,870 | 41.6% |
| HaGeZi Normal | 181,936 | 80,278 | 44.1% |
| AdAway | 6,540 | 3,459 | 52.9% |
| OISD Big | 245,637 | 166,732 | 67.9% |
| Dan Pollock | 13,069 | 9,919 | 75.9% |
| Peter Lowe | 7,150 | 3,890 | 54.4% |
| Dandelion Sprout | 480 | 298 | 62.1% |
| EasyList | 56,236 | 9,228 | 16.4% |
| EasyPrivacy | 56,043 | 25,685 | 45.8% |
| uBO Ads | 1,763 | 1,719 | 97.5% |
| uBO Privacy | 1,435 | 1,354 | 94.4% |
| uBO Badware | 4,128 | 4,080 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,939 | 1,935 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **756,306** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 756,306 |
| **DNSZeroList.txt** (all sources, deduped) | **514,098** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **347,366** |

Deduplication removed 242,208 duplicate rule instances (32.0% of the raw total).
Dropping OISD Big removes a further 166,732 rules (32.4% of the full list).
