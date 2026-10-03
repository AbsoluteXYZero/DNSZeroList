# Blocklist stats

_Generated 2026-10-03 03:02:53 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,794 | 74,546 | 41.9% |
| HaGeZi Normal | 199,122 | 96,732 | 48.6% |
| AdAway | 6,540 | 3,449 | 52.7% |
| OISD Big | 244,217 | 162,940 | 66.7% |
| Dan Pollock | 13,082 | 9,933 | 75.9% |
| Peter Lowe | 7,134 | 3,885 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 54,097 | 9,225 | 17.1% |
| EasyPrivacy | 56,216 | 25,740 | 45.8% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,445 | 1,363 | 94.3% |
| uBO Badware | 4,250 | 4,200 | 98.8% |
| uBO Quick Fixes | 144 | 135 | 93.8% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **768,274** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 768,274 |
| **DNSZeroList.txt** (all sources, deduped) | **525,938** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **362,998** |

Deduplication removed 242,336 duplicate rule instances (31.5% of the raw total).
Dropping OISD Big removes a further 162,940 rules (31.0% of the full list).
