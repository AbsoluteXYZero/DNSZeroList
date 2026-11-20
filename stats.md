# Blocklist stats

_Generated 2026-11-20 04:58:52 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 191,812 | 90,020 | 46.9% |
| HaGeZi Normal | 194,785 | 89,073 | 45.7% |
| AdAway | 6,540 | 3,443 | 52.6% |
| OISD Big | 233,222 | 135,566 | 58.1% |
| Dan Pollock | 13,090 | 9,951 | 76.0% |
| Peter Lowe | 7,168 | 3,889 | 54.3% |
| Dandelion Sprout | 490 | 307 | 62.7% |
| EasyList | 53,387 | 9,259 | 17.3% |
| EasyPrivacy | 56,723 | 26,076 | 46.0% |
| uBO Ads | 1,765 | 1,721 | 97.5% |
| uBO Privacy | 1,467 | 1,375 | 93.7% |
| uBO Badware | 4,737 | 4,681 | 98.8% |
| uBO Quick Fixes | 172 | 161 | 93.6% |
| uBO Unbreak | 1,944 | 1,940 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **767,338** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 767,338 |
| **DNSZeroList.txt** (all sources, deduped) | **515,593** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **380,027** |

Deduplication removed 251,745 duplicate rule instances (32.8% of the raw total).
Dropping OISD Big removes a further 135,566 rules (26.3% of the full list).
