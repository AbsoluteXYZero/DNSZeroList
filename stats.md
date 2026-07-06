# Blocklist stats

_Generated 2026-07-06 02:23:43 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 155,360 | 56,980 | 36.7% |
| HaGeZi Normal | 158,207 | 59,501 | 37.6% |
| AdAway | 6,540 | 3,533 | 54.0% |
| OISD Big | 325,762 | 243,896 | 74.9% |
| Dan Pollock | 12,909 | 9,727 | 75.4% |
| Peter Lowe | 7,058 | 3,845 | 54.5% |
| Dandelion Sprout | 480 | 284 | 59.2% |
| EasyList | 54,117 | 9,335 | 17.2% |
| EasyPrivacy | 55,466 | 26,685 | 48.1% |
| uBO Ads | 1,787 | 1,738 | 97.3% |
| uBO Privacy | 1,372 | 1,290 | 94.0% |
| uBO Badware | 4,163 | 4,118 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,925 | 1,921 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **785,275** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 785,275 |
| **DNSZeroList.txt** (all sources, deduped) | **551,041** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **307,145** |

Deduplication removed 234,234 duplicate rule instances (29.8% of the raw total).
Dropping OISD Big removes a further 243,896 rules (44.3% of the full list).
