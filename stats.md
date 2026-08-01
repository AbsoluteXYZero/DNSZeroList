# Blocklist stats

_Generated 2026-08-01 01:59:40 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 161,832 | 56,691 | 35.0% |
| HaGeZi Normal | 180,979 | 82,076 | 45.4% |
| AdAway | 6,540 | 3,465 | 53.0% |
| OISD Big | 337,558 | 256,081 | 75.9% |
| Dan Pollock | 12,972 | 9,821 | 75.7% |
| Peter Lowe | 7,058 | 3,831 | 54.3% |
| Dandelion Sprout | 480 | 290 | 60.4% |
| EasyList | 60,475 | 9,341 | 15.4% |
| EasyPrivacy | 55,624 | 26,762 | 48.1% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,389 | 1,309 | 94.2% |
| uBO Badware | 4,186 | 4,140 | 98.9% |
| uBO Quick Fixes | 92 | 83 | 90.2% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **832,924** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 832,924 |
| **DNSZeroList.txt** (all sources, deduped) | **590,066** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **333,985** |

Deduplication removed 242,858 duplicate rule instances (29.2% of the raw total).
Dropping OISD Big removes a further 256,081 rules (43.4% of the full list).
