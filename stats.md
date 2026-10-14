# Blocklist stats

_Generated 2026-10-14 16:13:02 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 184,459 | 79,939 | 43.3% |
| HaGeZi Normal | 159,817 | 63,834 | 39.9% |
| AdAway | 6,540 | 3,449 | 52.7% |
| OISD Big | 237,825 | 158,520 | 66.7% |
| Dan Pollock | 13,084 | 9,972 | 76.2% |
| Peter Lowe | 7,130 | 3,884 | 54.5% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 57,515 | 9,257 | 16.1% |
| EasyPrivacy | 56,287 | 26,029 | 46.2% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,450 | 1,366 | 94.2% |
| uBO Badware | 4,266 | 4,216 | 98.8% |
| uBO Quick Fixes | 183 | 172 | 94.0% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **732,790** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 732,790 |
| **DNSZeroList.txt** (all sources, deduped) | **494,236** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **335,716** |

Deduplication removed 238,554 duplicate rule instances (32.6% of the raw total).
Dropping OISD Big removes a further 158,520 rules (32.1% of the full list).
