# Blocklist stats

_Generated 2026-09-21 17:29:48 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 181,586 | 74,648 | 41.1% |
| HaGeZi Normal | 200,527 | 96,220 | 48.0% |
| AdAway | 6,540 | 3,456 | 52.8% |
| OISD Big | 246,496 | 166,039 | 67.4% |
| Dan Pollock | 13,082 | 9,931 | 75.9% |
| Peter Lowe | 7,132 | 3,883 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 58,308 | 9,237 | 15.8% |
| EasyPrivacy | 56,114 | 25,704 | 45.8% |
| uBO Ads | 1,775 | 1,731 | 97.5% |
| uBO Privacy | 1,438 | 1,358 | 94.4% |
| uBO Badware | 4,226 | 4,176 | 98.8% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,939 | 1,935 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **779,773** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 779,773 |
| **DNSZeroList.txt** (all sources, deduped) | **532,090** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **366,051** |

Deduplication removed 247,683 duplicate rule instances (31.8% of the raw total).
Dropping OISD Big removes a further 166,039 rules (31.2% of the full list).
