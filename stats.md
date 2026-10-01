# Blocklist stats

_Generated 2026-10-01 17:45:36 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,317 | 74,525 | 42.0% |
| HaGeZi Normal | 200,656 | 98,300 | 49.0% |
| AdAway | 6,540 | 3,449 | 52.7% |
| OISD Big | 244,883 | 163,718 | 66.9% |
| Dan Pollock | 13,082 | 9,928 | 75.9% |
| Peter Lowe | 7,136 | 3,884 | 54.4% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 53,663 | 9,242 | 17.2% |
| EasyPrivacy | 56,211 | 25,736 | 45.8% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,444 | 1,363 | 94.4% |
| uBO Badware | 4,248 | 4,198 | 98.8% |
| uBO Quick Fixes | 144 | 135 | 93.8% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **769,557** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 769,557 |
| **DNSZeroList.txt** (all sources, deduped) | **527,932** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **364,214** |

Deduplication removed 241,625 duplicate rule instances (31.4% of the raw total).
Dropping OISD Big removes a further 163,718 rules (31.0% of the full list).
