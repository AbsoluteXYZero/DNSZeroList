# Blocklist stats

_Generated 2026-10-23 16:09:37 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 191,129 | 81,434 | 42.6% |
| HaGeZi Normal | 172,593 | 71,053 | 41.2% |
| AdAway | 6,540 | 3,447 | 52.7% |
| OISD Big | 236,218 | 154,007 | 65.2% |
| Dan Pollock | 13,085 | 9,964 | 76.1% |
| Peter Lowe | 7,158 | 3,896 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 60,530 | 9,259 | 15.3% |
| EasyPrivacy | 56,360 | 26,076 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,451 | 1,366 | 94.1% |
| uBO Badware | 4,852 | 4,802 | 99.0% |
| uBO Quick Fixes | 220 | 209 | 95.0% |
| uBO Unbreak | 1,943 | 1,939 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **754,371** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 754,371 |
| **DNSZeroList.txt** (all sources, deduped) | **504,673** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **350,666** |

Deduplication removed 249,698 duplicate rule instances (33.1% of the raw total).
Dropping OISD Big removes a further 154,007 rules (30.5% of the full list).
