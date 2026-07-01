# Blocklist stats

_Generated 2026-07-01 02:40:43 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 153,778 | 56,901 | 37.0% |
| HaGeZi Normal | 155,515 | 58,103 | 37.4% |
| AdAway | 6,540 | 3,533 | 54.0% |
| OISD Big | 332,299 | 251,730 | 75.8% |
| Dan Pollock | 12,904 | 9,739 | 75.5% |
| Peter Lowe | 7,064 | 3,845 | 54.4% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 52,580 | 9,313 | 17.7% |
| EasyPrivacy | 55,444 | 26,669 | 48.1% |
| uBO Ads | 1,787 | 1,737 | 97.2% |
| uBO Privacy | 1,372 | 1,290 | 94.0% |
| uBO Badware | 4,151 | 4,106 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,925 | 1,921 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **785,968** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 785,968 |
| **DNSZeroList.txt** (all sources, deduped) | **553,295** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **301,565** |

Deduplication removed 232,673 duplicate rule instances (29.6% of the raw total).
Dropping OISD Big removes a further 251,730 rules (45.5% of the full list).
