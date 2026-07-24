# Blocklist stats

_Generated 2026-07-24 13:19:53 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 159,833 | 56,745 | 35.5% |
| HaGeZi Normal | 180,210 | 82,445 | 45.7% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 333,053 | 251,926 | 75.6% |
| Dan Pollock | 12,959 | 9,805 | 75.7% |
| Peter Lowe | 7,056 | 3,829 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 58,577 | 9,312 | 15.9% |
| EasyPrivacy | 55,560 | 26,738 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,384 | 1,302 | 94.1% |
| uBO Badware | 4,184 | 4,137 | 98.9% |
| uBO Quick Fixes | 94 | 85 | 90.4% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **823,672** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 823,672 |
| **DNSZeroList.txt** (all sources, deduped) | **584,870** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **332,944** |

Deduplication removed 238,802 duplicate rule instances (29.0% of the raw total).
Dropping OISD Big removes a further 251,926 rules (43.1% of the full list).
