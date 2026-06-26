# Blocklist stats

_Generated 2026-06-26 02:34:19 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 159,305 | 56,910 | 35.7% |
| HaGeZi Normal | 160,276 | 56,957 | 35.5% |
| AdAway | 6,540 | 3,520 | 53.8% |
| OISD Big | 478,659 | 393,034 | 82.1% |
| Dan Pollock | 12,890 | 9,762 | 75.7% |
| Peter Lowe | 7,050 | 3,838 | 54.4% |
| Dandelion Sprout | 480 | 283 | 59.0% |
| EasyList | 58,100 | 9,358 | 16.1% |
| EasyPrivacy | 55,416 | 26,670 | 48.1% |
| uBO Ads | 1,787 | 1,737 | 97.2% |
| uBO Privacy | 1,363 | 1,282 | 94.1% |
| uBO Badware | 4,145 | 4,100 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,924 | 1,920 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **948,062** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 948,062 |
| **DNSZeroList.txt** (all sources, deduped) | **699,225** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **306,191** |

Deduplication removed 248,837 duplicate rule instances (26.2% of the raw total).
Dropping OISD Big removes a further 393,034 rules (56.2% of the full list).
