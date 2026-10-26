# Blocklist stats

_Generated 2026-10-26 17:58:35 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 180,629 | 81,311 | 45.0% |
| HaGeZi Normal | 170,463 | 72,345 | 42.4% |
| AdAway | 6,540 | 3,449 | 52.7% |
| OISD Big | 234,059 | 151,713 | 64.8% |
| Dan Pollock | 12,971 | 9,859 | 76.0% |
| Peter Lowe | 7,158 | 3,896 | 54.4% |
| Dandelion Sprout | 480 | 301 | 62.7% |
| EasyList | 49,969 | 9,239 | 18.5% |
| EasyPrivacy | 56,376 | 26,082 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,455 | 1,369 | 94.1% |
| uBO Badware | 4,855 | 4,805 | 99.0% |
| uBO Quick Fixes | 221 | 210 | 95.0% |
| uBO Unbreak | 1,945 | 1,941 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **728,933** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 728,933 |
| **DNSZeroList.txt** (all sources, deduped) | **493,076** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **341,363** |

Deduplication removed 235,857 duplicate rule instances (32.4% of the raw total).
Dropping OISD Big removes a further 151,713 rules (30.8% of the full list).
