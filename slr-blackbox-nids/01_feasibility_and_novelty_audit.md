# Stage 1 — Feasibility and Novelty Audit

**Review topic:** Black-Box Evasion Attacks Against Machine Learning-Based Network Intrusion Detection Systems: A Systematic Literature Review of Attacker Capabilities, Attack Costs, Transferability, and Defense Evaluation
**Audit date:** 16 November 2026 (updated with the user-supplied reference list the same day)
**Status: Provisional.** Full texts of the comparator reviews could **not** be retrieved from this environment (see §1). Every comparison below is based on **abstracts and bibliographic metadata only**. Step B of the brief ("inspect their full texts") is **not done**. Citations use the numbered reference list in Section 5.

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

## 2. Closest existing reviews

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

## 3. Overlap assessment (abstract-level, provisional)

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

## 4. Is a differentiated review still justified? (provisional answer)

- **Overlap is substantial and broader than first thought.** [3] already provides an NIDS-specific threat model and the feature-space vs executable-risk critique. [5] already systematises *realistic* attacks and defences. [8] already models realistic attacker capabilities. [7] already quantifies, with PRISMA at scale, how rare query-based black-box attacks are. [6]'s title indicates the same theory-vs-practice gap. A broad review, or one centred on attacker capabilities and realism (RQ1 alone), would **not** be justified.
- **A narrower contribution may remain**, *if* full-text inspection of [2]–[7] confirms that none systematically extracts (a) **target-query vs local-compute vs traffic costs** with explicit success denominators, and (b) a **source–target transferability evidence map** that separates cross-model, cross-dataset, cross-pipeline and cross-environment transfer. RQ2 and RQ3 are the most promising differentiators; RQ1 and RQ4 would serve as context.
- **Feasibility.** The supplied list contains **24 primary-study candidates** ([9]–[32]), plus [8] if it is reclassified. Together with the screening register (68 candidates in total), the eligible Q1/Q2 corpus may still be **at or below ~25 studies** after quartile and full-text checks (several candidate journals, e.g., *Computers*, *Security and Communication Networks*, *Int. J. Intelligent Systems*, *Complex & Intelligent Systems*, need quartile checks for the publication year). If so, a **focused SLR or systematic mapping review on black-box NIDS evasion costs and transferability** is recommended, positioned as an extension of [3], [5] and [7], not a replacement.

**Recommendation (provisional):** Do not write the full manuscript until (1) the full texts of [2]–[7] are compared against the extraction framework, and (2) SJR quartiles are verified. Do not claim "capability-conditioned, cost-aware synthesis" as novel before step (1).
