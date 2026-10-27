# Blocklist stats

_Generated 2026-10-27 17:05:05 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 184,560 | 84,740 | 45.9% |
| HaGeZi Normal | 171,454 | 72,745 | 42.4% |
| AdAway | 6,540 | 3,448 | 52.7% |
| OISD Big | 234,205 | 151,436 | 64.7% |
| Dan Pollock | 12,971 | 9,860 | 76.0% |
| Peter Lowe | 7,158 | 3,897 | 54.4% |
| Dandelion Sprout | 480 | 301 | 62.7% |
| EasyList | 50,290 | 9,235 | 18.4% |
| EasyPrivacy | 56,379 | 26,111 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,456 | 1,370 | 94.1% |
| uBO Badware | 4,855 | 4,805 | 99.0% |
| uBO Quick Fixes | 221 | 210 | 95.0% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **734,327** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 734,327 |
| **DNSZeroList.txt** (all sources, deduped) | **497,202** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **345,766** |

Deduplication removed 237,125 duplicate rule instances (32.3% of the raw total).
Dropping OISD Big removes a further 151,436 rules (30.5% of the full list).
