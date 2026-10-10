# Blocklist stats

_Generated 2026-10-10 16:39:03 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 181,836 | 78,631 | 43.2% |
| HaGeZi Normal | 159,965 | 62,694 | 39.2% |
| AdAway | 6,540 | 3,456 | 52.8% |
| OISD Big | 237,804 | 159,563 | 67.1% |
| Dan Pollock | 13,083 | 9,972 | 76.2% |
| Peter Lowe | 7,128 | 3,884 | 54.5% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 56,260 | 9,229 | 16.4% |
| EasyPrivacy | 56,266 | 26,002 | 46.2% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,445 | 1,362 | 94.3% |
| uBO Badware | 4,263 | 4,212 | 98.8% |
| uBO Quick Fixes | 160 | 151 | 94.4% |
| uBO Unbreak | 1,941 | 1,937 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **728,984** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 728,984 |
| **DNSZeroList.txt** (all sources, deduped) | **491,061** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **331,498** |

Deduplication removed 237,923 duplicate rule instances (32.6% of the raw total).
Dropping OISD Big removes a further 159,563 rules (32.5% of the full list).
