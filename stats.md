# Blocklist stats

_Generated 2026-10-01 03:16:08 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,132 | 74,556 | 42.1% |
| HaGeZi Normal | 200,319 | 98,183 | 49.0% |
| AdAway | 6,540 | 3,449 | 52.7% |
| OISD Big | 245,305 | 164,158 | 66.9% |
| Dan Pollock | 13,082 | 9,928 | 75.9% |
| Peter Lowe | 7,136 | 3,884 | 54.4% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 53,478 | 9,231 | 17.3% |
| EasyPrivacy | 56,209 | 25,738 | 45.8% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,444 | 1,363 | 94.4% |
| uBO Badware | 4,247 | 4,197 | 98.8% |
| uBO Quick Fixes | 144 | 135 | 93.8% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **769,269** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 769,269 |
| **DNSZeroList.txt** (all sources, deduped) | **528,118** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **363,960** |

Deduplication removed 241,151 duplicate rule instances (31.3% of the raw total).
Dropping OISD Big removes a further 164,158 rules (31.1% of the full list).
