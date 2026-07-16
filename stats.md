# Blocklist stats

_Generated 2026-07-16 01:49:44 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 157,649 | 56,913 | 36.1% |
| HaGeZi Normal | 161,753 | 64,445 | 39.8% |
| AdAway | 6,540 | 3,483 | 53.3% |
| OISD Big | 323,766 | 241,726 | 74.7% |
| Dan Pollock | 12,943 | 9,770 | 75.5% |
| Peter Lowe | 7,080 | 3,843 | 54.3% |
| Dandelion Sprout | 480 | 290 | 60.4% |
| EasyList | 56,173 | 9,331 | 16.6% |
| EasyPrivacy | 55,512 | 26,693 | 48.1% |
| uBO Ads | 1,785 | 1,738 | 97.4% |
| uBO Privacy | 1,379 | 1,297 | 94.1% |
| uBO Badware | 4,171 | 4,125 | 98.9% |
| uBO Quick Fixes | 97 | 87 | 89.7% |
| uBO Unbreak | 1,927 | 1,922 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **791,292** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 791,292 |
| **DNSZeroList.txt** (all sources, deduped) | **555,985** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **314,259** |

Deduplication removed 235,307 duplicate rule instances (29.7% of the raw total).
Dropping OISD Big removes a further 241,726 rules (43.5% of the full list).
