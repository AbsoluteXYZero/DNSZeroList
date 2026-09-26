# Blocklist stats

_Generated 2026-09-26 02:42:04 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 183,048 | 75,438 | 41.2% |
| HaGeZi Normal | 164,218 | 80,593 | 49.1% |
| AdAway | 6,540 | 3,448 | 52.7% |
| OISD Big | 243,926 | 168,054 | 68.9% |
| Dan Pollock | 13,082 | 9,946 | 76.0% |
| Peter Lowe | 7,132 | 3,952 | 55.4% |
| Dandelion Sprout | 480 | 309 | 64.4% |
| EasyList | 59,662 | 9,229 | 15.5% |
| EasyPrivacy | 56,168 | 25,814 | 46.0% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,439 | 1,362 | 94.6% |
| uBO Badware | 4,227 | 4,177 | 98.8% |
| uBO Quick Fixes | 136 | 127 | 93.4% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 37 | 100.0% |
| **Sum (before dedup)** | **743,811** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 743,811 |
| **DNSZeroList.txt** (all sources, deduped) | **515,909** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **347,855** |

Deduplication removed 227,902 duplicate rule instances (30.6% of the raw total).
Dropping OISD Big removes a further 168,054 rules (32.6% of the full list).
