# Blocklist stats

_Generated 2026-07-15 13:16:03 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 157,600 | 56,873 | 36.1% |
| HaGeZi Normal | 161,738 | 64,257 | 39.7% |
| AdAway | 6,540 | 3,480 | 53.2% |
| OISD Big | 324,491 | 242,281 | 74.7% |
| Dan Pollock | 12,939 | 9,765 | 75.5% |
| Peter Lowe | 7,080 | 3,842 | 54.3% |
| Dandelion Sprout | 480 | 288 | 60.0% |
| EasyList | 56,119 | 9,304 | 16.6% |
| EasyPrivacy | 55,511 | 26,693 | 48.1% |
| uBO Ads | 1,785 | 1,737 | 97.3% |
| uBO Privacy | 1,379 | 1,297 | 94.1% |
| uBO Badware | 4,171 | 4,125 | 98.9% |
| uBO Quick Fixes | 97 | 87 | 89.7% |
| uBO Unbreak | 1,927 | 1,922 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **791,894** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 791,894 |
| **DNSZeroList.txt** (all sources, deduped) | **556,290** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **314,009** |

Deduplication removed 235,604 duplicate rule instances (29.8% of the raw total).
Dropping OISD Big removes a further 242,281 rules (43.6% of the full list).
