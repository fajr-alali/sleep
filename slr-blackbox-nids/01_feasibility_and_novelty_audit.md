# Stage 1 — Feasibility and Novelty Audit

**Review topic:** Black-Box Evasion Attacks Against Machine Learning-Based Network Intrusion Detection Systems: A Systematic Literature Review of Attacker Capabilities, Attack Costs, Transferability, and Defense Evaluation
**Audit date:** 16 November 2026
**Status: Provisional.** Full texts of the comparator reviews could **not** be retrieved from this environment (see §1). Every comparison below is based on **abstracts and bibliographic metadata only**, and is labelled accordingly. Step B of the brief ("inspect their full texts") is **not done**.

---

## 1. Access conditions that constrain this audit

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

## 2. Closest existing reviews identified

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

## 3. Overlap assessment (abstract-level, provisional)

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

## 4. Is a differentiated review still justified? (provisional answer)

- **Substantial overlap exists.** RV1 already offers an NIDS-specific threat model and the feature-space vs executable-risk critique; RV2 already quantifies, at scale and with PRISMA, how rare query-based black-box attacks are and how dominant adversarial training is. A broad "adversarial evasion against NIDS" SLR would **not** be justified.
- **A narrower contribution may remain**, *if* full-text inspection of RV1, RV2 and RV3 confirms they do not systematically extract: (a) **target-query vs local-compute vs traffic costs** with explicit success denominators; (b) a **source–target transferability evidence map** that separates cross-model, cross-dataset, cross-pipeline and cross-environment transfer; (c) a **capability matrix** separating feedback type from data/feature/pipeline knowledge, specifically for black-box attacks.
- **Feasibility risk.** RV2 reports query-based black-box attacks in under 3% of 216 deep-learning IDS studies. Our title/abstract screening of the black-box subset kept 56 journal candidates (plus 7 seeds), and 11 of those appear in venues the reviewer expects to fall below Q2 (not verified). After SJR verification and full-text eligibility, the Q1/Q2 black-box corpus may be **at or below ~25 studies**. If so, the recommended design is a **focused SLR, or a systematic mapping review, on black-box NIDS evasion costs and transferability**, explicitly positioned as a deep extension of RV1/RV2, not a replacement.

**Recommendation (provisional):** Do not proceed to the full manuscript until (1) the full texts of RV1, RV2 and RV3 are compared against the extraction framework, and (2) SJR quartiles of the candidate journals are verified. Revisit the title and contribution claims after that comparison. The candidate phrase "capability-conditioned, cost-aware synthesis" must not be claimed as novel until step (1) is complete.
