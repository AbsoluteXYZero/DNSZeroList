# Blocklist stats

_Generated 2026-09-09 15:37:05 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,605 | 74,937 | 42.2% |
| HaGeZi Normal | 181,417 | 78,516 | 43.3% |
| AdAway | 6,540 | 3,470 | 53.1% |
| OISD Big | 255,313 | 169,658 | 66.5% |
| Dan Pollock | 13,060 | 9,916 | 75.9% |
| Peter Lowe | 7,116 | 3,869 | 54.4% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 54,103 | 9,216 | 17.0% |
| EasyPrivacy | 55,996 | 25,666 | 45.8% |
| uBO Ads | 1,770 | 1,727 | 97.6% |
| uBO Privacy | 1,432 | 1,350 | 94.3% |
| uBO Badware | 4,236 | 4,187 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,937 | 1,933 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **761,135** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 761,135 |
| **DNSZeroList.txt** (all sources, deduped) | **514,946** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **345,288** |

Deduplication removed 246,189 duplicate rule instances (32.3% of the raw total).
Dropping OISD Big removes a further 169,658 rules (32.9% of the full list).
