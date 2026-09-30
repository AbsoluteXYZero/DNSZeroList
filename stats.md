# Blocklist stats

_Generated 2026-09-30 17:17:47 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 176,981 | 74,555 | 42.1% |
| HaGeZi Normal | 200,319 | 98,170 | 49.0% |
| AdAway | 6,540 | 3,449 | 52.7% |
| OISD Big | 244,267 | 163,252 | 66.8% |
| Dan Pollock | 13,082 | 9,928 | 75.9% |
| Peter Lowe | 7,136 | 3,884 | 54.4% |
| Dandelion Sprout | 480 | 299 | 62.3% |
| EasyList | 53,338 | 9,232 | 17.3% |
| EasyPrivacy | 56,188 | 25,727 | 45.8% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,444 | 1,363 | 94.4% |
| uBO Badware | 4,247 | 4,197 | 98.8% |
| uBO Quick Fixes | 144 | 135 | 93.8% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **767,919** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 767,919 |
| **DNSZeroList.txt** (all sources, deduped) | **527,053** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **363,801** |

Deduplication removed 240,866 duplicate rule instances (31.4% of the raw total).
Dropping OISD Big removes a further 163,252 rules (31.0% of the full list).
