# Black-Box Evasion Attacks Against ML-Based NIDS — Systematic Review: Stage 1–3 Package

**Date:** 16 November 2026  
**Overall status: INCOMPLETE — not a manuscript; not submission-ready.** Numbered citations [n] refer to Section 5.

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
5. Reference list (user-supplied, verified)
Appendix A. Search log · Appendix B. Seed coverage test · Appendix C. Candidate register · Appendix D. Title/abstract screening log

---

## 1. Feasibility and Novelty Audit

**Review topic:** Black-Box Evasion Attacks Against Machine Learning-Based Network Intrusion Detection Systems: A Systematic Literature Review of Attacker Capabilities, Attack Costs, Transferability, and Defense Evaluation
**Audit date:** 16 November 2026 (updated with the user-supplied reference list the same day)
**Status: Provisional.** Full texts of the comparator reviews could **not** be retrieved from this environment (see §1). Every comparison below is based on **abstracts and bibliographic metadata only**. Step B of the brief ("inspect their full texts") is **not done**. Citations use the numbered reference list in Section 5.

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

### 1.2 Closest existing reviews

**Comparator set:** the seven reviews in the user-supplied list ([1]–[7]); the threat-modelling paper [8] is listed separately. All metadata were verified in Crossref. Q1/Q2 status is **pending** for every journal.

| Ref | Review | Journal, year | Abstract-level scope | Basis |
|---|---|---|---|---|
| [1] | He, Kim & Asghar — *AML for NIDS: A comprehensive survey* | IEEE COMST, 2023 | Survey since 2015; CV-vs-NIDS differences; reviews **white-box and black-box** attacks and their applicability to NIDS; defences | Abstract |
| [2] | Ennaji et al. — *Adversarial challenges in NIDS: Research insights and future prospects* | IEEE Access, 2025 | Survey of adversarial threats to ML-based IDS on structured network data (abstract truncated in the API) | Abstract (partial) |
| [3] | Alatawi — *Adversarial evasion in ML-based NIDS: A systematic review, threat modeling, and research roadmap* | IEEE Access, 2026 | Kitchenham-informed SLR of **186 studies (2018–2026)**; NIDS-specific lifecycle-aware threat model; taxonomy across generation, robustness evaluation and defence; finds that much reported success "reflects diagnostic feature-space sensitivity rather than executable, deployable adversarial risk" and that many defences show "component-level robustness" | Abstract |
| [4] | Espindola et al. — *Understanding the adversary: A survey of AML in network intrusion detection* | Computer Science Review, 2026 | Abstract not available via open APIs; Crossref lists an associated preprint, which is not used | Title only |
| [5] | Vitorino, Praça & Maia — *SoK: Realistic adversarial attacks and defenses for intelligent NID* | Computers & Security, 2023 | Systematisation of knowledge (SoK) of adversarial approaches that generate **realistic** examples under network and protocol constraints, and of defences usable with real traffic flows | Abstract |
| [6] | Hasan et al. — *Adversarial attacks against NIDS: Bridging the gap between theoretical vulnerabilities and practical constraints* | Internet of Things, 2026 | Abstract not available via open APIs; the title indicates a focus on practical attack constraints | Title only |
| [7] | Winanto & Idris — *Adversarial robustness of DL-based IDS: A SLR of attacks, defenses, datasets, and open challenges* | IEEE Access, 2026 | PRISMA 2020 SLR, Jan 2020–Mar 2026; 5,890 records (Scopus, IEEE Xplore, WoS, ScienceDirect); **216 primary studies**; FGSM in 76.9%, C&W 60.2%, PGD 50.9%, adversarial training 61.6%; **query-based black-box attacks rare** (Square Attack 2.8%, AutoAttack 2.3%) | Abstract |
| [8] | Apruzzese et al. — *Modeling realistic adversarial attacks against NIDS* | Digital Threats: Research and Practice, 2022 | Models the **real capabilities and circumstances** attackers need, then applies the model to attacks from the literature. Classification (comparator vs primary study) to be decided after full-text reading | Abstract |

**Other reviews found by the searches (not in the supplied list):** *Computer Networks* 2022 comparative study (10.1016/j.comnet.2022.109073); *Future Internet* 2023 survey (10.3390/fi15020062); *IEEE TAI* 2026 review (10.1109/TAI.2025.3641908); *IEEE Access* 2020 systematic review (10.1109/ACCESS.2020.2974752); IoT-focused reviews in *Future Internet* 2024 and *ACM CSUR* 2025; *JCP* 2022 functionality-preservation survey. **Contextual (outside the journal policy):** *Adversarial Black-Box Attacks Against NIDS: A Survey* (IEEE AIIoT 2021 conference, 10.1109/AIIoT52608.2021.9454214).

---

### 1.3 Overlap assessment (abstract-level, provisional)

| Proposed contribution element | [3] Alatawi 2026 | [7] Winanto & Idris 2026 | [5] Vitorino et al. 2023 | [1] He et al. 2023 | [6], [8] |
|---|---|---|---|---|---|
| NIDS-specific attacker capabilities (RQ1) | **Yes**: lifecycle-aware threat model | Not stated | Partly (realistic-attack conditions) | Partly (black-box vs white-box applicability) | **[8] Yes**: models real attacker capabilities and circumstances |
| Feature-space vs executable/traffic realizability | **Yes**: central finding | Not stated | **Yes**: realistic examples under network constraints | Yes: CV-vs-NIDS feature space | [6] likely (from title) |
| Black-box-specific synthesis (query/transfer/surrogate) | Not stated | **Partly**: quantifies how rare query-based attacks are | Not stated | Partly | — |
| **Attack-cost accounting** (target queries, compute, data, bytes/packets, delay) | Not stated in abstract | Not stated in abstract | Not stated in abstract | Not stated | Not determinable |
| **Transferability evidence map** (cross-model/dataset/pipeline/environment) | Not stated in abstract | Not stated in abstract | Not stated in abstract | Not stated | Not determinable |
| Defence-evaluation rigour (adaptive attackers, valid traffic) | **Yes**: "component-level robustness" critique | Partly (defence frequencies; certified defences rare) | **Yes**: defences for realistic settings | Partly | — |

"Not stated in abstract" does **not** mean the review omits the topic. This must be checked in the full texts before any differentiation claim.

---

### 1.4 Is a differentiated review still justified? (provisional answer)

- **Overlap is substantial and broader than first thought.** [3] already provides an NIDS-specific threat model and the feature-space vs executable-risk critique. [5] already systematises *realistic* attacks and defences. [8] already models realistic attacker capabilities. [7] already quantifies, with PRISMA at scale, how rare query-based black-box attacks are. [6]'s title indicates the same theory-vs-practice gap. A broad review, or one centred on attacker capabilities and realism (RQ1 alone), would **not** be justified.
- **A narrower contribution may remain**, *if* full-text inspection of [2]–[7] confirms that none systematically extracts (a) **target-query vs local-compute vs traffic costs** with explicit success denominators, and (b) a **source–target transferability evidence map** that separates cross-model, cross-dataset, cross-pipeline and cross-environment transfer. RQ2 and RQ3 are the most promising differentiators; RQ1 and RQ4 would serve as context.
- **Feasibility.** The supplied list contains **24 primary-study candidates** ([9]–[32]), plus [8] if it is reclassified. Together with the screening register (68 candidates in total), the eligible Q1/Q2 corpus may still be **at or below ~25 studies** after quartile and full-text checks (several candidate journals, e.g., *Computers*, *Security and Communication Networks*, *Int. J. Intelligent Systems*, *Complex & Intelligent Systems*, need quartile checks for the publication year). If so, a **focused SLR or systematic mapping review on black-box NIDS evasion costs and transferability** is recommended, positioned as an extension of [3], [5] and [7], not a replacement.

**Recommendation (provisional):** Do not write the full manuscript until (1) the full texts of [2]–[7] are compared against the extraction framework, and (2) SJR quartiles are verified. Do not claim "capability-conditioned, cost-aware synthesis" as novel before step (1).

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

In addition, **7 seed articles** were added to the candidate register directly (one may be white-box only), and **5 articles from the user-supplied reference list** ([14], [15], [22], [26], [31]) were added afterwards. **Candidate register: 68 records** (`data/candidate_register.csv`), all with Crossref-verified metadata and none with verified quartile or full text. The reviewer expects 11 of them to fall below Q2 or be unranked, but this is **not verified**, and they remain in the register.

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
| Records identified — other methods | 14 seed titles (12 verified); user-supplied reference list (34 references, 5 new candidates) |
| Duplicates removed | 1,582 (4,970 − 3,388) |
| Records removed by automated rules | 2,592 (publication-type rules 796 + relevance rules 1,796)ᵃ; 3,388 − 2,592 = 796 remain |
| Records screened (title/abstract, manual) | 129 of 796 (**667 pending**) |
| Records excluded at title/abstract | 70 (+3 routed to reviews) |
| Reports sought for retrieval | 68 |
| Reports not retrieved | **68** (no full-text access yet) |
| Reports assessed for eligibility | **0** |
| Studies included | **0 (review incomplete)** |

ᵃ Exact breakdown: publication-type rules removed 796 (40 + 135 + 621); relevance rules removed 1,796 (971 + 825); 995 of those 1,796 were title-only (see deviation). This table will be completed only from recorded counts.

---

## 4. Outstanding-Actions Register

| ID | Action | Why it blocks completion | Who / what is needed | Status |
|---|---|---|---|---|
| OA-1 | Retrieve and read the full texts of comparator reviews [1]–[7] and the threat-modelling paper [8] | Novelty cannot be judged from abstracts; [3], [5], [7] and [8] overlap substantially | PDFs supplied by the user ([2], [3] and [7] are in IEEE Access, which is open access) | Pending external access |
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

## 5. Reference List (user-supplied, verified)

References are numbered as supplied by the user, in IEEE style. **Verification** means that authors, title, journal, volume, year and DOI were checked against the Crossref record on 16 Nov 2026. It does **not** mean the technical content was verified: no full text has been read, and **no SJR quartile has been verified**.

### 5.1 Numbered references

[1] K. He, D. D. Kim, and M. R. Asghar, "Adversarial machine learning for network intrusion detection systems: A comprehensive survey," IEEE Commun. Surveys Tuts., vol. 25, no. 1, pp. 538–566, 1st Quart. 2023, doi: 10.1109/COMST.2022.3233793.

[2] S. Ennaji, F. De Gaspari, D. Hitaj, A. Kbidi, and L. V. Mancini, "Adversarial challenges in network intrusion detection systems: Research insights and future prospects," IEEE Access, vol. 13, pp. 148613–148645, 2025, doi: 10.1109/ACCESS.2025.3600984.

[3] H. A. Alatawi, "Adversarial evasion in machine-learning-based network intrusion detection: A systematic review, threat modeling, and research roadmap," IEEE Access, vol. 14, pp. 122143–122176, 2026, doi: 10.1109/ACCESS.2026.3720554.

[4] A. da S. Espindola, A. O. Santin, A. Casimiro, P. M. Ferreira, and E. K. Viegas, "Understanding the adversary: A survey of adversarial machine learning in network intrusion detection," Comput. Sci. Rev., vol. 62, Art. no. 100995, 2026, doi: 10.1016/j.cosrev.2026.100995.

[5] J. Vitorino, I. Praça, and E. Maia, "SoK: Realistic adversarial attacks and defenses for intelligent network intrusion detection," Comput. Secur., vol. 134, Art. no. 103433, 2023, doi: 10.1016/j.cose.2023.103433.

[6] M. M. Hasan, R. Islam, Q. Mamun, M. Z. Islam, and J. Gao, "Adversarial attacks against network intrusion detection systems: Bridging the gap between theoretical vulnerabilities and practical constraints," Internet Things, vol. 38, Art. no. 101997, 2026, doi: 10.1016/j.iot.2026.101997.

[7] E. A. Winanto and M. Y. Idris, "Adversarial robustness of deep learning-based intrusion detection systems: A systematic literature review of attacks, defenses, datasets, and open challenges," IEEE Access, vol. 14, pp. 149555–149591, 2026, doi: 10.1109/ACCESS.2026.3733985.

[8] G. Apruzzese, M. Andreolini, L. Ferretti, M. Marchetti, and M. Colajanni, "Modeling realistic adversarial attacks against network intrusion detection systems," Digit. Threats: Res. Pract., vol. 3, no. 3, Art. no. 31, Sep. 2022, doi: 10.1145/3469659.

[9] G. Apruzzese, M. Andreolini, M. Marchetti, A. Venturi, and M. Colajanni, "Deep reinforcement adversarial learning against botnet evasion attacks," IEEE Trans. Netw. Service Manag., vol. 17, no. 4, pp. 1975–1987, Dec. 2020, doi: 10.1109/TNSM.2020.3031843.

[10] S. Zhang, X. Xie, and Y. Xu, "A brute-force black-box method to attack machine learning-based systems in cybersecurity," IEEE Access, vol. 8, pp. 128250–128263, 2020, doi: 10.1109/ACCESS.2020.3008433.

[11] D. Han et al., "Evaluating and improving adversarial robustness of machine learning-based network intrusion detectors," IEEE J. Sel. Areas Commun., vol. 39, no. 8, pp. 2632–2647, Aug. 2021, doi: 10.1109/JSAC.2021.3087242.

[12] H. Qiu, T. Dong, T. Zhang, J. Lu, G. Memmi, and M. Qiu, "Adversarial attacks against network intrusion detection in IoT systems," IEEE Internet Things J., vol. 8, no. 13, pp. 10327–10335, Jul. 2021, doi: 10.1109/JIOT.2020.3048038.

[13] P. T. Duy, L. K. Tien, N. H. Khoa, D. T. T. Hien, A. G.-T. Nguyen, and V.-H. Pham, "DIGFuPAS: Deceive IDS with GAN and function-preserving on adversarial samples in SDN-enabled networks," Comput. Secur., vol. 109, Art. no. 102367, 2021, doi: 10.1016/j.cose.2021.102367.

[14] S. Guo, J. Zhao, X. Li, J. Duan, D. Mu, and X. Jing, "A black-box attack method against machine-learning-based anomaly network flow detection models," Secur. Commun. Netw., vol. 2021, Art. no. 5578335, 2021, doi: 10.1155/2021/5578335.

[15] J. Chen, X. Gao, R. Deng, Y. He, C. Fang, and P. Cheng, "Generating adversarial examples against machine learning-based intrusion detector in industrial control systems," IEEE Trans. Dependable Secure Comput., vol. 19, no. 3, pp. 1810–1825, May/Jun. 2022, doi: 10.1109/TDSC.2020.3037500.

[16] Y. Sharon, D. Berend, Y. Liu, A. Shabtai, and Y. Elovici, "TANTRA: Timing-based adversarial network traffic reshaping attack," IEEE Trans. Inf. Forensics Security, vol. 17, pp. 3225–3237, 2022, doi: 10.1109/TIFS.2022.3201377.

[17] C. Zhang, X. Costa-Pérez, and P. Patras, "Adversarial attacks against deep learning-based network intrusion detection systems and defense mechanisms," IEEE/ACM Trans. Netw., vol. 30, no. 3, pp. 1294–1311, Jun. 2022, doi: 10.1109/TNET.2021.3137084.

[18] S. Alahmed, Q. Alasad, M. M. Hammood, J.-S. Yuan, and M. Alawad, "Mitigation of black-box attacks on intrusion detection systems-based ML," Computers, vol. 11, no. 7, Art. no. 115, 2022, doi: 10.3390/computers11070115.

[19] I. Debicha, B. Cochez, T. Kenaza, T. Debatty, J.-M. Dricot, and W. Mees, "Adv-Bot: Realistic adversarial botnet attacks against network intrusion detection systems," Comput. Secur., vol. 129, Art. no. 103176, 2023, doi: 10.1016/j.cose.2023.103176.

[20] S. Aldhaheri and A. Alhuzali, "SGAN-IDS: Self-attention-based generative adversarial network against intrusion detection systems," Sensors, vol. 23, no. 18, Art. no. 7796, 2023, doi: 10.3390/s23187796.

[21] H. Yan et al., "Automatic evasion of machine learning-based network intrusion detection systems," IEEE Trans. Dependable Secure Comput., vol. 21, no. 1, pp. 153–167, Jan./Feb. 2024, doi: 10.1109/TDSC.2023.3247585.

[22] M. Wang, N. Yang, N. J. Forcade-Perkins, and N. Weng, "ProGen: Projection-based adversarial attack generation against network intrusion detection," IEEE Trans. Inf. Forensics Security, vol. 19, pp. 5476–5491, 2024, doi: 10.1109/TIFS.2024.3402155.

[23] N. Alhussien, A. Aleroud, A. Melhem, and S. Y. Khamaiseh, "Constraining adversarial attacks on network intrusion detection systems: Transferability and defense analysis," IEEE Trans. Netw. Service Manag., vol. 21, no. 3, pp. 2751–2772, Jun. 2024, doi: 10.1109/TNSM.2024.3357316.

[24] Y. Zhang, Y. Wu, and X. Huang, "Toward transferable adversarial attacks against autoencoder-based network intrusion detectors," IEEE Trans. Ind. Informat., vol. 20, no. 12, pp. 13863–13872, Dec. 2024, doi: 10.1109/TII.2024.3435532.

[25] S. Sharma and Z. Chen, "A systematic study of adversarial attacks against network intrusion detection systems," Electronics, vol. 13, no. 24, Art. no. 5030, 2024, doi: 10.3390/electronics13245030.

[26] K. Roshan and A. Zafar, "Black-box adversarial transferability: An empirical study in cybersecurity perspective," Comput. Secur., vol. 141, Art. no. 103853, 2024, doi: 10.1016/j.cose.2024.103853.

[27] F. Aloraini, A. Javed, and O. Rana, "Adversarial attacks on intrusion detection systems in in-vehicle networks of connected and autonomous vehicles," Sensors, vol. 24, no. 12, Art. no. 3848, 2024, doi: 10.3390/s24123848.

[28] S. Okada et al., "XAI-driven black-box adversarial attacks on network intrusion detectors," Int. J. Inf. Secur., vol. 24, Art. no. 103, 2025, doi: 10.1007/s10207-025-01016-0.

[29] D. Xu et al., "Securing data privacy in NIDS: Black-box adversarial attacks," Int. J. Intell. Syst., vol. 2025, Art. no. 1500333, 2025, doi: 10.1155/int/1500333.

[30] H. Zhang et al., "Explainable and transferable adversarial attack for ML-based network intrusion detectors," IEEE Trans. Dependable Secure Comput., vol. 22, no. 5, pp. 5090–5107, Sep./Oct. 2025, doi: 10.1109/TDSC.2025.3560486.

[31] Z. Awad, M. Zakaria, and R. Hassan, "An enhanced ensemble defense framework for boosting adversarial robustness of intrusion detection systems," Sci. Rep., vol. 15, Art. no. 14177, 2025, doi: 10.1038/s41598-025-94023-z.

[32] S. Ennaji, E. Benkhelifa, and L. V. Mancini, "Vulnerability disclosure through adaptive black-box adversarial attacks in network intrusion detection systems," Complex Intell. Syst., vol. 12, Art. no. 18, 2026, doi: 10.1007/s40747-025-02115-0.

[33] B. Kitchenham and S. Charters, "Guidelines for performing systematic literature reviews in software engineering," Keele Univ. and Durham Univ., UK, Tech. Rep. EBSE-2007-01, 2007.

[34] M. J. Page et al., "The PRISMA 2020 statement: An updated guideline for reporting systematic reviews," BMJ, vol. 372, Art. no. n71, 2021, doi: 10.1136/bmj.n71.

### 5.2 Verification status and crosswalk

| Ref | Role | Metadata verified (Crossref) | Discrepancies | Candidate-register ID | Journal eligibility (SJR) | Full text read |
|---|---|---|---|---|---|---|
| [1] | Comparator review | Yes | None | — | Pending | No |
| [2] | Comparator review | Yes | None | — | Pending | No |
| [3] | Comparator review | Yes | None | — | Pending | No |
| [4] | Comparator review | Yes | Crossref links a preprint; cite and extract the journal version only. | — | Pending | No |
| [5] | Comparator review | Yes | None | — | Pending | No |
| [6] | Comparator review | Yes | None | — | Pending | No |
| [7] | Comparator review | Yes | None | — | Pending | No |
| [8] | Threat-modelling paper (classify after full text) | Yes | Crossref lists pages 1–19 for Art. no. 31 (ACM article numbering); consistent. | — (comparator) | Pending | No |
| [9] | Primary-study candidate | Yes | None | C58 | Pending | No |
| [10] | Primary-study candidate | Yes | None | C01 | Pending | No |
| [11] | Primary-study candidate | Yes | None | C02 | Pending | No |
| [12] | Primary-study candidate | Yes | None | C03 | Pending | No |
| [13] | Primary-study candidate | Yes | None | C60 | Pending | No |
| [14] | Primary-study candidate | Yes | Crossref lists pages 1–13 for Art. no. 5578335; consistent. | C64 | Pending | No |
| [15] | Primary-study candidate | Yes | None | C65 | Pending | No |
| [16] | Primary-study candidate | Yes | None | C59 | Pending | No |
| [17] | Primary-study candidate | Yes | None | C04 | Pending | No |
| [18] | Primary-study candidate | Yes | None | C07 | Pending | No |
| [19] | Primary-study candidate | Yes | None | C11 | Pending | No |
| [20] | Primary-study candidate | Yes | None | C14 | Pending | No |
| [21] | Primary-study candidate | Yes | None | C17 | Pending | No |
| [22] | Primary-study candidate | Yes | None | C66 | Pending | No |
| [23] | Primary-study candidate | Yes | None | C19 | Pending | No |
| [24] | Primary-study candidate | Yes | None | C22 | Pending | No |
| [25] | Primary-study candidate | Yes | None | C15 | Pending | No |
| [26] | Primary-study candidate | Yes | None | C67 | Pending | No |
| [27] | Primary-study candidate | Yes | None | C16 | Pending | No |
| [28] | Primary-study candidate | Yes | None | C34 | Pending | No |
| [29] | Primary-study candidate | Yes | None | C32 | Pending | No |
| [30] | Primary-study candidate | Yes | None | C20 | Pending | No |
| [31] | Primary-study candidate | Yes | None | C68 | Pending | No |
| [32] | Primary-study candidate | Yes | None | C33 | Pending | No |
| [33] | Methodological | Not verifiable via Crossref (technical report, no DOI) | — | — | n/a | n/a |
| [34] | Methodological | Yes | Crossref record has no volume field; 372:n71 per BMJ citation. | — | n/a | n/a |

**Summary:** 33 of 34 references were confirmed against Crossref with no substantive discrepancy; [33] cannot be checked this way. Of the 24 primary-study candidates [9]–[32], 19 were already in the candidate register from the executed searches, and 5 ([14], [15], [22], [26], [31]) were added as C64–C68 with source 'user-supplied list'. None is yet confirmed as eligible: quartiles and full-text eligibility are pending (OA-2, OA-7).

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

## Appendix C. Candidate register (68 records)

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
| C64 | A Black-Box Attack Method against Machine-Learning-Based Anomaly Network Flow Detection Models | Security and Communication Networks | 2021 | 2021/1-13 | [10.1155/2021/5578335](https://doi.org/10.1155/2021/5578335) | user-supplied reference list [14] | Substitute-model black-box attack on anomaly flow detectors (abstract) | unverified |
| C65 | Generating Adversarial Examples Against Machine Learning-Based Intrusion Detector in Industrial Control Systems | IEEE Transactions on Dependable and Secure Computing | 2022 | 19/3/1810-1825 | [10.1109/tdsc.2020.3037500](https://doi.org/10.1109/tdsc.2020.3037500) | user-supplied reference list [15] | ICS IDS; optimal-solution and GAN attacks under protocol constraints; attacker knowledge to verify | unverified |
| C66 | ProGen: Projection-Based Adversarial Attack Generation Against Network Intrusion Detection | IEEE Transactions on Information Forensics and Security | 2024 | 19/5476-5491 | [10.1109/tifs.2024.3402155](https://doi.org/10.1109/tifs.2024.3402155) | user-supplied reference list [22] | Traffic-space attack generation (ProGen); black-box component to verify | unverified |
| C67 | Black-box adversarial transferability: An empirical study in cybersecurity perspective | Computers & Security | 2024 | 141/103853 | [10.1016/j.cose.2024.103853](https://doi.org/10.1016/j.cose.2024.103853) | user-supplied reference list [26] | Empirical surrogate-to-target black-box transferability in attack detection (abstract) | unverified |
| C68 | An enhanced ensemble defense framework for boosting adversarial robustness of intrusion detection systems | Scientific Reports | 2025 | 15/1/14177 | [10.1038/s41598-025-94023-z](https://doi.org/10.1038/s41598-025-94023-z) | user-supplied reference list [31] | Ensemble defence; confirm black-box attacks in evaluation | unverified |

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
