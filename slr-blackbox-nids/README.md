# SLR (in progress): Black-Box Evasion Attacks Against ML-Based NIDS

**Overall status: INCOMPLETE. This is not a manuscript and must not be described as submission-ready.**

| Stage | Status | File |
|---|---|---|
| 1 Feasibility and novelty audit | Provisional (abstracts only; comparator full texts not read) | `01_feasibility_and_novelty_audit.md` |
| 2 Protocol | Provisional, unregistered | `02_protocol.md` |
| 3 Searches and screening | Partially completed and evidenced | `03_search_and_screening_report.md` |
| 4 Full-text extraction and appraisal | Pending external access | `04_outstanding_actions.md` |
| 5–7 Synthesis, manuscript, integrity audit | Not started | — |

## Data (all files exist in this folder)
- `data/search_log.csv`: every executed search (source, exact query, fields, date, filters, returned, exported, cap).
- `data/seed_coverage_test.csv`: seed papers and whether each search round found them.
- `data/screening_log_blackbox_subset.csv`: manual title/abstract decisions for 129 records, with reasons.
- `data/candidate_register.csv`: 63 candidates with Crossref-verified metadata and separate status fields (journal eligibility, full text retrieved, extracted, independently checked). All quartile and full-text fields are pending.
- `data/raw/`: raw API exports and intermediate files (JSON).
- `scripts/`: `s2search.py` (Semantic Scholar search with logging), `crsearch.py` (Crossref search with logging), `lookup.py` (Crossref title verification).

Screening and pre-screening rules were run as inline scripts during the session. Their logic is described in `03_search_and_screening_report.md` §3; they are not yet saved as standalone files (OA-9).
