# Blocklist stats

_Generated 2026-07-09 14:34:26 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 155,632 | 56,985 | 36.6% |
| HaGeZi Normal | 160,118 | 63,295 | 39.5% |
| AdAway | 6,540 | 3,533 | 54.0% |
| OISD Big | 327,000 | 244,672 | 74.8% |
| Dan Pollock | 12,930 | 9,803 | 75.8% |
| Peter Lowe | 7,062 | 3,849 | 54.5% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 54,280 | 9,308 | 17.1% |
| EasyPrivacy | 55,484 | 26,691 | 48.1% |
| uBO Ads | 1,786 | 1,738 | 97.3% |
| uBO Privacy | 1,377 | 1,295 | 94.0% |
| uBO Badware | 4,167 | 4,121 | 98.9% |
| uBO Quick Fixes | 92 | 83 | 90.2% |
| uBO Unbreak | 1,927 | 1,922 | 99.7% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **788,911** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 788,911 |
| **DNSZeroList.txt** (all sources, deduped) | **555,880** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **311,208** |

Deduplication removed 233,031 duplicate rule instances (29.5% of the raw total).
Dropping OISD Big removes a further 244,672 rules (44.0% of the full list).
