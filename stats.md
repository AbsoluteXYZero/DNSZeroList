# Blocklist stats

_Generated 2026-10-24 02:38:08 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 191,304 | 81,436 | 42.6% |
| HaGeZi Normal | 172,593 | 71,071 | 41.2% |
| AdAway | 6,540 | 3,447 | 52.7% |
| OISD Big | 236,125 | 153,836 | 65.2% |
| Dan Pollock | 12,971 | 9,859 | 76.0% |
| Peter Lowe | 7,158 | 3,896 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 60,680 | 9,241 | 15.2% |
| EasyPrivacy | 56,363 | 26,077 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,451 | 1,366 | 94.1% |
| uBO Badware | 4,852 | 4,802 | 99.0% |
| uBO Quick Fixes | 220 | 209 | 95.0% |
| uBO Unbreak | 1,943 | 1,939 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **754,492** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 754,492 |
| **DNSZeroList.txt** (all sources, deduped) | **504,553** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **350,717** |

Deduplication removed 249,939 duplicate rule instances (33.1% of the raw total).
Dropping OISD Big removes a further 153,836 rules (30.5% of the full list).
