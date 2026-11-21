# Blocklist stats

_Generated 2026-11-21 04:54:27 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 192,173 | 90,115 | 46.9% |
| HaGeZi Normal | 194,449 | 89,172 | 45.9% |
| AdAway | 6,540 | 3,444 | 52.7% |
| OISD Big | 226,557 | 131,063 | 57.8% |
| Dan Pollock | 13,090 | 9,959 | 76.1% |
| Peter Lowe | 7,142 | 3,877 | 54.3% |
| Dandelion Sprout | 490 | 306 | 62.4% |
| EasyList | 53,724 | 9,256 | 17.2% |
| EasyPrivacy | 56,727 | 26,071 | 46.0% |
| uBO Ads | 1,765 | 1,721 | 97.5% |
| uBO Privacy | 1,467 | 1,376 | 93.8% |
| uBO Badware | 4,737 | 4,681 | 98.8% |
| uBO Quick Fixes | 172 | 161 | 93.6% |
| uBO Unbreak | 1,947 | 1,943 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **761,016** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 761,016 |
| **DNSZeroList.txt** (all sources, deduped) | **510,839** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **379,776** |

Deduplication removed 250,177 duplicate rule instances (32.9% of the raw total).
Dropping OISD Big removes a further 131,063 rules (25.7% of the full list).
