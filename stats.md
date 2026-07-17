# Blocklist stats

_Generated 2026-07-17 01:53:25 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 158,008 | 56,915 | 36.0% |
| HaGeZi Normal | 162,593 | 65,119 | 40.1% |
| AdAway | 6,540 | 3,483 | 53.3% |
| OISD Big | 324,447 | 242,157 | 74.6% |
| Dan Pollock | 12,944 | 9,771 | 75.5% |
| Peter Lowe | 7,082 | 3,844 | 54.3% |
| Dandelion Sprout | 480 | 290 | 60.4% |
| EasyList | 56,487 | 9,316 | 16.5% |
| EasyPrivacy | 55,521 | 26,694 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,380 | 1,298 | 94.1% |
| uBO Badware | 4,173 | 4,126 | 98.9% |
| uBO Quick Fixes | 96 | 86 | 89.6% |
| uBO Unbreak | 1,930 | 1,925 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **793,492** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 793,492 |
| **DNSZeroList.txt** (all sources, deduped) | **557,443** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **315,286** |

Deduplication removed 236,049 duplicate rule instances (29.7% of the raw total).
Dropping OISD Big removes a further 242,157 rules (43.4% of the full list).
