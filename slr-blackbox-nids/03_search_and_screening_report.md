# Stage 3 — Executed Searches and Screening (partial)

**Status: Partially completed and evidenced.** Every count below comes from the files in `data/`. Nothing is estimated.

## 1. Executed searches (16 November 2026)
Full log: `data/search_log.csv` (raw: `data/raw/search_log.jsonl`; exports: `data/raw/*.json`).

| Tag | Source and fields searched | Query (abridged; exact text in the log) | Date filter | Returned | Exported |
|---|---|---|---|---|---|
| S2-focused | Semantic Scholar bulk search: title + abstract | (intrusion detection \| NIDS \| network intrusion) + (adversarial \| evasion) + (black-box terms \| query-/decision-/score-based \| transferab* \| surrogate/substitute model*) | 2020–2026 | 154 | 154 |
| S2-broad | Semantic Scholar: title + abstract | (network intrusion detection \| NIDS) + (adversarial \| evasion) + (machine learning \| deep learning) | 2020–2026 | 443 | 443 |
| S2-reviews | Semantic Scholar: title + abstract | (intrusion detection \| NIDS) + (adversarial \| evasion) + (survey \| review \| systematic …) | 2020–2026 | 401 | 401 |
| S2-amend1 | Semantic Scholar: title + abstract | (intrusion detection \| botnet detection/detector* \| network traffic classif* \| flow-based detect* \| anomaly detection system*) + (adversarial \| evasion \| evasion attack*) + (network \| traffic \| flow*) | 2020–2026 | 2,373 | 2,373 |
| CR ×8 | Crossref `query.bibliographic` (metadata fields; **not** abstracts or full text) | 8 strings (see log) | from 2020-01-01; type = journal-article | 0.5–3.6 M (relevance-ranked) | 200 each (199 for one) = 1,599 |

**Not searched** (inaccessible from this environment): Scopus, Web of Science, IEEE Xplore, ACM DL, ScienceDirect, SpringerLink, Wiley. Ready-to-run adaptations are in §5. Crossref metadata lookup is **not** equivalent to searching publisher full-text databases.

## 2. Seed coverage test and amendment
Fourteen seed titles were identified independently (from domain knowledge) and verified in Crossref; 12 resolved to the intended journal article (`data/seed_coverage_test.csv`).
- The initial S2 queries (focused, broad, reviews) found **9/12**. Missed: Alhajjar et al., *ESWA* 2021; Apruzzese et al., *IEEE TNSM* 2020 ("botnet detection" wording); Chen et al., *Digital Communications and Networks* 2021.
- **Amendment 1** (documented): the S2-amend1 query (broader detector vocabulary) plus the Crossref searches. After the amendment, **12/12** seeds were found.

## 3. Records, deduplication and pre-screening (actual counts)
| Step | Count | Source |
|---|---|---|
| Records exported (S2 3,371 + Crossref 1,599) | 4,970 | search log |
| Unique records after de-duplication (DOI, else S2 ID) | 3,388 | `raw/all_records.json` |
| Removed: no DOI (journal version cannot be verified) | 40 | script |
| Removed: preprint DOI or venue (arXiv/SSRN/TechRxiv/Research Square/Preprints) | 135 | script |
| Removed: not a journal article (Semantic Scholar type) | 621 | script |
| **Remaining after publication-type rules** | **2,592** | |
| Removed by automated relevance rule 1 (lacks adversarial/evasion terms *and* network-IDS terms) or off-domain title | 971 | script |
| Removed by automated relevance rule 2 (no adversarial-attack/evasion phrase or no network-IDS phrase) | 825 | script |
| **Remaining for manual title/abstract screening** | **796** | `raw/screen2.json` |

⚠ **Deviation from the brief:** 995 of the rule-excluded records had **no abstract available**, so the rules were effectively applied to their **titles only**. The brief prohibits title-only relevance filtering. These 995 records must be re-screened once abstracts are obtained (Outstanding action OA-3). The automated rules are also stricter than the brief intends, and must be validated or replaced by manual screening.

## 4. Manual title/abstract screening (partial)
Of the 796 records, **129** state a black-box, query, surrogate/substitute, transfer or gray-box element in the title or abstract. **All 129 were screened manually** (`data/screening_log_blackbox_subset.csv`):
- **56** included for full-text assessment;
- **3** routed to the review register;
- **70** excluded (conference proceedings that Semantic Scholar mislabels as journals; off-topic; poisoning; host-only; non-NIDS).

The remaining **667** records were **not yet screened manually**. They may contain black-box experiments not mentioned in the abstract (OA-4).

In addition, **7 seed articles** were added to the candidate register directly (one may be white-box only). **Candidate register: 63 records** (`data/candidate_register.csv`), all with Crossref-verified metadata and none with verified quartile or full text. The reviewer expects 11 of them to fall below Q2 or be unranked, but this is **not verified**, and they remain in the register.

## 5. Database-specific strings for the outstanding searches (not executed)
**Scopus (TITLE-ABS-KEY):**
```
TITLE-ABS-KEY ( ( "intrusion detection" OR "network intrusion detection" OR nids OR "botnet detect*" )
 AND ( "adversarial example*" OR "adversarial attack*" OR evasion )
 AND ( "black box" OR "black-box" OR blackbox OR "query based" OR "query-based" OR "decision based" OR "decision-based"
       OR "score based" OR "score-based" OR transferab* OR "surrogate model*" OR "substitute model*" ) )
 AND PUBYEAR > 2019 AND ( LIMIT-TO ( DOCTYPE , "ar" ) ) AND ( LIMIT-TO ( SRCTYPE , "j" ) )
```
Broad complement: `TITLE-ABS-KEY ( ( "network intrusion detection" OR nids ) AND ( adversarial OR evasion ) AND ( "machine learning" OR "deep learning" ) ) AND PUBYEAR > 2019 AND DOCTYPE(ar)`.
**Web of Science (TS=):** `TS=(("intrusion detection" OR NIDS) AND ("adversarial example*" OR "adversarial attack*" OR evasion) AND ("black box" OR "black-box" OR "query-based" OR "decision-based" OR "score-based" OR transferab* OR "surrogate model*" OR "substitute model*"))`, Document Type = Article, PY = 2020–2026.
**IEEE Xplore (Command Search, All Metadata):** `("intrusion detection" OR NIDS) AND (adversarial OR evasion) AND ("black-box" OR "black box" OR "query-based" OR transferability OR surrogate OR substitute)`, Content type = Journals, 2020–2026.
**ACM DL / ScienceDirect / SpringerLink / Wiley:** same terms in Abstract/Title/Keywords fields, article type = research article, 2020 onward.

## 6. PRISMA 2020 flow: status of each box
| PRISMA box | Value |
|---|---|
| Records identified — databases | S2 3,371; Crossref 1,599 (other databases: **not searched**) |
| Records identified — other methods | 14 seed titles (12 verified) |
| Duplicates removed | 1,582 (4,970 − 3,388) |
| Records removed by automated rules | 2,592 (publication-type rules 796 + relevance rules 1,796)ᵃ; 3,388 − 2,592 = 796 remain |
| Records screened (title/abstract, manual) | 129 of 796 (**667 pending**) |
| Records excluded at title/abstract | 70 (+3 routed to reviews) |
| Reports sought for retrieval | 63 |
| Reports not retrieved | **63** (no full-text access yet) |
| Reports assessed for eligibility | **0** |
| Studies included | **0 (review incomplete)** |

ᵃ Exact breakdown: publication-type rules removed 796 (40 + 135 + 621); relevance rules removed 1,796 (971 + 825); 995 of those 1,796 were title-only (see deviation). This table will be completed only from recorded counts.
