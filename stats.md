# Blocklist stats

_Generated 2026-10-27 03:01:36 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 184,347 | 84,807 | 46.0% |
| HaGeZi Normal | 170,581 | 72,342 | 42.4% |
| AdAway | 6,540 | 3,449 | 52.7% |
| OISD Big | 234,192 | 151,557 | 64.7% |
| Dan Pollock | 12,971 | 9,859 | 76.0% |
| Peter Lowe | 7,158 | 3,896 | 54.4% |
| Dandelion Sprout | 480 | 301 | 62.7% |
| EasyList | 50,094 | 9,230 | 18.4% |
| EasyPrivacy | 56,377 | 26,111 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,455 | 1,369 | 94.1% |
| uBO Badware | 4,855 | 4,805 | 99.0% |
| uBO Quick Fixes | 221 | 210 | 95.0% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **733,029** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 733,029 |
| **DNSZeroList.txt** (all sources, deduped) | **496,721** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **345,164** |

Deduplication removed 236,308 duplicate rule instances (32.2% of the raw total).
Dropping OISD Big removes a further 151,557 rules (30.5% of the full list).
