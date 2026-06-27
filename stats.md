# Blocklist stats

_Generated 2026-06-27 02:27:41 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 159,368 | 56,840 | 35.7% |
| HaGeZi Normal | 160,444 | 57,398 | 35.8% |
| AdAway | 6,540 | 3,528 | 53.9% |
| OISD Big | 335,358 | 249,890 | 74.5% |
| Dan Pollock | 12,891 | 9,661 | 74.9% |
| Peter Lowe | 7,044 | 3,832 | 54.4% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 58,404 | 9,361 | 16.0% |
| EasyPrivacy | 55,422 | 26,658 | 48.1% |
| uBO Ads | 1,787 | 1,737 | 97.2% |
| uBO Privacy | 1,363 | 1,282 | 94.1% |
| uBO Badware | 4,149 | 4,104 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,924 | 1,920 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **805,301** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 805,301 |
| **DNSZeroList.txt** (all sources, deduped) | **556,213** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **306,323** |

Deduplication removed 249,088 duplicate rule instances (30.9% of the raw total).
Dropping OISD Big removes a further 249,890 rules (44.9% of the full list).
