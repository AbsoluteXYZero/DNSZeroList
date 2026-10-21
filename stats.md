# Blocklist stats

_Generated 2026-10-21 02:38:26 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 190,094 | 82,444 | 43.4% |
| HaGeZi Normal | 168,161 | 68,935 | 41.0% |
| AdAway | 6,540 | 3,447 | 52.7% |
| OISD Big | 233,474 | 153,541 | 65.8% |
| Dan Pollock | 13,085 | 9,965 | 76.2% |
| Peter Lowe | 7,176 | 3,905 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 59,684 | 9,239 | 15.5% |
| EasyPrivacy | 56,338 | 26,098 | 46.3% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,451 | 1,366 | 94.1% |
| uBO Badware | 4,284 | 4,234 | 98.8% |
| uBO Quick Fixes | 214 | 203 | 94.9% |
| uBO Unbreak | 1,943 | 1,939 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **744,737** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 744,737 |
| **DNSZeroList.txt** (all sources, deduped) | **500,325** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **346,784** |

Deduplication removed 244,412 duplicate rule instances (32.8% of the raw total).
Dropping OISD Big removes a further 153,541 rules (30.7% of the full list).
