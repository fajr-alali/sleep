# Stage 2 — Review Protocol (draft v0.1, 16 November 2026)

**Registration:** Not registered. No PROSPERO/OSF identifier exists; none is claimed.
**Protocol status:** Drafted *after* the initial searches were executed (same day). Search amendments are documented in `03_search_and_screening_report.md`. Prospective registration is recommended before Stage 4.
**Reviewers:** One reviewer (AI-assisted: Claude, under the user's direction). No second reviewer; no agreement statistic exists.

## 1. Research questions (exactly four)
- **RQ1:** What knowledge, feedback, access, and traffic-manipulation capabilities are assumed for attackers conducting black-box evasion against ML-based network intrusion detection systems?
- **RQ2:** What black-box evasion methods are evaluated, and what query, computational, data-acquisition, and network-perturbation costs are reported for successful evasion?
- **RQ3:** How transferable are black-box evasion attacks across target models, training datasets, feature-extraction pipelines, and network environments, and under what experimental conditions is transferability demonstrated?
- **RQ4:** How rigorously are defenses evaluated against black-box evasion, particularly regarding adaptive attackers, realistic traffic constraints, clean detection performance, and reproducibility?

## 2. Eligibility
**Include:** peer-reviewed journal articles; Q1/Q2 under §3; published 1 Jan 2020 – search date; inference-time evasion against ML/DL **network** IDS (flow- or packet-based; enterprise, cloud, SDN, IoT, IIoT, ICS, and in-vehicle networks*); at least one query-based, transfer-based, surrogate-based or hybrid black-box attack whose results can be extracted separately; or a defence evaluated against at least one such attack.
\*In-vehicle (CAN) IDS: included as "other network setting". This is a reviewer decision made at screening and is flagged for sensitivity analysis.

**Exclude:** preprints (arXiv, SSRN, TechRxiv, Research Square); conference/workshop papers, theses, reports, white papers; retracted articles; poisoning/backdoor as the main attack; model extraction or membership inference only; purely white-box studies; malware-file, phishing, image, spam or source-code tasks; host-only IDS; IDS studies with no adversarial evaluation; GAN data augmentation without an attacker; benign distribution shift; protocol fuzzing unrelated to ML evasion.

Overlapping publications: a journal paper and its earlier conference version are grouped into one *study family*; only the journal version is extracted.

## 3. Journal-ranking policy (predefined before any verification)
- **Source:** SCImago Journal Rank (SJR).
- **Predefined subject categories:** Computer Networks and Communications; Computer Science Applications; Information Systems; Artificial Intelligence; Software; Hardware and Architecture; Signal Processing; Electrical and Electronic Engineering; Safety, Risk, Reliability and Quality; Computer Science (miscellaneous); Control and Systems Engineering.
- **Rule:** eligible if Q1 or Q2 in **any** predefined category that the journal is listed under in the SJR ranking year. Record every category and quartile, not only the qualifying one.
- **Year:** publication-year quartile; if not yet published (e.g., 2026), the latest available year is used and labelled **proxy**. No 2026 quartile will be invented.
- **Record:** journal, ISSN/eISSN, publication year, SJR year, category, quartile, verification URL, verification date.
- **Status today:** **pending for every journal**. SCImago is not reachable from this environment.

## 4. Extraction framework
As specified in the brief (§9 A–H): bibliographic data; detection setting; attacker capabilities (eight knowledge items; feedback type: score, hard-label, indirect, none, unclear; local-surrogate white-box access vs target black-box access); attack method; costs (target queries by stage, surrogate cost, data acquisition, wall-clock time, hardware, bytes/packets/flows/delay, per-attempt vs per-success, one-time vs recurring); transferability (source/target, family, dataset, pipeline, environment, leakage); defence evaluation; reproducibility artefacts. Every substantive claim is recorded with page, section/table/figure and an evidence note, using the labels: Reported / Explicitly not implemented / Not reported / Unclear / Not applicable.

## 5. Appraisal
Eight domains (brief §11), each judged Adequate / Partially adequate / Inadequate / Unclear / Not applicable with page-level evidence. No aggregate score threshold.

## 6. Synthesis
Structured narrative per RQ with descriptive statistics and exact denominators; transfer matrices where reported; a conceptual cost vector C = (target queries, local compute, data acquisition, added bytes, added packets, delay), presented as a descriptive framework only. Meta-analysis only if comparable outcomes exist (not expected).

## 7. Status of this protocol's stages
| Stage | Status |
|---|---|
| 1 Feasibility and novelty audit | **Provisional** (abstract-level only) |
| 2 Protocol | **Provisional** (this document; unregistered) |
| 3 Searches and screening | **Partially completed and evidenced** (see report) |
| 4 Full-text extraction and appraisal | **Pending external access** |
| 5–7 Synthesis, manuscript, integrity audit | **Not started** |
