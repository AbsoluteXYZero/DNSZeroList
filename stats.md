# Blocklist stats

_Generated 2026-08-26 12:32:59 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,905 | 75,089 | 42.2% |
| HaGeZi Normal | 189,451 | 85,720 | 45.2% |
| AdAway | 6,540 | 3,461 | 52.9% |
| OISD Big | 267,752 | 183,991 | 68.7% |
| Dan Pollock | 13,036 | 9,884 | 75.8% |
| Peter Lowe | 7,068 | 3,840 | 54.3% |
| Dandelion Sprout | 480 | 296 | 61.7% |
| EasyList | 54,661 | 9,205 | 16.8% |
| EasyPrivacy | 55,916 | 25,631 | 45.8% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,425 | 1,344 | 94.3% |
| uBO Badware | 4,189 | 4,142 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,936 | 1,932 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **782,258** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 782,258 |
| **DNSZeroList.txt** (all sources, deduped) | **536,855** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **352,864** |

Deduplication removed 245,403 duplicate rule instances (31.4% of the raw total).
Dropping OISD Big removes a further 183,991 rules (34.3% of the full list).
