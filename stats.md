# Blocklist stats

_Generated 2026-07-04 02:03:18 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 154,716 | 56,926 | 36.8% |
| HaGeZi Normal | 154,710 | 57,738 | 37.3% |
| AdAway | 6,540 | 3,534 | 54.0% |
| OISD Big | 325,704 | 246,421 | 75.7% |
| Dan Pollock | 12,909 | 9,787 | 75.8% |
| Peter Lowe | 7,058 | 3,835 | 54.3% |
| Dandelion Sprout | 480 | 285 | 59.4% |
| EasyList | 53,486 | 9,326 | 17.4% |
| EasyPrivacy | 55,457 | 26,676 | 48.1% |
| uBO Ads | 1,787 | 1,738 | 97.3% |
| uBO Privacy | 1,372 | 1,290 | 94.0% |
| uBO Badware | 4,159 | 4,114 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,925 | 1,921 | 99.8% |
| uBO Resource Abuse | 36 | 35 | 97.2% |
| **Sum (before dedup)** | **780,432** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 780,432 |
| **DNSZeroList.txt** (all sources, deduped) | **548,710** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **302,289** |

Deduplication removed 231,722 duplicate rule instances (29.7% of the raw total).
Dropping OISD Big removes a further 246,421 rules (44.9% of the full list).
