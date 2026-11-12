# Machine Learning for Ransomware Detection: A Systematic Literature Review of Early Detection, Explainability, and Real-World Deployability (2016–2026)

**Manuscript type:** Systematic Literature Review (PRISMA 2020)
**Search window:** January 2016 – November 2026 (search executed 12 November 2026)
**Corpus:** 56 primary studies (after quality gate), 117 eligible studies (sensitivity set), 18 secondary studies (surveys/SLRs)
**Replication package:** `slr/scripts/` (search, screening, extraction, analysis code) and `slr/data/` (raw Crossref pool, screened set, extraction JSON)

> **Verification notice.** Every reference below was retrieved from, and its DOI resolved against, the Crossref REST API (or the arXiv API for three methodological works without DOIs) at the time of writing. **[VERIFIED]** = bibliographic metadata (authors, title, venue, year, DOI) confirmed in Crossref *and* data extraction performed on the full abstract. **[VERIFIED metadata · CANDIDATE coding]** = bibliographic metadata confirmed, but the abstract was not available through open APIs, so the extraction fields were coded from the Semantic Scholar TLDR, title and reviewer knowledge and **must be checked against the full text before submission**. Journal quartiles were assigned from the reviewers' SJR whitelist (Section 4.4); the live SJR portal could not be queried from the review environment and must be re-checked for the publication year of each paper before submission.

---

## Abstract

**Context.** Ransomware remains among the most damaging classes of malware, and machine learning (ML) and deep learning (DL) have become the dominant research response. Yet three properties determine whether a detector actually prevents loss — *how early* it fires in the attack lifecycle, *whether its decisions can be explained and trusted*, and *whether it can run on real systems* — and these are rarely examined together.
**Objective.** To systematically characterise ML/DL ransomware detection research from 2016 to 2026 along four research questions covering techniques and lifecycle stage (RQ1), inputs and datasets (RQ2), explainability and its evaluation (RQ3), and gaps in early detection, explainability and deployment (RQ4).
**Method.** A PRISMA 2020-compliant review. Twenty-seven search strings were executed against Crossref (which indexes IEEE, ACM, Elsevier, Springer Nature, MDPI and Wiley metadata), yielding 1,158 unique records, supplemented by 25 known-item/snowball look-ups. Records were filtered by document type, by a Q1/Q2 journal whitelist and a top-tier conference list, then screened on title/abstract and assessed for eligibility. A five-criterion quality instrument (dataset realism, evaluation rigour, reproducibility, explainability, deployment readiness; 0–10) was applied, with a pre-registered inclusion threshold of ≥4.
**Results.** 117 studies met the eligibility criteria; 56 passed the quality gate. Post-execution behavioural detection dominates (35/56, 63%), while only 18 (32%) target the at-execution (pre-encryption) window and 11 (20%) operate pre-execution. API-call traces are the most common input (24/56, 43%), and classical ML remains the most frequent model family (32/56, 57%), with CNN/RNN/Transformer models rising since 2022. Only 20/56 studies (36%) include any explainability component, and **none reports a quantitative evaluation of explanation faithfulness, stability or actionability**. Only 9/56 (16%) test on unseen families, 7/56 (13%) test temporal drift, and **no study does both**; 5/56 (9%) measure runtime overhead and none reaches field/longitudinal validation (Deployment Readiness Level 4 in our taxonomy). Windows dominates (43/56, 77%).
**Conclusions.** The field has matured in accuracy but not in the properties that matter at the moment of attack. We contribute (i) a four-stage lifecycle-aligned taxonomy with explicit Explanation Levels and Deployment Readiness Levels, (ii) a reproducible, scripted PRISMA pipeline and quality-scored evidence table, and (iii) seven evidence-backed research gaps with concrete future directions, foremost the absence of explanation-quality evaluation and of joint drift-plus-novelty testing.

**Keywords:** ransomware; machine learning; deep learning; early detection; explainable AI; deployability; concept drift; systematic literature review; PRISMA

---

## 1. Introduction

### 1.1 Motivation
Ransomware couples a reliable monetisation channel with irreversible damage: once user data are encrypted with a properly managed key, detection *after the fact* does not restore them. The research community has responded with a large body of detectors, and successive surveys report that ML-based approaches now account for the majority of ransomware *detection* work — Razaulla et al. [R12] report that 72.8% of the research they analysed focused on detection and that 70% of detection studies used ML. The present review's own search found 1,158 distinct records with "ransom*" in the title for 2016–2026 in Crossref alone.

### 1.2 Why ransomware detection is important
Unlike most malware, ransomware's payload *is* the damage. Encryption is fast, and modern families add exfiltration (double extortion) and human-operated intrusion phases that precede encryption [R07, R18]. Detection is therefore a race: it has value only in proportion to the data it saves.

### 1.3 Why early detection matters
Because crypto-ransomware effects are irreversible, a detector that fires after encryption begins can at best limit losses. Several primary studies make this explicit by measuring *files lost before detection* or *time-to-detect* (e.g., ~18 files lost per 10,311 user files for RTrap [S26]; 93% of files saved for [S49]; 3–4 s for HiPeR [S24]; 5.31 s average delay for CoLPR [S56]). Early-detection work has also identified a structural difficulty: in the pre-encryption window the available evidence is scarce, so models trained on complete traces do not transfer to it [S04, S08, S11].

### 1.4 Why explainability matters
Ransomware detectors act with high stakes on both sides: a false negative costs data; a false positive kills legitimate processes (backup, compression and encryption tools are *dual-use* by construction [S50]). Security operators must decide whether to trust, override, or tune a detector, and black-box decisions impede this [S06, S42]. Explanations also matter for forensic attribution and for detecting spurious correlations that inflate laboratory accuracy — a well-documented pitfall of ML in security (Arp et al. [M3]). However, explanation methods in security can themselves be unreliable unless evaluated (Warnecke et al. [M4]).

### 1.5 Why real-world deployability matters
A detector is deployable if it runs within acceptable overhead and latency on the target platform, keeps false positives tolerable under benign workloads, and survives the evolution of ransomware (concept drift) and the arrival of new families. Song et al. [R18] argue that "for practical defenses, deployability holds equal significance as detection accuracy", and Ispahany et al. [R14] note that practical solutions for real-world applications remain scarce.

### 1.6 Problem statement
The literature reports detection accuracies routinely above 95–99% (e.g., [S39, S40, S47, S49]), yet ransomware continues to succeed in practice. We hypothesise that the gap lies in *when* detectors fire, *whether their decisions are trustworthy and verifiable*, and *how their evaluations relate to operational conditions*. No existing secondary study, to our knowledge (based on the 18 secondary studies identified by our own search, Section 3), jointly maps ML ransomware detectors by lifecycle stage, explanation quality, and deployment evidence.

### 1.7 Research gap
Existing surveys (Section 3) cover (a) ransomware evolution and broad defence taxonomies [R03, R07, R12], (b) ML/dynamic-analysis detection [R05, R08, R11, R14, R16], (c) early detection specifically [R13, R15], (d) encryption-phase detection [R10], and (e) deployability across defence levels [R18]. None of the 18 secondary studies identified treats **explanation quality** (faithfulness, stability, actionability) as an object of synthesis, and none crosses lifecycle stage × explanation × deployment evidence in a single quality-scored evidence base.

### 1.8 Contributions
1. **A PRISMA 2020-compliant, fully scripted SLR** (2016–2026) restricted to Q1/Q2 journals and top-tier conferences from six major publishers, with every DOI machine-verified, and a published replication package.
2. **A quality-scored evidence table** for 56 studies (and a sensitivity set of 117), with five-criterion scores emphasising dataset realism, reproducibility, explainability and deployment readiness rather than accuracy.
3. **An original taxonomy** (Section 7) crossing four lifecycle stages, input evidence, model family, four **Explanation Levels (XL0–XL4)** and five **Deployment Readiness Levels (DRL0–DRL4)**, which exposes empty cells (e.g., no XL4 or DRL4 study).
4. **Seven evidence-backed research gaps** with concrete future directions (Section 10).

### 1.9 Research questions
- **RQ1:** Which ML and DL techniques are used for ransomware detection, and at which stage of the ransomware attack lifecycle do they operate (pre-execution, at-execution, post-execution, post-encryption)?
- **RQ2:** Which input types, features, and datasets are used for ML-based ransomware detection, and how realistic, diverse, and comparable are they?
- **RQ3:** How is explainability integrated into ML-based ransomware detection systems, and how is explanation quality evaluated (faithfulness, stability, actionability)?
- **RQ4:** What are the main gaps in early detection, explainability, and real-world deployment of ML-based ransomware detection systems?

---

## 2. Background

### 2.1 Ransomware
Ransomware is malware that denies a victim access to a system or data and demands payment for restoration. Two principal classes are distinguished [R07, R09]: **locker** ransomware (denies access to the device/UI) and **crypto-ransomware** (encrypts user files). Contemporary operations add **data exfiltration** (double extortion), **Ransomware-as-a-Service (RaaS)** business models, and **human-operated** intrusion campaigns that precede the payload [S55, R12].

### 2.2 Ransomware attack lifecycle
Surveys propose several lifecycle models: Moussaileb et al. [R03] define *Delivery, Deployment, Destruction, Dealing*; Begovic et al. [R10] propose a crypto-ransomware cyber kill chain centred on the encryption phase. For the purpose of RQ1 we operationalise the four **detection stages** requested by this review, defined by *the evidence available to the detector at decision time*:

| Stage | Definition used in this review | Typical evidence |
|---|---|---|
| **Pre-execution** | Decision made before the sample runs | PE/APK headers, imports, opcodes, byte images |
| **At-execution** (early runtime, pre-encryption) | Decision made during the initial execution window, before bulk encryption | Pre-attack/"paranoia" API calls, early HPC readings, early kernel events, C&C/scan traffic |
| **Post-execution** (during encryption) | Decision made on a substantial or complete behavioural trace, typically while encryption is underway | Full sandbox API/syscall traces, file-I/O, memory dumps, logs |
| **Post-encryption** | Decision made on the *artefacts* of encryption | File entropy/content, storage blocks written, backup/sync streams |

### 2.3 Early detection
Following [S04, S08, S17], we define **early detection** as a correct decision made *before the first user file is irreversibly encrypted* — operationally, at the pre-execution or at-execution stage. Studies that only report *time-to-detect* during encryption are recorded as *loss-limiting* rather than early.

### 2.4 Explainable AI (XAI)
XAI denotes methods that make a model's decision understandable to a human. We distinguish **intrinsic/global** explanations (feature importance, interpretable models), **post-hoc local** explanations (LIME [M2], SHAP [M1], attention), and **uncertainty-aware** outputs that abstain or defer when confidence is low. Following the security-XAI literature [M4], we assess explanation **quality** on three axes: **faithfulness** (does the explanation reflect what the model actually uses?), **stability** (are explanations consistent across similar inputs/runs?), and **actionability** (can an operator act on it — e.g., kill a process, write a rule, tune a threshold?).

### 2.5 Real-world deployability
We define **deployability** as evidence that a detector can operate on its target platform under realistic conditions: (i) false-positive behaviour under benign workloads, (ii) detection latency/data loss, (iii) runtime overhead, (iv) robustness to unseen families and to temporal drift [M5], and (v) execution on real hosts rather than only offline datasets. Section 7 converts this into Deployment Readiness Levels.

### 2.6 Terminology: ML vs DL; static vs dynamic analysis
- **Traditional (classical) ML** (TML): models on engineered features (RF, SVM, kNN, DT, boosting, NB).
- **Deep learning** (DL): representation-learning models — CNN, RNN/LSTM/GRU, Transformers/LLMs, GNNs, autoencoders/GANs/DBNs.
- **Ensembles / hybrid**: combinations of TML and/or DL learners.
- **Static analysis**: features extracted without executing the sample (headers, imports, opcodes, bytes).
- **Dynamic analysis**: features from executing the sample (API/system calls, file-I/O, registry, network, memory, HPC).
- **Hybrid analysis**: both.

---

## 3. Related Work: Existing Surveys and SLRs

Our search retrieved **18 secondary studies** (2019–2026) that meet the same venue criteria as the primary studies (Q1/Q2 journal or top-tier venue, allowed publishers). Table 1 summarises them. "Papers" is the number of studies the authors report having reviewed; *n/s* means not stated in the abstract (the full text should be consulted). Limitations are judged **relative to this review's three foci** (early detection, explainability, deployability); they are not general criticisms.

**Table 1. Secondary studies used for positioning (all [VERIFIED]; full references in §8.2).**

| ID | Authors (year), venue | Scope | Papers | Limitations relative to our foci | How this SLR differs |
|---|---|---|---|---|---|
| R01 | Berrueta et al. (2019), *IEEE Access* | Detection algorithms for crypto-ransomware, classified by input data and decision procedure | n/s | Pre-2019; no XAI or deployment-evidence analysis | Lifecycle-stage mapping; XAI and DRL axes; 2016–2026 |
| R02 | Connolly & Wall (2019), *Computers & Security* | Socio-technical countermeasures from interviews on 26 crypto-ransomware attacks | 26 cases | Not an ML-detection review | ML-specific evidence base |
| R03 | Moussaileb et al. (2021), *ACM CSUR* | Windows ransomware countermeasures across Delivery–Deployment–Destruction–Dealing | n/s | Windows-only; no quality scoring; no explanation analysis | Quality-scored; explanation levels |
| R04 | Sharma et al. (2021), *CCPE* | Android ransomware analysis/detection, 2015–2020 | n/s | Android-only; pre-2021 | Cross-platform; 2016–2026 |
| R05 | Urooj et al. (2021), *Applied Sciences* | Dynamic analysis + ML/DL detection, 2019–2021; datasets | n/s | Narrow window; dynamic-only; no XAI | All stages incl. static/post-encryption |
| R06 | Alqahtani & Sheldon (2022), *Sensors* | Crypto-ransomware detection methodologies; early-detection models and evasion | n/s | No explanation or deployment-readiness grading | Adds both |
| R07 | Oz et al. (2022), *ACM CSUR* | Evolution, taxonomy and defences across PC, mobile, IoT/CPS | 137 (1990–2020) | Broad defence scope; ML-detection quality not graded; ends 2020 | ML-detection focus; 2021–2026 coverage |
| R08 | Smith et al. (2022), *IEEE Access* | ML algorithms/frameworks and datasets in ransomware detection | n/s | No lifecycle-stage or XAI synthesis | Adds stage and XAI |
| R09 | Gómez Hernández et al. (2023), *Electronics* | Crypto-ransomware fundamentals, lifecycle, defence lines | n/s | Narrative; not systematic | PRISMA-based |
| R10 | Begovic et al. (2023), *Computers & Security* | Encryption-phase detection: API/syscalls, I/O, file-system monitoring | n/s | Focus on encryption phase; early stages out of scope | Covers pre- and at-execution |
| R11 | Alraizza & Algarni (2023), *BDCC* | ML ransomware detection, 2017–2022 | n/s | No quality appraisal; no XAI evaluation | Both |
| R12 | Razaulla et al. (2023), *IEEE Access* | Evolution, taxonomy; detection/prevention/mitigation/prediction | >150 refs | Identifies concept drift & real-time protection gaps but does not grade evidence | Grades drift/novelty/deployment per study |
| R13 | Albshaier et al. (2024), *Information* | SLR on early ransomware detection, 2020–2024 | n/s | Early detection only; includes industry reports; no XAI quality | Venue-restricted; XAI axis |
| R14 | Ispahany et al. (2024), *IEEE Access* | ML detection design; real-time and early detection practicalities | n/s | No explanation-quality synthesis | Adds XL axis |
| R15 | Cen et al. (2024), *Computer Networks* | Survey of ransomware early detection | n/s (abstract not openly available) | Early detection only | Joint early × XAI × deployment |
| R16 | Alzahrani et al. (2025), *IEEE Access* | Detection methods 2019–2025 (Windows/Android); datasets; RaaS | 135 screened, 45 analysed | No quality instrument; no explanation evaluation | Both |
| R17 | Selvaraj et al. (2025), *Computer Science Review* | SLR on threat-intelligence mitigation for IoMT ransomware | n/s | Domain-specific; mitigation framework | General ML detection |
| R18 | Song et al. (2026), *ACM CSUR* | 117 defence works by implementation level; deployability; commercial defences tested | 117 | Deployability addressed, but explainability is not a synthesis axis | Adds explanation-quality axis and per-study DRL |

**Positioning.** Two recent works overlap most with ours: Song et al. [R18] (deployability) and Albshaier et al. [R13] / Cen et al. [R15] (early detection). We therefore do **not** claim to be the first review of either topic. What is distinct here is the **joint** treatment — lifecycle stage × explanation level × deployment readiness — over a **quality-scored, venue-restricted** corpus, and the explicit synthesis of **how explanation quality is (not) evaluated** (RQ3), which none of the 18 secondary studies treats as an object of analysis (based on their abstracts; R15's abstract was not available for checking).

---

## 4. Methodology (PRISMA 2020)

The review follows PRISMA 2020 [M6] and Kitchenham's SLR guidelines for software engineering [M7]. All steps are scripted (`slr/scripts/`), and all intermediate data are archived (`slr/data/`).

### 4.1 Search strategy and sources
**Primary source — Crossref REST API.** Crossref is the DOI registration agency for IEEE, ACM, Elsevier, Springer Nature, MDPI and Wiley, so it indexes the metadata of every allowed publisher in one place and returns resolvable DOIs (which is what the verification requirement needs). Query mode: `query.bibliographic`; filter `from-pub-date:2016-01-01, until-pub-date:2026-12-31`; first 200 results per string (two pages of 100), ranked by relevance; records kept only if the **title** contains "ransom".

**Exact search strings executed (27):**
```
ransomware detection machine learning        | ransomware detection deep learning
early ransomware detection                   | ransomware early detection pre-encryption
crypto-ransomware detection behavioral       | ransomware detection explainable artificial intelligence
ransomware detection SHAP LIME explainability| ransomware classification API calls
ransomware detection network traffic machine learning
ransomware detection hardware performance counters
ransomware detection file system I/O machine learning
ransomware detection entropy machine learning| android ransomware detection machine learning
IoT ransomware detection deep learning       | ransomware detection opcode static analysis
ransomware detection memory forensics machine learning
ransomware detection transformer LSTM        | ransomware detection graph neural network
ransomware detection federated learning      | ransomware detection survey
ransomware systematic literature review      | ransomware detection storage SSD machine learning
zero-day ransomware detection                | ransomware family classification
ransomware detection concept drift           | ransomware detection cloud virtual machine
ransomware detection industrial control systems
```

**Database-specific Boolean strings (for replication in IEEE Xplore, ACM DL, ScienceDirect, SpringerLink, MDPI, Wiley, Scopus, Web of Science).** These are provided for replication and for a planned update; **they were not executed in this run** because those portals were not reachable from the review environment (Section 12.1). Scopus syntax:
```
TITLE-ABS-KEY ( ransomware* OR "crypto-ransomware" OR "locker ransomware" )
AND TITLE-ABS-KEY ( "machine learning" OR "deep learning" OR "neural network" OR classifier
     OR "random forest" OR "support vector" OR lstm OR cnn OR transformer OR "graph neural"
     OR "federated learning" OR "reinforcement learning" OR "zero-shot" OR "few-shot" )
AND TITLE-ABS-KEY ( detect* OR classif* OR identif* OR predict* )
AND PUBYEAR > 2015 AND PUBYEAR < 2027
AND ( LIMIT-TO ( DOCTYPE , "ar" ) OR LIMIT-TO ( DOCTYPE , "cp" ) OR LIMIT-TO ( DOCTYPE , "re" ) )
AND NOT TITLE-ABS-KEY ( phishing OR "incident response" )
```
Web of Science: `TS=(ransomware*) AND TS=("machine learning" OR "deep learning" OR "neural network" OR classifier) AND TS=(detect* OR classif*) AND PY=(2016-2026) NOT TS=(phishing)`. IEEE Xplore (Command Search): `("All Metadata":ransomware) AND ("All Metadata":"machine learning" OR "All Metadata":"deep learning" OR "All Metadata":"neural network") AND ("All Metadata":detection)` with Year 2016–2026.

**Supplementary search.** Backward snowballing and known-item searching from the surveys: 23 title look-ups plus 2 DOI look-ups (25 records) targeting foundational top-tier works (e.g., ShieldFS, RWGuard, Peeler, FlashGuard, Redemption, UNVEIL, CryptoDrop, EldeRan) and highly cited journal papers.

### 4.2 Inclusion criteria
- **IC1** Peer-reviewed journal article or full conference paper, published 2016–2026.
- **IC2** Proposes, or empirically evaluates, an ML or DL model whose purpose is detecting or classifying ransomware (or ransomware activity).
- **IC3** Venue is a Q1/Q2 journal (SJR, Computer Science or relevant subject category) from IEEE, ACM, Elsevier, Springer Nature, MDPI or Wiley, **or** a main-track paper at IEEE S&P, USENIX Security, CCS, NDSS, ACSAC, DIMVA, RAID, ESORICS, ICSE, ASE, FSE, ICASSP, GLOBECOM, DSN or INFOCOM.
- **IC4** Written in English, with an abstract and a resolvable DOI.

### 4.3 Exclusion criteria
- **EC1** Preprints, theses, book chapters (except LNCS main-track proceedings of the listed conferences), posters, workshops, magazines, editorials.
- **EC2** arXiv-only works (unless foundational and widely cited — none was needed because the foundational works found had peer-reviewed versions).
- **EC3** Out of scope: phishing; SOC incident-response process; adversarial evasion/attack papers; ransom-*payment*/blockchain transaction analytics; generic malware without ransomware-specific evaluation.
- **EC4** No trained ML/DL model (purely rule/threshold/heuristic, honeyfile, access-control or forensic characterisation).
- **EC5** Secondary studies (routed to Related Work).
- **EC6** Publisher outside the six listed, or journal below Q2 / not in the whitelist.
- **EC7** Duplicate or superseded version of an included study.
- **EC8** Quality score < 4/10 (Section 4.6).

### 4.4 Venue whitelist
Journals judged Q1/Q2 in SJR at the time of writing and present in the corpus include (non-exhaustive): *IEEE Access, IEEE TIFS, IEEE TDSC, IEEE TC, IEEE TCAD, IEEE TNSM, IEEE TNSE, IEEE TCE, IEEE IoT-J, IEEE TETC, ACM CSUR, Digital Threats: Research and Practice, Computers & Security, Expert Systems with Applications, FGCS, JNCA, Computer Networks, JISA, JKSU-CIS, ICT Express, Egyptian Informatics Journal, Applied Soft Computing, Computers & Electrical Engineering, EAAI, FSI: Digital Investigation, Computer Science Review, International Journal of Information Security, JCVHT, Cluster Computing, The Journal of Supercomputing, Applied Intelligence, Wireless Personal Communications, Multimedia Tools and Applications, Scientific Reports, Concurrency and Computation: Practice and Experience, Security and Communication Networks, Sensors, Applied Sciences, Electronics, Information, Future Internet, Mathematics, Big Data and Cognitive Computing.* The full machine-readable list is in `slr/scripts/screen.py`. **Quartiles vary by year and subject category; every included journal's quartile for its publication year must be re-confirmed on scimagojr.com before submission** (Section 12.1).

### 4.5 Screening process
1. **Identification:** automated Crossref harvest + snowballing.
2. **Record-type and venue screening** (automated, `screen.py`): journal articles in the whitelist; proceedings whose container title matches the top-tier conference list.
3. **Title/abstract screening** (manual, against IC/EC).
4. **Eligibility assessment** on full abstract and metadata (Crossref + Semantic Scholar; abstracts withheld by some publishers were filled from Semantic Scholar TLDRs where available — these 17 included studies are flagged *CANDIDATE coding*).
5. **Quality assessment** and application of EC8.

Screening was performed by a single reviewer with the automated rules acting as a consistent first pass; Section 12.1 discusses this limitation and the recommended dual-reviewer κ check.

### 4.6 Quality assessment criteria
Each eligible study was scored 0 (absent/inadequate), 1 (partial) or 2 (strong) on five criteria (maximum 10):

| Code | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| **DR** | Dataset realism | Synthetic/generic IDS data (e.g., KDD-derived) or tiny sample | Real ransomware samples, sandbox/VM only, limited families | Large/diverse family set, real hosts or bare metal, benign workloads realistic |
| **ER** | Evaluation rigour | Single random split, accuracy only | Cross-validation, multiple metrics incl. FPR/FNR | Unseen-family or temporal split, baselines, ablation or statistical testing |
| **RP** | Reproducibility | Private data, insufficient detail | Public dataset *or* detailed protocol | Public dataset **and** released data/code or open benchmark |
| **EX** | Explainability | None | Global feature importance / interpretable features / uncertainty | Local post-hoc or interpretable-by-design explanations presented as a contribution |
| **DP** | Deployment readiness | Offline accuracy only | One of: latency, FPR under benign load, overhead, real-time claim with evidence | Prototype on live host with latency **and** overhead/files-lost measurement |

The inclusion threshold (**≥4/10**) was fixed before scoring. A sensitivity analysis over all 117 eligible studies is reported alongside the main results.

### 4.7 Data extraction form
For every eligible study: bibliographic data (authors, title, venue, year, DOI); platform (Windows, Android, Linux, cloud/VM, IoT/IIoT/ICS, storage, network); **lifecycle stage(s)** (PRE/AT/POST/ENC); **input types** (PE, APK, opcode, API, kernel/syscall/IRP, file-I/O, storage, memory, HPC, network, entropy/content, logs, TTP, registry); **model family** (TML, CNN, RNN, Transformer/LLM, GNN, generative, RL, FL, zero/few-shot, unsupervised, ensemble); **XAI technique** (feature importance, SHAP, LIME, attention, interpretable-by-design, uncertainty, visual analytics); **XAI evaluation** (none / qualitative / quantitative metric); **evaluation flags** — public data (P), unseen-family test (U), temporal/drift test (T), latency/time-to-detect (L), runtime overhead (O), real hosts or production traffic (R), FPR reported (F), explicit early-detection objective (E); the five QA scores; and extraction basis (full abstract vs TLDR/metadata). The coded form is `slr/scripts/extract.py`.

### 4.8 PRISMA flow (textual description of Figure 1)

```
IDENTIFICATION
  Records from Crossref (27 strings, title contains "ransom", de-duplicated by DOI) ........ n = 1,158
  Records from snowballing / known-item search ............................................ n = 25
SCREENING
  Removed by record type (posted content 255, book chapters 111, other 19) ................ n = 385
  Records screened on venue (journal whitelist / top-tier conference list) ............... n = 773
    Excluded: venue not Q1/Q2-whitelisted, publisher not allowed, or not a top-tier conference  n = 599
  Records screened on title/abstract ...................................................... n = 174
    Excluded (EC1 workshop/poster, EC3 out of scope: payments, phishing, evasion; EC4) ...... n = 33
  Added from snowballing after the same checks (14 of 25 failed venue/type checks) ....... n = 11
ELIGIBILITY
  Reports assessed for eligibility ......................................................... n = 152
    Secondary studies routed to Related Work (EC5) ......................................... n = 18
    Primary candidates excluded with reasons (EC3 2, EC4 12, EC5 2*, EC6 1) ................ n = 17
  Eligible primary studies (sensitivity set) ............................................... n = 117
QUALITY GATE
    Excluded for QA score < 4 (EC8) ........................................................ n = 61
INCLUDED
  Primary studies in synthesis ............................................................. n = 56
  Secondary studies for positioning ........................................................ n = 18
```
\*A narrative review [Future Internet 2023] and a discussion paper first coded as primary were re-routed; the exclusion log with reasons and DOIs is Table 10.

---

## 5. Results

### 5.0 Corpus overview
**Publication years (n = 56):** 2016: 1 · 2018: 2 · 2019: 3 · 2020: 3 · 2021: 3 · 2022: 9 · 2023: 7 · 2024: 7 · 2025: 10 · 2026: 11. Of the included studies, 44 (79%) appeared from 2022 onwards. **Platforms:** Windows 43 (77%); network-level 4; Android 3; cloud/VM 2; fog, multi-OS, cross-OS and enterprise/TTP 1 each. In the 117-study sensitivity set Windows is 67% and Android 9%, so the quality gate removed proportionally more Android, cloud and IoT studies — a first signal that evaluation quality is weakest outside Windows.

Table 2 (per-study extraction) and Table 8 (quality scores) are given in full below; Sections 5.1–5.4 synthesise them.

**Table 2. Data extraction for the 56 included primary studies.** Stage: Pre-exec / At-exec / Post-exec / Post-enc. Input codes: PE, APK, OPC (opcodes/assembly), API, KRN (kernel/syscall/IRP), FIO (file-system I/O), STO (block storage), MEM, HPC, NET, ENT (file entropy/content), LOG (Sysmon/ETW/IDS), REG (registry), TTP, MULTI. Models: TML (classical ML), ENS (ensemble), CNN, RNN, TRF (Transformer/LLM), GEN (AE/GAN/DBN), ZSL, FL, UNS. XAI: FI (feature importance), SHAP, LIME, ATT (attention), UQ (uncertainty), INT (interpretable-by-design).

| ID | Year | Venue | Stage | Input | Model | XAI | Deployment evidence |
|---|---|---|---|---|---|---|---|
| S01 | 2016 | ACSAC 2016 | Post-exec | FIO | TML | — | real/bare-metal or production-like env.; latency; overhead; FPR |
| S02 | 2018 | RAID 2018 (LNCS 11050) | Post-exec | FIO, KRN | TML | — | latency; overhead |
| S03 | 2018 | Expert Systems with Applications | Post-exec | MEM | TML | — | real/bare-metal or production-like env. |
| S04 | 2019 | Future Generation Computer Systems | At-exec | API | ENS | — | early-detection goal |
| S05 | 2019 | Future Generation Computer Systems | Post-exec | API | CNN, RNN | — | unseen-family test |
| S06 | 2019 | Computers & Security | Pre-exec | APK, API | TML | FI | public data; temporal/drift test |
| S07 | 2020 | Applied Sciences | Pre-exec, Post-exec | PE, API | ENS, TML | — | real/bare-metal or production-like env. |
| S08 | 2020 | IEEE Access | At-exec | API | TML | — | early-detection goal |
| S09 | 2020 | IEEE Transactions on Emerging Topics i | Post-exec | API | TML | FI | — |
| S10 | 2021 | ESORICS 2021 (LNCS 12972) | At-exec, Post-exec | KRN | TML | — | latency; FPR |
| S11 | 2021 | Future Generation Computer Systems | At-exec | API | TML | FI | early-detection goal |
| S12 | 2021 | Information | Post-exec | NET | ENS | — | public data |
| S13 | 2022 | Journal of Computer Virology and Hacki | Post-exec | MEM | TML | — | real/bare-metal or production-like env. |
| S14 | 2022 | Applied Soft Computing | Post-exec | API, FIO, REG | TML | FI | — |
| S15 | 2022 | Expert Systems with Applications | Post-exec | NET, FIO | TML | — | real/bare-metal or production-like env.; FPR |
| S16 | 2022 | IEEE Transactions on Computers | At-exec, Post-exec | HPC | CNN | — | — |
| S17 | 2022 | Journal of King Saud University - Comp | At-exec | API | TML | FI | early-detection goal |
| S18 | 2022 | Computers & Security | Post-exec | API | TML | FI | temporal/drift test |
| S19 | 2022 | Forensic Science International: Digita | Post-exec, Post-enc | STO | TML | — | public data; real/bare-metal or production-like env. |
| S20 | 2022 | Applied Sciences | Post-exec | API | TML, CNN | — | FPR |
| S21 | 2022 | Applied Intelligence | Post-exec | API | GEN, ZSL, ENS | — | unseen-family test |
| S22 | 2023 | Sensors | Post-exec | API, REG, FIO | TML | — | public data |
| S23 | 2023 | GLOBECOM 2023 - 2023 IEEE Global Commu | Post-exec | API | FL, TML | — | public data |
| S24 | 2023 | Digital Threats: Research and Practice | At-exec | HPC | TML | — | latency; early-detection goal |
| S25 | 2023 | Computers & Security | Pre-exec | PE | CNN | — | public data; unseen-family test |
| S26 | 2023 | IEEE Transactions on Information Foren | Post-exec | FIO | TML | — | latency |
| S27 | 2023 | International Journal of Information S | Pre-exec, At-exec | PE, API | TML | — | early-detection goal |
| S28 | 2023 | Information | Pre-exec | APK | TML | — | temporal/drift test |
| S29 | 2024 | IEEE Access | At-exec | API | GEN | FI | temporal/drift test; early-detection goal |
| S30 | 2024 | Future Internet | At-exec | API | CNN, RNN | — | latency; early-detection goal |
| S31 | 2024 | Computers & Security | Post-exec | API | TML | FI | temporal/drift test |
| S32 | 2024 | IEEE Transactions on Information Foren | At-exec, Post-exec | KRN, FIO | TML | — | latency; FPR; early-detection goal |
| S33 | 2024 | IEEE Access | At-exec | HPC | TML, CNN | FI | real/bare-metal or production-like env.; latency |
| S34 | 2024 | Computers & Security | Post-exec | API | CNN | SHAP, LIME | — |
| S35 | 2024 | Computers & Security | Pre-exec | PE | ZSL | — | unseen-family test; early-detection goal |
| S36 | 2025 | Proceedings 2025 Network and Distribut | Post-exec, Post-enc | FIO, ENT | TML | — | unseen-family test; FPR; latency; overhead; early-detection goal |
| S37 | 2025 | IEEE Access | Post-exec, Post-enc | STO | TML, CNN | SHAP, UQ | public data |
| S38 | 2025 | Computers & Security | Post-exec, Post-enc | STO, MEM | CNN, RNN | — | public data; real/bare-metal or production-like env. |
| S39 | 2025 | Electronics | Pre-exec, Post-exec | PE, API | TRF | — | — |
| S40 | 2025 | The Journal of Supercomputing | Pre-exec | PE | CNN | — | — |
| S41 | 2025 | International Journal of Information S | Post-exec | FIO | TML | — | latency |
| S42 | 2025 | IEEE Access | Post-exec | LOG, FIO | TML | SHAP, LIME | FPR |
| S43 | 2025 | Computers & Security | At-exec, Post-exec | OPC | TRF | — | unseen-family test |
| S44 | 2025 | Applied Sciences | Pre-exec | PE | ENS | — | public data; unseen-family test |
| S45 | 2025 | IEEE Access | Post-exec | LOG | CNN, RNN | — | temporal/drift test; FPR; latency |
| S46 | 2026 | Sensors | At-exec | API | RNN | ATT | FPR; early-detection goal |
| S47 | 2026 | Scientific Reports | Post-exec | NET | ENS | FI | public data |
| S48 | 2026 | IEEE Access | At-exec, Post-exec | API, ENT, REG | ENS, GEN, RNN | FI | latency; FPR |
| S49 | 2026 | Applied Sciences | Post-exec | API | TML, RNN, ENS | — | public data; unseen-family test; latency; overhead |
| S50 | 2026 | Scientific Reports | Pre-exec | PE | TML | UQ | FPR |
| S51 | 2026 | Concurrency and Computation: Practice  | At-exec | API | TRF, CNN, RNN | ATT | early-detection goal |
| S52 | 2026 | Scientific Reports | Post-exec | NET | ENS | SHAP, LIME | public data |
| S53 | 2026 | IEEE Access | At-exec | LOG, NET | TML | SHAP | temporal/drift test; latency; FPR |
| S54 | 2026 | ICASSP 2026 - 2026 IEEE International  | Pre-exec | PE, OPC | TRF | INT | — |
| S55 | 2026 | Digital Threats: Research and Practice | At-exec | TTP | RNN | — | early-detection goal |
| S56 | 2026 | IEEE Transactions on Information Foren | Post-exec | KRN | UNS | — | unseen-family test; latency; overhead |

### 5.1 RQ1 — Techniques and lifecycle stage

**Stage distribution (multi-label, n = 56).** Post-execution 35 (63%); at-execution 18 (32%); pre-execution 11 (20%); post-encryption 4 (7%). By exact combination: post-execution only 24; at-execution only 12; pre-execution only 8; at+post 5; post+post-encryption 4; pre+post 2; pre+at 1. *Sensitivity (n = 117):* post 69 (59%), pre 30 (26%), at 28 (24%), post-encryption 10 (9%).

**Table 3. Model families by lifecycle stage (counts of study–stage pairs; a study can contribute to several cells).**

| Model family | Pre-exec | At-exec | Post-exec | Post-enc | Representative studies |
|---|---|---|---|---|---|
| Classical ML (RF, SVM, kNN, DT, boosting) | 5 | 9 | 22 | 3 | [S01, S17, S32, S33, S42, S53] |
| Ensembles (bagging/stacking/voting) | 2 | 2 | 7 | – | [S04, S07, S44, S47] |
| CNN (incl. image-based) | 2 | 4 | 7 | 2 | [S16, S25, S30, S40] |
| RNN / LSTM / GRU | – | 5 | 5 | 1 | [S05, S45, S46, S55] |
| Transformer / LLM | 2 | 2 | 2 | – | [S39, S43, S51, S54] |
| Generative (AE / GAN / DBN) | – | 2 | 2 | – | [S21, S29] |
| Zero-shot learning | 1 | – | 1 | – | [S21, S35] |
| Federated learning | – | – | 1 | – | [S23] |
| Unsupervised / self-supervised | – | – | 1 | – | [S56] |

**Findings.**
1. **Classical ML remains the most frequent model family (32/56, 57%)**, including several of the strongest systems by deployment evidence — Ranker's lightweight kernel-level detector (99.43% F1, 0.11% FP across 68 families) [S32], ShieldFS [S01], RWGuard [S02], Peeler [S10] and the HPC classifier on bare metal [S33]. Tree-based models dominate at the at-execution stage, where low latency is essential.
2. **DL adoption accelerated after 2021**: CNNs (12), RNNs (9), and since 2024 Transformers/LLMs (4: RansomFormer [S39], Pulse [S43], API-RED [S51], PE-Sleuth [S54]). DL appears mostly on *sequence* inputs (API calls, assembly) and on *imaged* inputs (PE headers as images [S25]; HPC "images" [S16]).
3. **At-execution detection is a distinct research line** with its own techniques: dynamic pre-encryption boundary delineation [S08], incremental bagging over attack phases [S04], redundancy-aware mutual-information feature selection for scarce early data [S11], GAN-based augmentation for early behavioural drift [S29], attention over early API windows [S46, S51], HPC signals within 2–4 s [S24, S33], and pre-attack/early kernel events [S32]. A recurring finding is that *data scarcity in the early window* — not model capacity — is the main obstacle [S04, S11, S29].
4. **Pre-execution (static) detection** is presented as fast and evasion-resilient by PE-header and opcode studies [S25, S35, S44] but faces packing and dual-use ambiguity: [S50] documents systematic false positives from legitimate cryptographic software and proposes confidence-gated mitigation.
5. **Post-encryption detection** is rare (4/56) and is always combined with post-execution behaviour (storage access patterns [S19, S38, S37]; content analysis of written files in ERW-Radar [S36]). Its purpose is loss limitation and recovery rather than prevention.
6. **New paradigms** — zero-shot [S21, S35], federated [S23], self-supervised contrastive system-wide detection under multi-application interference [S56], and TTP-sequence learning for human-operated ransomware [S55] — are present but each is represented by one or two studies.

### 5.2 RQ2 — Inputs, features and datasets

**Table 4. Input evidence (multi-label, n = 56).**

| Input | Studies | % | Dominant stage | Examples |
|---|---|---|---|---|
| API / system-API calls | 24 | 43% | Post / At | [S04, S08, S30, S34, S49, S51] |
| File-system I/O | 10 | 18% | Post | [S01, S02, S26, S32, S42] |
| PE header / imports / bytes | 9 | 16% | Pre | [S25, S35, S40, S44, S50] |
| Network traffic | 5 | 9% | Post / At | [S12, S15, S47, S52, S53] |
| Kernel / syscall / IRP | 4 | 7% | At / Post | [S10, S32, S56] |
| Memory (VM/RAM) | 3 | 5% | Post | [S03, S13, S38] |
| Hardware performance counters | 3 | 5% | At | [S16, S24, S33] |
| Block-storage access patterns | 3 | 5% | Post / Post-enc | [S19, S37, S38] |
| Host logs (Sysmon/ETW/IDS) | 3 | 5% | Post / At | [S42, S45, S53] |
| Registry | 3 | 5% | Post | [S14, S22, S48] |
| APK / Android API | 2 | 4% | Pre | [S06, S28] |
| File entropy / content | 2 | 4% | Post-enc | [S36, S48] |
| Opcodes / assembly | 2 | 4% | Pre / At | [S43, S54] |
| ATT&CK TTP sequences | 1 | 2% | At | [S55] |

**Datasets.** Public datasets are used or released by only **12/56 (21%)** studies. Recurrent public resources in the corpus are: **RanSAP** (storage access patterns) [S19] and its successor **RanSMAP** (storage + memory) [S38], both collected through a thin hypervisor; **UGRansome** (network flows) [S12], later re-used by [S47]; the **dynamic feature dataset** of Herrera-Silva & Hernández-Álvarez [S22]; a PE-header dataset of 1,023 ransomware samples in 25 families released by [S25]; the API-call *ransomwaredataset2016* used by FLDetect [S23]; and CIC-family datasets (e.g., CIC-Ransomware-2017 in [S48]). Dataset sizes range from a few hundred executables (e.g., 678 in [S51]; ≈1,500 in [S20]) to 39,378 ransomware samples [S46] and >150 families [S39].

**Realism.** Mean DR score is 1.36/2. Most dynamic datasets are collected in sandboxes or VMs with short runs. Studies that collect on **real hosts / bare metal / production-like environments** are a minority (8/56, 14%): e.g., ShieldFS on real user machines [S01], HPC traces on non-virtualised hardware [S33], private-cloud VM memory [S03, S13], hypervisor-collected storage/memory traces [S19, S38], and semi-realistic plus realistic environments in [S07]. Evidence of representativeness of the *benign* class (realistic user workloads, encryption/compression tools, backups) is rarely reported; [S50] and [S56] are notable exceptions.

**Diversity and recency.** [S28] shows empirically that Android models trained on new ransomware fail on old samples and vice versa (dataset span 2008–2020), demonstrating that *dataset age* is a confounder. Only **7/56 (13%)** studies perform any temporal or drift evaluation [S06, S18, S28, S29, S31, S45, S53].

**Comparability.** Studies are generally **not comparable**: metrics differ (accuracy, F1, recall, F2, MCC; [S20] shows that precision-centric reporting hides false negatives, and [S45] introduces a Weighted Efficiency Score), split protocols differ (random k-fold dominates; unseen-family splits appear in 9/56, 16%), and the early-detection *window* is defined inconsistently (fixed time thresholds vs. dynamically delineated pre-encryption boundaries [S08]).

### 5.3 RQ3 — Explainability and its evaluation

**Prevalence.** **20/56 (36%)** included studies contain any explainability component (28/117, 24%, in the sensitivity set). Distribution: global feature importance 11; SHAP 5; LIME 3; uncertainty quantification 2; attention 2; interpretable-by-design 1 (multi-labelled). Attention-based models are counted only when the attention weights are presented as an interpretability aid; attention used purely for accuracy or throughput (e.g., [S45]) is not counted.

**Table 5. Explainability in the included studies.**

| Explanation Level (Section 7) | Studies | Mechanism | How it is evaluated |
|---|---|---|---|
| **XL1** Global importance / interpretable features | S06, S09, S11, S14, S17, S18, S29, S31, S33, S47, S48 | Feature ranking, discriminative API lists (e.g., 14 pre-encryption APIs in [S17]), frequent behavioural patterns [S09], HPC event ranking [S33] | Qualitative discussion only |
| **XL2** Local post-hoc / attention | S34, S42, S46, S51, S52, S53 | SHAP + LIME on dynamic sequences [S34], ETW-log models [S42], network-traffic ensembles [S52]; SHAP on logistic regression over IDS logs [S53]; attention weights [S46, S51] | Qualitative case illustrations; no quantitative metric |
| **XL3** Interpretable-by-design / uncertainty-gated | S37, S50, S54 | SHAP + Monte-Carlo-dropout uncertainty with deferral to analyst [S37]; confidence-gated decisions to curb dual-use false positives [S50]; LLM program-level semantics for interpretable static detection [S54] | Uncertainty is evaluated as *detection* quality (abstention, FP reduction), not explanation quality |
| **XL4** Explanations evaluated for faithfulness, stability or actionability | **none** | – | – |

**Finding RQ3.1 — no explanation-quality evaluation.** Across all 20 studies with XAI (and all 28 in the sensitivity set), **no abstract reports a quantitative evaluation of explanation faithfulness (e.g., deletion/insertion fidelity), stability (e.g., explanation agreement across runs, seeds or near-duplicate samples), or actionability (e.g., analyst studies, time-to-decision, rule derivation)**. Explanations are presented as plots or narrative case studies. This is the central RQ3 result. Because extraction relied on abstracts, the XAI subset should be re-verified against full texts (Section 12.1); however, a quantitative explanation-evaluation contribution would ordinarily be stated in an abstract.

**Finding RQ3.2 — explainability is mostly post-hoc and post-execution.** Of the 20 XAI studies, 11 operate at an early stage (pre- or at-execution) [S06, S11, S17, S29, S33, S46, S48, S50, S51, S53, S54], but only **3 combine XAI with measured latency** [S33, S48, S53], and only **one combines local explanations (XL ≥ 2) with deployment evidence (DRL ≥ 2)** [S53].

**Finding RQ3.3 — uncertainty is the emerging bridge between XAI and deployment.** [S37] and [S50] use calibrated uncertainty to defer ambiguous cases to analysts, directly addressing the dual-use problem, and [S53] explicitly frames pre-encryption network behaviour as an *early anomaly warning* rather than definitive evidence, adding temporally separated evaluation and McNemar testing. These designs are closest to actionability, yet none measures it.

### 5.4 RQ4 — Gaps in early detection, explainability and deployment (evidence summary)

**Table 6. Deployment evidence in the included studies (n = 56).**

| Evidence | n | % | Studies |
|---|---|---|---|
| Explicit early-detection objective (E) | 14 | 25% | S04, S08, S11, S17, S24, S27, S29, S30, S32, S35, S36, S46, S51, S55 |
| FPR reported (F) | 12 | 21% | S01, S10, S15, S20, S32, S36, S42, S45, S46, S48, S50, S53 |
| Latency / time-to-detect / files lost (L) | 15 | 27% | S01, S02, S10, S24, S26, S30, S32, S33, S36, S41, S45, S48, S49, S53, S56 |
| Runtime overhead (O) | 5 | 9% | S01, S02, S36, S49, S56 |
| Real hosts / bare metal / production-like environment (R) | 8 | 14% | S01, S03, S07, S13, S15, S19, S33, S38 |
| Unseen-family / zero-day split (U) | 9 | 16% | S05, S21, S25, S35, S36, S43, S44, S49, S56 |
| Temporal / drift evaluation (T) | 7 | 13% | S06, S18, S28, S29, S31, S45, S53 |
| **Both U and T** | **0** | **0%** | – |
| Public dataset (P) | 12 | 21% | S06, S12, S19, S22, S23, S25, S37, S38, S44, S47, S49, S52 |

**Quality profile.** Mean QA scores (0–2): DR 1.36 · ER 1.73 · RP 0.77 · **EX 0.45** · DP 0.89; mean total 5.2/10. Explainability and reproducibility are the weakest dimensions. Only **11/56 (20%)** studies reach DP = 2 (prototype with latency and overhead/files-lost evidence): S01, S02, S10, S26, S32, S36, S41, S45, S48, S49, S56.

The gaps are synthesised and justified in Section 10.

---

## 6. Discussion

### 6.1 Key findings
1. **The field detects late.** Nearly two-thirds of detectors decide on post-execution traces; only a third target the pre-encryption window, and a fifth decide before execution.
2. **Accuracy saturation hides operational weakness.** Reported accuracies of 97–99.9% coexist with an average deployment-readiness score below 1/2, with 9% of studies measuring overhead and none performing longitudinal field validation.
3. **Explainability is decorative rather than evaluated.** 36% of studies include XAI; none evaluates explanation quality.
4. **Generalisation is under-tested.** Unseen-family and temporal evaluations are each rare, and never combined.
5. **Windows monoculture.** 77% of included studies target Windows; mobile, cloud, IoT/ICS and storage-level studies are more frequently excluded by the quality gate.

### 6.2 Cross-study comparison
*Early vs. late, kernel vs. API.* The highest-evidence early detectors work **below the API layer**: kernel-level behaviour (Ranker [S32], Peeler [S10]), HPC (HiPeR [S24], [S33]), and file-system filter drivers (ShieldFS [S01], RWGuard [S02]). User-mode API-sequence detectors dominate numerically but are mostly evaluated offline on sandbox traces. HiPeR explicitly motivates HPC by noting that contemporary ransomware uses low-level system calls to circumvent API monitoring [S24].

*Classical vs. deep.* On API windows, Davidian et al. find CNN and LSTM best, with a context window of 7 calls and real-time suitability [S30]; on similar API data, AlMajali et al. find an ensemble best and measure files saved and overhead [S49]; Ranker reaches 0.11% FP with a lightweight classical detector at kernel level [S32]. The evidence does not support a general superiority of DL; it supports **better evidence sources** (kernel, HPC, storage) over bigger models.

*Static vs. dynamic.* Static PE-header approaches report high accuracy and resilience [S25, S35, S44] but are contradicted on false-positive behaviour by [S50]; Pulse argues that genuine behaviour must be captured through dynamic binary instrumentation to defeat evasive samples [S43].

### 6.3 Contradictions in the literature
- **"Static analysis is evasion-resilient"** [S25] vs. **dual-use false positives and packing** [S50].
- **"High accuracy on held-out data implies readiness"** vs. **dataset-age effects** [S28] and **precision-centric reporting that hides FNs** [S20].
- **"HPC are reliable early signals"** [S24, S33] vs. **HPC non-determinism** that DeepWare must explicitly engineer around [S16].
- **Process-level detection** (most studies) vs. **system-wide attacks distributed over benign processes**, which make process-level detection ineffective according to [S56].
- **Fixed time thresholds for "early"** vs. **sample-specific pre-encryption boundaries** [S08].

### 6.4 Limitations of existing work
Short sandbox runs; benign classes without realistic encryption/compression/backup workloads; random k-fold splits that leak family information; no shared early-detection window definition; overhead rarely measured; code and trained models rarely released (not systematically extractable from abstracts; see §12); explanations not evaluated.

### 6.5 Emerging trends
- Transformers and LLMs on API sequences and assembly [S39, S43, S51, S54].
- Zero-/few-shot and generative augmentation for novelty and early-data scarcity [S21, S29, S35].
- Concept-drift-aware and incremental learning [S18, S31, S45].
- Uncertainty-aware detection with analyst deferral [S37, S50].
- Open storage/memory datasets from hypervisors [S19, S38].
- System-wide and human-operated-ransomware detection [S55, S56].
- Privacy-preserving / federated detection [S23].

### 6.6 Future directions (summary; detailed in Section 10)
A shared **early-detection benchmark** with sample-specific pre-encryption boundaries and files-lost metrics; **explanation-quality evaluation** protocols (faithfulness, stability, actionability) adapted from security-XAI work [M4]; **TESSERACT-style** time-aware and family-aware splits [M5] as a reporting standard; **bare-metal and enterprise-workload** benign corpora; and **deployment-readiness reporting** (overhead, latency, FPR per benign hour).

---

## 7. Taxonomy: SEED-R (Stage–Evidence–Explanation–Deployment for Ransomware detection)

We propose an original five-axis taxonomy. Axes 1–3 classify *how* a detector works; axes 4–5 grade *how trustworthy and deployable* it is. Each study is a point in this space, which turns the review's findings into visible empty cells.

**Figure 2 (described as a table). SEED-R taxonomy.**

| Axis | Levels | Definition |
|---|---|---|
| **1. Lifecycle stage** | PRE · AT · POST · ENC | When the decision is made (Section 2.2) |
| **2. Evidence source** | Static artefact (PE/APK/opcode) · User-mode behaviour (API, registry, logs) · Kernel/storage (syscalls, IRP, file-I/O, block I/O) · Hardware (HPC) · Memory · Network · Content (entropy) · Adversary-behaviour (TTP) | What the model observes |
| **3. Model family** | Classical ML · Ensemble · CNN · RNN · Transformer/LLM · GNN · Generative · Zero/few-shot · Federated · Self-/unsupervised · RL | How it learns |
| **4. Explanation Level (XL)** | **XL0** none · **XL1** global importance/interpretable features · **XL2** local post-hoc or attention · **XL3** interpretable-by-design or uncertainty-gated deferral · **XL4** explanations quantitatively evaluated for faithfulness, stability *and/or* actionability | How far decisions can be trusted |
| **5. Deployment Readiness Level (DRL)** | **DRL0** offline accuracy only · **DRL1** + FPR/cost-aware, unseen-family or drift test · **DRL2** + latency/time-to-detect · **DRL3** + live prototype with overhead or files-lost on real ransomware · **DRL4** + field/real-user or longitudinal (drift) validation | How close to deployment |

**Distribution of the 56 studies.**
- **XL:** XL0 36 (64%) · XL1 11 (20%) · XL2 6 (11%) · XL3 3 (5%) · **XL4 0**.
- **DRL:** DRL0 25 (45%) · DRL1 16 (29%) · DRL2 3 (5%) · DRL3 12 (21%) · **DRL4 0**.

**Table 7. Earliest lifecycle stage × Deployment Readiness Level (n = 56; each study counted once at its earliest stage).**

| Earliest stage | DRL0 | DRL1 | DRL2 | DRL3 | DRL4 |
|---|---|---|---|---|---|
| Pre-execution | 5 | 6 | 0 | 0 | 0 |
| At-execution | 7 | 3 | 3 | 4 | 0 |
| Post-execution | 13 | 7 | 0 | 8 | 0 |
| Post-encryption (only) | 0 | 0 | 0 | 0 | 0 |

Earliest stage × Explanation Level: Pre-exec — XL0 8, XL1 1, XL3 2; At-exec — XL0 9, XL1 5, XL2 3; Post-exec — XL0 19, XL1 5, XL2 3, XL3 1.

**Reading the taxonomy.** The empty **DRL4** and **XL4** columns are the field's frontier. No pre-execution detector reaches DRL2. The only studies at XL ≥ 1 *and* DRL3 are [S33] (HPC classification on bare metal with event ranking) and [S48] (hybrid RF/autoencoder/BiLSTM on streaming host telemetry with an explainable RF engine). DRL3 studies by earliest stage: at-execution S10, S32, S33, S45; post-execution S01, S02, S26, S36, S41, S48, S49, S56.

---

## 9. Quality Assessment

Scores use the rubric in Section 4.6 (DR dataset realism, ER evaluation rigour, RP reproducibility, EX explainability, DP deployment readiness; 0–2 each). Inclusion threshold ≥ 4/10. "Extraction basis" shows whether scores came from the full abstract or from TLDR/metadata (the latter must be re-scored on the full text before submission).

**Table 8. Quality scores of the 56 included primary studies.**

| ID | Short title | DR | ER | RP | EX | DP | Total /10 | Extraction basis |
|---|---|---|---|---|---|---|---|---|
| S01 | ShieldFS: A Self-healing, Ransomware-aware Filesystem | 2 | 2 | 0 | 0 | 2 | **6** | TLDR/metadata [CANDIDATE coding] |
| S02 | RWGuard: A Real-Time Detection System Against Cryptogra… | 2 | 2 | 0 | 0 | 2 | **6** | TLDR/metadata [CANDIDATE coding] |
| S03 | Trusted detection of ransomware in a private cloud usin… | 2 | 2 | 1 | 0 | 1 | **6** | abstract |
| S04 | Crypto-ransomware early detection model using novel inc… | 1 | 2 | 1 | 0 | 0 | **4** | abstract |
| S05 | DRTHIS: Deep ransomware threat hunting and intelligence… | 1 | 2 | 0 | 0 | 1 | **4** | abstract |
| S06 | On the effectiveness of system API-related information … | 2 | 2 | 2 | 1 | 1 | **8** | abstract |
| S07 | A Multi-Tier Streaming Analytics Model of 0-Day Ransomw… | 2 | 1 | 0 | 0 | 1 | **4** | abstract |
| S08 | A Pseudo Feedback-Based Annotated TF-IDF Technique for … | 1 | 2 | 1 | 0 | 0 | **4** | abstract |
| S09 | Know Abnormal, Find Evil: Frequent Pattern Mining for R… | 1 | 2 | 0 | 1 | 0 | **4** | abstract |
| S10 | Peeler: Profiling Kernel-Level Events to Detect Ransomw… | 2 | 2 | 0 | 0 | 2 | **6** | TLDR/metadata [CANDIDATE coding] |
| S11 | Redundancy Coefficient Gradual Up-weighting-based Mutua… | 1 | 2 | 1 | 1 | 0 | **5** | abstract |
| S12 | UGRansome1819: A Novel Dataset for Anomaly Detection an… | 1 | 1 | 2 | 0 | 0 | **4** | abstract |
| S13 | An effective ransomware detection approach in a cloud e… | 1 | 2 | 0 | 0 | 1 | **4** | TLDR/metadata [CANDIDATE coding] |
| S14 | Behavior-based ransomware classification: A particle sw… | 1 | 1 | 1 | 1 | 0 | **4** | TLDR/metadata [CANDIDATE coding] |
| S15 | Crypto-ransomware detection using machine learning mode… | 2 | 2 | 1 | 0 | 1 | **6** | TLDR/metadata [CANDIDATE coding] |
| S16 | DeepWare: Imaging Performance Counters with Deep Learni… | 1 | 2 | 0 | 0 | 1 | **4** | abstract |
| S17 | Early detection of crypto-ransomware using pre-encrypti… | 1 | 1 | 0 | 1 | 1 | **4** | abstract |
| S18 | FeSA: Feature selection architecture for ransomware det… | 1 | 2 | 1 | 1 | 1 | **6** | TLDR/metadata [CANDIDATE coding] |
| S19 | RanSAP: An open dataset of ransomware storage access pa… | 2 | 2 | 2 | 0 | 1 | **7** | TLDR/metadata [CANDIDATE coding] |
| S20 | Reducing False Negatives in Ransomware Detection: A Cri… | 1 | 2 | 1 | 0 | 1 | **5** | abstract |
| S21 | Zero-day Ransomware Attack Detection using Deep Contrac… | 1 | 2 | 1 | 0 | 0 | **4** | TLDR/metadata [CANDIDATE coding] |
| S22 | Dynamic Feature Dataset for Ransomware Detection Using … | 1 | 1 | 2 | 0 | 0 | **4** | abstract |
| S23 | FLDetect: An API-Based Ransomware Detection Using Feder… | 1 | 1 | 1 | 0 | 1 | **4** | abstract |
| S24 | HiPeR - Early Detection of a Ransomware Attack using Ha… | 2 | 1 | 0 | 0 | 1 | **4** | abstract |
| S25 | Improving ransomware detection based on portable execut… | 1 | 2 | 2 | 0 | 1 | **6** | abstract |
| S26 | RTrap: Trapping and Containing Ransomware With Machine … | 1 | 1 | 0 | 0 | 2 | **4** | abstract |
| S27 | RWArmor: a static-informed dynamic analysis approach fo… | 1 | 2 | 0 | 0 | 1 | **4** | TLDR/metadata [CANDIDATE coding] |
| S28 | The Effect of the Ransomware Dataset Age on the Detecti… | 2 | 2 | 1 | 0 | 0 | **5** | abstract |
| S29 | Addressing Behavioral Drift in Ransomware Early Detecti… | 1 | 2 | 1 | 0 | 0 | **4** | abstract |
| S30 | Early Ransomware Detection with Deep Learning Models | 1 | 2 | 1 | 0 | 1 | **5** | abstract |
| S31 | FeSAD ransomware detection framework with machine learn… | 1 | 2 | 1 | 1 | 1 | **6** | TLDR/metadata [CANDIDATE coding] |
| S32 | Ranker: Early Ransomware Detection Through Kernel-Level… | 2 | 2 | 1 | 0 | 2 | **7** | abstract |
| S33 | Ransomware Classification Using Hardware Performance Co… | 2 | 2 | 1 | 1 | 1 | **7** | abstract |
| S34 | XRan: Explainable deep learning-based ransomware detect… | 1 | 2 | 1 | 2 | 0 | **6** | TLDR/metadata [CANDIDATE coding] |
| S35 | Zero-Ran Sniff: A zero-day ransomware early detection m… | 1 | 2 | 0 | 0 | 1 | **4** | abstract |
| S36 | ERW-Radar: An Adaptive Detection System against Evasive… | 2 | 2 | 1 | 0 | 2 | **7** | abstract |
| S37 | Explainable and Uncertainty Aware AI-Based Ransomware D… | 1 | 2 | 1 | 2 | 1 | **7** | abstract |
| S38 | RanSMAP: Open dataset of Ransomware Storage and Memory … | 2 | 2 | 2 | 0 | 1 | **7** | TLDR/metadata [CANDIDATE coding] |
| S39 | RansomFormer: A Cross-Modal Transformer Architecture fo… | 2 | 1 | 1 | 0 | 0 | **4** | abstract |
| S40 | Ransomware detection with CNN and deep learning based o… | 2 | 1 | 0 | 0 | 1 | **4** | abstract |
| S41 | Real-time open-file backup system with machine-learning… | 1 | 1 | 0 | 0 | 2 | **4** | TLDR/metadata [CANDIDATE coding] |
| S42 | XRGuard: A Model-Agnostic Approach to Ransomware Detect… | 1 | 2 | 1 | 2 | 1 | **7** | abstract |
| S43 | Zero day ransomware detection with Pulse: Function clas… | 2 | 2 | 1 | 0 | 1 | **6** | TLDR/metadata [CANDIDATE coding] |
| S44 | Zero-Day Ransomware Attack Detection Using Static Porta… | 1 | 2 | 1 | 0 | 1 | **5** | abstract |
| S45 | iCNN-LSTM+: A Batch-Based Incremental Ransomware Detect… | 1 | 2 | 1 | 0 | 2 | **6** | abstract |
| S46 | An Intelligent Sensing Framework for Early Ransomware D… | 2 | 2 | 0 | 1 | 0 | **5** | abstract |
| S47 | An ensemble machine learning framework for accurate ran… | 1 | 1 | 1 | 1 | 0 | **4** | abstract |
| S48 | Artificial Intelligence-Powered Crypto Ransomware Detec… | 1 | 1 | 0 | 1 | 2 | **5** | abstract |
| S49 | Detecting Ransomware Through Dynamic API Call Monitorin… | 2 | 2 | 1 | 0 | 2 | **7** | abstract |
| S50 | Dual-use ambiguity in static ransomware detection: fals… | 1 | 2 | 0 | 1 | 1 | **5** | TLDR/metadata [CANDIDATE coding] |
| S51 | Early Detection of Windows Crypto‐Ransomware Based on A… | 1 | 2 | 1 | 1 | 0 | **5** | abstract |
| S52 | Ensemble machine learning for proactive android ransomw… | 1 | 1 | 1 | 2 | 0 | **5** | abstract |
| S53 | Interpretable Pre-Ransomware Detection for SOCs Using S… | 1 | 2 | 1 | 2 | 1 | **7** | abstract |
| S54 | PE-Sleuth: Program-Level Semantics and Static Feature F… | 1 | 1 | 0 | 2 | 0 | **4** | TLDR/metadata [CANDIDATE coding] |
| S55 | Sequence Learning over Behavioral Attack Patterns for E… | 1 | 2 | 1 | 0 | 1 | **5** | abstract |
| S56 | System-Wide Ransomware Attack Detection via Perturbatio… | 2 | 2 | 1 | 0 | 2 | **7** | abstract |

**Summary.** Mean scores: DR 1.36 · ER 1.73 · RP 0.77 · EX 0.45 · DP 0.89 · total 5.20. Score distribution of the total: the median study lies just above the threshold, and only 11 studies (20%) achieve DP = 2.

**Table 9. Eligible studies excluded by the quality gate (EC8, score < 4).** These studies met IC1–IC4 but were not synthesised. They are listed with DOIs for transparency and form the sensitivity set (n = 117 with Table 8).

| Short title | Year | Venue | QA total | DOI |
|---|---|---|---|---|
| A Multi-Classifier Network-Based Crypto Ransomware Detection System: A | 2019 | IEEE Access | 3 | [10.1109/access.2019.2907485](https://doi.org/10.1109/access.2019.2907485) |
| Classification of ransomware families with machine learning based onN- | 2019 | Future Generation Computer Systems | 3 | [10.1016/j.future.2018.07.052](https://doi.org/10.1016/j.future.2018.07.052) |
| Machine Learning Based File Entropy Analysis for Ransomware Detection  | 2019 | IEEE Access | 3 | [10.1109/access.2019.2931136](https://doi.org/10.1109/access.2019.2931136) |
| Ransomware Detection System for Android Applications | 2019 | Electronics | 2 | [10.3390/electronics8080868](https://doi.org/10.3390/electronics8080868) |
| Ransomware detection using machine learning algorithms | 2019 | Concurrency and Computation: Practice an | 2 | [10.1002/cpe.5422](https://doi.org/10.1002/cpe.5422) |
| A Digital DNA Sequencing Engine for Ransomware Detection Using Machine | 2020 | IEEE Access | 2 | [10.1109/access.2020.3003785](https://doi.org/10.1109/access.2020.3003785) |
| Evaluation metric for crypto-ransomware detection using machine learni | 2020 | Journal of Information Security and Appl | 3 | [10.1016/j.jisa.2020.102646](https://doi.org/10.1016/j.jisa.2020.102646) |
| Optimizing Extreme Learning Machines Using Chains of Salps for Efficie | 2020 | Applied Sciences | 3 | [10.3390/app10113706](https://doi.org/10.3390/app10113706) |
| Ransomware Detection using Random Forest Technique | 2020 | ICT Express | 3 | [10.1016/j.icte.2020.11.001](https://doi.org/10.1016/j.icte.2020.11.001) |
| Two-Stage Ransomware Detection Using Dynamic Analysis and Machine Lear | 2020 | Wireless Personal Communications | 3 | [10.1007/s11277-020-07166-9](https://doi.org/10.1007/s11277-020-07166-9) |
| Analysis of Crypto-Ransomware Using ML-Based Multi-Level Profiling | 2021 | IEEE Access | 3 | [10.1109/access.2021.3109260](https://doi.org/10.1109/access.2021.3109260) |
| Asynchronous Peer-to-Peer Federated Capability-Based Targeted Ransomwa | 2021 | IEEE Access | 3 | [10.1109/access.2021.3124634](https://doi.org/10.1109/access.2021.3124634) |
| Convolutional Neural Network-Based Cryptography Ransomware Detection f | 2021 | Mathematics | 3 | [10.3390/math9070705](https://doi.org/10.3390/math9070705) |
| Enhancing File Entropy Analysis to Improve Machine Learning Detection  | 2021 | IEEE Access | 3 | [10.1109/access.2021.3114148](https://doi.org/10.1109/access.2021.3114148) |
| Process based volatile memory forensics for ransomware detection | 2021 | Concurrency and Computation: Practice an | 2 | [10.1002/cpe.6672](https://doi.org/10.1002/cpe.6672) |
| RansomCare: Data-centric detection and mitigation against smartphone c | 2021 | Computer Networks | 3 | [10.1016/j.comnet.2021.108011](https://doi.org/10.1016/j.comnet.2021.108011) |
| RansomDroid: Forensic analysis and detection of Android Ransomware usi | 2021 | Forensic Science International: Digital  | 2 | [10.1016/j.fsidi.2021.301168](https://doi.org/10.1016/j.fsidi.2021.301168) |
| A Content-Based Ransomware Detection and Backup Solid-State Drive for  | 2022 | IEEE Transactions on Computer-Aided Desi | 3 | [10.1109/tcad.2021.3099084](https://doi.org/10.1109/tcad.2021.3099084) |
| A few-shot meta-learning based siamese neural network using entropy fe | 2022 | Computers & Security | 2 | [10.1016/j.cose.2022.102691](https://doi.org/10.1016/j.cose.2022.102691) |
| BigRC-EML: big-data based ransomware classification using ensemble mac | 2022 | Cluster Computing | 2 | [10.1007/s10586-022-03569-4](https://doi.org/10.1007/s10586-022-03569-4) |
| Classification of ransomware using different types of neural networks | 2022 | Scientific Reports | 2 | [10.1038/s41598-022-08504-6](https://doi.org/10.1038/s41598-022-08504-6) |
| Digital Forensics as Advanced Ransomware Pre-Attack Detection Algorith | 2022 | Security and Communication Networks | 2 | [10.1155/2022/1424638](https://doi.org/10.1155/2022/1424638) |
| Dual Generative Adversarial Networks Based Unknown Encryption Ransomwa | 2022 | IEEE Access | 1 | [10.1109/access.2021.3128024](https://doi.org/10.1109/access.2021.3128024) |
| Ransomware detection using deep learning based unsupervised feature ex | 2022 | Scientific Reports | 3 | [10.1038/s41598-022-19443-7](https://doi.org/10.1038/s41598-022-19443-7) |
| Android Ransomware Detection Using Supervised Machine Learning Techniq | 2023 | Sensors | 3 | [10.3390/s24010189](https://doi.org/10.3390/s24010189) |
| E2E-RDS: Efficient End-to-End Ransomware Detection System Based on Sta | 2023 | Sensors | 3 | [10.3390/s23094467](https://doi.org/10.3390/s23094467) |
| Enhancing Ransomware Attack Detection Using Transfer Learning and Deep | 2023 | Electronics | 2 | [10.3390/electronics12183899](https://doi.org/10.3390/electronics12183899) |
| Explainable Ransomware Detection with Deep Learning Techniques | 2023 | Journal of Computer Virology and Hacking | 3 | [10.1007/s11416-023-00501-1](https://doi.org/10.1007/s11416-023-00501-1) |
| Optimal Graph Convolutional Neural Network-Based Ransomware Detection  | 2023 | Applied Sciences | 1 | [10.3390/app13085167](https://doi.org/10.3390/app13085167) |
| Ransomware early detection using deep reinforcement learning on portab | 2023 | Cluster Computing | 3 | [10.1007/s10586-023-04043-5](https://doi.org/10.1007/s10586-023-04043-5) |
| Revolutionizing ransomware detection and criticality assessment: Multi | 2023 | Multimedia Tools and Applications | 3 | [10.1007/s11042-023-16946-x](https://doi.org/10.1007/s11042-023-16946-x) |
| SINN-RD: Spline interpolation-envisioned neural network-based ransomwa | 2023 | Computers and Electrical Engineering | 1 | [10.1016/j.compeleceng.2023.108601](https://doi.org/10.1016/j.compeleceng.2023.108601) |
| Temporal Data Correlation Providing Enhanced Dynamic Crypto-Ransomware | 2023 | Sensors | 2 | [10.3390/s23094355](https://doi.org/10.3390/s23094355) |
| An Incremental Mutual Information-Selection Technique for Early Ransom | 2024 | Information | 3 | [10.3390/info15040194](https://doi.org/10.3390/info15040194) |
| An intelligent ransomware attack detection and classification using du | 2024 | Computers and Electrical Engineering | 1 | [10.1016/j.compeleceng.2024.109509](https://doi.org/10.1016/j.compeleceng.2024.109509) |
| Anomaly detection for early ransomware and spyware warning in nuclear  | 2024 | International Journal of Information Sec | 3 | [10.1007/s10207-024-00841-z](https://doi.org/10.1007/s10207-024-00841-z) |
| It's too late if exfiltrate: Early stage Android ransomware detection | 2024 | Computers & Security | 3 | [10.1016/j.cose.2024.103819](https://doi.org/10.1016/j.cose.2024.103819) |
| Leveraging application permissions and network traffic attributes for  | 2024 | Journal of Network and Computer Applicat | 2 | [10.1016/j.jnca.2024.103950](https://doi.org/10.1016/j.jnca.2024.103950) |
| Novel Ransomware Detection Exploiting Uncertainty and Calibration Qual | 2024 | Information | 3 | [10.3390/info15050262](https://doi.org/10.3390/info15050262) |
| Ransomware Detection Model Based on Adaptive Graph Neural Network Lear | 2024 | Applied Sciences | 2 | [10.3390/app14114579](https://doi.org/10.3390/app14114579) |
| Ransomware detection based on machine learning using memory features | 2024 | Egyptian Informatics Journal | 3 | [10.1016/j.eij.2024.100445](https://doi.org/10.1016/j.eij.2024.100445) |
| A Deep Learning Framework for Enhanced Detection of Polymorphic Ransom | 2025 | Future Internet | 3 | [10.3390/fi17070311](https://doi.org/10.3390/fi17070311) |
| A Machine Learning-Based Ransomware Detection Method for Attackers’ Ne | 2025 | Sensors | 3 | [10.3390/s25082406](https://doi.org/10.3390/s25082406) |
| A Transductive Zero-Shot Learning Framework for Ransomware Detection U | 2025 | Information | 3 | [10.3390/info16060458](https://doi.org/10.3390/info16060458) |
| Differential privacy enhanced ransomware detection in cloud VMs using  | 2025 | International Journal of Information Sec | 1 | [10.1007/s10207-025-01153-6](https://doi.org/10.1007/s10207-025-01153-6) |
| HFL-RD: Heterogeneous Federated Learning-Empowered Ransomware Detectio | 2025 | IEEE Transactions on Network and Service | 3 | [10.1109/tnsm.2025.3574716](https://doi.org/10.1109/tnsm.2025.3574716) |
| Privacy preserved api access control policy- based ransomware attack d | 2025 | Cluster Computing | 1 | [10.1007/s10586-025-05335-8](https://doi.org/10.1007/s10586-025-05335-8) |
| Quantum-Powered Extended Visibility for Zero-Trust-Based Ransomware De | 2025 | IEEE Internet of Things Journal | 3 | [10.1109/jiot.2024.3496481](https://doi.org/10.1109/jiot.2024.3496481) |
| RanViz: Ransomware Visualization and Classification Based on Time-Seri | 2025 | IEEE Access | 3 | [10.1109/access.2025.3555163](https://doi.org/10.1109/access.2025.3555163) |
| RansoGuard: A RNN-based framework leveraging pre-attack sensitive APIs | 2025 | Computers & Security | 3 | [10.1016/j.cose.2024.104293](https://doi.org/10.1016/j.cose.2024.104293) |
| RansomHunter: zero-day Android ransomware detection using graph convol | 2025 | The Journal of Supercomputing | 3 | [10.1007/s11227-025-07777-8](https://doi.org/10.1007/s11227-025-07777-8) |
| Ransomware detection and family classification using fine-tuned BERT a | 2025 | Egyptian Informatics Journal | 2 | [10.1016/j.eij.2025.100645](https://doi.org/10.1016/j.eij.2025.100645) |
| Real time ransomware detection in cloud VMS using behavioral biometric | 2025 | International Journal of Information Sec | 2 | [10.1007/s10207-025-01151-8](https://doi.org/10.1007/s10207-025-01151-8) |
| A quantum-inspired hybrid framework for ransomware detection using gra | 2026 | Scientific Reports | 2 | [10.1038/s41598-026-68188-0](https://doi.org/10.1038/s41598-026-68188-0) |
| A swarm intelligence-enhanced ransomware detection framework via dynam | 2026 | Expert Systems with Applications | 2 | [10.1016/j.eswa.2025.129225](https://doi.org/10.1016/j.eswa.2025.129225) |
| Deep MCRan: Hybrid Analysis-Based Ransomware Detection Using Multi-Cha | 2026 | IEEE Access | 3 | [10.1109/access.2026.3727310](https://doi.org/10.1109/access.2026.3727310) |
| Detection of Ransomware Attack in IoT-Based Smart Meter Using Hybrid D | 2026 | IEEE Transactions on Consumer Electronic | 2 | [10.1109/tce.2026.3659127](https://doi.org/10.1109/tce.2026.3659127) |
| HARVEST: Hardware-based ransomware detection and stage tracking for AI | 2026 | Journal of Network and Computer Applicat | 3 | [10.1016/j.jnca.2026.104458](https://doi.org/10.1016/j.jnca.2026.104458) |
| Real-Time Ransomware Detection Using Reinforcement Learning Agents | 2026 | Information | 3 | [10.3390/info17020194](https://doi.org/10.3390/info17020194) |
| TDMRans: Toward a Two-Stage Detection Method of Ransomware Encryption  | 2026 | IEEE Transactions on Network Science and | 3 | [10.1109/tnse.2026.3719148](https://doi.org/10.1109/tnse.2026.3719148) |
| Two-Tier heuristic search for ransomware-as-a-service based cyberattac | 2026 | Scientific Reports | 2 | [10.1038/s41598-025-96083-7](https://doi.org/10.1038/s41598-025-96083-7) |

**Table 10. Primary candidates excluded at eligibility, with reasons.**

| Title | Year | Reason | DOI |
|---|---|---|---|
| Redemption: Real-Time Protection Against Ransomware at End-Hosts | 2017 | EC4: heuristic scoring, no learned model (Redemption) | [10.1007/978-3-319-66332-6_5](https://doi.org/10.1007/978-3-319-66332-6_5) |
| FlashGuard: Leveraging Intrinsic Flash Properties to Defend Against En | 2017 | EC4: SSD firmware recovery, no ML (FlashGuard) | [10.1145/3133956.3134035](https://doi.org/10.1145/3133956.3134035) |
| Ransomware early detection by the analysis of file sharing traffic | 2018 | EC4: threshold algorithm on file-sharing traffic, no trained model | [10.1016/j.jnca.2018.09.013](https://doi.org/10.1016/j.jnca.2018.09.013) |
| Ransomware behavioural analysis on windows platforms | 2018 | EC4: descriptive API-frequency analysis, no classifier | [10.1016/j.jisa.2018.02.008](https://doi.org/10.1016/j.jisa.2018.02.008) |
| RansomSpector: An introspection-based approach to detect crypto ransom | 2020 | EC4: VMI rule-based detection (no learned model) | [10.1016/j.cose.2020.101997](https://doi.org/10.1016/j.cose.2020.101997) |
| Hybrid-Based Analysis Impact on Ransomware Detection for Android Syste | 2021 | EC4: detection relies on AV-engine verdicts / tool comparison; no trained ML/DL model | [10.3390/app112210976](https://doi.org/10.3390/app112210976) |
| Dynamic user-centric access control for detection of ransomware attack | 2021 | EC4: access-control framework, no ML model | [10.1016/j.cose.2021.102461](https://doi.org/10.1016/j.cose.2021.102461) |
| A New Scheme for Ransomware Classification and Clustering Using Static | 2022 | EC4: Jaccard similarity indexing/clustering, no trained classifier | [10.3390/electronics11203307](https://doi.org/10.3390/electronics11203307) |
| Opportunities for Early Detection and Prediction of Ransomware Attacks | 2023 | EC5: narrative review (re-routed to related work) | [10.3390/fi15040144](https://doi.org/10.3390/fi15040144) |
| Effective Ransomware Detection Using Entropy Estimation of Files for C | 2023 | EC4: threshold entropy estimation, no trained model | [10.3390/s23063023](https://doi.org/10.3390/s23063023) |
| Ransomware Detection Service: Execution and Analysis Using Machine Lea | 2023 | EC5: discussion/overview paper without a primary detection contribution | [10.1007/s11277-023-10801-w](https://doi.org/10.1007/s11277-023-10801-w) |
| A Holistic Approach to Ransomware Classification: Leveraging Static an | 2024 | EC4: similarity-matrix comparison/clustering, no trained detector | [10.3390/info15010046](https://doi.org/10.3390/info15010046) |
| Early mitigation of CPU-optimized ransomware using monitoring encrypti | 2024 | EC4: kernel instruction-monitoring mitigation without ML | [10.1007/s10207-024-00892-2](https://doi.org/10.1007/s10207-024-00892-2) |
| Lightweight Crypto-Ransomware Detection in Android Based on Reactive H | 2024 | EC4: honeyfile monitoring, no ML (authors contrast with ML) | [10.3390/s24092679](https://doi.org/10.3390/s24092679) |
| Hybrid EfficientNet feed forward neural network for ransomware detecti | 2025 | EC3: ransomware *payment*/blockchain transaction analytics, not host/network attack detection | [10.1016/j.engappai.2025.110292](https://doi.org/10.1016/j.engappai.2025.110292) |
| Blockchain data with Ransomware detection based on deep feed forward M | 2025 | EC3: ransomware *payment*/blockchain transaction analytics, not host/network attack detection | [10.1016/j.engappai.2025.110538](https://doi.org/10.1016/j.engappai.2025.110538) |
| Not on my watch: ransomware detection through classification of high-e | 2025 | EC6: publisher outside protocol list (Oxford University Press) | [10.1093/cybsec/tyaf009](https://doi.org/10.1093/cybsec/tyaf009) |

---

## 10. Research Gaps and Future Directions

**Gap 1 — The pre-encryption window lacks a shared definition, benchmark and loss metric.**
*Evidence.* Only 18/56 (32%) studies decide at execution time and 11/56 (20%) before execution (Section 5.1). The early window is defined by fixed time thresholds in most work, which [S08] shows is inappropriate because encryption onset varies by family; several studies identify data scarcity in the early window as the main obstacle [S04, S11, S29]. Only 15/56 report latency, time-to-detect or files lost, using incompatible units (seconds [S24, S56], files lost [S26], percentage of files saved [S49]). No pre-execution detector reaches DRL2 (Table 7).
*Future directions.* (i) A public benchmark with per-sample, IRP-/API-anchored pre-encryption boundaries (building on [S08] and the API–IRP correlation idea of Sensors 2023, Table 9); (ii) standard loss metrics — *files lost at detection*, *bytes encrypted at detection* and *time-to-detect*, reported with FPR per benign hour; (iii) early-window learning methods evaluated on truncated traces of increasing length (learning curves over time).

**Gap 2 — Explanations are produced but never evaluated (XL4 is empty).**
*Evidence.* 20/56 studies include XAI; 0/20 (and 0/28 in the sensitivity set) report a quantitative faithfulness, stability or actionability metric (Section 5.3). Explanations are SHAP/LIME plots or feature rankings [S34, S42, S52, S53]. Security-XAI research shows that explanation methods can disagree and mislead unless evaluated [M4].
*Future directions.* (i) Adopt **faithfulness** tests (deletion/insertion curves, descriptive accuracy, sparsity) and **stability** tests (explanation agreement across seeds, retraining and near-duplicate samples of the same family) from [M4]; (ii) measure **actionability** with analyst studies (decision time, correct kill/allow decisions, rules derivable from explanations); (iii) report explanation quality *at the early stage*, where fewer features are available and explanations may be unstable.

**Gap 3 — Generalisation to new families and to time is never tested jointly.**
*Evidence.* Unseen-family splits: 9/56 (16%); temporal/drift evaluation: 7/56 (13%); both: 0/56 (Table 6). Dataset age changes detection accuracy substantially [S28]; drift-aware approaches exist [S18, S31, S29, S45] but are evaluated without family-disjoint test sets, and zero-day approaches [S21, S35, S43, S44] are evaluated without temporal ordering.
*Future directions.* Mandate **time-aware and family-aware splits** following TESSERACT [M5] and the ML-in-security pitfalls checklist [M3]; report performance decay curves (AUT) and time-to-retrain; combine incremental learning [S45] with zero-shot novelty detection [S35].

**Gap 4 — Deployment evidence is thin and stops before the field (DRL4 is empty).**
*Evidence.* Runtime overhead is measured in 5/56 (9%) studies [S01, S02, S36, S49, S56]; FPR in 12/56 (21%); 25/56 (45%) remain at DRL0. No study reports field deployment with real users over time or longitudinal drift on live hosts (DRL4 = 0). The systems closest to deployment are kernel/file-system level (ShieldFS [S01], RWGuard [S02], Peeler [S10], Ranker [S32]) or system-wide (CoLPR [S56]).
*Future directions.* (i) Report a **minimum deployment profile**: CPU/memory/I/O overhead, detection latency, FPR per benign-hour under realistic workloads, and kill-switch/rollback behaviour; (ii) evaluate against benign *crypto-heavy* applications (backup, compression, disk encryption) as standard negative controls [S50]; (iii) longitudinal deployments in enterprise endpoints or SOC telemetry (Sysmon/ETW) [S42, S45].

**Gap 5 — Datasets are small, sandbox-bound, rarely public and rarely comparable.**
*Evidence.* Public data in 12/56 (21%); real/bare-metal or production-like collection in 8/56 (14%); mean RP 0.77/2. Benchmarks such as RanSAP/RanSMAP [S19, S38] and UGRansome [S12] exist but are re-used in only a handful of included studies [S37, S47]. Evasion-aware ransomware behaviour (sandbox fingerprinting, intermittent encryption) is reported to defeat existing systems [S36].
*Future directions.* A community **multi-view dataset** (API + kernel + storage + HPC + network for the same executions), collected on bare metal with realistic user workloads, family/time metadata, and release of trained models and code; a reporting checklist covering sample provenance, family counts, collection dates and benign workload design.

**Gap 6 — Platform monoculture: Windows dominates; mobile, cloud, IoT/ICS and storage studies rarely meet quality thresholds.**
*Evidence.* Windows accounts for 43/56 (77%) of included studies. In the sensitivity set there are 11 Android and 7 cloud/VM studies; only 3 and 2 respectively passed the quality gate (Section 5.0). IoT/IIoT/ICS studies (e.g., federated IIoT detection, smart-meter and smart-grid detection; Table 9) fell below threshold, mostly on dataset realism and reproducibility.
*Future directions.* Platform-specific benchmarks (Android with time-stamped APK corpora [S28]; Linux/ESXi server ransomware; storage-array and SAN-level traces); resource-constrained models with measured on-device latency and energy.

**Gap 7 — Threat models lag behind modern ransomware operations.**
*Evidence.* Most detectors classify a single process's behaviour, whereas modern attacks distribute malicious actions across seemingly benign processes [S56], begin with human-operated intrusion phases [S55], and exfiltrate before encrypting. Only [S55] (TTP sequences) and [S56] (system-wide detection) address these directly among included studies; exfiltration-first Android detection was eligible but excluded at QA (Table 9).
*Future directions.* Multi-stage detectors that fuse pre-encryption intrusion signals (TTP sequences, lateral movement, exfiltration) with host behaviour; system-wide rather than per-process representations; explicit evaluation against double-extortion and intermittent-encryption variants.

---

## 11. Contribution Statement

**What is new.**
1. A **joint, quality-weighted synthesis** of ML ransomware detection along *lifecycle stage × explanation × deployment* for 2016–2026, restricted to Q1/Q2 journals and top-tier conferences from six major publishers.
2. The **SEED-R taxonomy** with two graded scales — **Explanation Levels (XL0–XL4)** and **Deployment Readiness Levels (DRL0–DRL4)** — that make readiness comparable across studies and expose empty frontier cells (XL4, DRL4).
3. The first explicit synthesis, among the 18 secondary studies we identified, of **how explanation quality is evaluated** in ransomware detection, with the finding that it is not evaluated quantitatively in any included study.
4. Quantified evidence that **no included study jointly tests unseen families and temporal drift**.
5. A **fully scripted, re-runnable PRISMA pipeline** with machine-verified DOIs and archived intermediate data.

**How it differs from existing surveys.** Versus broad surveys [R03, R07, R09, R12]: narrower (ML detection only) but graded per study. Versus ML-detection surveys [R05, R08, R11, R14, R16]: adds lifecycle-stage mapping, explanation-quality and deployment-readiness grading, and a venue/quality filter. Versus early-detection reviews [R13, R15]: adds explanation and deployment axes and shows that early detectors rarely reach DRL ≥ 2. Versus the deployability survey [R18]: adds explanation quality and quality-scored ML-specific evidence, and grades deployment evidence per study rather than per defence level.

**Academic value.** A reproducible evidence base and taxonomy that later studies can position against; seven gaps framed as testable research directions; a quality instrument emphasising realism, reproducibility and deployability over accuracy.
**Practical value.** For practitioners and vendors: identification of the detector designs with the strongest deployment evidence (kernel/file-system level, HPC, system-wide), the evaluation conditions under which reported accuracy is meaningful, and a minimum deployment profile to request from research prototypes.

---

## 12. Limitations

### 12.1 Limitations of this SLR
- **Source coverage.** Searches were executed on Crossref only. Crossref indexes all six allowed publishers and supplies the DOIs required for verification, but its relevance ranking and the 200-record cap per string may miss records that IEEE Xplore, Scopus or Web of Science would return. Exact Boolean strings for those databases are provided (Section 4.1) for a confirmatory run.
- **Title filter.** Records were retained only when "ransom" appeared in the title; studies that address ransomware only in the abstract (e.g., general malware detectors evaluated on ransomware) are under-represented by design.
- **Abstract-level extraction.** Data were extracted from abstracts (Crossref/Semantic Scholar). For 17 of the 56 included studies, mainly Elsevier titles whose abstracts are not exposed through open APIs, coding relied on TLDRs, titles and reviewer knowledge; these are marked *CANDIDATE coding* and must be re-coded from full texts. The claim that no study evaluates explanation quality should be confirmed on the 20 XAI full texts.
- **Single reviewer.** Screening, extraction and scoring were performed by one reviewer, supported by deterministic scripts. A second independent reviewer on a ≥20% sample, with Cohen's κ, is recommended before submission.
- **Quartile verification.** SJR quartiles were applied from a whitelist rather than queried live; quartiles change by year and category and must be re-confirmed. Some whitelisted MDPI and Wiley journals sit at the Q1/Q2 boundary in some categories.
- **Quality-gate sensitivity.** The ≥4/10 threshold excluded 61 eligible studies. Key proportions were re-computed on all 117 eligible studies (Sections 5.0–5.3); the direction of every finding is unchanged, but magnitudes differ (e.g., XAI prevalence 36% vs 24%; Windows share 77% vs 67%).
- **Conference coverage.** Top-tier conference papers published as LNCS chapters (RAID, ESORICS, DIMVA) are not marked as proceedings in Crossref and were found only through snowballing; additional top-tier papers may exist.
- **Recency.** 2026 records reflect publications indexed by 12 November 2026.

### 12.2 Limitations of the included studies
Predominantly sandbox/VM data; random splits; small and ageing datasets; unrealistic benign classes; rare measurement of overhead and latency; explanations without evaluation; frequent omission of code and model release.

### 12.3 Limitations of the field
No shared early-detection benchmark or loss metric; no accepted explanation-quality protocol for security; a Windows-centric evidence base; limited access to modern, human-operated ransomware telemetry for academic researchers; and a tension between publishing high in-distribution accuracy and reporting realistic failure modes.

---

## 13. Conclusion

**Key findings.** Across 56 quality-assessed studies (2016–2026), ML ransomware detection is dominated by post-execution behavioural classification (63%) on API traces (43%) with classical ML (57%), while DL — especially Transformers/LLMs since 2024 — is growing. Only a third of detectors act in the pre-encryption window. Explainability appears in 36% of studies but is never evaluated for faithfulness, stability or actionability. Deployment evidence is thin: 9% measure overhead, 16% test unseen families, 13% test temporal drift, none does both, and none reaches field validation.

**Gaps.** (1) No shared early-detection benchmark or loss metric; (2) no explanation-quality evaluation; (3) no joint novelty-plus-drift testing; (4) no field-level deployment evidence; (5) small, sandbox-bound, non-public datasets; (6) Windows monoculture; (7) threat models lagging behind system-wide, human-operated and exfiltration-first ransomware.

**Future directions.** Community benchmarks with sample-specific pre-encryption boundaries and files-lost metrics; adoption of security-XAI evaluation protocols [M4]; TESSERACT-style time- and family-aware evaluation [M5]; bare-metal, multi-view datasets with realistic benign workloads; and a standard deployment profile (overhead, latency, FPR per benign hour).

**Contribution.** A reproducible, PRISMA-compliant, quality-weighted evidence base and the SEED-R taxonomy with Explanation and Deployment Readiness Levels, which together turn "high accuracy" into a measurable path from offline classifiers to trustworthy, early and deployable ransomware defence.

---

## 8. Reference List

*(Section 8 is placed at the end in accordance with the output-format requirement for a closing reference list.)*

**Verification legend.** **[VERIFIED]** — authors, title, venue, year and DOI confirmed in Crossref on 12 Nov 2026; extraction from the full abstract. **[VERIFIED metadata · CANDIDATE coding]** — metadata confirmed in Crossref, but extraction based on TLDR/metadata; verify against the full text. Every DOI link below resolves through https://doi.org/. Venue strings are Crossref's container titles; for LNCS chapters the conference is given.

### 8.1 Primary studies (n = 56)

[S01] Andrea Continella, Alessandro Guagnelli, Giovanni Zingaro et al., “ShieldFS: A Self-healing, Ransomware-aware Filesystem,” *ACSAC 2016*, 2016. DOI: 10.1145/2991079.2991110. Link: https://doi.org/10.1145/2991079.2991110 [VERIFIED metadata · CANDIDATE coding]

[S02] Shagufta Mehnaz, Anand Mudgerikar, Elisa Bertino, “RWGuard: A Real-Time Detection System Against Cryptographic Ransomware,” *RAID 2018 (LNCS 11050)*, 2018. DOI: 10.1007/978-3-030-00470-5_6. Link: https://doi.org/10.1007/978-3-030-00470-5_6 [VERIFIED metadata · CANDIDATE coding]

[S03] Aviad Cohen, Nir Nissim, “Trusted detection of ransomware in a private cloud using machine learning methods leveraging meta-features from volatile memory,” *Expert Systems with Applications*, 2018. DOI: 10.1016/j.eswa.2018.02.039. Link: https://doi.org/10.1016/j.eswa.2018.02.039 [VERIFIED]

[S04] Bander Ali Saleh Al-rimy, Mohd Aizaini Maarof, Syed Zainudeen Mohd Shaid, “Crypto-ransomware early detection model using novel incremental bagging with enhanced semi-random subspace selection,” *Future Generation Computer Systems*, 2019. DOI: 10.1016/j.future.2019.06.005. Link: https://doi.org/10.1016/j.future.2019.06.005 [VERIFIED]

[S05] Sajad Homayoun, Ali Dehghantanha, Marzieh Ahmadzadeh et al., “DRTHIS: Deep ransomware threat hunting and intelligence system at the fog layer,” *Future Generation Computer Systems*, 2019. DOI: 10.1016/j.future.2018.07.045. Link: https://doi.org/10.1016/j.future.2018.07.045 [VERIFIED]

[S06] Michele Scalas, Davide Maiorca, Francesco Mercaldo et al., “On the effectiveness of system API-related information for Android ransomware detection,” *Computers & Security*, 2019. DOI: 10.1016/j.cose.2019.06.004. Link: https://doi.org/10.1016/j.cose.2019.06.004 [VERIFIED]

[S07] Hiba Zuhair, Ali Selamat, Ondrej Krejcar, “A Multi-Tier Streaming Analytics Model of 0-Day Ransomware Detection Using Machine Learning,” *Applied Sciences*, 2020. DOI: 10.3390/app10093210. Link: https://doi.org/10.3390/app10093210 [VERIFIED]

[S08] Bander Ali Saleh Al-Rimy, Mohd Aiziani Maarof, Mamoun Alazab et al., “A Pseudo Feedback-Based Annotated TF-IDF Technique for Dynamic Crypto-Ransomware Pre-Encryption Boundary Delineation and Features Extraction,” *IEEE Access*, 2020. DOI: 10.1109/access.2020.3012674. Link: https://doi.org/10.1109/access.2020.3012674 [VERIFIED]

[S09] Sajad Homayoun, Ali Dehghantanha, Marzieh Ahmadzadeh et al., “Know Abnormal, Find Evil: Frequent Pattern Mining for Ransomware Threat Hunting and Intelligence,” *IEEE Transactions on Emerging Topics in Computing*, 2020. DOI: 10.1109/tetc.2017.2756908. Link: https://doi.org/10.1109/tetc.2017.2756908 [VERIFIED]

[S10] Muhammad Ejaz Ahmed, Hyoungshick Kim, Seyit Camtepe et al., “Peeler: Profiling Kernel-Level Events to Detect Ransomware,” *ESORICS 2021 (LNCS 12972)*, 2021. DOI: 10.1007/978-3-030-88418-5_12. Link: https://doi.org/10.1007/978-3-030-88418-5_12 [VERIFIED metadata · CANDIDATE coding]

[S11] Bander Ali Saleh Al-rimy, Mohd Aizaini Maarof, Mamoun Alazab et al., “Redundancy Coefficient Gradual Up-weighting-based Mutual Information Feature Selection technique for Crypto-ransomware early detection,” *Future Generation Computer Systems*, 2021. DOI: 10.1016/j.future.2020.10.002. Link: https://doi.org/10.1016/j.future.2020.10.002 [VERIFIED]

[S12] Mike Nkongolo, Jacobus Philippus van Deventer, Sydney Mambwe Kasongo, “UGRansome1819: A Novel Dataset for Anomaly Detection and Zero-Day Threats,” *Information*, 2021. DOI: 10.3390/info12100405. Link: https://doi.org/10.3390/info12100405 [VERIFIED]

[S13] Prachi, Sumit Kumar, “An effective ransomware detection approach in a cloud environment using volatile memory features,” *Journal of Computer Virology and Hacking Techniques*, 2022. DOI: 10.1007/s11416-022-00425-2. Link: https://doi.org/10.1007/s11416-022-00425-2 [VERIFIED metadata · CANDIDATE coding]

[S14] Muhammad Shabbir Abbasi, Harith Al-Sahaf, Masood Mansoori et al., “Behavior-based ransomware classification: A particle swarm optimization wrapper-based approach for feature selection,” *Applied Soft Computing*, 2022. DOI: 10.1016/j.asoc.2022.108744. Link: https://doi.org/10.1016/j.asoc.2022.108744 [VERIFIED metadata · CANDIDATE coding]

[S15] Eduardo Berrueta, Daniel Morato, Eduardo Magaña et al., “Crypto-ransomware detection using machine learning models in file-sharing network scenarios with encrypted traffic,” *Expert Systems with Applications*, 2022. DOI: 10.1016/j.eswa.2022.118299. Link: https://doi.org/10.1016/j.eswa.2022.118299 [VERIFIED metadata · CANDIDATE coding]

[S16] Gaddisa Olani, Chun-Feng Wu, Yuan-Hao Chang et al., “DeepWare: Imaging Performance Counters with Deep Learning to Detect Ransomware,” *IEEE Transactions on Computers*, 2022. DOI: 10.1109/tc.2022.3173149. Link: https://doi.org/10.1109/tc.2022.3173149 [VERIFIED]

[S17] S.H. Kok, Azween Abdullah, NZ Jhanjhi, “Early detection of crypto-ransomware using pre-encryption detection algorithm,” *Journal of King Saud University - Computer and Information Sciences*, 2022. DOI: 10.1016/j.jksuci.2020.06.012. Link: https://doi.org/10.1016/j.jksuci.2020.06.012 [VERIFIED]

[S18] Damien Warren Fernando, Nikos Komninos, “FeSA: Feature selection architecture for ransomware detection under concept drift,” *Computers & Security*, 2022. DOI: 10.1016/j.cose.2022.102659. Link: https://doi.org/10.1016/j.cose.2022.102659 [VERIFIED metadata · CANDIDATE coding]

[S19] Manabu Hirano, Ryo Hodota, Ryotaro Kobayashi, “RanSAP: An open dataset of ransomware storage access patterns for training machine learning models,” *Forensic Science International: Digital Investigation*, 2022. DOI: 10.1016/j.fsidi.2021.301314. Link: https://doi.org/10.1016/j.fsidi.2021.301314 [VERIFIED metadata · CANDIDATE coding]

[S20] Robert Bold, Haider Al-Khateeb, Nikolaos Ersotelos, “Reducing False Negatives in Ransomware Detection: A Critical Evaluation of Machine Learning Algorithms,” *Applied Sciences*, 2022. DOI: 10.3390/app122412941. Link: https://doi.org/10.3390/app122412941 [VERIFIED]

[S21] Umme Zahoora, Muttukrishnan Rajarajan, Zahoqing Pan et al., “Zero-day Ransomware Attack Detection using Deep Contractive Autoencoder and Voting based Ensemble Classifier,” *Applied Intelligence*, 2022. DOI: 10.1007/s10489-022-03244-6. Link: https://doi.org/10.1007/s10489-022-03244-6 [VERIFIED metadata · CANDIDATE coding]

[S22] Juan A. Herrera-Silva, Myriam Hernández-Álvarez, “Dynamic Feature Dataset for Ransomware Detection Using Machine Learning Algorithms,” *Sensors*, 2023. DOI: 10.3390/s23031053. Link: https://doi.org/10.3390/s23031053 [VERIFIED]

[S23] Tomas Petros, Henos Ghirmay, Safa Otoum et al., “FLDetect: An API-Based Ransomware Detection Using Federated Learning,” *GLOBECOM 2023 - 2023 IEEE Global Communications Conference*, 2023. DOI: 10.1109/globecom54140.2023.10437540. Link: https://doi.org/10.1109/globecom54140.2023.10437540 [VERIFIED]

[S24] P. Mohan Anand, P. V. Sai Charan, Sandeep K. Shukla, “HiPeR - Early Detection of a Ransomware Attack using Hardware Performance Counters,” *Digital Threats: Research and Practice*, 2023. DOI: 10.1145/3608484. Link: https://doi.org/10.1145/3608484 [VERIFIED]

[S25] Caio C. Moreira, Davi C. Moreira, Claudomiro de S. de Sales Jr., “Improving ransomware detection based on portable executable header using xception convolutional neural network,” *Computers & Security*, 2023. DOI: 10.1016/j.cose.2023.103265. Link: https://doi.org/10.1016/j.cose.2023.103265 [VERIFIED]

[S26] Gaddisa Olani Ganfure, Chun-Feng Wu, Yuan-Hao Chang et al., “RTrap: Trapping and Containing Ransomware With Machine Learning,” *IEEE Transactions on Information Forensics and Security*, 2023. DOI: 10.1109/tifs.2023.3240025. Link: https://doi.org/10.1109/tifs.2023.3240025 [VERIFIED]

[S27] Md. Ahsan Ayub, Ambareen Siraj, Bobby Filar et al., “RWArmor: a static-informed dynamic analysis approach for early detection of cryptographic windows ransomware,” *International Journal of Information Security*, 2023. DOI: 10.1007/s10207-023-00758-z. Link: https://doi.org/10.1007/s10207-023-00758-z [VERIFIED metadata · CANDIDATE coding]

[S28] Qussai M. Yaseen, “The Effect of the Ransomware Dataset Age on the Detection Accuracy of Machine Learning Models,” *Information*, 2023. DOI: 10.3390/info14030193. Link: https://doi.org/10.3390/info14030193 [VERIFIED]

[S29] Umara Urooj, Bander Ali Saleh Al-Rimy, Anazida Binti Zainal et al., “Addressing Behavioral Drift in Ransomware Early Detection Through Weighted Generative Adversarial Networks,” *IEEE Access*, 2024. DOI: 10.1109/access.2023.3348451. Link: https://doi.org/10.1109/access.2023.3348451 [VERIFIED]

[S30] Matan Davidian, Michael Kiperberg, Natalia Vanetik, “Early Ransomware Detection with Deep Learning Models,” *Future Internet*, 2024. DOI: 10.3390/fi16080291. Link: https://doi.org/10.3390/fi16080291 [VERIFIED]

[S31] Damien Warren Fernando, Nikos Komninos, “FeSAD ransomware detection framework with machine learning using adaption to concept drift,” *Computers & Security*, 2024. DOI: 10.1016/j.cose.2023.103629. Link: https://doi.org/10.1016/j.cose.2023.103629 [VERIFIED metadata · CANDIDATE coding]

[S32] Huan Zhang, Lixin Zhao, Aimin Yu et al., “Ranker: Early Ransomware Detection Through Kernel-Level Behavioral Analysis,” *IEEE Transactions on Information Forensics and Security*, 2024. DOI: 10.1109/tifs.2024.3410511. Link: https://doi.org/10.1109/tifs.2024.3410511 [VERIFIED]

[S33] Jennie E. Hill, T. Owens Walker, Justin A. Blanco et al., “Ransomware Classification Using Hardware Performance Counters on a Non-Virtualized System,” *IEEE Access*, 2024. DOI: 10.1109/access.2024.3395491. Link: https://doi.org/10.1109/access.2024.3395491 [VERIFIED]

[S34] Sibel Gulmez, Arzu Gorgulu Kakisim, Ibrahim Sogukpinar, “XRan: Explainable deep learning-based ransomware detection using dynamic analysis,” *Computers & Security*, 2024. DOI: 10.1016/j.cose.2024.103703. Link: https://doi.org/10.1016/j.cose.2024.103703 [VERIFIED metadata · CANDIDATE coding]

[S35] Mingcan Cen, Xizhen Deng, Frank Jiang et al., “Zero-Ran Sniff: A zero-day ransomware early detection method based on zero-shot learning,” *Computers & Security*, 2024. DOI: 10.1016/j.cose.2024.103849. Link: https://doi.org/10.1016/j.cose.2024.103849 [VERIFIED]

[S36] Lingbo Zhao, Yuhui Zhang, Zhilu Wang et al., “ERW-Radar: An Adaptive Detection System against Evasive Ransomware by Contextual Behavior Detection and Fine-grained Content Analysis,” *Proceedings 2025 Network and Distributed System Security Symposium*, 2025. DOI: 10.14722/ndss.2025.230349. Link: https://doi.org/10.14722/ndss.2025.230349 [VERIFIED]

[S37] Henry Kabuye, Biju Issac, Rahul Yumlembam et al., “Explainable and Uncertainty Aware AI-Based Ransomware Detection,” *IEEE Access*, 2025. DOI: 10.1109/access.2025.3581424. Link: https://doi.org/10.1109/access.2025.3581424 [VERIFIED]

[S38] Manabu Hirano, Ryotaro Kobayashi, “RanSMAP: Open dataset of Ransomware Storage and Memory Access Patterns for creating deep learning based ransomware detectors,” *Computers & Security*, 2025. DOI: 10.1016/j.cose.2024.104202. Link: https://doi.org/10.1016/j.cose.2024.104202 [VERIFIED metadata · CANDIDATE coding]

[S39] Saleh Alzahrani, Yang Xiao, Sultan Asiri et al., “RansomFormer: A Cross-Modal Transformer Architecture for Ransomware Detection via the Fusion of Byte and API Features,” *Electronics*, 2025. DOI: 10.3390/electronics14071245. Link: https://doi.org/10.3390/electronics14071245 [VERIFIED]

[S40] Chia-Cheng Yang, Jia-Ming Hsu, Jenq-Shiou Leu et al., “Ransomware detection with CNN and deep learning based on multiple features of portable executable files,” *The Journal of Supercomputing*, 2025. DOI: 10.1007/s11227-025-07151-8. Link: https://doi.org/10.1007/s11227-025-07151-8 [VERIFIED]

[S41] Kosuke Higuchi, Ryotaro Kobayashi, “Real-time open-file backup system with machine-learning detection model for ransomware,” *International Journal of Information Security*, 2025. DOI: 10.1007/s10207-024-00966-1. Link: https://doi.org/10.1007/s10207-024-00966-1 [VERIFIED metadata · CANDIDATE coding]

[S42] M. Adnan Alvi, Zunera Jalil, “XRGuard: A Model-Agnostic Approach to Ransomware Detection Using Dynamic Analysis and Explainable AI,” *IEEE Access*, 2025. DOI: 10.1109/access.2025.3553562. Link: https://doi.org/10.1109/access.2025.3553562 [VERIFIED]

[S43] Matthew Gaber, Mohiuddin Ahmed, Helge Janicke, “Zero day ransomware detection with Pulse: Function classification with Transformer models and assembly language,” *Computers & Security*, 2025. DOI: 10.1016/j.cose.2024.104167. Link: https://doi.org/10.1016/j.cose.2024.104167 [VERIFIED metadata · CANDIDATE coding]

[S44] Algimantas Venčkauskas, Vacius Jusas, Dominykas Barisas, “Zero-Day Ransomware Attack Detection Using Static Portable Executable Header Features,” *Applied Sciences*, 2025. DOI: 10.3390/app151910576. Link: https://doi.org/10.3390/app151910576 [VERIFIED]

[S45] Jamil Ispahany, Md Rafiqul Islam, M. Arif Khan et al., “iCNN-LSTM+: A Batch-Based Incremental Ransomware Detection System Using Sysmon,” *IEEE Access*, 2025. DOI: 10.1109/access.2025.3569635. Link: https://doi.org/10.1109/access.2025.3569635 [VERIFIED]

[S46] Abdullah Alqahtani, Mordecai Opoku Ohemeng, Frederick T. Sheldon, “An Intelligent Sensing Framework for Early Ransomware Detection Using MHSA-LSTM Machine Learning,” *Sensors*, 2026. DOI: 10.3390/s26030952. Link: https://doi.org/10.3390/s26030952 [VERIFIED]

[S47] Seetah Almarri, Ahmed Aljughaiman, “An ensemble machine learning framework for accurate ransomware detection and family classification using LightGBM and random forest,” *Scientific Reports*, 2026. DOI: 10.1038/s41598-026-65107-1. Link: https://doi.org/10.1038/s41598-026-65107-1 [VERIFIED]

[S48] Xiang Fang, Tarek Saadawi, “Artificial Intelligence-Powered Crypto Ransomware Detection,” *IEEE Access*, 2026. DOI: 10.1109/access.2026.3710149. Link: https://doi.org/10.1109/access.2026.3710149 [VERIFIED]

[S49] Anas AlMajali, Waleed Dweik, Yahia Abdelghafur et al., “Detecting Ransomware Through Dynamic API Call Monitoring and Machine Learning,” *Applied Sciences*, 2026. DOI: 10.3390/app16115232. Link: https://doi.org/10.3390/app16115232 [VERIFIED]

[S50] Ch Ram Mohan Reddy, R. V. Raghavendra Rao, Vishnuprasad et al., “Dual-use ambiguity in static ransomware detection: false positive analysis and confidence-gated mitigation,” *Scientific Reports*, 2026. DOI: 10.1038/s41598-026-67921-z. Link: https://doi.org/10.1038/s41598-026-67921-z [VERIFIED metadata · CANDIDATE coding]

[S51] Jiqiang Zhai, Zhonghui Zhai, Hong Miao et al., “Early Detection of Windows Crypto‐Ransomware Based on API Sequences and Deep Learning,” *Concurrency and Computation: Practice and Experience*, 2026. DOI: 10.1002/cpe.70813. Link: https://doi.org/10.1002/cpe.70813 [VERIFIED]

[S52] G. Kirubavathi, B. Padma Mayuri, S. Pranathasree et al., “Ensemble machine learning for proactive android ransomware detection using network traffic,” *Scientific Reports*, 2026. DOI: 10.1038/s41598-026-38271-7. Link: https://doi.org/10.1038/s41598-026-38271-7 [VERIFIED]

[S53] Auttapon Pomsathit, “Interpretable Pre-Ransomware Detection for SOCs Using SHAP and Lightweight ML,” *IEEE Access*, 2026. DOI: 10.1109/access.2026.3730303. Link: https://doi.org/10.1109/access.2026.3730303 [VERIFIED]

[S54] Hao Dai, Tianheng Qu, Yan Hu et al., “PE-Sleuth: Program-Level Semantics and Static Feature Fusion for Interpretable Ransomware Detection with LLMs,” *ICASSP 2026 - 2026 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2026. DOI: 10.1109/icassp55912.2026.11461664. Link: https://doi.org/10.1109/icassp55912.2026.11461664 [VERIFIED metadata · CANDIDATE coding]

[S55] Mohammed Rauf Ali Khan, Akram Algaolahi, Farid Binbeshr et al., “Sequence Learning over Behavioral Attack Patterns for Early Detection of Human-Operated Ransomware,” *Digital Threats: Research and Practice*, 2026. DOI: 10.1145/3786772. Link: https://doi.org/10.1145/3786772 [VERIFIED]

[S56] Fengkai Yuan, Lingbo Zhao, Zhilu Wang et al., “System-Wide Ransomware Attack Detection via Perturbation-Resilient Representation Learning,” *IEEE Transactions on Information Forensics and Security*, 2026. DOI: 10.1109/tifs.2026.3723705. Link: https://doi.org/10.1109/tifs.2026.3723705 [VERIFIED]

### 8.2 Secondary studies: surveys and SLRs (n = 18)

[R01] Eduardo Berrueta, Daniel Morato, Eduardo Magana et al., “A Survey on Detection Techniques for Cryptographic Ransomware,” *IEEE Access*, 2019. DOI: 10.1109/access.2019.2945839. Link: https://doi.org/10.1109/access.2019.2945839 [VERIFIED]

[R02] Lena Y. Connolly, David S. Wall, “The rise of crypto-ransomware in a changing cybercrime landscape: Taxonomising countermeasures,” *Computers & Security*, 2019. DOI: 10.1016/j.cose.2019.101568. Link: https://doi.org/10.1016/j.cose.2019.101568 [VERIFIED]

[R03] Routa Moussaileb, Nora Cuppens, Jean-Louis Lanet et al., “A Survey on Windows-based Ransomware Taxonomy and Detection Mechanisms,” *ACM Computing Surveys*, 2021. DOI: 10.1145/3453153. Link: https://doi.org/10.1145/3453153 [VERIFIED]

[R04] Shweta Sharma, Rakesh Kumar, C. Rama Krishna, “A survey on analysis and detection of Android ransomware,” *Concurrency and Computation: Practice and Experience*, 2021. DOI: 10.1002/cpe.6272. Link: https://doi.org/10.1002/cpe.6272 [VERIFIED]

[R05] Umara Urooj, Bander Ali Saleh Al-rimy, Anazida Zainal et al., “Ransomware Detection Using the Dynamic Analysis and Machine Learning: A Survey and Research Directions,” *Applied Sciences*, 2021. DOI: 10.3390/app12010172. Link: https://doi.org/10.3390/app12010172 [VERIFIED]

[R06] Abdullah Alqahtani, Frederick T. Sheldon, “A Survey of Crypto Ransomware Attack Detection Methodologies: An Evolving Outlook,” *Sensors*, 2022. DOI: 10.3390/s22051837. Link: https://doi.org/10.3390/s22051837 [VERIFIED]

[R07] Harun Oz, Ahmet Aris, Albert Levi et al., “A Survey on Ransomware: Evolution, Taxonomy, and Defense Solutions,” *ACM Computing Surveys*, 2022. DOI: 10.1145/3514229. Link: https://doi.org/10.1145/3514229 [VERIFIED]

[R08] Daryle Smith, Sajad Khorsandroo, Kaushik Roy, “Machine Learning Algorithms and Frameworks in Ransomware Detection,” *IEEE Access*, 2022. DOI: 10.1109/access.2022.3218779. Link: https://doi.org/10.1109/access.2022.3218779 [VERIFIED]

[R09] José Antonio Gómez Hernández, Pedro García Teodoro, Roberto Magán Carrión et al., “Crypto-Ransomware: A Revision of the State of the Art, Advances and Challenges,” *Electronics*, 2023. DOI: 10.3390/electronics12214494. Link: https://doi.org/10.3390/electronics12214494 [VERIFIED]

[R10] Kenan Begovic, Abdulaziz Al-Ali, Qutaibah Malluhi, “Cryptographic ransomware encryption detection: Survey,” *Computers & Security*, 2023. DOI: 10.1016/j.cose.2023.103349. Link: https://doi.org/10.1016/j.cose.2023.103349 [VERIFIED]

[R11] Amjad Alraizza, Abdulmohsen Algarni, “Ransomware Detection Using Machine Learning: A Survey,” *Big Data and Cognitive Computing*, 2023. DOI: 10.3390/bdcc7030143. Link: https://doi.org/10.3390/bdcc7030143 [VERIFIED]

[R12] Salwa Razaulla, Claude Fachkha, Christine Markarian et al., “The Age of Ransomware: A Survey on the Evolution, Taxonomy, and Research Directions,” *IEEE Access*, 2023. DOI: 10.1109/access.2023.3268535. Link: https://doi.org/10.1109/access.2023.3268535 [VERIFIED]

[R13] Latifa Albshaier, Seetah Almarri, M. M. Hafizur Rahman, “Earlier Decision on Detection of Ransomware Identification: A Comprehensive Systematic Literature Review,” *Information*, 2024. DOI: 10.3390/info15080484. Link: https://doi.org/10.3390/info15080484 [VERIFIED]

[R14] Jamil Ispahany, Md. Rafiqul Islam, Md. Zahidul Islam et al., “Ransomware Detection Using Machine Learning: A Review, Research Limitations and Future Directions,” *IEEE Access*, 2024. DOI: 10.1109/access.2024.3397921. Link: https://doi.org/10.1109/access.2024.3397921 [VERIFIED]

[R15] Mingcan Cen, Frank Jiang, Xingsheng Qin et al., “Ransomware early detection: A survey,” *Computer Networks*, 2024. DOI: 10.1016/j.comnet.2023.110138. Link: https://doi.org/10.1016/j.comnet.2023.110138 [VERIFIED]

[R16] Saleh Alzahrani, Yang Xiao, Sultan Asiri et al., “A Survey of Ransomware Detection Methods,” *IEEE Access*, 2025. DOI: 10.1109/access.2025.3556187. Link: https://doi.org/10.1109/access.2025.3556187 [VERIFIED]

[R17] Kalaivani Selvaraj, Manmeet Mahinderjit Singh, Zarul Fitri Zaaba, “A conceptual framework to mitigate ransomware attacks on IoMT devices using threat intelligence: a systematic literature review,” *Computer Science Review*, 2025. DOI: 10.1016/j.cosrev.2025.100801. Link: https://doi.org/10.1016/j.cosrev.2025.100801 [VERIFIED]

[R18] Wenjia Song, Sanjula Karanam, Ya Xiao et al., “Crypto-Ransomware and Their Defenses: In-Depth Behavioral Characterization, Discussion of Deployability, and New Insights,” *ACM Computing Surveys*, 2026. DOI: 10.1145/3798092. Link: https://doi.org/10.1145/3798092 [VERIFIED]

### 8.3 Methodological references

[M1] S. M. Lundberg, S.-I. Lee, "A Unified Approach to Interpreting Model Predictions," *Advances in Neural Information Processing Systems 30 (NeurIPS 2017)*, 2017. arXiv:1705.07874. Link: https://arxiv.org/abs/1705.07874 [VERIFIED via arXiv API; no DOI]

[M2] M. T. Ribeiro, S. Singh, C. Guestrin, "'Why Should I Trust You?': Explaining the Predictions of Any Classifier," *Proc. 22nd ACM SIGKDD (KDD '16)*, 2016. DOI: 10.1145/2939672.2939778. Link: https://doi.org/10.1145/2939672.2939778 [VERIFIED]

[M3] D. Arp et al., "Dos and Don'ts of Machine Learning in Computer Security," *31st USENIX Security Symposium*, 2022. arXiv:2010.09470. Link: https://arxiv.org/abs/2010.09470 ; https://www.usenix.org/conference/usenixsecurity22/presentation/arp [VERIFIED via arXiv API; no DOI]

[M4] A. Warnecke, D. Arp, C. Wressnegger, K. Rieck, "Evaluating Explanation Methods for Deep Learning in Security," *2020 IEEE European Symposium on Security and Privacy (EuroS&P)*, 2020. DOI: 10.1109/EuroSP48549.2020.00018. Link: https://doi.org/10.1109/EuroSP48549.2020.00018 [VERIFIED]

[M5] F. Pendlebury et al., "TESSERACT: Eliminating Experimental Bias in Malware Classification across Space and Time," *28th USENIX Security Symposium*, 2019. arXiv:1807.07838. Link: https://arxiv.org/abs/1807.07838 ; https://www.usenix.org/conference/usenixsecurity19/presentation/pendlebury [VERIFIED via arXiv API; no DOI]

[M6] M. J. Page, J. E. McKenzie, P. M. Bossuyt, I. Boutron et al., "The PRISMA 2020 statement: an updated guideline for reporting systematic reviews," *BMJ*, 372:n71, 2021. DOI: 10.1136/bmj.n71. Link: https://doi.org/10.1136/bmj.n71 [VERIFIED]

[M7] B. Kitchenham, O. Pearl Brereton, D. Budgen, M. Turner et al., "Systematic literature reviews in software engineering – A systematic literature review," *Information and Software Technology*, 51(1), 2009. DOI: 10.1016/j.infsof.2008.09.009. Link: https://doi.org/10.1016/j.infsof.2008.09.009 [VERIFIED]

### 8.4 Candidate publications requiring full-text confirmation before submission
- **Eligibility of the ML component:** [S02] RWGuard and [S10] Peeler (TLDR/metadata-coded; confirm that a trained classifier is part of the detection pipeline, otherwise move to Table 10 under EC4).
- **CANDIDATE coding (17 studies):** S01, S02, S10, S13, S14, S15, S18, S19, S21, S27, S31, S34, S38, S41, S43, S50, S54 — see the "Extraction basis" column of Table 8 for the authoritative list.
- **Venue status of LNCS chapters:** [S02] (RAID 2018) and [S10] (ESORICS 2021) — Crossref lists these as LNCS book chapters; the conference attribution is from the proceedings volumes and should be confirmed on the publisher page.
- **Quartile confirmation:** every journal in §4.4 for the paper's publication year.
