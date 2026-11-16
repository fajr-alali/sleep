# Black-Box Evasion Attacks Against ML-Based NIDS — Systematic Review: Stage 1–3 Package

**Date:** 16 November 2026  
**Overall status: INCOMPLETE — not a manuscript; not submission-ready.**

| Stage | Status |
|---|---|
| 1 Feasibility and novelty audit | Provisional (abstracts only; comparator full texts not read) |
| 2 Protocol | Provisional, unregistered |
| 3 Searches and screening | Partially completed and evidenced |
| 4 Full-text extraction and appraisal | Pending external access |
| 5–7 Synthesis, manuscript, integrity audit | Not started |

## Contents
1. Feasibility and novelty audit
2. Review protocol
3. Executed searches and screening
4. Outstanding-actions register
Appendix A. Search log · Appendix B. Seed coverage test · Appendix C. Candidate register · Appendix D. Title/abstract screening log

---

## 1. Feasibility and Novelty Audit

**Review topic:** Black-Box Evasion Attacks Against Machine Learning-Based Network Intrusion Detection Systems: A Systematic Literature Review of Attacker Capabilities, Attack Costs, Transferability, and Defense Evaluation
**Audit date:** 16 November 2026
**Status: Provisional.** Full texts of the comparator reviews could **not** be retrieved from this environment (see §1). Every comparison below is based on **abstracts and bibliographic metadata only**, and is labelled accordingly. Step B of the brief ("inspect their full texts") is **not done**.

---

### 1.1 Access conditions that constrain this audit

| Source | Purpose | Result in this environment (16 Nov 2026) |
|---|---|---|
| Crossref REST API | Metadata, DOI, ISSN, type, update/retraction flags | Accessible |
| Semantic Scholar Graph API | Title+abstract search; abstracts | Accessible (rate-limited) |
| Unpaywall API | Open-access locations | Accessible |
| SCImago (scimagojr.com) | Quartile verification | **Not accessible**: the site returned HTTP 403 to automated requests; further attempts were stopped |
| Publisher full text (MDPI, IEEE Xplore, ScienceDirect, …) | Full-text reading | **Not accessible**: MDPI returned 403; the IEEE open-access PDF request was blocked by the session's safety policy; no further attempts were made |
| Scopus, Web of Science, IEEE Xplore search, ACM DL search | Database searching | **Not accessible / not searched** |

Consequences: (i) no journal quartile has been verified; (ii) no full text has been read; (iii) database coverage is limited to Semantic Scholar (title + abstract) and Crossref (metadata).

---

### 1.2 Closest existing reviews identified

These were identified from the executed searches (`data/search_log.csv`, tag `S2-reviews` and others). Inclusion here does **not** mean the Q1/Q2 policy was verified; that is pending for all of them.

| ID | Review (DOI) | Type / journal | Abstract-level scope | Basis |
|---|---|---|---|---|
| RV1 | *Adversarial Evasion in Machine-Learning-Based Network Intrusion Detection: A Systematic Review, Threat Modeling, and …* — 10.1109/ACCESS.2026.3720554 | IEEE Access, 2026 | Kitchenham-informed SLR of **186 studies (2018–2026)**; NIDS-specific, lifecycle-aware threat model; taxonomy across adversarial generation, robustness evaluation and defence; finds that "much reported evasion success reflects diagnostic feature-space sensitivity rather than executable, deployable adversarial risk" and that "many defenses demonstrate component-level robustness" | Abstract |
| RV2 | *Adversarial Robustness of Deep Learning-Based Intrusion Detection Systems: A Systematic Literature Review of Attacks, De…* — 10.1109/ACCESS.2026.3733985 | IEEE Access, 2026 | PRISMA 2020 SLR, Jan 2020–Mar 2026; 5,890 records from Scopus, IEEE Xplore, WoS and ScienceDirect; **216 primary studies**; reports FGSM in 76.9%, C&W 60.2%, PGD 50.9%, adversarial training 61.6%, and **query-based black-box attacks rare** (Square Attack 2.8%, AutoAttack 2.3%) | Abstract |
| RV3 | *Understanding the adversary: A survey of adversarial machine learning in network intrusion detection* — 10.1016/j.cosrev.2026.100995 | Computer Science Review, 2026 | Abstract not available via open APIs | Title only |
| RV4 | *Adversarial Machine Learning for Network Intrusion Detection Systems: A Comprehensive Survey* — 10.1109/COMST.2022.3233793 | IEEE Communications Surveys & Tutorials, 2023 | Survey since 2015; CV-vs-NIDS differences; reviews **white-box and black-box** attacks and their applicability to NIDS; defences | Abstract |
| RV5 | *Adversarial machine learning for network intrusion detection: A comparative study* — 10.1016/j.comnet.2022.109073 | Computer Networks, 2022 | Abstract not available via open APIs | Title only |
| RV6 | *Adversarial Machine Learning Attacks against Intrusion Detection Systems: A Survey on Strategies and Defense* — 10.3390/fi15020062 | Future Internet, 2023 | Survey of attack types against IDS and defence strategies; gaps | Abstract |
| RV7 | *Contrast Duality of Adversarial Learning in Network Intrusion: A Review* — 10.1109/TAI.2025.3641908 | IEEE Transactions on Artificial Intelligence, 2026 | Poisoning, test-time evasion, reverse engineering; adversarial training as defence | Abstract (published version; the open copy is an arXiv preprint and was **not** used) |
| RV8 | *Adversarial Machine Learning Applied to Intrusion and Malware Scenarios: A Systematic Review* — 10.1109/ACCESS.2020.2974752 | IEEE Access, 2020 | AML in intrusion and malware detection; practicality untested in intrusion scenarios; small, outdated datasets | Abstract |
| RV9 | *A Holistic Review of Machine Learning Adversarial Attacks in IoT Networks* — 10.3390/fi16010032 | Future Internet, 2024 | IoT IDS, malware detection and device identification; two-dimensional attack framework | Abstract |
| RV10 | *Adversarial Machine Learning in IoT Security: A Comprehensive Survey* — 10.1145/3785665 | ACM Computing Surveys, 2025 | AML for IoT IDS; MITRE-inspired attack framework; human-in-the-loop | Abstract |
| RV11 | *Functionality-Preserving Adversarial Machine Learning for Robust Classification in Cybersecurity and Intrusion Detection* — 10.3390/jcp2010010 | Journal of Cybersecurity and Privacy, 2022 | Survey focused on functionality preservation | Abstract |

**Contextual literature (outside the Q1/Q2 journal policy, not used as comparators):** *Adversarial Black-Box Attacks Against Network Intrusion Detection Systems: A Survey* (IEEE AIIoT 2021 conference, 10.1109/AIIoT52608.2021.9454214), the closest topical match by title; two arXiv-only reviews (10.48550/arXiv.2112.03315, 10.48550/arXiv.2303.07003).

---

### 1.3 Overlap assessment (abstract-level, provisional)

| Proposed contribution element | RV1 (IEEE Access 2026) | RV2 (IEEE Access 2026) | RV4 (COMST 2023) | Others |
|---|---|---|---|---|
| NIDS-specific threat model / attacker capabilities (RQ1) | **Yes**: "lifecycle-aware, NIDS-specific threat model" | Not stated | Partly: black-box vs white-box applicability | RV10: attack lifecycle framework |
| Feature-space vs executable/traffic-space realizability | **Yes**: central finding | Not stated | Yes: CV-vs-NIDS feature-space differences | RV11: functionality preservation |
| Black-box-specific synthesis (query vs transfer vs surrogate) | Not stated | **Partly**: quantifies how rare query-based black-box attacks are | Partly | — |
| **Attack-cost accounting** (queries, compute, data, bytes/packets, delay) | Not stated in abstract | Not stated in abstract | Not stated | Not stated |
| **Transferability evidence map** (cross-model, cross-dataset, cross-pipeline, cross-environment) | Not stated in abstract | Not stated in abstract | Not stated | Not stated |
| Defence-evaluation rigour (adaptive attackers, valid traffic) | **Yes**: "component-level robustness" critique | Partly: defence frequencies, certified defences rare | Partly | — |
| PRISMA / systematic method | Kitchenham-informed | PRISMA 2020, 216 studies, κ = 0.81 on a sample | Survey | RV8 systematic |

"Not stated in abstract" does **not** mean the review omits the topic; this must be checked in the full text before any differentiation claim.

---

### 1.4 Is a differentiated review still justified? (provisional answer)

- **Substantial overlap exists.** RV1 already offers an NIDS-specific threat model and the feature-space vs executable-risk critique; RV2 already quantifies, at scale and with PRISMA, how rare query-based black-box attacks are and how dominant adversarial training is. A broad "adversarial evasion against NIDS" SLR would **not** be justified.
- **A narrower contribution may remain**, *if* full-text inspection of RV1, RV2 and RV3 confirms they do not systematically extract: (a) **target-query vs local-compute vs traffic costs** with explicit success denominators; (b) a **source–target transferability evidence map** that separates cross-model, cross-dataset, cross-pipeline and cross-environment transfer; (c) a **capability matrix** separating feedback type from data/feature/pipeline knowledge, specifically for black-box attacks.
- **Feasibility risk.** RV2 reports query-based black-box attacks in under 3% of 216 deep-learning IDS studies. Our title/abstract screening of the black-box subset kept 56 journal candidates (plus 7 seeds), and 11 of those appear in venues the reviewer expects to fall below Q2 (not verified). After SJR verification and full-text eligibility, the Q1/Q2 black-box corpus may be **at or below ~25 studies**. If so, the recommended design is a **focused SLR, or a systematic mapping review, on black-box NIDS evasion costs and transferability**, explicitly positioned as a deep extension of RV1/RV2, not a replacement.

**Recommendation (provisional):** Do not proceed to the full manuscript until (1) the full texts of RV1, RV2 and RV3 are compared against the extraction framework, and (2) SJR quartiles of the candidate journals are verified. Revisit the title and contribution claims after that comparison. The candidate phrase "capability-conditioned, cost-aware synthesis" must not be claimed as novel until step (1) is complete.

---

## 2. Review Protocol

**Registration:** Not registered. No PROSPERO/OSF identifier exists; none is claimed.
**Protocol status:** Drafted *after* the initial searches were executed (same day). Search amendments are documented in `03_search_and_screening_report.md`. Prospective registration is recommended before Stage 4.
**Reviewers:** One reviewer (AI-assisted: Claude, under the user's direction). No second reviewer; no agreement statistic exists.

### 2.1 Research questions (exactly four)
- **RQ1:** What knowledge, feedback, access, and traffic-manipulation capabilities are assumed for attackers conducting black-box evasion against ML-based network intrusion detection systems?
- **RQ2:** What black-box evasion methods are evaluated, and what query, computational, data-acquisition, and network-perturbation costs are reported for successful evasion?
- **RQ3:** How transferable are black-box evasion attacks across target models, training datasets, feature-extraction pipelines, and network environments, and under what experimental conditions is transferability demonstrated?
- **RQ4:** How rigorously are defenses evaluated against black-box evasion, particularly regarding adaptive attackers, realistic traffic constraints, clean detection performance, and reproducibility?

### 2.2 Eligibility
**Include:** peer-reviewed journal articles; Q1/Q2 under §3; published 1 Jan 2020 – search date; inference-time evasion against ML/DL **network** IDS (flow- or packet-based; enterprise, cloud, SDN, IoT, IIoT, ICS, and in-vehicle networks*); at least one query-based, transfer-based, surrogate-based or hybrid black-box attack whose results can be extracted separately; or a defence evaluated against at least one such attack.
\*In-vehicle (CAN) IDS: included as "other network setting". This is a reviewer decision made at screening and is flagged for sensitivity analysis.

**Exclude:** preprints (arXiv, SSRN, TechRxiv, Research Square); conference/workshop papers, theses, reports, white papers; retracted articles; poisoning/backdoor as the main attack; model extraction or membership inference only; purely white-box studies; malware-file, phishing, image, spam or source-code tasks; host-only IDS; IDS studies with no adversarial evaluation; GAN data augmentation without an attacker; benign distribution shift; protocol fuzzing unrelated to ML evasion.

Overlapping publications: a journal paper and its earlier conference version are grouped into one *study family*; only the journal version is extracted.

### 2.3 Journal-ranking policy (predefined before any verification)
- **Source:** SCImago Journal Rank (SJR).
- **Predefined subject categories:** Computer Networks and Communications; Computer Science Applications; Information Systems; Artificial Intelligence; Software; Hardware and Architecture; Signal Processing; Electrical and Electronic Engineering; Safety, Risk, Reliability and Quality; Computer Science (miscellaneous); Control and Systems Engineering.
- **Rule:** eligible if Q1 or Q2 in **any** predefined category that the journal is listed under in the SJR ranking year. Record every category and quartile, not only the qualifying one.
- **Year:** publication-year quartile; if not yet published (e.g., 2026), the latest available year is used and labelled **proxy**. No 2026 quartile will be invented.
- **Record:** journal, ISSN/eISSN, publication year, SJR year, category, quartile, verification URL, verification date.
- **Status today:** **pending for every journal**. SCImago is not reachable from this environment.

### 2.4 Extraction framework
As specified in the brief (§9 A–H): bibliographic data; detection setting; attacker capabilities (eight knowledge items; feedback type: score, hard-label, indirect, none, unclear; local-surrogate white-box access vs target black-box access); attack method; costs (target queries by stage, surrogate cost, data acquisition, wall-clock time, hardware, bytes/packets/flows/delay, per-attempt vs per-success, one-time vs recurring); transferability (source/target, family, dataset, pipeline, environment, leakage); defence evaluation; reproducibility artefacts. Every substantive claim is recorded with page, section/table/figure and an evidence note, using the labels: Reported / Explicitly not implemented / Not reported / Unclear / Not applicable.

### 2.5 Appraisal
Eight domains (brief §11), each judged Adequate / Partially adequate / Inadequate / Unclear / Not applicable with page-level evidence. No aggregate score threshold.

### 2.6 Synthesis
Structured narrative per RQ with descriptive statistics and exact denominators; transfer matrices where reported; a conceptual cost vector C = (target queries, local compute, data acquisition, added bytes, added packets, delay), presented as a descriptive framework only. Meta-analysis only if comparable outcomes exist (not expected).

### 2.7 Status of this protocol's stages
| Stage | Status |
|---|---|
| 1 Feasibility and novelty audit | **Provisional** (abstract-level only) |
| 2 Protocol | **Provisional** (this document; unregistered) |
| 3 Searches and screening | **Partially completed and evidenced** (see report) |
| 4 Full-text extraction and appraisal | **Pending external access** |
| 5–7 Synthesis, manuscript, integrity audit | **Not started** |

---

## 3. Executed Searches and Screening

**Status: Partially completed and evidenced.** Every count below comes from the files in `data/`. Nothing is estimated.

### 3.1 Executed searches (16 November 2026)
Full log: `data/search_log.csv` (raw: `data/raw/search_log.jsonl`; exports: `data/raw/*.json`).

| Tag | Source and fields searched | Query (abridged; exact text in the log) | Date filter | Returned | Exported |
|---|---|---|---|---|---|
| S2-focused | Semantic Scholar bulk search: title + abstract | (intrusion detection \| NIDS \| network intrusion) + (adversarial \| evasion) + (black-box terms \| query-/decision-/score-based \| transferab* \| surrogate/substitute model*) | 2020–2026 | 154 | 154 |
| S2-broad | Semantic Scholar: title + abstract | (network intrusion detection \| NIDS) + (adversarial \| evasion) + (machine learning \| deep learning) | 2020–2026 | 443 | 443 |
| S2-reviews | Semantic Scholar: title + abstract | (intrusion detection \| NIDS) + (adversarial \| evasion) + (survey \| review \| systematic …) | 2020–2026 | 401 | 401 |
| S2-amend1 | Semantic Scholar: title + abstract | (intrusion detection \| botnet detection/detector* \| network traffic classif* \| flow-based detect* \| anomaly detection system*) + (adversarial \| evasion \| evasion attack*) + (network \| traffic \| flow*) | 2020–2026 | 2,373 | 2,373 |
| CR ×8 | Crossref `query.bibliographic` (metadata fields; **not** abstracts or full text) | 8 strings (see log) | from 2020-01-01; type = journal-article | 0.5–3.6 M (relevance-ranked) | 200 each (199 for one) = 1,599 |

**Not searched** (inaccessible from this environment): Scopus, Web of Science, IEEE Xplore, ACM DL, ScienceDirect, SpringerLink, Wiley. Ready-to-run adaptations are in §5. Crossref metadata lookup is **not** equivalent to searching publisher full-text databases.

### 3.2 Seed coverage test and amendment
Fourteen seed titles were identified independently (from domain knowledge) and verified in Crossref; 12 resolved to the intended journal article (`data/seed_coverage_test.csv`).
- The initial S2 queries (focused, broad, reviews) found **9/12**. Missed: Alhajjar et al., *ESWA* 2021; Apruzzese et al., *IEEE TNSM* 2020 ("botnet detection" wording); Chen et al., *Digital Communications and Networks* 2021.
- **Amendment 1** (documented): the S2-amend1 query (broader detector vocabulary) plus the Crossref searches. After the amendment, **12/12** seeds were found.

### 3.3 Records, deduplication and pre-screening (actual counts)
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

### 3.4 Manual title/abstract screening (partial)
Of the 796 records, **129** state a black-box, query, surrogate/substitute, transfer or gray-box element in the title or abstract. **All 129 were screened manually** (`data/screening_log_blackbox_subset.csv`):
- **56** included for full-text assessment;
- **3** routed to the review register;
- **70** excluded (conference proceedings that Semantic Scholar mislabels as journals; off-topic; poisoning; host-only; non-NIDS).

The remaining **667** records were **not yet screened manually**. They may contain black-box experiments not mentioned in the abstract (OA-4).

In addition, **7 seed articles** were added to the candidate register directly (one may be white-box only). **Candidate register: 63 records** (`data/candidate_register.csv`), all with Crossref-verified metadata and none with verified quartile or full text. The reviewer expects 11 of them to fall below Q2 or be unranked, but this is **not verified**, and they remain in the register.

### 3.5 Database-specific strings for the outstanding searches (not executed)
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

### 3.6 PRISMA 2020 flow: status of each box
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

---

## 4. Outstanding-Actions Register

| ID | Action | Why it blocks completion | Who / what is needed | Status |
|---|---|---|---|---|
| OA-1 | Retrieve and read full texts of the closest reviews: RV1 (10.1109/ACCESS.2026.3720554), RV2 (10.1109/ACCESS.2026.3733985), RV3 (10.1016/j.cosrev.2026.100995), RV4 (10.1109/COMST.2022.3233793) | Novelty cannot be judged from abstracts; RV1/RV2 overlap substantially | PDFs supplied by the user (RV1 and RV2 are open access) | Pending external access |
| OA-2 | Verify the SJR quartile of every candidate journal under the predefined categories (record year, category, quartile, URL, date) | No study can enter the synthesis without it | A human checking scimagojr.com, or an exported SJR CSV supplied to the session | Pending human verification |
| OA-3 | Re-screen the 995 records excluded by rule on title only (no abstract) | Violates the no-title-only-filter rule | Abstracts (Scopus/WoS export) or manual screening | Pending |
| OA-4 | Manually screen the remaining 667 records (no black-box term in title/abstract) | May contain separable black-box experiments | Reviewer time; full text for ambiguous cases | Pending |
| OA-5 | Run the Scopus, Web of Science and IEEE Xplore searches (strings in report §5) and record yields | Required discovery sources not searched | Institutional database access | Pending external access |
| OA-6 | Forward/backward citation searching from included studies | Not done | After OA-7 | Pending |
| OA-7 | Retrieve full texts of the eligible candidates; full-text eligibility; extraction with page-level evidence; appraisal | Brief forbids abstract-only coding | PDFs (open-access ones from the user, paywalled ones via institutional access) | Pending external access |
| OA-8 | Second reviewer on a sample, with κ | Single AI-assisted reviewer so far | A human reviewer | Pending human verification |
| OA-9 | Save the inline screening scripts as files; prepare a PRISMA checklist | Reproducibility | Me (next session) | Pending |
| OA-10 | Decide on scope (focused SLR vs mapping review; in-vehicle CAN inclusion) after OA-1 and OA-2 | Corpus may fall below about 25 studies | The user | Pending decision |

---

## Appendix A. Search log (all executed searches)

| Tag | Source | Exact query | Executed (UTC) | Date filter | Doc-type filter | Returned | Exported | Cap |
|---|---|---|---|---|---|---|---|---|
| S2-focused | Semantic Scholar Graph API /paper/search/bulk (fields searched: title+abstract) | `("intrusion detection" \| NIDS \| "network intrusion") + (adversarial \| evasion) + ("black box" \| "black-box" \| blackbox \| "query based" \| "query-based" \| "decision based" \| "decision-based" \| "score based" \| "score-based" \| transferab* \| "surrogate model*" \| "substitute model*")` | 2026-11-16T12:56:22 | year=2020-2026 | none at query time (applied in screening) | 154 | 154 | none (paged to completion) |
| S2-broad | Semantic Scholar Graph API /paper/search/bulk (fields searched: title+abstract) | `("network intrusion detection" \| NIDS) + (adversarial \| evasion) + ("machine learning" \| "deep learning")` | 2026-11-16T12:56:37 | year=2020-2026 | none at query time (applied in screening) | 443 | 443 | none (paged to completion) |
| S2-reviews | Semantic Scholar Graph API /paper/search/bulk (fields searched: title+abstract) | `("intrusion detection" \| NIDS) + (adversarial \| evasion) + (survey \| review \| "systematic literature review" \| "systematic review")` | 2026-11-16T12:56:51 | year=2020-2026 | none at query time (applied in screening) | 401 | 401 | none (paged to completion) |
| S2-amend1 | Semantic Scholar Graph API /paper/search/bulk (fields searched: title+abstract) | `("intrusion detection" \| "botnet detection" \| "botnet detector*" \| "network traffic classif*" \| "flow-based detect*" \| "anomaly detection system*") + (adversarial \| evasion \| "evasion attack*") + (network \| traffic \| flow*)` | 2026-11-16T12:59:38 | year=2020-2026 | none at query time (applied in screening) | 2373 | 2373 | none (paged to completion) |
| CR | Crossref REST API /works (query.bibliographic; metadata fields, not abstracts/full text) | `black-box adversarial attack network intrusion detection` | 2026-11-16T12:59:51 | from-pub-date:2020-01-01 | type:journal-article | 1124167 | 200 | first 200 by relevance |
| CR | Crossref REST API /works (query.bibliographic; metadata fields, not abstracts/full text) | `evasion attack network intrusion detection machine learning` | 2026-11-16T13:00:05 | from-pub-date:2020-01-01 | type:journal-article | 2030148 | 199 | first 200 by relevance |
| CR | Crossref REST API /works (query.bibliographic; metadata fields, not abstracts/full text) | `adversarial examples intrusion detection deep learning` | 2026-11-16T13:00:25 | from-pub-date:2020-01-01 | type:journal-article | 1696271 | 200 | first 200 by relevance |
| CR | Crossref REST API /works (query.bibliographic; metadata fields, not abstracts/full text) | `transferability adversarial network intrusion detection` | 2026-11-16T13:00:35 | from-pub-date:2020-01-01 | type:journal-article | 950014 | 200 | first 200 by relevance |
| CR | Crossref REST API /works (query.bibliographic; metadata fields, not abstracts/full text) | `adversarial botnet detection evasion` | 2026-11-16T13:00:51 | from-pub-date:2020-01-01 | type:journal-article | 526556 | 200 | first 200 by relevance |
| CR | Crossref REST API /works (query.bibliographic; metadata fields, not abstracts/full text) | `adversarial traffic generation intrusion detection GAN evasion` | 2026-11-16T13:01:05 | from-pub-date:2020-01-01 | type:journal-article | 837656 | 200 | first 200 by relevance |
| CR | Crossref REST API /works (query.bibliographic; metadata fields, not abstracts/full text) | `defense adversarial attacks network intrusion detection` | 2026-11-16T13:01:23 | from-pub-date:2020-01-01 | type:journal-article | 998296 | 200 | first 200 by relevance |
| CR | Crossref REST API /works (query.bibliographic; metadata fields, not abstracts/full text) | `query-based attack intrusion detection system` | 2026-11-16T13:01:38 | from-pub-date:2020-01-01 | type:journal-article | 3585059 | 200 | first 200 by relevance |

## Appendix B. Seed coverage test

| Seed title | DOI | Venue | Verified journal seed | Found by initial queries | Found after amendment |
|---|---|---|---|---|---|
| Adversarial Attacks Against Deep Learning-Based Network Intrusion Detection Systems and Defense Mechanisms | 10.1109/tnet.2021.3137084 | IEEE/ACM Transactions on Networking | yes | True | True |
| Evaluating and Improving Adversarial Robustness of Machine Learning-Based Network Intrusion Detectors | 10.1109/jsac.2021.3087242 | IEEE Journal on Selected Areas in Communications | yes | True | True |
| Adversarial machine learning in Network Intrusion Detection Systems | 10.1016/j.eswa.2021.115782 | Expert Systems with Applications | yes | False | True |
| Adv-Bot: Realistic adversarial botnet attacks against network intrusion detection systems | 10.1016/j.cose.2023.103176 | Computers & Security | yes | True | True |
| TAD: Transfer learning-based multi-adversarial detection of evasion attacks against network intrusion detection systems | 10.1016/j.future.2022.08.011 | Future Generation Computer Systems | yes | True | True |
| Deep Reinforcement Adversarial Learning Against Botnet Evasion Attacks | 10.1109/tnsm.2020.3031843 | IEEE Transactions on Network and Service Management | yes | False | True |
| Adversarial Attacks Against Network Intrusion Detection in IoT Systems | 10.1109/aiiot52608.2021.9454214 | 2021 IEEE World AI IoT Congress (AIIoT) | no (Crossref returned a different record) | True | True |
| TANTRA: Timing-Based Adversarial Network Traffic Reshaping Attack | 10.1109/tifs.2022.3201377 | IEEE Transactions on Information Forensics and Security | yes | True | True |
| DIGFuPAS: Deceive IDS with GAN and function-preserving on adversarial samples in SDN-enabled networks | 10.1016/j.cose.2021.102367 | Computers & Security | yes | True | True |
| Fooling intrusion detection systems using adversarially autoencoder | 10.1016/j.dcan.2020.11.001 | Digital Communications and Networks | yes | False | True |
| Defending network intrusion detection systems against adversarial evasion attacks | 10.1016/j.future.2020.04.013 | Future Generation Computer Systems | yes | True | True |
| Modeling Realistic Adversarial Attacks against Network Intrusion Detection Systems | 10.1145/3469659 | Digital Threats: Research and Practice | yes | True | True |
| Adversarial examples for network intrusion detection systems | 10.2139/ssrn.7042179 |  | no (Crossref returned a different record) | False | False |
| A gradient-based approach for adversarial attack on deep learning-based network intrusion detection systems | 10.1016/j.asoc.2023.110173 | Applied Soft Computing | yes | True | True |

## Appendix C. Candidate register (63 records)

All metadata verified in Crossref on 16 Nov 2026. **For every record: journal eligibility (SJR quartile) = pending; full text retrieved = no; full text extracted = no; extraction independently checked = no.** Quartile expectations are the reviewer's unverified judgement and do not exclude any record.

| ID | Title | Journal | Online date | Vol/Issue/Pages | DOI | Source | T/A note | Quartile expectation |
|---|---|---|---|---|---|---|---|---|
| C01 | A Brute-Force Black-Box Method to Attack Machine Learning-Based Systems in Cybersecurity | IEEE Access | 2020 | 8/128250-128263 | [10.1109/access.2020.3008433](https://doi.org/10.1109/access.2020.3008433) | search (black-box-hint subset) | Black-box brute-force attack on ML security systems; confirm NIDS target | unverified |
| C02 | Evaluating and Improving Adversarial Robustness of Machine Learning-Based Network Intrusion Detectors | IEEE Journal on Selected Areas in Communications | 2021-8 | 39/8/2632-2647 | [10.1109/jsac.2021.3087242](https://doi.org/10.1109/jsac.2021.3087242) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C03 | Adversarial Attacks Against Network Intrusion Detection in IoT Systems | IEEE Internet of Things Journal | 2021-7-1 | 8/13/10327-10335 | [10.1109/jiot.2020.3048038](https://doi.org/10.1109/jiot.2020.3048038) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C04 | Adversarial Attacks Against Deep Learning-Based Network Intrusion Detection Systems and Defense Mechanisms | IEEE/ACM Transactions on Networking | 2022-6 | 30/3/1294-1311 | [10.1109/tnet.2021.3137084](https://doi.org/10.1109/tnet.2021.3137084) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C05 | Generate qualified adversarial attacks and foster enhanced models based on generative adversarial networks | Intelligent Data Analysis | 2022-9-5 | 26/5/1359-1377 | [10.3233/ida-216134](https://doi.org/10.3233/ida-216134) | search (black-box-hint subset) | GAN attack generation for IDS; confirm black-box | unverified |
| C06 | Hierarchical Adversarial Attacks Against Graph-Neural-Network-Based IoT Network Intrusion Detection System | IEEE Internet of Things Journal | 2022-6-15 | 9/12/9310-9319 | [10.1109/jiot.2021.3130434](https://doi.org/10.1109/jiot.2021.3130434) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C07 | Mitigation of Black-Box Attacks on Intrusion Detection Systems-Based ML | Computers | 2022-7-20 | 11/7/115 | [10.3390/computers11070115](https://doi.org/10.3390/computers11070115) | search (black-box-hint subset) | Defence (GAN adv. training) vs black-box attack | unverified |
| C08 | Statistical Detection of Adversarial Examples in Blockchain-Based Federated Forest In-Vehicle Network Intrusion Detection Systems | IEEE Access | 2022 | 10/109366-109384 | [10.1109/access.2022.3212412](https://doi.org/10.1109/access.2022.3212412) | search (black-box-hint subset) | In-vehicle CAN IDS; transferability (scope: in-vehicle network) | unverified |
| C09 | TAD: Transfer learning-based multi-adversarial detection of evasion attacks against network intrusion detection systems | Future Generation Computer Systems | 2023-1 | 138/185-197 | [10.1016/j.future.2022.08.011](https://doi.org/10.1016/j.future.2022.08.011) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C10 | A simple framework to enhance the adversarial robustness of deep learning-based intrusion detection system | Computers & Security | 2024-2 | 137/103644 | [10.1016/j.cose.2023.103644](https://doi.org/10.1016/j.cose.2023.103644) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C11 | Adv-Bot: Realistic adversarial botnet attacks against network intrusion detection systems | Computers & Security | 2023-6 | 129/103176 | [10.1016/j.cose.2023.103176](https://doi.org/10.1016/j.cose.2023.103176) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C12 | Constrained optimization based adversarial example generation for transfer attacks in network intrusion detection systems | Optimization Letters | 2023-5-23 | 18/9/2169-2188 | [10.1007/s11590-023-02007-7](https://doi.org/10.1007/s11590-023-02007-7) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C13 | EIFDAA: Evaluation of an IDS with function-discarding adversarial attacks in the IIoT | Heliyon | 2023-2 | 9/2/e13520 | [10.1016/j.heliyon.2023.e13520](https://doi.org/10.1016/j.heliyon.2023.e13520) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C14 | SGAN-IDS: Self-Attention-Based Generative Adversarial Network against Intrusion Detection Systems | Sensors | 2023-9-11 | 23/18/7796 | [10.3390/s23187796](https://doi.org/10.3390/s23187796) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C15 | A Systematic Study of Adversarial Attacks Against Network Intrusion Detection Systems | Electronics | 2024-12-21 | 13/24/5030 | [10.3390/electronics13245030](https://doi.org/10.3390/electronics13245030) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C16 | Adversarial Attacks on Intrusion Detection Systems in In-Vehicle Networks of Connected and Autonomous Vehicles | Sensors | 2024-6-14 | 24/12/3848 | [10.3390/s24123848](https://doi.org/10.3390/s24123848) | search (black-box-hint subset) | In-vehicle IDS; substitute model from OBD data | unverified |
| C17 | Automatic Evasion of Machine Learning-Based Network Intrusion Detection Systems | IEEE Transactions on Dependable and Secure Computing | 2024-1 | 21/1/153-167 | [10.1109/tdsc.2023.3247585](https://doi.org/10.1109/tdsc.2023.3247585) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C18 | Comprehensive Botnet Detection by Mitigating Adversarial Attacks, Navigating the Subtleties of Perturbation Distances and Fortifying Predictions with Conformal Layers | Information Fusion | 2024-11 | 111/102529 | [10.1016/j.inffus.2024.102529](https://doi.org/10.1016/j.inffus.2024.102529) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C19 | Constraining Adversarial Attacks on Network Intrusion Detection Systems: Transferability and Defense Analysis | IEEE Transactions on Network and Service Management | 2024-6 | 21/3/2751-2772 | [10.1109/tnsm.2024.3357316](https://doi.org/10.1109/tnsm.2024.3357316) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C20 | Explainable and Transferable Adversarial Attack for ML-Based Network Intrusion Detectors | IEEE Transactions on Dependable and Secure Computing | 2025-9 | 22/5/5090-5107 | [10.1109/tdsc.2025.3560486](https://doi.org/10.1109/tdsc.2025.3560486) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C21 | RobEns: Robust Ensemble Adversarial Machine Learning Framework for Securing IoT Traffic | Sensors | 2024-4-19 | 24/8/2626 | [10.3390/s24082626](https://doi.org/10.3390/s24082626) | search (black-box-hint subset) | Defence ensemble; confirm black-box evaluation | unverified |
| C22 | Toward Transferable Adversarial Attacks Against Autoencoder-Based Network Intrusion Detectors | IEEE Transactions on Industrial Informatics | 2024-12 | 20/12/13863-13872 | [10.1109/tii.2024.3435532](https://doi.org/10.1109/tii.2024.3435532) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C23 | Adversarial Attack Detection in Industrial Control Systems Using LSTM-Based Intrusion Detection and Black-Box Defense Strategies | Journal of Cyber Security and Risk Auditing | 2025-5-5 | 2025/3/4-22 | [10.63180/jcsra.thestap.2025.3.2](https://doi.org/10.63180/jcsra.thestap.2025.3.2) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | reviewer expects below Q2 or unranked - NOT verified |
| C24 | Adversarial Robustness of Network IDS (Structured Data) | Journal of Al-Qadisiyah for Computer Science and Mathematics | 2025-12-30 | 17/4 | [10.29304/jqcsm.2025.17.42554](https://doi.org/10.29304/jqcsm.2025.17.42554) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | reviewer expects below Q2 or unranked - NOT verified |
| C25 | Adversarial Threats to Cloud IDS: Robust Defense With Adversarial Training and Feature Selection | IEEE Access | 2025 | 13/84992-85003 | [10.1109/access.2025.3567038](https://doi.org/10.1109/access.2025.3567038) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C26 | Adversarial attack and defense in AI-powered intrusion detection | Journal of Computer Science and Cybernetics | 2025-11-11 | 41/4/387-402 | [10.15625/1813-9663/22884](https://doi.org/10.15625/1813-9663/22884) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | reviewer expects below Q2 or unranked - NOT verified |
| C27 | Assessing the Resilience of Automotive Intrusion Detection Systems to Adversarial Manipulation | ACM Transactions on Cyber-Physical Systems | 2025-8-4 | 9/3/1-27 | [10.1145/3737294](https://doi.org/10.1145/3737294) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C28 | Breaking and Healing: GAN-Based Adversarial Attacks and Post-Adversarial Recovery for 5G IDSs | IEEE Access | 2025 | 13/132109-132125 | [10.1109/access.2025.3587605](https://doi.org/10.1109/access.2025.3587605) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C29 | CARD: Robustness-Preserving Transfer Learning for Network Intrusion Detection via Contrastive Adversarial Representation Distillation | IEEE Transactions on Dependable and Secure Computing | 2025-9 | 22/5/5134-5151 | [10.1109/tdsc.2025.3562600](https://doi.org/10.1109/tdsc.2025.3562600) | search (black-box-hint subset) | Transfer-learning defence; confirm evasion attack is black-box | unverified |
| C30 | Exploring transferable adversarial attacks for Deep Learning-based Network Intrusion Detection | Journal of Network and Computer Applications | 2025-10 | 242/104255 | [10.1016/j.jnca.2025.104255](https://doi.org/10.1016/j.jnca.2025.104255) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C31 | NonsaliencyCrossover: A Novel Adversarial Example Generation Strategy for IDS Using Explainable AI | IEEE Internet of Things Journal | 2025-9-15 | 12/18/38680-38696 | [10.1109/jiot.2025.3586721](https://doi.org/10.1109/jiot.2025.3586721) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C32 | Securing Data Privacy in NIDS: Black‐Box Adversarial Attacks | International Journal of Intelligent Systems | 2025-10-31 | 2025/1/1500333 | [10.1155/int/1500333](https://doi.org/10.1155/int/1500333) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | reviewer expects below Q2 or unranked - NOT verified |
| C33 | Vulnerability disclosure through adaptive black-box adversarial attacks in network intrusion detection systems | Complex & Intelligent Systems | 2025-11-25 | 12/1/18 | [10.1007/s40747-025-02115-0](https://doi.org/10.1007/s40747-025-02115-0) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C34 | Xai-driven black-box adversarial attacks on network intrusion detectors | International Journal of Information Security | 2025-3-26 | 24/3/103 | [10.1007/s10207-025-01016-0](https://doi.org/10.1007/s10207-025-01016-0) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C35 | Adversarial Attack on CAN IDS Leveraging Multi-DDQN Agent | IEEE Access | 2026 | 14/13445-13462 | [10.1109/access.2025.3649307](https://doi.org/10.1109/access.2025.3649307) | search (black-box-hint subset) | In-vehicle CAN IDS; DDQN agent | unverified |
| C36 | Adversarial Transferability in AI-based Network Intrusion Detection: A Comparative Study of ANN and CNN Models | International Journal of Information Technology and Computer Science | 2026-8-8 | 18/4/170-198 | [10.5815/ijitcs.2026.04.11](https://doi.org/10.5815/ijitcs.2026.04.11) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | reviewer expects below Q2 or unranked - NOT verified |
| C37 | Adversarial manipulation of CAN bus IDS | Discover Artificial Intelligence | 2026-4-13 | 6/1/545 | [10.1007/s44163-026-00951-8](https://doi.org/10.1007/s44163-026-00951-8) | search (black-box-hint subset) | In-vehicle CAN IDS | reviewer expects below Q2 or unranked - NOT verified |
| C38 | Adversarial resilience in cloud based machine learning: a unified framework for robust threat detection and forecasting | Journal of Cloud Computing | 2026-8-4 | 15/1/146 | [10.1186/s13677-026-00962-x](https://doi.org/10.1186/s13677-026-00962-x) | search (black-box-hint subset) | Cloud ML adversarial resilience; confirm NIDS + black-box | unverified |
| C39 | COMPARATIVE ANALYSIS OF BLACK-BOX TARGETED ADVERSARIAL ATTACKS ON DL-BASED NIDS: A STUDY OF C&W AND JSMA USING CICDDOS2019 | International journal of Computer Networks & Communications | 2026-1-28 | 18/1/109-128 | [10.5121/ijcnc.2026.18107](https://doi.org/10.5121/ijcnc.2026.18107) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | reviewer expects below Q2 or unranked - NOT verified |
| C40 | DEFENSIVE DISTILLATION AND GENERATIVE ADVERSARIAL NETWORKS (GANS) MITIGATING BLACK-BOX EVASION ATTACKS ON CLOUD-BASED INTRUSION DETECTION SYSTEMS | INTERNATIONAL RESEARCH JOURNAL OF MODERNIZATION IN ENGINEERING TECHNOLOGY AND SCIENCE | 2026-10-26 | — | [10.56726/irjmets103202](https://doi.org/10.56726/irjmets103202) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | reviewer expects below Q2 or unranked - NOT verified |
| C41 | Enhancing adversarial robustness of network intrusion detection systems against gray-box attacks | Computer Networks | 2026-12 | 291/112856 | [10.1016/j.comnet.2026.112856](https://doi.org/10.1016/j.comnet.2026.112856) | search (black-box-hint subset) | Gray-box attacks; confirm separable black-box results | unverified |
| C42 | Evaluating the Robustness and Transferable Adversarial Example Resistance of Multimodal Learning-based Intrusion Detection Systems against Evasion Attacks | Mobile Networks and Applications | 2026-8-30 | 31/3-4/287-305 | [10.1007/s11036-026-02522-8](https://doi.org/10.1007/s11036-026-02522-8) | search (black-box-hint subset) | Transferable AEs vs multimodal IDS; confirm network IDS | unverified |
| C43 | Explainable Robust Cloud Intrusion Detection Against Adversarial Evasion Using SHAP-Guided Feature Reweighting | Computer Life | 2026-7-20 | 14/3/1-6 | [10.54097/cttx6294](https://doi.org/10.54097/cttx6294) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | reviewer expects below Q2 or unranked - NOT verified |
| C44 | Feature-Space Adversarial Robustness Evaluation of Lightweight ML-Based Intrusion Detection for IoT and Healthcare-Sensing Networks | IEEE Access | 2026 | 14/141428-141454 | [10.1109/access.2026.3732098](https://doi.org/10.1109/access.2026.3732098) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C45 | FlowUAP: Evading Network Intrusion Detection Systems With Type-Specific Universal Adversarial Perturbations | IEEE Transactions on Information Forensics and Security | 2026 | 21/9048-9063 | [10.1109/tifs.2026.3737644](https://doi.org/10.1109/tifs.2026.3737644) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C46 | Game-Theoretic Cost-Sensitive Adversarial Training for Robust Cloud Intrusion Detection Against GAN-Based Evasion Attacks | Applied Sciences | 2026-4-18 | 16/8/3944 | [10.3390/app16083944](https://doi.org/10.3390/app16083944) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C47 | LLM-Orchestrated Evasion of Tabular NIDS and GAN Augmentation for Multimodal Detection | Applied Sciences | 2026-10-14 | 16/20/10178 | [10.3390/app162010178](https://doi.org/10.3390/app162010178) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C48 | <i>Liuer Mihou</i>                     : A Practical Gray-Box Adversarial Attack Against Anomaly-Based Network Intrusion Detection Systems | IEEE Transactions on Network and Service Management | 2026 | 23/8500-8514 | [10.1109/tnsm.2026.3742885](https://doi.org/10.1109/tnsm.2026.3742885) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C49 | Making the Best of Both Worlds: Universal Perturbations for Live Black-Box Evasion Against NIDS in Encrypted Traffic | IEEE Transactions on Networking | 2026 | 34/6013-6028 | [10.1109/ton.2026.3710207](https://doi.org/10.1109/ton.2026.3710207) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C50 | RandomForestNN Classification for Adversarial AI Black-Box Techniques on MITRE ATT&CK Labeled Data | Electronics | 2026-6-12 | 15/12/2598 | [10.3390/electronics15122598](https://doi.org/10.3390/electronics15122598) | search (black-box-hint subset) | Black-box techniques on MITRE ATT&CK-labelled data; confirm NIDS | unverified |
| C51 | Revisiting adversarial robustness in NIDS: a multi-dataset evaluation of test-time evasion attacks | International Journal of Information Security | 2026-11-5 | 25/6/184 | [10.1007/s10207-026-01353-8](https://doi.org/10.1007/s10207-026-01353-8) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C52 | Robust AI-Driven Intrusion Detection and Defense for Next-Generation Consumer Services | IEEE Transactions on Consumer Electronics | 2026-2 | 72/1/1544-1553 | [10.1109/tce.2025.3631965](https://doi.org/10.1109/tce.2025.3631965) | search (black-box-hint subset) | No abstract; confirm scope | unverified |
| C53 | Security and Resilience of AI-Enabled Edge Computing in Industrial IoT: Vulnerabilities, Defense Strategies, and Future Directions | Mesopotamian Journal of CyberSecurity | 2026-10-13 | 6/1/28-49 | [10.68212/2958-6542.1132](https://doi.org/10.68212/2958-6542.1132) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | reviewer expects below Q2 or unranked - NOT verified |
| C54 | Slice-Aware Adversarial Vulnerability Analysis of TabNet-Based Intrusion Detection in 5G Network Slicing | Symmetry | 2026-10-13 | 18/10/1700 | [10.3390/sym18101700](https://doi.org/10.3390/sym18101700) | search (black-box-hint subset) | TabNet 5G slices; confirm black-box | unverified |
| C55 | Targeted adversarial traffic generation: black-box approach to evade intrusion detection systems in IoT networks | International Journal of Machine Learning and Cybernetics | 2026-2-2 | 17/2/58 | [10.1007/s13042-025-02873-w](https://doi.org/10.1007/s13042-025-02873-w) | search (black-box-hint subset) | NIDS evasion with black-box/transfer/query component stated in abstract | unverified |
| C56 | Uncertainty-Aware Evidential Adversarial Defense for Cloud Intrusion Detection under GAN-Based Evasion Attacks | International Journal of Advanced Engineering and Technology Research | 2026-7-20 | 2/3/42-48 | [10.54097/6bm9sm08](https://doi.org/10.54097/6bm9sm08) | search (black-box-hint subset) | GAN-based black-box transfer attack in evaluation of defence | reviewer expects below Q2 or unranked - NOT verified |
| C57 | Adversarial machine learning in Network Intrusion Detection Systems | Expert Systems with Applications | 2021 | — | [10.1016/j.eswa.2021.115782](https://doi.org/10.1016/j.eswa.2021.115782) | seed (independently identified) | Evasion of NIDS (GAN/PSO/GA); confirm black-box | unverified |
| C58 | Deep Reinforcement Adversarial Learning Against Botnet Evasion Attacks | IEEE Transactions on Network and Service Management | 2020 | — | [10.1109/tnsm.2020.3031843](https://doi.org/10.1109/tnsm.2020.3031843) | seed (independently identified) | Botnet-detector evasion via deep RL (query-based feedback likely) | unverified |
| C59 | TANTRA: Timing-Based Adversarial Network Traffic Reshaping Attack | IEEE Transactions on Information Forensics and Security | 2022 | — | [10.1109/tifs.2022.3201377](https://doi.org/10.1109/tifs.2022.3201377) | seed (independently identified) | Timing-based traffic reshaping; confirm attacker knowledge | unverified |
| C60 | DIGFuPAS: Deceive IDS with GAN and function-preserving on adversarial samples in SDN-enabled networks | Computers & Security | 2021 | — | [10.1016/j.cose.2021.102367](https://doi.org/10.1016/j.cose.2021.102367) | seed (independently identified) | GAN, function-preserving, SDN; black-box per title context | unverified |
| C61 | Fooling intrusion detection systems using adversarially autoencoder | Digital Communications and Networks | 2021 | — | [10.1016/j.dcan.2020.11.001](https://doi.org/10.1016/j.dcan.2020.11.001) | seed (independently identified) | Adversarial autoencoder evasion; knowledge assumptions to verify | unverified |
| C62 | Defending network intrusion detection systems against adversarial evasion attacks | Future Generation Computer Systems | 2020 | — | [10.1016/j.future.2020.04.013](https://doi.org/10.1016/j.future.2020.04.013) | seed (independently identified) | Defence against evasion; confirm black-box attacks evaluated | unverified |
| C63 | A gradient-based approach for adversarial attack on deep learning-based network intrusion detection systems | Applied Soft Computing | 2023 | — | [10.1016/j.asoc.2023.110173](https://doi.org/10.1016/j.asoc.2023.110173) | seed (independently identified) | Gradient-based attack - may be white-box only | unverified |

## Appendix D. Title/abstract screening log (black-box-hint subset, 129 records)

| # | Year | Title | Venue (Semantic Scholar) | Decision | Reason |
|---|---|---|---|---|---|
| 0 | 2020 | A Brute-Force Black-Box Method to Attack Machine Learning-Based Systems in Cybersecurity | IEEE Access | include for full text | — |
| 1 | 2020 | An Adversarial Attack Detection Paradigm With Swarm Optimization | 2020 International Joint Conference on Neural Networks (IJCNN) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 2 | 2020 | Avoiding Network and Host Detection using Packet Bit-masking | International Conference on E-Business and Telecommunication Networks | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 3 | 2020 | ECEM - Generating Adversarial Logs under Black-box Setting in Web Security | GLOBECOM 2020 - 2020 IEEE Global Communications Conference | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 4 | 2020 | Evading a Machine Learning-based Intrusion Detection System through Adversarial Perturbations | Proceedings of the International Conference on Research in Adaptive and Convergent Systems | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 5 | 2020 | Evaluating and Improving Adversarial Robustness of Machine Learning-Based Network Intrusion Detectors | IEEE Journal on Selected Areas in Communications | include for full text | — |
| 6 | 2020 | Tiki-Taka: Attacking and Defending Deep Learning-based Intrusion Detection Systems | Proceedings of the 2020 ACM SIGSAC Conference on Cloud Computing Security Workshop | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 7 | 2021 | Adversarial Attacks Against Network Intrusion Detection in IoT Systems | IEEE Internet of Things Journal | include for full text | — |
| 8 | 2021 | Adversarial Black-Box Attacks Against Network Intrusion Detection Systems: A Survey | 2021 IEEE World AI IoT Congress (AIIoT) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 9 | 2021 | Adversarial Machine Learning and Cognitive AI for Autonomous Defense against Advanced Cyber Threats | International Journal of Computer Technology and Electronics Communication | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 10 | 2021 | Crafting Adversarial Example to Bypass Flow-&ML- based Botnet Detector via RL | Proceedings of the 24th International Symposium on Research in Attacks, Intrusions and Defenses | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 11 | 2021 | Detect & Reject for Transferability of Black-box Adversarial Attacks Against Network Intrusion Detection Systems | International Conference on Advances in Cybersecurity | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 12 | 2022 | Adversarial Attacks Against Deep Learning-Based Network Intrusion Detection Systems and Defense Mechanisms | IEEE/ACM Transactions on Networking | include for full text | — |
| 13 | 2022 | Dual Generative Adversarial Networks Based Unknown Encryption Ransomware Attack Detection | IEEE Access | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 14 | 2022 | Functionality-Preserving Adversarial Machine Learning for Robust Classification in Cybersecurity and Intrusion Detection Domains: A Survey | J. Cybersecur. Priv. | route to review register | secondary study |
| 15 | 2022 | Generate qualified adversarial attacks and foster enhanced models based on generative adversarial networks | Intelligent Data Analysis | include for full text | — |
| 16 | 2022 | Hierarchical Adversarial Attacks Against Graph-Neural-Network-Based IoT Network Intrusion Detection System | IEEE Internet of Things Journal | include for full text | — |
| 17 | 2022 | Mitigation of Black-Box Attacks on Intrusion Detection Systems-Based ML | Comput. | include for full text | — |
| 18 | 2022 | Statistical Detection of Adversarial Examples in Blockchain-Based Federated Forest In-Vehicle Network Intrusion Detection Systems | IEEE Access | include for full text | — |
| 19 | 2022 | TAD: Transfer Learning-based Multi-Adversarial Detection of Evasion Attacks against Network Intrusion Detection Systems | Future Gener. Comput. Syst. | include for full text | — |
| 20 | 2023 | A Deep Learning Based Semi-Supervised Network Intrusion Detection System Robust to Adversarial Attacks | Proceedings of the 10th International Conference on Networking, Systems and Security | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 21 | 2023 | A Simple Framework to Enhance the Adversarial Robustness of Deep Learning-based Intrusion Detection System | Comput. Secur. | include for full text | — |
| 22 | 2023 | Adv-Bot: Realistic Adversarial Botnet Attacks against Network Intrusion Detection Systems | Comput. Secur. | include for full text | — |
| 23 | 2023 | Adversarial Machine Learning for Network Intrusion Detection Systems: A Comprehensive Survey | IEEE Communications Surveys & Tutorials | route to review register | secondary study |
| 24 | 2023 | An Ensemble Learning to Detect Decision-Based Adversarial Attacks in Industrial Control Systems | 2023 IEEE Symposium Series on Computational Intelligence (SSCI) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 25 | 2023 | Constrained optimization based adversarial example generation for transfer attacks in network intrusion detection systems | Optimization Letters | include for full text | — |
| 26 | 2023 | EIFDAA: Evaluation of an IDS with function-discarding adversarial attacks in the IIoT | Heliyon | include for full text | — |
| 27 | 2023 | On the Resilience of Machine Learning-Based IDS for Automotive Networks | 2023 IEEE Vehicular Networking Conference (VNC) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 28 | 2023 | Resilient Machine Learning (rML) Against Adversarial Attacks on Industrial Control Systems | 2023 20th ACS/IEEE International Conference on Computer Systems and Applications (AICCSA) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 29 | 2023 | SGAN-IDS: Self-Attention-Based Generative Adversarial Network against Intrusion Detection Systems | Sensors (Basel, Switzerland) | include for full text | — |
| 30 | 2023 | The Efficacy of Transformer-based Adversarial Attacks in Security Domains | MILCOM 2023 - 2023 IEEE Military Communications Conference (MILCOM) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 31 | 2024 | A Hierarchical Deep Learning Architecture for Robust Intrusion Detection in Time-Evolving Security Landscapes | International Journal for Research in Applied Science and Engineering Technology | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 32 | 2024 | A Systematic Study of Adversarial Attacks Against Network Intrusion Detection Systems | Electronics | include for full text | — |
| 33 | 2024 | ADVANCED MACHINE LEARNING TECHNIQUES FOR CYBERSECURITY: OPPORTUNITIES AND EMERGING CHALLENGES | International journal of science and engineering | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 34 | 2024 | Adversarial Attacks on Intrusion Detection Systems in In-Vehicle Networks of Connected and Autonomous Vehicles | Sensors (Basel, Switzerland) | include for full text | — |
| 35 | 2024 | Adversarial Dynamic Load-Altering Cyberattacks Against Peak Shaving Using Residential Electric Water Heaters | IEEE Transactions on Smart Grid | exclude | EC: not NIDS (smart-grid load attacks) |
| 36 | 2024 | Automatic Evasion of Machine Learning-Based Network Intrusion Detection Systems | IEEE Transactions on Dependable and Secure Computing | include for full text | — |
| 37 | 2024 | CANEDERLI: On The Impact of Adversarial Training and Transferability on CAN Intrusion Detection Systems | Proceedings of the 2024 ACM Workshop on Wireless Security and Machine Learning | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 38 | 2024 | Comprehensive Botnet Detection by Mitigating Adversarial Attacks, Navigating the Subtleties of Perturbation Distances and Fortifying Predictions with Conformal Layers | Inf. Fusion | include for full text | — |
| 39 | 2024 | Constraining Adversarial Attacks on Network Intrusion Detection Systems: Transferability and Defense Analysis | IEEE Transactions on Network and Service Management | include for full text | — |
| 40 | 2024 | Evading Botnet Detection | Proceedings of the 39th ACM/SIGAPP Symposium on Applied Computing | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 41 | 2024 | Evading IoT Intrusion Detection Systems with GAN | 2024 19th Asia Joint Conference on Information Security (AsiaJCIS) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 42 | 2024 | Explainable and Transferable Adversarial Attack for ML-Based Network Intrusion Detectors | IEEE Transactions on Dependable and Secure Computing | include for full text | — |
| 43 | 2024 | Intrusion Detection Using Machine Learning and Deep Learning Models on Cyber Security Attacks | VFAST Transactions on Software Engineering | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 44 | 2024 | Investigating the Robustness Against Transferable Adversarial Attacks of Learning-Based Network Intrusion Detection System | 2024 RIVF International Conference on Computing and Communication Technologies (RIVF) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 45 | 2024 | Investigating the Transferability of Evasion Attacks in Network Intrusion Detection Systems Considering Domain-Specific Constraints | Web Information System and Application Conference | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 46 | 2024 | Let the Noise Speak: Harnessing Noise for a Unified Defense Against Adversarial and Backdoor Attacks | European Symposium on Research in Computer Security | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 47 | 2024 | PANDA: Practical Adversarial Attack Against Network Intrusion Detection | 2024 54th Annual IEEE/IFIP International Conference on Dependable Systems and Networks - Supplemental Volume (DSN-S) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 48 | 2024 | Rigorous Evaluation of Machine Learning-Based Intrusion Detection Against Adversarial Attacks | 2024 IEEE International Conference on Cyber Security and Resilience (CSR) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 49 | 2024 | RobEns: Robust Ensemble Adversarial Machine Learning Framework for Securing IoT Traffic | Sensors (Basel, Switzerland) | include for full text | — |
| 50 | 2024 | Stealthy Adversarial Attacks on Intrusion Detection Systems: A Functionality-Preserving Approach | 2024 International Wireless Communications and Mobile Computing (IWCMC) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 51 | 2024 | Toward Transferable Adversarial Attacks Against Autoencoder-Based Network Intrusion Detectors | IEEE Transactions on Industrial Informatics | include for full text | — |
| 52 | 2024 | Towards realistic problem-space adversarial attacks against machine learning in network intrusion detection | Proceedings of the 19th International Conference on Availability, Reliability and Security | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 53 | 2025 | A Deterministic, Rule-Based Framework for Detecting Anomalous IP Packet Fragmentation | Future Internet | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 54 | 2025 | AI-Driven Adversarial Attacks and Defenses in Network Security | International Research Journal on Advanced Engineering Hub (IRJAEH) | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 55 | 2025 | ARTEMIS: Adaptive Reweighing for Transferable Evasion via Meta-learning in Zero-Query Network Intrusion Detection Systems | 2025 IEEE 33rd International Conference on Network Protocols (ICNP) | exclude | EC: conference paper |
| 56 | 2025 | Adversarial AI the New Frontier in Cybersecurity Threats and Defenses | Journal of Science, Technology and Engineering Research | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 57 | 2025 | Adversarial Attack Detection in Industrial Control Systems Using LSTM-Based Intrusion Detection and Black-Box Defense Strategies | Journal of Cyber Security and Risk Auditing | include for full text | — |
| 58 | 2025 | Adversarial Robustness of Network IDS (Structured Data) | Journal of Al-Qadisiyah for Computer Science and Mathematics | include for full text | — |
| 59 | 2025 | Adversarial Threats to Cloud IDS: Robust Defense With Adversarial Training and Feature Selection | IEEE Access | include for full text | — |
| 60 | 2025 | Adversarial attack and defense in AI-powered intrusion detection | Journal of Computer Science and Cybernetics | include for full text | — |
| 61 | 2025 | Artificial Intelligence for Improving Cybersecurity Framework | INTERNATIONAL JOURNAL OF SCIENTIFIC RESEARCH IN ENGINEERING AND MANAGEMENT | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 62 | 2025 | Assessing the Resilience of Automotive Intrusion Detection Systems to Adversarial Manipulation | ACM Transactions on Cyber-Physical Systems | include for full text | — |
| 63 | 2025 | Breaking and Healing: GAN-Based Adversarial Attacks and Post-Adversarial Recovery for 5G IDSs | IEEE Access | include for full text | — |
| 64 | 2025 | Bringing to Light: Adversarial Poisoning Detection for ML-Based IDS in Software-Defined Networks | IEEE Transactions on Network Science and Engineering | exclude | EC: poisoning detection |
| 65 | 2025 | CARD: Robustness-Preserving Transfer Learning for Network Intrusion Detection via Contrastive Adversarial Representation Distillation | IEEE Transactions on Dependable and Secure Computing | include for full text | — |
| 66 | 2025 | Constrained Network Adversarial Attacks: Validity, Robustness, and Transferability | 2025 21st International Conference on Distributed Computing in Smart Systems and the Internet of Things (DCOSS-IoT) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 67 | 2025 | Cross-Domain Adversarial Attacks: Translating Network Intrusion to CAN Bus Evasion in V2X Environments | 2025 IEEE 101st Vehicular Technology Conference (VTC2025-Spring) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 68 | 2025 | Deep Learning Architectures for Automated Threat Detection and Mitigation in Modern Cyber Security Systems | Journal of Information Systems Engineering and Management | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 69 | 2025 | Explainable and perturbation-resilient model for cyber-threat detection in industrial control systems Networks | Discover Internet of Things | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 70 | 2025 | Exploring transferable adversarial attacks for Deep Learning-based Network Intrusion Detection | J. Netw. Comput. Appl. | include for full text | — |
| 71 | 2025 | FASER-IN: Evasion of Network Intrusion Detection Systems in Industrial Networks | Proceedings of the 11th ACM Cyber-Physical System Security Workshop | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 72 | 2025 | FortiNIDS: Defending Smart City IoT Infrastructures Against Transferable Adversarial Poisoning in Machine Learning-Based Intrusion Detection Systems | Sensors (Basel, Switzerland) | exclude | EC: poisoning |
| 73 | 2025 | GenAtt NIDS Attack: A Practical Generative Adversarial Attack Against Network Intrusion Detection Systems | 2025 29th International Computer Conference, Computer Society of Iran (CSICC) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 74 | 2025 | Harnessing Artificial Intelligence to Strengthen Intrusion Detection in Modern Network System | International Journal of Scientific Research and Management (IJSRM) | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 75 | 2025 | MasqueradeGAN‐GP: A Generative Adversarial Network Framework for Evading Black‐Box Intrusion Detection Systems | Internet Technology Letters | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 76 | 2025 | NonsaliencyCrossover: A Novel Adversarial Example Generation Strategy for IDS Using Explainable AI | IEEE Internet of Things Journal | include for full text | — |
| 77 | 2025 | ProvADShield: A Multimodel Ensemble Defender Against Adversarial Attacks on Provenance Graph Host Intrusion Detector | IET Information Security | exclude | EC: host-only (provenance-graph HIDS) |
| 78 | 2025 | Real-Time Evasion Detection in Tree Ensemble Automotive Intrusion Detection Systems | 2025 IEEE Vehicular Networking Conference (VNC) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 79 | 2025 | Revealing the Vulnerabilities of Learning-based Network Intrusion Detectors through XAI-guided Adversarial Attack | 2025 IEEE 31th International Conference on Parallel and Distributed Systems (ICPADS) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 80 | 2025 | Securing Data Privacy in NIDS: Black‐Box Adversarial Attacks | International Journal of Intelligent Systems | include for full text | — |
| 81 | 2025 | The use of neural networks for real-time big data analysis | Программные системы и вычислительные методы | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 82 | 2025 | Vulnerability disclosure through adaptive black-box adversarial attacks in network intrusion detection systems | Complex & Intelligent Systems | include for full text | — |
| 83 | 2025 | Xai-driven black-box adversarial attacks on network intrusion detectors | International Journal of Information Security | include for full text | — |
| 84 | 2026 | A privacy-preserving source-free unsupervised domain adaptation framework for robust network intrusion detection under domain shift | Engineering Research Express | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 85 | 2026 | AI-Powered Cybersecurity: Emerging Trends and Challenges – A Narrative Review | Iraqi Journal for Computers and Informatics | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 86 | 2026 | Adversarial Attack on CAN IDS Leveraging Multi-DDQN Agent | IEEE Access | include for full text | — |
| 87 | 2026 | Adversarial Machine Learning in Cybersecurity: A Survey of Attacks, Defenses, and Robustness Evaluation | International Journal of Innovations in Science, Engineering And Management | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 88 | 2026 | Adversarial Robustness of Deep Learning-Based Intrusion Detection Systems: A Systematic Literature Review of Attacks, Defenses, Datasets, and Open Challenges | IEEE Access | route to review register | secondary study |
| 89 | 2026 | Adversarial Transferability in AI-based Network Intrusion Detection: A Comparative Study of ANN and CNN Models | International Journal of Information Technology and Computer Science | include for full text | — |
| 90 | 2026 | Adversarial manipulation of CAN bus IDS | Discover Artificial Intelligence | include for full text | — |
| 91 | 2026 | Adversarial resilience in cloud based machine learning: a unified framework for robust threat detection and forecasting | Journal of Cloud Computing | include for full text | — |
| 92 | 2026 | Artificial Intelligence-Based Intrusion Detection Systems for Cloud and Internet of Things (IoT) Environments | International Journal of Computer Information Systems and Industrial Management Applications | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 93 | 2026 | Attention Guided Graph Neural Network andBayesian Reasoning Framework for Cross-ZoneCyber-Physical Threat Intelligence and ContextAware Predictive Smart Defense | International Journal of Computer Network and Information Security | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 94 | 2026 | Black‐Box Adversarial Attack With Nesterov‐AdaX Momentum on Airport Ground Vehicle Surveillance | Transactions on Emerging Telecommunications Technologies | exclude | EC: not NIDS (vehicle surveillance imagery) |
| 95 | 2026 | COMPARATIVE ANALYSIS OF BLACK-BOX TARGETED ADVERSARIAL ATTACKS ON DL-BASED NIDS: A STUDY OF C&W AND JSMA USING CICDDOS2019 | International journal of Computer Networks &amp; Communications | include for full text | — |
| 96 | 2026 | DDoS Adversarial Attacks Detection with Deep Neural Networks in P4 Programmable Switches | 2026 Joint European Conference on Networks and Communications & 6G Summit (EuCNC/6G Summit) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 97 | 2026 | DEFENSIVE DISTILLATION AND GENERATIVE ADVERSARIAL NETWORKS (GANS) MITIGATING BLACK-BOX EVASION ATTACKS ON CLOUD-BASED INTRUSION DETECTION SYSTEMS | INTERNATIONAL RESEARCH JOURNAL OF MODERNIZATION IN ENGINEERING TECHNOLOGY AND SCIENCE | include for full text | — |
| 98 | 2026 | Defending Intrusion Detection Systems from Black-Box Adversarial Threats in OneM2M-Based IoT Networks | 2026 13th International Conference on Future Internet of Things and Cloud (FiCloud) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 99 | 2026 | EXPLAINABLE ARTIFICIAL INTELLIGENCE FOR CYBERSECURITY: TECHNIQUES, APPLICATIONS, CHALLENGES, AND FUTURE RESEARCH DIRECTIONS | Jana Nexus: Journal of Computer Science | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 100 | 2026 | Enhancing adversarial robustness of network intrusion detection systems against gray-box attacks | Computer Networks | include for full text | — |
| 101 | 2026 | Evaluating the Robustness and Transferable Adversarial Example Resistance of Multimodal Learning-based Intrusion Detection Systems against Evasion Attacks | Mobile Networks and Applications | include for full text | — |
| 102 | 2026 | Explainable Robust Cloud Intrusion Detection Against Adversarial Evasion Using SHAP-Guided Feature Reweighting | Computer Life | include for full text | — |
| 103 | 2026 | FEVA-ICS: Benchmarking Adversarial Robustness of Machine Learning-based Intrusion Detection Systems in Industrial Control Systems | Proceedings of the 12th ACM Cyber-Physical System Security Workshop | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 104 | 2026 | Feature-Space Adversarial Robustness Evaluation of Lightweight ML-Based Intrusion Detection for IoT and Healthcare-Sensing Networks | IEEE Access | include for full text | — |
| 105 | 2026 | FlowUAP: Evading Network Intrusion Detection Systems With Type-Specific Universal Adversarial Perturbations | IEEE Transactions on Information Forensics and Security | include for full text | — |
| 106 | 2026 | Game-Theoretic Cost-Sensitive Adversarial Training for Robust Cloud Intrusion Detection Against GAN-Based Evasion Attacks | Applied Sciences | include for full text | — |
| 107 | 2026 | Hive-AI: a defended multi-service honeypot framework for generative AI APIs | International Journal of Information Security | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 108 | 2026 | Impact of Query and Non-Query Black-Box Evasion Attacks on UAV Intrusion Detection Systems | 2026 IEEE 23rd Consumer Communications & Networking Conference (CCNC) | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 109 | 2026 | KEYSER: Stateful Adversarial Campaign Evaluation of ML-Based Intrusion Detection in Industrial Automation | 2026 IEEE 31st International Conference on Emerging Technologies and Factory Automation (ETFA) | exclude | EC: conference paper |
| 110 | 2026 | LLM-Orchestrated Evasion of Tabular NIDS and GAN Augmentation for Multimodal Detection | Applied Sciences | include for full text | — |
| 111 | 2026 | Leakage-aware and imbalance-robust gradient boosting for intrusion detection in cyber-physical healthcare systems under adversarial AI threats | Scientific Reports | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 112 | 2026 | Liuer Mihou: A Practical Gray-Box Adversarial Attack Against Anomaly-Based Network Intrusion Detection Systems | IEEE Transactions on Network and Service Management | include for full text | — |
| 113 | 2026 | MACHINE LEARNING FOR NETWORK INTRUSION DETECTION IN USA CRITICAL INFRASTRUCTURE: CHALLENGES AND OPPORTUNITIES | International Journal of Network Security &amp; Its Applications | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 114 | 2026 | MSCNN-BiLSTM: A Network Intrusion Detection Model Optimized by Genetic Algorithm with Deep Spatio-Temporal Feature Learning | Informatica (Slovenia) | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 115 | 2026 | Machine Learning for Network Intrusion Detection: An Analytical Review of Methods, Benchmark Datasets, and the Gap Between Reported and Operational Performance | International Journal of Information &amp; Digital Security | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 116 | 2026 | Making the Best of Both Worlds: Universal Perturbations for Live Black-Box Evasion Against NIDS in Encrypted Traffic | IEEE Transactions on Networking | include for full text | — |
| 117 | 2026 | RandomForestNN Classification for Adversarial AI Black-Box Techniques on MITRE ATT&CK Labeled Data | Electronics | include for full text | — |
| 118 | 2026 | Revisiting adversarial robustness in NIDS: a multi-dataset evaluation of test-time evasion attacks | International Journal of Information Security | include for full text | — |
| 119 | 2026 | Robust AI-Driven Intrusion Detection and Defense for Next-Generation Consumer Services | IEEE Transactions on Consumer Electronics | include for full text | — |
| 120 | 2026 | Robustness Evaluation of Graph Neural Network-Based Network Intrusion Detection Systems against Adversarial Flow Injection | International Conference on Security and Cryptography | exclude | EC: conference/workshop proceedings (S2 type mis-labelled) |
| 121 | 2026 | Security and Resilience of AI-Enabled Edge Computing in Industrial IoT: Vulnerabilities, Defense Strategies, and Future Directions | Mesopotamian Journal of CyberSecurity | include for full text | — |
| 122 | 2026 | Slice-Aware Adversarial Vulnerability Analysis of TabNet-Based Intrusion Detection in 5G Network Slicing | Symmetry | include for full text | — |
| 123 | 2026 | Targeted adversarial traffic generation: black-box approach to evade intrusion detection systems in IoT networks | International Journal of Machine Learning and Cybernetics | include for full text | — |
| 124 | 2026 | The Explainability–Robustness Collision in Graph Neural Network Intrusion Detection: A Critical Survey | Computer and Decision Making: An International Journal | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 125 | 2026 | Uncertainty-Aware Evidential Adversarial Defense for Cloud Intrusion Detection under GAN-Based Evasion Attacks | International Journal of Advanced Engineering and Technology Research | include for full text | — |
| 126 | 2026 | Utilizing Meta-Learning to Enhance the Transferability of GAN-Based Adversarial Traffic Generation | ICC 2026 - IEEE International Conference on Communications | exclude | EC: conference paper |
| 127 | 2026 | ZK-FLGuard: Verifiable Privacy via Zero-Knowledge Proofs in Federated Anomaly Detection for 5G Edge-IoT Systems | International Journal of Computer Theory and Engineering | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |
| 128 | 2026 | ZORAN-Sec: A Zero Trust–Compliant Intrusion Detection Framework for Open RAN With a Lightweight Transformer | IEEE Open Journal of the Communications Society | exclude | EC: off-topic / not an evasion attack or defence against ML-NIDS, or non-research article (title/abstract) |

---
*Raw API exports and scripts: `slr-blackbox-nids/data/raw/` and `slr-blackbox-nids/scripts/`.*
