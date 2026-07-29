# Blocklist stats

_Generated 2026-07-29 13:48:31 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 161,189 | 56,738 | 35.2% |
| HaGeZi Normal | 180,764 | 81,628 | 45.2% |
| AdAway | 6,540 | 3,464 | 53.0% |
| OISD Big | 337,554 | 255,267 | 75.6% |
| Dan Pollock | 12,963 | 9,812 | 75.7% |
| Peter Lowe | 7,058 | 3,830 | 54.3% |
| Dandelion Sprout | 480 | 290 | 60.4% |
| EasyList | 59,874 | 9,338 | 15.6% |
| EasyPrivacy | 55,595 | 26,749 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,388 | 1,307 | 94.2% |
| uBO Badware | 4,186 | 4,140 | 98.9% |
| uBO Quick Fixes | 91 | 82 | 90.1% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **831,424** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 831,424 |
| **DNSZeroList.txt** (all sources, deduped) | **588,833** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **333,566** |

Deduplication removed 242,591 duplicate rule instances (29.2% of the raw total).
Dropping OISD Big removes a further 255,267 rules (43.4% of the full list).
