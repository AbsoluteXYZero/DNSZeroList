# Blocklist stats

_Generated 2026-11-22 04:13:39 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 192,233 | 89,884 | 46.8% |
| HaGeZi Normal | 194,710 | 89,850 | 46.1% |
| AdAway | 6,540 | 3,444 | 52.7% |
| OISD Big | 224,266 | 129,142 | 57.6% |
| Dan Pollock | 13,090 | 9,963 | 76.1% |
| Peter Lowe | 7,142 | 3,874 | 54.2% |
| Dandelion Sprout | 490 | 306 | 62.4% |
| EasyList | 54,077 | 9,259 | 17.1% |
| EasyPrivacy | 56,735 | 26,070 | 46.0% |
| uBO Ads | 1,765 | 1,721 | 97.5% |
| uBO Privacy | 1,467 | 1,376 | 93.8% |
| uBO Badware | 4,737 | 4,681 | 98.8% |
| uBO Quick Fixes | 172 | 161 | 93.6% |
| uBO Unbreak | 1,949 | 1,945 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **759,409** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 759,409 |
| **DNSZeroList.txt** (all sources, deduped) | **509,164** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **380,022** |

Deduplication removed 250,245 duplicate rule instances (33.0% of the raw total).
Dropping OISD Big removes a further 129,142 rules (25.4% of the full list).
