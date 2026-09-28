# Blocklist stats

_Generated 2026-09-28 18:59:36 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 176,317 | 74,641 | 42.3% |
| HaGeZi Normal | 200,054 | 98,633 | 49.3% |
| AdAway | 6,540 | 3,450 | 52.8% |
| OISD Big | 244,400 | 163,552 | 66.9% |
| Dan Pollock | 13,082 | 9,928 | 75.9% |
| Peter Lowe | 7,134 | 3,883 | 54.4% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 52,744 | 9,223 | 17.5% |
| EasyPrivacy | 56,181 | 25,723 | 45.8% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,442 | 1,361 | 94.4% |
| uBO Badware | 4,242 | 4,192 | 98.8% |
| uBO Quick Fixes | 142 | 133 | 93.7% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **766,511** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 766,511 |
| **DNSZeroList.txt** (all sources, deduped) | **527,239** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **363,687** |

Deduplication removed 239,272 duplicate rule instances (31.2% of the raw total).
Dropping OISD Big removes a further 163,552 rules (31.0% of the full list).
