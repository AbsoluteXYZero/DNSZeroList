# Blocklist stats

_Generated 2026-11-20 19:27:08 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 192,022 | 90,120 | 46.9% |
| HaGeZi Normal | 194,312 | 89,177 | 45.9% |
| AdAway | 6,540 | 3,444 | 52.7% |
| OISD Big | 226,326 | 130,993 | 57.9% |
| Dan Pollock | 13,090 | 9,959 | 76.1% |
| Peter Lowe | 7,142 | 3,878 | 54.3% |
| Dandelion Sprout | 490 | 307 | 62.7% |
| EasyList | 53,596 | 9,270 | 17.3% |
| EasyPrivacy | 56,724 | 26,073 | 46.0% |
| uBO Ads | 1,765 | 1,721 | 97.5% |
| uBO Privacy | 1,467 | 1,376 | 93.8% |
| uBO Badware | 4,737 | 4,681 | 98.8% |
| uBO Quick Fixes | 172 | 161 | 93.6% |
| uBO Unbreak | 1,947 | 1,943 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **760,366** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 760,366 |
| **DNSZeroList.txt** (all sources, deduped) | **510,597** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **379,604** |

Deduplication removed 249,769 duplicate rule instances (32.8% of the raw total).
Dropping OISD Big removes a further 130,993 rules (25.7% of the full list).
