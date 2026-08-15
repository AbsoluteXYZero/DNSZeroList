# Blocklist stats

_Generated 2026-08-15 00:43:02 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 155,895 | 57,018 | 36.6% |
| HaGeZi Normal | 181,000 | 82,212 | 45.4% |
| AdAway | 6,540 | 3,459 | 52.9% |
| OISD Big | 266,488 | 184,732 | 69.3% |
| Dan Pollock | 13,008 | 9,857 | 75.8% |
| Peter Lowe | 7,074 | 3,842 | 54.3% |
| Dandelion Sprout | 480 | 294 | 61.3% |
| EasyList | 54,033 | 9,321 | 17.3% |
| EasyPrivacy | 55,700 | 26,785 | 48.1% |
| uBO Ads | 1,769 | 1,725 | 97.5% |
| uBO Privacy | 1,407 | 1,328 | 94.4% |
| uBO Badware | 4,165 | 4,121 | 98.9% |
| uBO Quick Fixes | 90 | 81 | 90.0% |
| uBO Unbreak | 1,934 | 1,929 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **749,620** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 749,620 |
| **DNSZeroList.txt** (all sources, deduped) | **512,859** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **328,127** |

Deduplication removed 236,761 duplicate rule instances (31.6% of the raw total).
Dropping OISD Big removes a further 184,732 rules (36.0% of the full list).
