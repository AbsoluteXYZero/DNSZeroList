# Blocklist stats

_Generated 2026-11-12 05:00:33 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 190,611 | 80,058 | 42.0% |
| HaGeZi Normal | 208,182 | 81,577 | 39.2% |
| AdAway | 6,540 | 3,442 | 52.6% |
| OISD Big | 227,721 | 132,548 | 58.2% |
| Dan Pollock | 13,090 | 9,950 | 76.0% |
| Peter Lowe | 7,156 | 3,879 | 54.2% |
| Dandelion Sprout | 490 | 306 | 62.4% |
| EasyList | 52,325 | 9,255 | 17.7% |
| EasyPrivacy | 56,581 | 26,009 | 46.0% |
| uBO Ads | 1,766 | 1,722 | 97.5% |
| uBO Privacy | 1,467 | 1,378 | 93.9% |
| uBO Badware | 4,734 | 4,678 | 98.8% |
| uBO Quick Fixes | 171 | 160 | 93.6% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **772,817** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 772,817 |
| **DNSZeroList.txt** (all sources, deduped) | **502,741** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **370,193** |

Deduplication removed 270,076 duplicate rule instances (34.9% of the raw total).
Dropping OISD Big removes a further 132,548 rules (26.4% of the full list).
