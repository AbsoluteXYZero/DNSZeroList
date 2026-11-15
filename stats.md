# Blocklist stats

_Generated 2026-11-15 03:57:47 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 191,759 | 79,811 | 41.6% |
| HaGeZi Normal | 221,307 | 92,258 | 41.7% |
| AdAway | 6,540 | 3,303 | 50.5% |
| OISD Big | 227,861 | 131,221 | 57.6% |
| Dan Pollock | 13,090 | 9,915 | 75.7% |
| Peter Lowe | 7,160 | 3,885 | 54.3% |
| Dandelion Sprout | 490 | 306 | 62.4% |
| EasyList | 53,443 | 9,262 | 17.3% |
| EasyPrivacy | 56,616 | 25,945 | 45.8% |
| uBO Ads | 1,766 | 1,722 | 97.5% |
| uBO Privacy | 1,469 | 1,377 | 93.7% |
| uBO Badware | 4,741 | 4,685 | 98.8% |
| uBO Quick Fixes | 172 | 161 | 93.6% |
| uBO Unbreak | 1,951 | 1,947 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **788,402** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 788,402 |
| **DNSZeroList.txt** (all sources, deduped) | **513,855** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **382,634** |

Deduplication removed 274,547 duplicate rule instances (34.8% of the raw total).
Dropping OISD Big removes a further 131,221 rules (25.5% of the full list).
