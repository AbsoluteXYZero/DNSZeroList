# Blocklist stats

_Generated 2026-10-30 03:41:17 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 185,418 | 84,627 | 45.6% |
| HaGeZi Normal | 172,633 | 73,380 | 42.5% |
| AdAway | 6,540 | 3,448 | 52.7% |
| OISD Big | 234,798 | 151,587 | 64.6% |
| Dan Pollock | 12,971 | 9,860 | 76.0% |
| Peter Lowe | 7,170 | 3,905 | 54.5% |
| Dandelion Sprout | 480 | 301 | 62.7% |
| EasyList | 51,121 | 9,248 | 18.1% |
| EasyPrivacy | 56,397 | 26,112 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,457 | 1,370 | 94.0% |
| uBO Badware | 4,855 | 4,805 | 99.0% |
| uBO Quick Fixes | 221 | 210 | 95.0% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **737,819** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 737,819 |
| **DNSZeroList.txt** (all sources, deduped) | **498,723** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **347,136** |

Deduplication removed 239,096 duplicate rule instances (32.4% of the raw total).
Dropping OISD Big removes a further 151,587 rules (30.4% of the full list).
