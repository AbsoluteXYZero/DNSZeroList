# Blocklist stats

_Generated 2026-09-11 02:11:56 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 178,139 | 74,914 | 42.1% |
| HaGeZi Normal | 181,641 | 78,858 | 43.4% |
| AdAway | 6,540 | 3,472 | 53.1% |
| OISD Big | 246,700 | 167,014 | 67.7% |
| Dan Pollock | 13,064 | 9,920 | 75.9% |
| Peter Lowe | 7,122 | 3,871 | 54.4% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 54,616 | 9,228 | 16.9% |
| EasyPrivacy | 56,005 | 25,669 | 45.8% |
| uBO Ads | 1,768 | 1,724 | 97.5% |
| uBO Privacy | 1,432 | 1,351 | 94.3% |
| uBO Badware | 4,236 | 4,187 | 98.8% |
| uBO Quick Fixes | 94 | 85 | 90.4% |
| uBO Unbreak | 1,937 | 1,933 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **753,811** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 753,811 |
| **DNSZeroList.txt** (all sources, deduped) | **512,711** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **345,697** |

Deduplication removed 241,100 duplicate rule instances (32.0% of the raw total).
Dropping OISD Big removes a further 167,014 rules (32.6% of the full list).
