# Blocklist stats

_Generated 2026-09-19 02:23:11 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 180,696 | 74,715 | 41.3% |
| HaGeZi Normal | 199,045 | 95,546 | 48.0% |
| AdAway | 6,540 | 3,458 | 52.9% |
| OISD Big | 247,354 | 167,229 | 67.6% |
| Dan Pollock | 13,082 | 9,931 | 75.9% |
| Peter Lowe | 7,124 | 3,876 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 57,441 | 9,214 | 16.0% |
| EasyPrivacy | 56,075 | 25,691 | 45.8% |
| uBO Ads | 1,763 | 1,719 | 97.5% |
| uBO Privacy | 1,437 | 1,356 | 94.4% |
| uBO Badware | 4,142 | 4,093 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,939 | 1,935 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **777,248** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 777,248 |
| **DNSZeroList.txt** (all sources, deduped) | **531,762** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **364,533** |

Deduplication removed 245,486 duplicate rule instances (31.6% of the raw total).
Dropping OISD Big removes a further 167,229 rules (31.4% of the full list).
