# Blocklist stats

_Generated 2026-09-13 15:20:52 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 179,077 | 74,968 | 41.9% |
| HaGeZi Normal | 180,305 | 79,581 | 44.1% |
| AdAway | 6,540 | 3,460 | 52.9% |
| OISD Big | 245,574 | 166,927 | 68.0% |
| Dan Pollock | 13,064 | 9,921 | 75.9% |
| Peter Lowe | 7,150 | 3,889 | 54.4% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 55,515 | 9,214 | 16.6% |
| EasyPrivacy | 56,029 | 25,681 | 45.8% |
| uBO Ads | 1,763 | 1,719 | 97.5% |
| uBO Privacy | 1,435 | 1,354 | 94.4% |
| uBO Badware | 4,126 | 4,078 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,937 | 1,933 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **753,125** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 753,125 |
| **DNSZeroList.txt** (all sources, deduped) | **512,737** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **345,810** |

Deduplication removed 240,388 duplicate rule instances (31.9% of the raw total).
Dropping OISD Big removes a further 166,927 rules (32.6% of the full list).
