# Blocklist stats

_Generated 2026-10-17 02:16:32 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 185,597 | 79,734 | 43.0% |
| HaGeZi Normal | 164,454 | 67,447 | 41.0% |
| AdAway | 6,540 | 3,450 | 52.8% |
| OISD Big | 235,993 | 157,093 | 66.6% |
| Dan Pollock | 13,085 | 9,970 | 76.2% |
| Peter Lowe | 7,170 | 3,901 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 58,335 | 9,258 | 15.9% |
| EasyPrivacy | 56,305 | 26,032 | 46.2% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,451 | 1,366 | 94.1% |
| uBO Badware | 4,266 | 4,216 | 98.8% |
| uBO Quick Fixes | 185 | 174 | 94.1% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **737,614** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 737,614 |
| **DNSZeroList.txt** (all sources, deduped) | **497,293** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **340,200** |

Deduplication removed 240,321 duplicate rule instances (32.6% of the raw total).
Dropping OISD Big removes a further 157,093 rules (31.6% of the full list).
