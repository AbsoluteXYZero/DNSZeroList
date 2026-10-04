# Blocklist stats

_Generated 2026-10-04 16:12:06 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 178,288 | 77,364 | 43.4% |
| HaGeZi Normal | 156,923 | 60,891 | 38.8% |
| AdAway | 6,540 | 3,457 | 52.9% |
| OISD Big | 244,331 | 165,531 | 67.7% |
| Dan Pollock | 13,082 | 9,980 | 76.3% |
| Peter Lowe | 7,134 | 3,884 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 54,564 | 9,220 | 16.9% |
| EasyPrivacy | 56,224 | 25,744 | 45.8% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,445 | 1,363 | 94.3% |
| uBO Badware | 4,252 | 4,201 | 98.8% |
| uBO Quick Fixes | 147 | 138 | 93.9% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **727,163** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 727,163 |
| **DNSZeroList.txt** (all sources, deduped) | **490,482** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **324,951** |

Deduplication removed 236,681 duplicate rule instances (32.5% of the raw total).
Dropping OISD Big removes a further 165,531 rules (33.7% of the full list).
