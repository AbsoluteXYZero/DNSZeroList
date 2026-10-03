# Blocklist stats

_Generated 2026-10-03 15:29:14 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,968 | 74,542 | 41.9% |
| HaGeZi Normal | 199,284 | 96,812 | 48.6% |
| AdAway | 6,540 | 3,448 | 52.7% |
| OISD Big | 244,155 | 162,734 | 66.7% |
| Dan Pollock | 13,082 | 9,933 | 75.9% |
| Peter Lowe | 7,134 | 3,885 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 54,261 | 9,221 | 17.0% |
| EasyPrivacy | 56,221 | 25,742 | 45.8% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,445 | 1,363 | 94.3% |
| uBO Badware | 4,252 | 4,201 | 98.8% |
| uBO Quick Fixes | 147 | 138 | 93.9% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **768,722** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 768,722 |
| **DNSZeroList.txt** (all sources, deduped) | **525,928** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **363,194** |

Deduplication removed 242,794 duplicate rule instances (31.6% of the raw total).
Dropping OISD Big removes a further 162,734 rules (30.9% of the full list).
