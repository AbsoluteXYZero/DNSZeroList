# Blocklist stats

_Generated 2026-09-14 02:33:10 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 179,254 | 74,969 | 41.8% |
| HaGeZi Normal | 180,305 | 79,589 | 44.1% |
| AdAway | 6,540 | 3,460 | 52.9% |
| OISD Big | 245,476 | 166,754 | 67.9% |
| Dan Pollock | 13,064 | 9,921 | 75.9% |
| Peter Lowe | 7,150 | 3,889 | 54.4% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 55,667 | 9,206 | 16.5% |
| EasyPrivacy | 56,032 | 25,681 | 45.8% |
| uBO Ads | 1,763 | 1,719 | 97.5% |
| uBO Privacy | 1,435 | 1,354 | 94.4% |
| uBO Badware | 4,126 | 4,078 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,937 | 1,933 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **753,359** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 753,359 |
| **DNSZeroList.txt** (all sources, deduped) | **512,724** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **345,970** |

Deduplication removed 240,635 duplicate rule instances (31.9% of the raw total).
Dropping OISD Big removes a further 166,754 rules (32.5% of the full list).
