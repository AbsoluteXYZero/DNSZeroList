# Blocklist stats

_Generated 2026-07-27 02:04:58 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 160,515 | 56,755 | 35.4% |
| HaGeZi Normal | 181,044 | 82,733 | 45.7% |
| AdAway | 6,540 | 3,465 | 53.0% |
| OISD Big | 334,046 | 252,562 | 75.6% |
| Dan Pollock | 12,961 | 9,807 | 75.7% |
| Peter Lowe | 7,058 | 3,830 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 59,237 | 9,332 | 15.8% |
| EasyPrivacy | 55,567 | 26,738 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,386 | 1,304 | 94.1% |
| uBO Badware | 4,186 | 4,139 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **826,855** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 826,855 |
| **DNSZeroList.txt** (all sources, deduped) | **586,484** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **333,922** |

Deduplication removed 240,371 duplicate rule instances (29.1% of the raw total).
Dropping OISD Big removes a further 252,562 rules (43.1% of the full list).
