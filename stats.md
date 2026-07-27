# Blocklist stats

_Generated 2026-07-27 14:12:33 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 160,660 | 56,737 | 35.3% |
| HaGeZi Normal | 181,394 | 82,890 | 45.7% |
| AdAway | 6,540 | 3,465 | 53.0% |
| OISD Big | 334,835 | 253,287 | 75.6% |
| Dan Pollock | 12,962 | 9,809 | 75.7% |
| Peter Lowe | 7,058 | 3,830 | 54.3% |
| Dandelion Sprout | 480 | 289 | 60.2% |
| EasyList | 59,383 | 9,334 | 15.7% |
| EasyPrivacy | 55,573 | 26,742 | 48.1% |
| uBO Ads | 1,774 | 1,728 | 97.4% |
| uBO Privacy | 1,387 | 1,305 | 94.1% |
| uBO Badware | 4,186 | 4,139 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,931 | 1,926 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **828,293** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 828,293 |
| **DNSZeroList.txt** (all sources, deduped) | **587,535** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **334,248** |

Deduplication removed 240,758 duplicate rule instances (29.1% of the raw total).
Dropping OISD Big removes a further 253,287 rules (43.1% of the full list).
