# Blocklist stats

_Generated 2026-10-02 17:05:49 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 177,654 | 74,543 | 42.0% |
| HaGeZi Normal | 199,122 | 96,731 | 48.6% |
| AdAway | 6,540 | 3,449 | 52.7% |
| OISD Big | 244,464 | 163,233 | 66.8% |
| Dan Pollock | 13,082 | 9,933 | 75.9% |
| Peter Lowe | 7,134 | 3,885 | 54.5% |
| Dandelion Sprout | 480 | 300 | 62.5% |
| EasyList | 53,960 | 9,224 | 17.1% |
| EasyPrivacy | 56,213 | 25,738 | 45.8% |
| uBO Ads | 1,776 | 1,733 | 97.6% |
| uBO Privacy | 1,445 | 1,363 | 94.3% |
| uBO Badware | 4,248 | 4,198 | 98.8% |
| uBO Quick Fixes | 144 | 135 | 93.8% |
| uBO Unbreak | 1,940 | 1,936 | 99.8% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **768,239** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 768,239 |
| **DNSZeroList.txt** (all sources, deduped) | **526,086** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **362,853** |

Deduplication removed 242,153 duplicate rule instances (31.5% of the raw total).
Dropping OISD Big removes a further 163,233 rules (31.0% of the full list).
