# Blocklist stats

_Generated 2026-10-29 17:48:43 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 185,224 | 84,622 | 45.7% |
| HaGeZi Normal | 172,633 | 73,371 | 42.5% |
| AdAway | 6,540 | 3,448 | 52.7% |
| OISD Big | 234,686 | 151,577 | 64.6% |
| Dan Pollock | 12,971 | 9,860 | 76.0% |
| Peter Lowe | 7,166 | 3,902 | 54.5% |
| Dandelion Sprout | 480 | 301 | 62.7% |
| EasyList | 50,974 | 9,277 | 18.2% |
| EasyPrivacy | 56,396 | 26,115 | 46.3% |
| uBO Ads | 1,775 | 1,732 | 97.6% |
| uBO Privacy | 1,456 | 1,370 | 94.1% |
| uBO Badware | 4,855 | 4,805 | 99.0% |
| uBO Quick Fixes | 221 | 210 | 95.0% |
| uBO Unbreak | 1,946 | 1,942 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **737,360** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 737,360 |
| **DNSZeroList.txt** (all sources, deduped) | **498,555** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **346,978** |

Deduplication removed 238,805 duplicate rule instances (32.4% of the raw total).
Dropping OISD Big removes a further 151,577 rules (30.4% of the full list).
