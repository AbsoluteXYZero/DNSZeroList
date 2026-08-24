# Blocklist stats

_Generated 2026-08-24 12:29:37 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,282 | 75,172 | 42.4% |
| HaGeZi Normal | 188,340 | 85,243 | 45.3% |
| AdAway | 6,540 | 3,462 | 52.9% |
| OISD Big | 268,129 | 184,530 | 68.8% |
| Dan Pollock | 13,030 | 9,878 | 75.8% |
| Peter Lowe | 7,066 | 3,839 | 54.3% |
| Dandelion Sprout | 480 | 296 | 61.7% |
| EasyList | 54,101 | 9,217 | 17.0% |
| EasyPrivacy | 55,901 | 25,628 | 45.8% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,424 | 1,343 | 94.3% |
| uBO Badware | 4,183 | 4,136 | 98.9% |
| uBO Quick Fixes | 89 | 80 | 89.9% |
| uBO Unbreak | 1,935 | 1,931 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **780,308** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 780,308 |
| **DNSZeroList.txt** (all sources, deduped) | **536,407** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **351,877** |

Deduplication removed 243,901 duplicate rule instances (31.3% of the raw total).
Dropping OISD Big removes a further 184,530 rules (34.4% of the full list).
