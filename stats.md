# Blocklist stats

_Generated 2026-09-12 02:18:03 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 178,503 | 74,953 | 42.0% |
| HaGeZi Normal | 180,051 | 79,739 | 44.3% |
| AdAway | 6,540 | 3,471 | 53.1% |
| OISD Big | 245,133 | 166,724 | 68.0% |
| Dan Pollock | 13,064 | 9,921 | 75.9% |
| Peter Lowe | 7,148 | 3,886 | 54.4% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 54,962 | 9,227 | 16.8% |
| EasyPrivacy | 56,011 | 25,673 | 45.8% |
| uBO Ads | 1,768 | 1,724 | 97.5% |
| uBO Privacy | 1,433 | 1,352 | 94.3% |
| uBO Badware | 4,239 | 4,189 | 98.8% |
| uBO Quick Fixes | 94 | 85 | 90.4% |
| uBO Unbreak | 1,935 | 1,931 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **751,398** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 751,398 |
| **DNSZeroList.txt** (all sources, deduped) | **512,269** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **345,545** |

Deduplication removed 239,129 duplicate rule instances (31.8% of the raw total).
Dropping OISD Big removes a further 166,724 rules (32.5% of the full list).
