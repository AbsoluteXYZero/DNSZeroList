# Blocklist stats

_Generated 2026-10-29 03:38:30 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 185,047 | 84,678 | 45.8% |
| HaGeZi Normal | 172,000 | 73,069 | 42.5% |
| AdAway | 6,540 | 3,448 | 52.7% |
| OISD Big | 234,454 | 151,500 | 64.6% |
| Dan Pollock | 12,971 | 9,860 | 76.0% |
| Peter Lowe | 7,166 | 3,902 | 54.5% |
| Dandelion Sprout | 480 | 301 | 62.7% |
| EasyList | 50,770 | 9,244 | 18.2% |
| EasyPrivacy | 56,387 | 26,112 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,456 | 1,370 | 94.1% |
| uBO Badware | 4,855 | 4,805 | 99.0% |
| uBO Quick Fixes | 221 | 210 | 95.0% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **736,105** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 736,105 |
| **DNSZeroList.txt** (all sources, deduped) | **497,952** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **346,452** |

Deduplication removed 238,153 duplicate rule instances (32.4% of the raw total).
Dropping OISD Big removes a further 151,500 rules (30.4% of the full list).
