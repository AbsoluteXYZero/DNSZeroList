# Blocklist stats

_Generated 2026-08-17 00:43:34 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 156,625 | 56,986 | 36.4% |
| HaGeZi Normal | 182,539 | 82,871 | 45.4% |
| AdAway | 6,540 | 3,463 | 53.0% |
| OISD Big | 269,567 | 187,097 | 69.4% |
| Dan Pollock | 13,008 | 9,856 | 75.8% |
| Peter Lowe | 7,074 | 3,842 | 54.3% |
| Dandelion Sprout | 480 | 294 | 61.3% |
| EasyList | 54,620 | 9,343 | 17.1% |
| EasyPrivacy | 55,835 | 26,761 | 47.9% |
| uBO Ads | 1,770 | 1,726 | 97.5% |
| uBO Privacy | 1,407 | 1,328 | 94.4% |
| uBO Badware | 4,166 | 4,122 | 98.9% |
| uBO Quick Fixes | 90 | 81 | 90.0% |
| uBO Unbreak | 1,934 | 1,929 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **755,692** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 755,692 |
| **DNSZeroList.txt** (all sources, deduped) | **516,795** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **329,698** |

Deduplication removed 238,897 duplicate rule instances (31.6% of the raw total).
Dropping OISD Big removes a further 187,097 rules (36.2% of the full list).
