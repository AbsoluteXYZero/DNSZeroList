# Blocklist stats

_Generated 2026-07-10 02:04:40 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 155,805 | 57,004 | 36.6% |
| HaGeZi Normal | 159,478 | 62,493 | 39.2% |
| AdAway | 6,540 | 3,478 | 53.2% |
| OISD Big | 493,500 | 410,241 | 83.1% |
| Dan Pollock | 12,931 | 9,783 | 75.7% |
| Peter Lowe | 7,062 | 3,839 | 54.4% |
| Dandelion Sprout | 480 | 281 | 58.5% |
| EasyList | 54,442 | 9,308 | 17.1% |
| EasyPrivacy | 55,486 | 26,686 | 48.1% |
| uBO Ads | 1,786 | 1,738 | 97.3% |
| uBO Privacy | 1,377 | 1,295 | 94.0% |
| uBO Badware | 4,168 | 4,122 | 98.9% |
| uBO Quick Fixes | 92 | 83 | 90.2% |
| uBO Unbreak | 1,927 | 1,922 | 99.7% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **955,110** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 955,110 |
| **DNSZeroList.txt** (all sources, deduped) | **721,661** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **311,420** |

Deduplication removed 233,449 duplicate rule instances (24.4% of the raw total).
Dropping OISD Big removes a further 410,241 rules (56.8% of the full list).
