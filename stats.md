# Blocklist stats

_Generated 2026-10-02 03:16:57 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,459 | 74,568 | 42.0% |
| HaGeZi Normal | 198,941 | 96,586 | 48.6% |
| AdAway | 6,540 | 3,449 | 52.7% |
| OISD Big | 244,795 | 163,551 | 66.8% |
| Dan Pollock | 13,082 | 9,933 | 75.9% |
| Peter Lowe | 7,136 | 3,884 | 54.4% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 53,782 | 9,226 | 17.2% |
| EasyPrivacy | 56,211 | 25,738 | 45.8% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,444 | 1,363 | 94.4% |
| uBO Badware | 4,248 | 4,198 | 98.8% |
| uBO Quick Fixes | 144 | 135 | 93.8% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **768,015** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 768,015 |
| **DNSZeroList.txt** (all sources, deduped) | **526,113** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **362,562** |

Deduplication removed 241,902 duplicate rule instances (31.5% of the raw total).
Dropping OISD Big removes a further 163,551 rules (31.1% of the full list).
