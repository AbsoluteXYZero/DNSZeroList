# Blocklist stats

_Generated 2026-08-07 12:42:14 UTC_

- **Total rules** = rules a source carries (after parsing to adblock form, including ones also present in other lists).
- **Unique** = rules that ONLY that source provides (exclusive contribution).
- **% unique** = Unique / Total for that source.

## Per source

| Source | Total rules | Unique | % unique |
| --- | ---: | ---: | ---: |
| AdGuard DNS Filter | 163,628 | 56,709 | 34.7% |
| HaGeZi Normal | 182,616 | 82,418 | 45.1% |
| AdAway | 6,540 | 3,464 | 53.0% |
| OISD Big | 435,332 | 353,598 | 81.2% |
| Dan Pollock | 12,988 | 9,841 | 75.8% |
| Peter Lowe | 7,066 | 3,838 | 54.3% |
| Dandelion Sprout | 480 | 292 | 60.8% |
| EasyList | 62,190 | 9,328 | 15.0% |
| EasyPrivacy | 55,650 | 26,773 | 48.1% |
| uBO Ads | 1,771 | 1,727 | 97.5% |
| uBO Privacy | 1,391 | 1,312 | 94.3% |
| uBO Badware | 4,274 | 4,228 | 98.9% |
| uBO Quick Fixes | 93 | 84 | 90.3% |
| uBO Unbreak | 1,932 | 1,927 | 99.7% |
| uBO Resource Abuse | 37 | 36 | 97.3% |
| **Sum (before dedup)** | **935,988** | | |

## Deduplicated totals

| Output | Rules |
| --- | ---: |
| Sum of all sources before dedup | 935,988 |
| **DNSZeroList.txt** (all sources, deduped) | **690,168** |
| **DNSZeroList_no_oisd.txt** (no OISD, deduped) | **336,570** |

Deduplication removed 245,820 duplicate rule instances (26.3% of the raw total).
Dropping OISD Big removes a further 353,598 rules (51.2% of the full list).
