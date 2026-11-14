# Agentic AI for Automated Incident Response in Security Operations Centers: A Systematic Literature Review

**Manuscript type:** Systematic Literature Review (PRISMA 2020)
**Search window:** January 2021 – November 2026 (searches executed 14 November 2026)
**Corpus:** 26 primary studies (after quality gate) · 41 eligible studies (sensitivity set) · 11 secondary studies · 2 contextual studies
**Replication package:** `slr-agentic-soc/scripts/` and `slr-agentic-soc/data/`

> **Verification notice.** Every reference was retrieved from, and its DOI resolved against, the Crossref REST API at the time of writing; no preprint or arXiv-only work is cited. **[VERIFIED]** = authors, title, venue, year and DOI confirmed in Crossref *and* extraction from the full abstract. **[VERIFIED metadata · CANDIDATE coding]** = metadata confirmed, but the abstract was not exposed by open APIs (mostly Elsevier), so coding relied on the Semantic Scholar/SciSpace TL;DR and title; these must be re-coded from the full text. Journal quartiles were applied from the reviewers' SJR whitelist and must be re-confirmed on scimagojr.com for each paper's publication year before submission.

---

## Abstract

**Context.** Security Operations Centers (SOCs) face alert volumes and attack speeds that exceed human capacity. Agentic AI — systems that perceive, plan, reason, use tools and execute actions toward a goal — promises to automate incident response (IR), but autonomy without safety and governance is itself a risk.
**Objective.** To systematically characterise agentic AI for automated SOC incident response (2021–2026) along architectures and autonomy (RQ1), automated IR tasks and their evaluation (RQ2), integration with SOC tooling, analysts, and safety/governance mechanisms (RQ3), and open gaps (RQ4).
**Method.** PRISMA 2020-compliant review. Forty search strings were executed against Crossref (indexing IEEE, ACM, Elsevier, Springer Nature, MDPI and Wiley), yielding 1,169 unique records, plus 43 known-item/snowball look-ups verified in Crossref. Records were filtered by document type, a Q1/Q2 journal whitelist and a top-tier conference list; preprints and workshops were excluded. A five-criterion quality instrument (autonomy, evaluation rigour, reproducibility, safety, deployment readiness; 0–10, threshold ≥ 4) was applied.
**Results.** 41 studies were eligible and 26 passed the quality gate; 14 of the 26 (54%) were published in 2026, showing an emerging field. Reinforcement-learning (RL) agents (13/26) and LLM-based or LLM–RL hybrid agents (13/26) are equally represented. Full autonomy (A4) is the most common level (12/26, 46%), but **every fully autonomous agent was evaluated only in simulation or emulation — none in a production SOC**. Containment dominates the automated tasks (18/26, 69%); triage (2), reporting (2) and response planning (2) are rare, and **no study automates the end-to-end IR lifecycle**. **7/26 (27%) report no safety mechanism**, only **one** uses an explicit human approval gate, only **one** includes a human-expert evaluation, and **no included LLM agent reports an evaluation against prompt injection**. Mean deployment-readiness score is 0.50/2.
**Conclusions.** Agentic SOC IR research has produced capable agents in simulated environments but not yet trustworthy, governable agents in operational SOCs. We contribute an original five-axis taxonomy (ATLAS-IR) with graded autonomy and safety-assurance levels, a scripted and verifiable PRISMA pipeline, and seven evidence-backed gaps with future directions.

**Keywords:** agentic AI; LLM agents; autonomous cyber defence; security operations center; incident response; SOAR; reinforcement learning; human-in-the-loop; AI safety; governance; systematic literature review

---

## 1. Introduction

### 1.1 Motivation
SOC analysts triage, investigate, contain and remediate incidents under severe time pressure. The ingestion of telemetry from SIEM, EDR, network and cloud sources has outpaced human capacity, a condition widely described as *alert fatigue* [P04]. Conventional automation — Security Orchestration, Automation and Response (SOAR) — encodes response logic in static playbooks that are brittle, hard to scale, and unable to reason over novel incidents [P12, R01]. Two families of learning agents now promise to close this gap: **reinforcement-learning (RL) agents** that learn response policies by interacting with a (simulated) environment [P02, P06, P07], and **large-language-model (LLM) agents** that plan, call tools and generate response actions from natural-language knowledge [P09, P11, P20].

### 1.2 Why SOC incident response is important
Incident response determines the eventual cost of an intrusion: delays in containment allow lateral movement and data loss, while wrong actions disrupt legitimate business operations. In operational technology and cyber-physical systems, a wrong response can also cause physical harm [P15, P25].

### 1.3 Why agentic AI matters
Agentic systems go beyond classification. They can decompose an incident into steps, gather evidence with tools, reason about hypotheses, and take or recommend actions (e.g., firewall rules, host isolation, service restoration) [P09, P12, P15]. This is the first AI paradigm that can, in principle, automate the *decision and action* layer of a SOC rather than only the *detection* layer.

### 1.4 Why autonomy matters
The value of automation scales with autonomy: an agent that only recommends saves analyst time but not response time; an agent that acts within seconds can contain fast-moving attacks. Hammar and colleagues formalise the timing of response decisions as optimal stopping problems, showing that *when* to act is itself a learnable decision [P02, P06].

### 1.5 Why safety and governance matter
Autonomy amplifies errors. LLM agents hallucinate, and an incident narrative that cites real events can still be wrong in every causal relation, leading to "isolating the wrong controller or revoking a legitimate operator" [P15]. RL agents may overreact to manipulated telemetry [P16]. LLM-based analysis of untrusted evidence is vulnerable to instructions embedded in that evidence (indirect prompt injection) [C2]. Governance — who authorises which action, under what constraints, with what audit trail — is therefore a first-class requirement, not an add-on.

### 1.6 Problem statement
Despite rapid growth, it is unclear (i) which agent architectures achieve which levels of autonomy, (ii) which IR tasks they actually automate and how convincingly this is evaluated, (iii) how agents are integrated with SOC tools and analysts and constrained by safety and governance mechanisms, and (iv) what prevents deployment in real SOCs.

### 1.7 Research gap
Existing secondary studies (Section 3) review LLMs in cybersecurity broadly [R03, R05, R06], LLM-based agents across all security functions including offensive uses [R10], agentic AI for IoT security [R08], AI-driven SIEM–SOAR integration [R09], and intrusion-response systems for cyber-physical systems [R02]. None of the 11 secondary studies we identified (i) restricts the evidence base to peer-reviewed, Q1/Q2-journal or top-tier-conference studies of agents that *execute or plan* SOC IR actions, (ii) unifies RL-based autonomous cyber-defence agents and LLM agents under a common autonomy scale, and (iii) grades each study's safety-assurance and deployment readiness.

### 1.8 Contributions
1. A **PRISMA 2020-compliant, scripted and DOI-verified SLR** of agentic AI for SOC IR (2021–2026) that excludes preprints and workshops.
2. A **unified autonomy scale (A1–A4)** applied consistently to RL and LLM agents, and a five-criterion **quality instrument** focused on autonomy, rigour, reproducibility, safety and deployment readiness.
3. **ATLAS-IR**, an original five-axis taxonomy (Autonomy, Task, Learning/architecture, Assimilation of tools, Safety assurance) with graded Safety-Assurance Levels.
4. **Seven evidence-backed research gaps** with concrete directions.

### 1.9 Research questions
- **RQ1:** Which agentic AI architectures and techniques are used for automated incident response in Security Operations Centers (SOCs), and what levels of autonomy do they achieve?
- **RQ2:** Which SOC incident response tasks (triage, investigation, containment, remediation, reporting) are automated by agentic AI systems, and how are they evaluated?
- **RQ3:** How do agentic AI systems integrate with SOC tools, data sources, and human analysts, and what safety and governance mechanisms are used?
- **RQ4:** What are the main gaps in autonomy, safety, evaluation, and real-world deployment of agentic AI for SOC incident response?

---

## 2. Background

### 2.1 Agentic AI
We define an **agentic AI system** as one that, given a goal, (i) perceives an environment through observations or tools, (ii) plans or selects a sequence of actions, (iii) executes or proposes those actions, and (iv) updates its behaviour from feedback — with some degree of autonomy from human direction. This definition is architecture-neutral: it covers LLM-based agents and learned sequential decision-makers (RL agents) alike, which is why both are in scope.

### 2.2 LLM-based agents
An **LLM-based agent** uses a large language model as its reasoning core, typically in a loop of *thought → tool call → observation* (e.g., ReAct-style), with memory and access to tools such as log queries, threat-intelligence look-ups or configuration APIs [P09, P21, P23].

### 2.3 Multi-agent systems
A **multi-agent system (MAS)** decomposes the task among cooperating agents with distinct roles (e.g., planner, investigator, verifier) or among distributed defenders (multi-agent RL, MARL) [P09, P16, P24, P17].

### 2.4 SOC incident response
Following the canonical IR lifecycle (preparation; detection and analysis; containment, eradication and recovery; post-incident activity), we use five operational **SOC IR tasks**: **triage** (prioritise and route alerts), **investigation** (gather evidence, reconstruct attack chains, hunt), **containment** (stop spread: block, isolate, quarantine), **remediation/recovery** (restore services, eradicate, harden), and **reporting** (explain, document, communicate). We additionally code **response planning** (generating an action plan without executing it).

### 2.5 Autonomy levels
| Level | Name | Definition used in this review |
|---|---|---|
| **A1** | Assistance | The agent analyses or recommends; humans decide and act |
| **A2** | Human-in-the-loop | The agent proposes concrete actions or priorities that a human approves or applies |
| **A3** | Bounded autonomy | The agent executes actions itself, but only within explicit constraints, gates, allow-lists or admissible-action sets |
| **A4** | Full autonomy | The agent executes actions without human approval or explicit action constraints (in the included studies, always within a simulated or emulated environment) |

### 2.6 Traditional ML vs LLM assistants vs conventional SOAR vs agentic AI
| Paradigm | What it does | Decision authority | Adaptivity |
|---|---|---|---|
| Traditional ML | Classifies/scores (detection, anomaly) | None — outputs labels | Retraining |
| LLM assistant (copilot) | Answers analyst questions, summarises | Human | Prompting |
| Conventional SOAR | Executes pre-written playbooks | Playbook author | Manual playbook edits |
| **Agentic AI** | Plans, uses tools, selects and executes/proposes actions | Shared (A1–A4) | Learning, in-context reasoning, planning |

### 2.7 RAG, tool use and agent orchestration
- **Retrieval-augmented generation (RAG):** the LLM conditions on documents retrieved at query time (CTI reports, runbooks, past incidents) to ground its output [P08, P26].
- **Tool use:** the agent invokes external functions (SIEM queries, CTI APIs, firewall/SDN controllers) and incorporates their results [P08, P01].
- **Agent orchestration:** a controller sequences agents or steps, enforces order and checks (e.g., investigation → validation → monitoring in [P12]; step-wise orchestration that suppresses hallucination in [P23]).

---

## 3. Related Work: Existing Surveys and SLRs

Our searches retrieved **11 secondary studies** in eligible venues. Table 1 summarises them. "Papers" is the number reported in the abstract (*n/s* = not stated there). Limitations are judged **relative to this review's focus**.

**Table 1. Secondary studies used for positioning (all [VERIFIED]; references in §8.2).**

| ID | Authors (year), venue | Scope | Papers | Limitations relative to our focus | How this SLR differs |
|---|---|---|---|---|---|
| R01 | Islam, Babar & Nepal (2019), *ACM CSUR* | Multivocal review of security orchestration (academic + grey literature, 2007–2017) | n/s | Pre-dates LLM and modern RL agents; includes grey literature | Learning agents only; 2021–2026; peer-reviewed only |
| R02 | Bashendy, Tantawy & Erradi (2023), *Computers & Security* | Intrusion-response systems for cyber-physical systems | n/s | CPS-specific; not agentic/LLM-focused; no autonomy scale | Unified autonomy scale across RL and LLM agents |
| R03 | Hasanov et al. (2024), *IEEE Access* | LLMs in cybersecurity (offensive, defensive, governance), 2018–2024 | 177 | Broad; not IR- or agent-specific | IR-specific, agent-specific |
| R04 | Ferrag et al. (2025), *Internet of Things and Cyber-Physical Systems* | Generative AI / LLM applications and vulnerabilities in cybersecurity | n/s | Broad; abstract not openly available for verification of scope | IR-specific; quality-scored |
| R05 | Ding et al. (2025), *Applied Soft Computing* | LLMs for cyber resilience | n/s | Broad resilience lens; no autonomy/safety grading | Autonomy and safety grading |
| R06 | Zhang et al. (2025), *Cybersecurity* | LLMs in cybersecurity: construction, applications, challenges | >300 | Includes many preprints; not agent- or IR-specific | Peer-reviewed only; IR agents |
| R07 | Ekelhart et al. (2026), *ICT Express* | LLMs in cyber threat intelligence; regulation-aware architecture | n/s | CTI rather than IR execution | IR actions and governance of execution |
| R08 | Nageshwaran & Ezekiel (2026), *Electronics* | Agentic AI and LLMs for autonomous **IoT** cybersecurity (PRISMA; IEEE/ACM/MDPI) | 153 (2020–2026) | IoT-specific; three publishers; action scope includes detection and vulnerability discovery | SOC IR scope; six publishers; quality gate; safety-assurance levels |
| R09 | El-Attar, Attar & El-Hajj (2026), *Array* | SLR of AI-driven SIEM–SOAR integration in SOCs | n/s (abstract not openly available) | SIEM–SOAR integration lens; autonomy and safety grading not evident from metadata | Agent architectures, autonomy scale and safety grading |
| R10 | Fatouros et al. (2026), *Journal of Cybersecurity and Privacy* | LLM-based agents for cybersecurity across functions (PRISMA; Jan 2022–Apr 2026) | 59 | Sources resolve predominantly to arXiv (preprints included); LLM agents only (no RL agents); covers offensive functions (penetration testing) | Preprints excluded; RL and LLM agents unified; defensive IR only |
| R11 | Sammartino (2026), *Knowledge-Based Systems* | Security threats to and defences of LLM-driven agentic/multi-agent systems | n/s | Security *of* agents, not agents *for* IR | Uses its threat lens to assess IR agents (RQ3) |

**Positioning.** Three recent works overlap substantially with ours — R08 (agentic AI for IoT security), R09 (AI-driven SIEM–SOAR in SOCs) and R10 (LLM-based agents for cybersecurity, including SOC automation). We therefore **do not claim to be the first review** of agentic AI in cybersecurity or in SOCs. Our distinct contribution is the combination of: (a) a **peer-reviewed-only** evidence base (no preprints, no workshops) restricted to Q1/Q2 journals and top-tier conferences; (b) **joint coverage of RL-based autonomous cyber-defence agents and LLM agents** under one autonomy scale; (c) **per-study grading** of autonomy, safety assurance and deployment readiness; and (d) a **defensive IR-only** scope that excludes phishing, ransomware/malware detection and vulnerability detection.

---

## 4. Methodology (PRISMA 2020)

The review follows PRISMA 2020 [M1] and Kitchenham et al.'s SLR guidance [M2]. All steps are scripted and archived.

### 4.1 Search strategy and sources
**Primary source — Crossref REST API.** Crossref registers DOIs for IEEE, ACM, Elsevier, Springer Nature, MDPI and Wiley, so it covers all permitted publishers in one index and returns resolvable DOIs needed for verification. Query mode `query.bibliographic`; filter `from-pub-date:2021-01-01, until-pub-date:2026-12-31`; first 200 relevance-ranked results per string. A record was kept only if its **title** matched both an *agent/automation* pattern (`agent|autonom|llm|large language|gpt|generative|soar|orchestrat|copilot|reinforcement|self-healing|chatbot|language model`) and a *security-response* pattern (`incident|SOC|security operation|cyber defen*|response|alert|triage|threat hunt|intrusion|cybersecurity|network defen*|attack|threat`).

**Round 1 (25 strings):**
```
agentic AI incident response security operations center | LLM agent security operations center
large language model agents incident response            | autonomous incident response cyber security
autonomous cyber defense agent reinforcement learning    | multi-agent system cyber incident response
AI agent alert triage security operations                | large language model security operations center automation
SOAR security orchestration automation response machine learning
automated intrusion response system reinforcement learning | LLM threat hunting autonomous agent
retrieval augmented generation incident response cybersecurity
large language model cyber threat intelligence agent
autonomous cyber operations deep reinforcement learning defender
human-AI teaming security operations center              | LLM-based agent cybersecurity tool use
automated incident handling playbook generation large language model
self-healing network autonomous response attack          | agentic AI cybersecurity survey
large language models cybersecurity survey               | AI security operations center survey
automated cyber incident response survey                 | autonomous network defense agent
LLM log analysis incident investigation                  | generative AI security operations
```
**Round 2 (15 strings, run after round-1 screening to close vocabulary gaps):**
```
agentic artificial intelligence cyber defense          | intrusion response system deep reinforcement learning
automated intrusion response optimal policy            | autonomous security operations center
LLM agent security alert investigation                 | large language model incident response automation
cyber defense agent CybORG reinforcement learning       | multi-agent reinforcement learning network defense
self-adaptive security response attack mitigation reinforcement learning
moving target defense reinforcement learning autonomous | large language model SOC analyst
AI agents security orchestration playbooks
autonomous response advanced persistent threat reinforcement learning
LLM digital forensics incident investigation agent      | reinforcement learning cyber attack mitigation software defined network
```

**Database-specific strings for replication** (IEEE Xplore, ACM DL, ScienceDirect, SpringerLink, MDPI, Wiley, Scopus, Web of Science). These were **not executed in this run** because those portals were not reachable from the review environment (Section 12.1). Scopus syntax:
```
TITLE-ABS-KEY ( ( "agentic" OR "AI agent*" OR "LLM agent*" OR "language model agent*" OR "multi-agent"
     OR "autonomous agent*" OR "autonomous cyber defen*" OR "reinforcement learning" OR "large language model*" )
  AND ( "incident response" OR "intrusion response" OR "security operation* center*" OR "security operation* centre*"
     OR SOC OR SOAR OR "alert triage" OR "threat hunting" OR "attack investigation" OR "cyber defen*" ) )
AND PUBYEAR > 2020 AND PUBYEAR < 2027
AND ( LIMIT-TO ( DOCTYPE , "ar" ) OR LIMIT-TO ( DOCTYPE , "cp" ) OR LIMIT-TO ( DOCTYPE , "re" ) )
AND NOT TITLE-ABS-KEY ( phishing OR ransomware OR "malware detection" OR "vulnerability detection" OR "penetration test*" )
```
Web of Science: `TS=(("agentic" OR "LLM agent*" OR "autonomous cyber defen*" OR "reinforcement learning" OR "large language model*") AND ("incident response" OR "intrusion response" OR "security operation* cent*" OR SOAR OR "alert triage" OR "threat hunting")) NOT TS=(phishing OR ransomware OR "malware detection" OR "vulnerability detection") AND PY=(2021-2026)`.
IEEE Xplore: `(("All Metadata":agentic OR "All Metadata":"LLM agent" OR "All Metadata":"autonomous cyber defense" OR "All Metadata":"reinforcement learning") AND ("All Metadata":"incident response" OR "All Metadata":"intrusion response" OR "All Metadata":"security operations center" OR "All Metadata":SOAR))`, years 2021–2026.

**Supplementary search.** (i) 43 title look-ups in Crossref for works cited by surveys or surfaced by five SciSpace semantic searches (used only for *discovery*; every candidate was then verified in Crossref and subjected to the same venue rules); (ii) backward snowballing from the surveys.

### 4.2 Inclusion criteria
- **IC1** Peer-reviewed journal article or main-track conference paper, 2021–2026.
- **IC2** Proposes or evaluates an **agentic** system — an LLM agent, multi-agent system, RL/game-theoretic agent, or planner — that **plans, selects, executes or orchestrates incident-response actions or investigation steps** in a security context.
- **IC3** Q1/Q2 journal (SJR) from IEEE, ACM, Elsevier, Springer Nature, MDPI or Wiley, **or** main track of IEEE S&P, USENIX Security, CCS, NDSS, ACSAC, DIMVA, RAID, ESORICS, ICSE, ASE, FSE, ICASSP, GLOBECOM, DSN or INFOCOM.
- **IC4** English, with a resolvable DOI.

### 4.3 Exclusion criteria
- **EC1** Preprints, arXiv-only papers, workshops (including ACSAC/S&P workshops), posters, book chapters (except LNCS main-track proceedings of listed conferences), theses, magazines.
- **EC2** Topics outside scope: phishing, ransomware detection, malware analysis, vulnerability detection, offensive/penetration-testing agents.
- **EC3** Non-security "incidents" (IT operations, SRE, vehicle software faults).
- **EC4** Not agentic: detection-only models, LLM assistants/copilots without planning, tool use or action selection, descriptive usage studies.
- **EC5** Secondary studies (routed to Related Work).
- **EC6** Publisher outside the six permitted, or journal below Q2 / not whitelisted.
- **EC7** Quality score < 4/10.

### 4.4 Screening process
1. Automated harvest and de-duplication by DOI.
2. Automated record-type screening (journal/proceedings articles only) and venue screening (`screen.py`: journal whitelist; conference-title pattern for the 15 listed conferences — this excludes workshops whose container titles name the conference, which were removed manually under EC1).
3. Manual title/abstract screening against IC/EC.
4. Eligibility assessment on abstracts (Crossref, Semantic Scholar, SciSpace).
5. Quality assessment and EC7.
Screening was performed by one reviewer with deterministic scripts as a first pass (see §12.1).

### 4.5 Quality assessment criteria (0 / 1 / 2 each; maximum 10)

| Code | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| **AU** | Autonomy level | Recommendation only, or autonomy unclear | Human-in-the-loop, or autonomy demonstrated only in an abstract simulator | Bounded/full autonomy demonstrated on emulated or real infrastructure or real attack data, with explicit boundaries |
| **ER** | Evaluation rigour | Single scenario, no baseline | Baselines or benchmark dataset | Multiple scenarios/datasets, strong baselines, ablation, statistical or expert evaluation |
| **RP** | Reproducibility | Private data/environment | Public benchmark or dataset (e.g., CAGE/CybORG, OpTC, CERT, UNSW-NB15) | Public benchmark **and** released code/environment |
| **SF** | Safety & governance | None | One mechanism (constraints, grounding, XAI, privacy, robustness) | Explicit safety/governance contribution (verification, safe RL, response gate, human approval, abstention) with evaluation |
| **DP** | Deployment readiness | Simulation only | Emulation/testbed, real infrastructure components, or latency/overhead measured | Production SOC or live operational deployment |

### 4.6 Data extraction form
Bibliographic data; **architecture** (LLM single agent, LLM multi-agent, RAG pipeline, LLM–RL hybrid, single-agent DRL, MARL, game-theoretic RL, MDP planner, neuro-symbolic/verifier); **autonomy level** (A1–A4); **SOC tasks** (triage, investigation, containment, remediation, planning, reporting); **evaluation environment** (simulator, emulation/testbed, offline dataset, human-expert evaluation, production); **tool/data integration** (SIEM/SOAR/IDS alerts, host/provenance logs, CTI, knowledge graph/vector store, SDN, firewall, digital twin); **safety/governance mechanisms** (action constraints, formal/deterministic verification or gates, safe RL, XAI, abstention/consistency checks, evidence grounding, privacy, human approval, robustness evaluation); **QA scores**; extraction basis. The coded form is `scripts/extract.py`.

### 4.7 PRISMA flow (textual description of Figure 1)
```
IDENTIFICATION
  Crossref records, round 1 (25 strings) ................................................. n = 875
  Crossref records, round 2 (15 strings), new after de-duplication ....................... n = 294
  Unique database records ................................................................ n = 1,169
  Known-item / snowball look-ups verified in Crossref ................................... n = 43
SCREENING
  Removed by record type (posted content 211, book chapters 80, peer-review reports 38, other 24) n = 353
  Records screened on venue (journal/proceedings articles) .............................. n = 816
    Excluded: journal not Q1/Q2-whitelisted, publisher not permitted, or conference not top-tier n = 688
  Records screened on title/abstract .................................................... n = 128
    Excluded (EC2 out of scope, EC3 non-security incidents, EC4 detection-only/not agentic) n = 81
  Added from look-ups after identical checks (29 of 43 failed venue/type/scope checks) ... n = 14
ELIGIBILITY
  Reports assessed for eligibility ....................................................... n = 61
    Secondary studies → Related Work (EC5) ............................................... n = 11
    Primary candidates excluded with reasons (EC1 2, EC3 3, EC4 4) ...................... n = 9
  Eligible primary studies (sensitivity set) ............................................ n = 41
QUALITY GATE
    Excluded for QA < 4 (EC7) ............................................................ n = 15
INCLUDED
  Primary studies in synthesis ........................................................... n = 26
  Secondary studies ...................................................................... n = 11
  Contextual studies (excluded as primary, cited for RQ3 context) ........................ n = 2
```
Excluded-with-reason and below-threshold studies are listed with DOIs in Tables 9 and 10.

---

## 5. Results

### 5.0 Corpus overview
**Years (n = 26):** 2022: 2 · 2023: 1 · 2024: 3 · 2025: 6 · 2026: 14. Over half of the evidence base is from 2026, and LLM-based agents appear only from 2025. **Venues:** IEEE TNSM (3), IEEE TDSC (2), Applied Sciences (4), Computer Networks (2), and single papers in IEEE TIFS, IEEE TII, IEEE TCE, IEEE TNSE, IEEE Intelligent Systems, Computers & Security, ESWA, Electronics, Information, Scientific Reports, plus four top-tier conference papers (NDSS 2026, ACSAC 2025, ESORICS 2026, DSN 2026) and GLOBECOM 2025.

**Table 2. Data extraction for the 26 included studies.** Architecture codes as in §4.6; autonomy A1–A4 as in §2.5. Tasks: TRI triage, INV investigation, CON containment, REM remediation/recovery, PLN planning, REP reporting. Evaluation: SIM simulator, EMU emulation/testbed, DS offline dataset, HUM human-expert evaluation. Integration: LOG host/provenance logs, KG knowledge graph/vector store, SIEM alerts/SOAR, CTI, SDN. Safety: CONSTR constraints, VER verification/gate, SRL safe RL, XAI, ABST abstention/consistency, GRD grounding, PRIV privacy, HUM human approval, ROB robustness evaluation.

| ID | Year | Venue | Architecture | Autonomy | SOC tasks | Evaluation | Tool / data integration | Safety & governance |
|---|---|---|---|---|---|---|---|---|
| P01 | 2022 | IEEE Transactions on Network and S | DRL | A4 Full | CON | EMU | SDN | CONSTR |
| P02 | 2022 | IEEE Transactions on Network and S | GT | A4 Full | CON | EMU | — | — |
| P03 | 2023 | Applied Sciences | DRL | A4 Full | CON | EMU | SDN | — |
| P04 | 2024 | Computers & Security | DRL | A2 HITL | TRI | DS | SIEM | — |
| P05 | 2024 | IEEE Transactions on Industrial In | DRL | A3 Bounded | CON | SIM | — | XAI, CONSTR |
| P06 | 2024 | IEEE Transactions on Network and S | GT | A4 Full | CON | EMU | — | — |
| P07 | 2025 | IEEE Transactions on Information F | GT | A4 Full | CON, REM | EMU | — | ROB |
| P08 | 2025 | GLOBECOM 2025 - 2025 IEEE Global C | RAG | A1 Assist | INV, PLN | DS, HUM | SIEM, CTI, KG | GRD |
| P09 | 2025 | 2025 IEEE Annual Computer Security | LLM-MA | A3 Bounded | INV | DS | LOG | — |
| P10 | 2025 | Computer Networks | HYB | A3 Bounded | CON, REP | SIM | SDN, KG | CONSTR, XAI |
| P11 | 2025 | IEEE Intelligent Systems | LLM-SA | A4 Full | CON | SIM | — | XAI |
| P12 | 2025 | Information | LLM-SA | A3 Bounded | INV, CON, REM | EMU | SIEM | VER, HUM |
| P13 | 2026 | IEEE Transactions on Network Scien | HYB | A4 Full | CON | SIM | — | — |
| P14 | 2026 | IEEE Transactions on Dependable an | HYB | A4 Full | CON, REM | SIM | — | ROB |
| P15 | 2026 | Applied Sciences | NS | A3 Bounded | INV, CON | EMU | LOG, KG | VER, GRD, CONSTR |
| P16 | 2026 | Expert Systems with Applications | MARL | A3 Bounded | INV, CON | DS | LOG | CONSTR, XAI |
| P17 | 2026 | Applied Sciences | MARL | A4 Full | CON | SIM | CTI | PRIV, ROB |
| P18 | 2026 | IEEE Transactions on Dependable an | DRL | A4 Full | CON | SIM | — | VER |
| P19 | 2026 | 2026 56th Annual IEEE Internationa | DRL | A4 Full | CON | SIM | — | ROB |
| P20 | 2026 | Proceedings 2026 Network and Distr | HYB | A1 Assist | PLN, REM | DS | LOG, KG | ABST, GRD |
| P21 | 2026 | Applied Sciences | LLM-SA | A1 Assist | TRI, INV | DS | LOG, KG | GRD, CONSTR |
| P22 | 2026 | Scientific Reports | PLAN | A2 HITL | INV | DS | LOG | CONSTR |
| P23 | 2026 | Electronics | LLM-MA | A1 Assist | INV, REP | DS | LOG | GRD, CONSTR |
| P24 | 2026 | ESORICS 2026 (LNCS) | LLM-MA | A3 Bounded | INV | DS | LOG | — |
| P25 | 2026 | IEEE Transactions on Consumer Elec | DRL | A3 Bounded | CON | SIM | — | SRL |
| P26 | 2026 | Computer Networks | HYB | A4 Full | CON | SIM | KG | GRD |

**Table 3. Distinguishing characteristics of each included study.**

| ID | Short title | Key characteristics (from abstract) |
|---|---|---|
| P01 | DeepAir: Deep Reinforcement Learning for Adaptive Intrusion … | minimises benign-traffic impact; ~85% attack packets dropped |
| P02 | Intrusion Prevention Through Optimal Stopping | optimal stopping; simulation + emulation system |
| P03 | Reinforcement Learning as a Path to Autonomous Intelligent C… | CAN-bus agent on PASTA hardware testbed; 90% cyber resilience |
| P04 | Combating alert fatigue with AlertPro: Context-aware alert p… | RL alert prioritisation; +30% attack discovery; <0.5 s |
| P05 | Interpretable Cross-Layer Intrusion Response System Based on… | DRL distilled into decision trees; physical-domain policies |
| P06 | Learning Near-Optimal Intrusion Responses Against Dynamic At… | fictitious self-play vs dynamic attacker |
| P07 | Adaptive Security Response Strategies Through Conjectural On… | conjectural online learning under model misspecification; testbed |
| P08 | Advancing Autonomous Incident Response: Leveraging LLMs and … | hybrid CTI retrieval + external CTI platform queries; expert cross-validation |
| P09 | Clouseau: A Hierarchical Multi-Agent Approach for Autonomous… | hierarchical agents; DARPA OpTC + ATLAS; F1 99.78% single-host |
| P10 | Design and evaluation of an Autonomous Cyber Defence agent u… | DRL actuation + LLM + rule-based; KG chatbot for human experts |
| P11 | Leveraging Large Language Models for Autonomous Cyber Defens… | LLM agent on CAGE-2; par with best RL agent |
| P12 | Toward Robust Security Orchestration and Automated Response … | agentic-LLM SOAR; IVAM investigation-validation-active monitoring |
| P13 | Cyber Task Automation With Knowledge-Infused Reinforcement L… | LLM-guided RL; >75% faster convergence |
| P14 | Enhancing Cloud Network Resilience via a Robust LLM-Empowere… | LLM-empowered MARL; +68.5% availability |
| P15 | EviGuard: Machine-Verifiable Evidence Grounding for LLM-Base… | LLM proposes hypotheses; deterministic verifiers; response gate |
| P16 | Explainable autonomous cyber defense using adversarial multi… | causal DAG restricts admissible responses |
| P17 | FedMARL-LTI: Federated Multi-Agent Reinforcement Learning wi… | LLM-summarised DP semantic embeddings; Byzantine robustness |
| P18 | Formal Modeling and Verification of Deep Reinforcement Learn… | probabilistic model checking of DRL ACD policies |
| P19 | Generalizable Graph-based Reinforcement Learning Agents for … | graph observations; zero-shot transfer to new networks |
| P20 | Incident Response Planning Using a Lightweight Large Languag… | fine-tuned lightweight LLM + retrieval + lookahead planning; up to 22% shorter recovery |
| P21 | Insider Threat Detection and Evidence-Grounded Triage Using … | constrained ReAct-style agent; CERT r4.2 |
| P22 | Leveraging reinforcement learning for an efficient windows r… | DP planner with bounded RL refinement for forensic registry analysis |
| P23 | Local LLM-Based Cyber Incident Analysis in Air-Gapped Networ… | air-gapped local LLM; agent orchestration suppresses hallucination; Atomic Red Team |
| P24 | Minos: A Multi-agent Collaborative Framework for Provenance-… | provenance backward tracking; 14 scenarios, 5 public datasets |
| P25 | Safety-Aware Intrusion Response System Based on Safe Reinfor… | CMDP safety cost; safety cost 5.07 -> 0 |
| P26 | Towards generic defensive cyber agents: Leveraging large lan… | RAG over RL observation-action tuples; few-shot |

### 5.1 RQ1 — Architectures, techniques and autonomy levels

**Architectures (n = 26).** Two paradigms are equally represented:
- **RL-family agents — 13 (50%)**: single-agent deep RL 7 [P01, P03, P04, P05, P18, P19, P25]; game-theoretic/optimal-stopping RL 3 [P02, P06, P07]; multi-agent RL 2 [P16, P17]; MDP/dynamic-programming planner with bounded RL 1 [P22].
- **LLM-involving agents — 13 (50%)**: LLM–RL hybrids 5 [P10, P13, P14, P20, P26]; single LLM agents 3 [P11, P12, P21]; LLM multi-agent systems 3 [P09, P23, P24]; RAG pipeline 1 [P08]; neuro-symbolic LLM + deterministic verifiers 1 [P15].

In the sensitivity set (n = 41) RL dominates (DRL 17, MARL 6, game-theoretic 3), i.e., the quality gate removed proportionally more RL papers evaluated only in bespoke simulators.

**Techniques.** RL agents formalise response as an MDP/POMDP and learn policies with DQN/DDQN [P01], PPO-style methods on graph observations [P19], fictitious self-play against adaptive attackers [P06], threshold policies via stochastic approximation [P02], conjectural online learning under model misspecification [P07], constrained MDPs for safety [P25], and decision-tree distillation for interpretability [P05]. LLM agents use hierarchical multi-agent decomposition for investigation [P09, P24], constrained ReAct-style reasoning with evidence retrieval [P21], agent orchestration to suppress hallucination in air-gapped deployments [P23], RAG over CTI [P08], and code generation within SOAR [P12]. **Hybrids** use LLMs to guide RL exploration and accelerate convergence by more than 75% [P13], retrieve RL observation–action tuples for few-shot generalisation [P26], empower MARL to adapt to changing cloud topologies [P14], combine DRL actuation with an LLM/knowledge-graph interface to humans [P10], or fine-tune a lightweight LLM and add lookahead planning to reduce hallucination [P20].

**Table 4. Autonomy level by architecture (n = 26).**

| Autonomy | n | % | Architectures (counts) | Studies |
|---|---|---|---|---|
| A1 Assistance | 4 | 15% | RAG 1, LLM–RL hybrid 1, LLM single 1, LLM multi 1 | P08, P20, P21, P23 |
| A2 Human-in-the-loop | 2 | 8% | DRL 1, planner 1 | P04, P22 |
| A3 Bounded autonomy | 8 | 31% | DRL 2, LLM multi 2, hybrid 1, LLM single 1, neuro-symbolic 1, MARL 1 | P05, P09, P10, P12, P15, P16, P24, P25 |
| A4 Full autonomy | 12 | 46% | DRL 4, game-theoretic 3, hybrid 3, LLM single 1, MARL 1 | P01, P02, P03, P06, P07, P11, P13, P14, P17, P18, P19, P26 |

**Finding RQ1.1 — autonomy is highest where realism is lowest.** All 12 A4 studies were evaluated in simulators (7) or emulation/testbeds (5); none in an operational SOC. Conversely, the LLM agents that operate on real attack data (DARPA OpTC/ATLAS [P09], public provenance datasets [P24], CERT [P21], Atomic Red Team [P23]) are at A1 or A3 and mostly perform investigation rather than containment.

**Finding RQ1.2 — LLMs are entering as policy priors, not only as chat interfaces.** An LLM agent matched the best RL agent on the CAGE-2 challenge [P11]; LLM guidance accelerates RL convergence [P13]; and RAG over RL experience supports transfer to unseen adversaries [P26]. These results suggest LLMs reduce the training cost and brittleness of RL agents, the main criticisms of RL-only autonomous defence.

**Finding RQ1.3 — generalisation is the main RL frontier.** Graph-structured observations enabling zero-shot adaptation to new networks [P19] and conjecture-based learning under model misspecification [P07] address the "trained on one topology" problem.

### 5.2 RQ2 — Automated SOC tasks and their evaluation

**Table 5. SOC IR tasks automated (multi-label, n = 26).**

| Task | n | % | Studies |
|---|---|---|---|
| Containment / mitigation | 18 | 69% | P01, P02, P03, P05, P06, P07, P10, P11, P12, P13, P14, P15, P16, P17, P18, P19, P25, P26 |
| Investigation / hunting / reconstruction | 9 | 35% | P08, P09, P12, P15, P16, P21, P22, P23, P24 |
| Remediation / recovery | 4 | 15% | P07, P12, P14, P20 |
| Triage / prioritisation | 2 | 8% | P04, P21 |
| Response planning | 2 | 8% | P08, P20 |
| Reporting / explanation to humans | 2 | 8% | P10, P23 |

**Finding RQ2.1 — the IR lifecycle is automated piecewise.** No study automates triage → investigation → containment → remediation → reporting end-to-end. The broadest coverage is the agentic SOAR platform of [P12] (investigation, containment, remediation with validation and active monitoring). RL agents almost exclusively automate containment; LLM agents mostly investigation.

**Evaluation environments.** Simulator only: 10 (38%) [P05, P10, P11, P13, P14, P17, P18, P19, P25, P26]; offline datasets: 9 (35%) [P04, P08, P09, P16, P20, P21, P22, P23, P24]; emulation/testbeds: 7 (27%) [P01, P02, P03, P06, P07, P12, P15]; **human-expert evaluation: 1** [P08]; **production SOC: 0**.

**Metrics.** Metrics are heterogeneous and not comparable across studies: cumulative reward or defence success rate (RL in CAGE/CybORG-style simulators [P11, P13, P19, P26]); detection-style precision/recall/F1 for investigation (e.g., F1 99.78% single-host for Clouseau [P09]; 92% recall / 64% precision for Minos [P24]); attack discovery rate and decision latency for triage (+30% discovery, < 0.5 s [P04]); recovery time (up to 22% shorter [P20]); network availability (+68.5% [P14]); safety cost (5.07 → 0 [P25]); share of attack packets dropped and QoS impact (~85% dropped [P01]); cyber-resilience scores on a hardware testbed (90% vs 41% for a static defence [P03]); and expert agreement with LLM-judged output [P08]. **No shared benchmark spans RL and LLM agents**, and SOC-centric metrics such as mean time to contain or analyst workload saved are rarely reported in a controlled way.

### 5.3 RQ3 — Integration with tools, data and analysts; safety and governance

**Tool and data integration (n = 26).** Host/provenance logs 8 [P09, P15, P16, P20, P21, P22, P23, P24]; knowledge graphs/vector stores 6 [P08, P10, P15, P20, P21, P26]; SDN controllers 3 [P01, P03, P10]; SIEM/IDS alerts or SOAR 3 [P04, P08, P12]; CTI platforms/feeds 2 [P08, P17]. Integration with commercial SIEM/SOAR/EDR APIs or with interoperability standards (e.g., STIX, OpenC2, CACAO playbooks) is rarely described in the included abstracts; a STIX-grounded MARL defender exists but fell below the quality threshold (AD-CTIDRL, Table 9).

**Human–AI collaboration.** Humans appear as decision-makers in A1/A2 designs [P04, P08, P20, P21, P22, P23], as approvers of AI-generated actions in agentic SOAR [P12], and as recipients of explanations via a knowledge-graph chatbot [P10]. **Only one study evaluates outputs with security experts** [P08]. A large longitudinal study of 45 SOC analysts (3,090 queries over 10 months; excluded as primary because it studies LLM *assistant* use) found that analysts use LLMs for sensemaking and context-building rather than for high-stakes determinations, preserving their decision authority [C1] — a deployment reality not yet reflected in agent evaluations.

**Table 6. Safety and governance mechanisms (multi-label, n = 26).**

| Mechanism | n | Studies | What it does |
|---|---|---|---|
| Action constraints / admissible actions | 8 | P01, P05, P10, P15, P16, P21, P22, P23 | Restrict the action space (e.g., causal DAG of admissible transitions [P16]; benign-impact minimisation [P01]; vetted rules [P10]) |
| Evidence grounding / RAG | 6 | P08, P15, P20, P21, P23, P26 | Tie outputs to retrieved evidence |
| Explainability | 4 | P05, P10, P11, P16 | Decision trees from DRL [P05]; causal explanations [P16]; natural-language rationales [P11] |
| Robustness evaluation | 4 | P07, P14, P17, P19 | Model misspecification, topology change, Byzantine participants |
| Formal/deterministic verification or response gates | 3 | P12, P15, P18 | Probabilistic model checking of DRL policies [P18]; machine-checkable claims with a response gate [P15]; validation stage [P12] |
| Human approval | 1 | P12 | Analyst validation of agent actions |
| Abstention / consistency checks | 1 | P20 | Lookahead and consistency to reduce hallucinated actions |
| Safe (constrained) RL | 1 | P25 | CMDP with physical-safety cost |
| Privacy (DP / federated) | 1 | P17 | Differentially private CTI embeddings |
| **None reported** | **7** | P02, P03, P04, P06, P09, P13, P24 | — |

**Finding RQ3.1 — safety is optional.** 7/26 (27%) studies report no safety or governance mechanism; six of these are bounded or fully autonomous (A3/A4) [P02, P03, P06, P09, P13, P24]. In the sensitivity set, 19/41 (46%) report none.

**Finding RQ3.2 — governance is almost absent.** Only one study keeps a human approval step in the execution path [P12]; none reports audit logging, role-based authorisation of agent actions, rollback guarantees or alignment with governance frameworks. The strongest assurance designs are **verify-before-act** architectures: EviGuard lets the LLM only *propose* hypotheses, compiles them into machine-checkable claims, and blocks high-impact actions unless all critical preconditions are verified [P15]; formal verification bounds DRL agent behaviour [P18]; and safe RL drives physical safety cost to zero in a CPS testbed [P25].

**Finding RQ3.3 — LLM-agent-specific threats are unevaluated.** No included LLM agent reports an evaluation against **prompt injection**, tool misuse or data poisoning (based on abstracts). This matters because SOC agents ingest attacker-controlled content (logs, emails, files): evidence-borne prompt injection has been shown to steer LLM-assisted forensic triage [C2], and the security-of-agents literature catalogues these threats [R11].

### 5.4 RQ4 — Evidence for gaps (summary)
Mean QA scores (0–2): **AU 1.15 · ER 1.77 · RP 0.81 · SF 0.92 · DP 0.50**; mean total 5.15/10. Deployment readiness is the weakest dimension: no study scores DP = 2 (production), 7 score DP = 1. Section 10 develops the gaps.

---

## 6. Discussion

### 6.1 Key findings
1. **Two research traditions are converging.** RL-based autonomous cyber defence (2022–) and LLM agents (2025–) are now combined in hybrids [P10, P13, P14, P20, P26].
2. **Autonomy and realism are inversely related.** A4 agents act only in simulation or emulation; agents tested on real attack data are assistive or bounded and investigate rather than contain.
3. **Containment-centrism.** Two-thirds of studies automate containment; triage, reporting and planning are rare.
4. **Safety and governance lag autonomy.** A quarter of studies have no safety mechanism and only one keeps humans in the execution path.
5. **No production evidence.** No included study reports operation inside a production SOC.

### 6.2 Cross-study comparison
*RL vs LLM.* RL agents offer formal structure (threshold policies with proofs [P02, P06], convergence bounds [P07]) and fast inference, but require costly simulators and generalise poorly across topologies [P19]. LLM agents bring prior security knowledge and natural-language explanations [P11] and can operate on raw logs [P09, P24], but hallucinate [P15, P20, P23] and are slower. Hybrids address both: LLM priors accelerate RL [P13]; RL experience grounds LLM decisions [P26].

*Investigation agents.* Hierarchical LLM multi-agent investigators reach high F1 on DARPA OpTC/ATLAS [P09] and reconstruct attack scenarios from provenance graphs [P24]; RL also supports forensic planning [P22]. These are the most realistic evaluations in the corpus, yet they stop before containment.

*Safety designs.* Constraint-based (action filtering [P16], admissible actions [P05]), verification-based [P15, P18], safe-RL-based [P25] and grounding-based [P20, P21] approaches coexist with no comparative evaluation.

### 6.3 Contradictions in the literature
- **"LLMs can replace RL defenders"** [P11] vs **"LLMs are best used as guidance during training, not in-line"** — LLM latency and trust concerns motivate training-time use in [P13] and lightweight fine-tuned models in [P20].
- **"Full autonomy improves response"** (A4 studies reporting higher defence success) vs **"high-impact actions must be gated"** [P15] and **human authority is preserved in practice** [C1].
- **"Prompt engineering of frontier LLMs suffices"** vs evidence that it is costly and hallucination-prone, motivating lightweight fine-tuned planners [P20] and local distilled models [P23].
- **Correlation-based response policies** vs **causal constraints** that prevent overreaction to manipulated telemetry [P16].

### 6.4 Limitations of existing work
Bespoke simulators with unvalidated attacker models; small or synthetic incident sets; metrics that do not map to SOC KPIs; absent human-factors evaluation; limited code and environment release (an exception is the line of work by Hammar et al., whose simulation-plus-emulation methodology is the most reproducible [P02, P06, P07]); no adversarial evaluation of LLM agents.

### 6.5 Emerging trends
LLM–RL hybrids [P10, P13, P14, P26]; verify-before-act neuro-symbolic agents [P15]; formal verification of learned defenders [P18]; hierarchical multi-agent investigation [P09, P24]; local/air-gapped LLM agents for critical infrastructure [P23]; agentic SOAR replacing no-code playbooks [P12]; federated multi-organisation defence [P17].

### 6.6 Future directions (detailed in Section 10)
Shadow-mode and staged production trials; standardised SOC-IR agent benchmarks spanning RL and LLM agents; mandatory safety cases (constraints, verification, approval tiers, rollback); red-teaming against prompt injection and tool misuse; end-to-end lifecycle agents with human-centred evaluation; standards-based tool integration.

---

## 7. Taxonomy: ATLAS-IR

We propose **ATLAS-IR** — **A**utonomy, **T**ask, **L**earning architecture, **A**ssimilation of tools, **S**afety assurance — for agentic incident response. Axes 1 and 5 are *graded* (ordinal), enabling maturity comparison; axes 2–4 are *categorical*.

**Figure 2 (described as a table). ATLAS-IR taxonomy.**

| Axis | Levels / categories | Definition |
|---|---|---|
| **1. Autonomy (graded)** | A1 Assistance · A2 Human-in-the-loop · A3 Bounded autonomy · A4 Full autonomy | Who decides and who acts (§2.5) |
| **2. Task (lifecycle)** | Triage → Investigation → Planning → Containment → Remediation/Recovery → Reporting | Which IR stage(s) the agent automates |
| **3. Learning architecture** | *Learned policy:* DRL · MARL · game-theoretic RL · MDP planner — *Language reasoning:* single LLM agent · multi-agent LLM · RAG pipeline — *Hybrid:* LLM-guided RL · RL-grounded LLM — *Neuro-symbolic:* LLM + deterministic verifiers | How the agent decides |
| **4. Assimilation of tools & data** | Telemetry (logs, provenance, alerts) · Knowledge (CTI, KG, vector store, runbooks) · Actuators (SDN, firewall, EDR/SOAR actions) · Models of the environment (simulator, digital twin) · Human channel (approval, chat, explanation) | What the agent can see and touch |
| **5. Safety-Assurance Level (SAL, graded)** | **SAL0** none · **SAL1** soft controls (grounding, explanations, privacy) · **SAL2** hard controls on actions (constraints, admissible-action sets, safe RL) · **SAL3** verified or gated execution (formal verification, machine-checkable preconditions, human approval) · **SAL4** governed operation (SAL3 + audit, authorisation tiers, rollback, adversarial red-team evaluation, production monitoring) | How far the agent's actions can be trusted |

**Mapping of the 26 included studies.** Using the extraction codes: SAL0 = no mechanism; SAL1 = only GRD/XAI/PRIV/ROB/ABST; SAL2 = CONSTR or SRL without verification; SAL3 = VER or HUM.

| Autonomy \ SAL | SAL0 | SAL1 | SAL2 | SAL3 | SAL4 |
|---|---|---|---|---|---|
| A1 Assistance | – | P08, P20 | P21, P23 | – | – |
| A2 Human-in-the-loop | P04 | – | P22 | – | – |
| A3 Bounded autonomy | P09, P24 | – | P05, P10, P16, P25 | P12, P15 | – |
| A4 Full autonomy | P02, P03, P06, P13 | P07, P11, P14, P17, P19, P26 | P01 | P18 | – |

**Reading the taxonomy.** The desirable region — high autonomy with high assurance (A3/A4 × SAL3/SAL4) — contains only three studies [P12, P15, P18], and **SAL4 is empty**: no study combines verified execution with governance (audit, authorisation, rollback) and adversarial evaluation. Fully autonomous agents cluster at SAL0–SAL1. Across tasks, containment agents span all autonomy levels, whereas investigation agents stop at A3 and planning/reporting agents at A1.

---

## 9. Quality Assessment

Scores use the rubric of §4.5 (AU autonomy, ER evaluation rigour, RP reproducibility, SF safety & governance, DP deployment readiness; 0–2 each; threshold ≥ 4/10).

**Table 8. Quality scores of the 26 included studies.**

| ID | Short title | AU | ER | RP | SF | DP | Total /10 | Extraction basis |
|---|---|---|---|---|---|---|---|---|
| P01 | DeepAir: Deep Reinforcement Learning for Adaptive In… | 1 | 2 | 0 | 1 | 1 | **5** | abstract |
| P02 | Intrusion Prevention Through Optimal Stopping | 2 | 2 | 2 | 0 | 1 | **7** | abstract |
| P03 | Reinforcement Learning as a Path to Autonomous Intel… | 2 | 2 | 1 | 0 | 1 | **6** | abstract |
| P04 | Combating alert fatigue with AlertPro: Context-aware… | 1 | 2 | 1 | 0 | 1 | **5** | TLDR/metadata [CANDIDATE coding] |
| P05 | Interpretable Cross-Layer Intrusion Response System … | 1 | 1 | 0 | 2 | 0 | **4** | abstract |
| P06 | Learning Near-Optimal Intrusion Responses Against Dy… | 2 | 2 | 2 | 0 | 1 | **7** | abstract |
| P07 | Adaptive Security Response Strategies Through Conjec… | 2 | 2 | 2 | 1 | 1 | **8** | abstract |
| P08 | Advancing Autonomous Incident Response: Leveraging L… | 0 | 2 | 0 | 1 | 1 | **4** | abstract |
| P09 | Clouseau: A Hierarchical Multi-Agent Approach for Au… | 2 | 2 | 1 | 0 | 1 | **6** | abstract |
| P10 | Design and evaluation of an Autonomous Cyber Defence… | 1 | 1 | 1 | 1 | 0 | **4** | TLDR/metadata [CANDIDATE coding] |
| P11 | Leveraging Large Language Models for Autonomous Cybe… | 1 | 1 | 1 | 1 | 0 | **4** | abstract |
| P12 | Toward Robust Security Orchestration and Automated R… | 1 | 1 | 0 | 1 | 1 | **4** | abstract |
| P13 | Cyber Task Automation With Knowledge-Infused Reinfor… | 1 | 2 | 1 | 0 | 0 | **4** | abstract |
| P14 | Enhancing Cloud Network Resilience via a Robust LLM-… | 1 | 2 | 0 | 1 | 0 | **4** | abstract |
| P15 | EviGuard: Machine-Verifiable Evidence Grounding for … | 2 | 2 | 0 | 2 | 1 | **7** | abstract |
| P16 | Explainable autonomous cyber defense using adversari… | 1 | 2 | 1 | 2 | 0 | **6** | abstract |
| P17 | FedMARL-LTI: Federated Multi-Agent Reinforcement Lea… | 1 | 2 | 0 | 2 | 0 | **5** | abstract |
| P18 | Formal Modeling and Verification of Deep Reinforceme… | 1 | 2 | 1 | 2 | 0 | **6** | TLDR/metadata [CANDIDATE coding] |
| P19 | Generalizable Graph-based Reinforcement Learning Age… | 1 | 2 | 1 | 0 | 0 | **4** | abstract |
| P20 | Incident Response Planning Using a Lightweight Large… | 1 | 2 | 2 | 2 | 1 | **8** | TLDR/metadata [CANDIDATE coding] |
| P21 | Insider Threat Detection and Evidence-Grounded Triag… | 0 | 2 | 1 | 1 | 0 | **4** | abstract |
| P22 | Leveraging reinforcement learning for an efficient w… | 1 | 1 | 0 | 1 | 1 | **4** | abstract |
| P23 | Local LLM-Based Cyber Incident Analysis in Air-Gappe… | 0 | 1 | 1 | 1 | 1 | **4** | abstract |
| P24 | Minos: A Multi-agent Collaborative Framework for Pro… | 2 | 2 | 1 | 0 | 0 | **5** | TLDR/metadata [CANDIDATE coding] |
| P25 | Safety-Aware Intrusion Response System Based on Safe… | 1 | 2 | 0 | 2 | 0 | **5** | abstract |
| P26 | Towards generic defensive cyber agents: Leveraging l… | 1 | 2 | 1 | 0 | 0 | **4** | TLDR/metadata [CANDIDATE coding] |

**Summary.** Mean AU 1.15 · ER 1.77 · RP 0.81 · SF 0.92 · DP 0.50 · total 5.15. The highest-scoring studies (8/10) are the conjectural online learning approach [P07] and the lightweight LLM incident-response planner [P20]; EviGuard [P15] and the optimal-stopping studies [P02, P06] score 7.

**Table 9. Eligible studies below the quality threshold (EC7; n = 15).** These met IC1–IC4 and form, with Table 8, the sensitivity set (n = 41).

| Title | Year | Venue | Arch / autonomy | QA | DOI |
|---|---|---|---|---|---|
| A flexible SDN-based framework for slow-rate DDoS attack mitigation  | 2022 | Journal of Network and Computer Ap | DRL / A4 | 3 | [10.1016/j.jnca.2022.103444](https://doi.org/10.1016/j.jnca.2022.103444) |
| A method of network attack-defense game and collaborative defense de | 2024 | Computers & Security | MARL / A4 | 2 | [10.1016/j.cose.2024.103871](https://doi.org/10.1016/j.cose.2024.103871) |
| Deep-Reinforcement-Learning-Based Self-Evolving Moving Target Defens | 2024 | IEEE Internet of Things Journal | DRL / A4 | 2 | [10.1109/jiot.2024.3423022](https://doi.org/10.1109/jiot.2024.3423022) |
| Scalable and Autonomous Network Defense Using Reinforcement Learning | 2024 | IEEE Access | MARL / A4 | 2 | [10.1109/access.2024.3418931](https://doi.org/10.1109/access.2024.3418931) |
| ARCS: Adaptive Reinforcement Learning Framework for Automated Cybers | 2025 | Applied Sciences | DRL / A4 | 2 | [10.3390/app15020951](https://doi.org/10.3390/app15020951) |
| Autonomous cyber defense for AIoT using Graph Attention Network-Enha | 2025 | Computer Communications | DRL / A4 | 2 | [10.1016/j.comcom.2025.108265](https://doi.org/10.1016/j.comcom.2025.108265) |
| Deep Q-ICAN: A deep reinforcement learning-based approach for real-t | 2025 | Computer Networks | DRL / A4 | 2 | [10.1016/j.comnet.2025.111604](https://doi.org/10.1016/j.comnet.2025.111604) |
| GRAIN: Graph neural network and reinforcement learning aided causali | 2025 | Computers & Security | DRL / A1 | 3 | [10.1016/j.cose.2024.104180](https://doi.org/10.1016/j.cose.2024.104180) |
| A Federated Multi-Agent Communication Framework for Autonomous Cyber | 2026 | Sensors | LLM-MA / A4 | 3 | [10.3390/s26185775](https://doi.org/10.3390/s26185775) |
| A reinforcement learning-driven autonomous threat hunting agent with | 2026 | Scientific Reports | DRL / A4 | 2 | [10.1038/s41598-026-76851-9](https://doi.org/10.1038/s41598-026-76851-9) |
| AD-CTIDRL: a multi-agent method for threat intelligence-enhanced aut | 2026 | Complex & Intelligent Systems | MARL / A4 | 2 | [10.1007/s40747-026-02449-3](https://doi.org/10.1007/s40747-026-02449-3) |
| An adaptive firewall framework using deep reinforcement learning for | 2026 | Array | DRL / A4 | 2 | [10.1016/j.array.2026.101081](https://doi.org/10.1016/j.array.2026.101081) |
| Artificial intelligence driven multi agent framework for adaptive cy | 2026 | Scientific Reports | MARL / A4 | 3 | [10.1038/s41598-026-45937-9](https://doi.org/10.1038/s41598-026-45937-9) |
| Digital twin–guided graph-transformer with meta-reinforcement learni | 2026 | Scientific Reports | DRL / A3 | 3 | [10.1038/s41598-026-75705-8](https://doi.org/10.1038/s41598-026-75705-8) |
| Explainability-driven adaptive cyber deception control system for au | 2026 | Scientific Reports | DRL / A4 | 3 | [10.1038/s41598-026-64427-6](https://doi.org/10.1038/s41598-026-64427-6) |

**Table 10. Candidates excluded at eligibility, with reasons (n = 9).**

| Title | Year | Venue | Reason | DOI |
|---|---|---|---|---|
| AgentNIRS: An LLM-Driven Agent for Network Intrusion Response | 2025 | 2025 Annual Computer Security Appl | EC1: ACSAC *workshop* paper (main-track only) | [10.1109/acsacw69556.2025.00054](https://doi.org/10.1109/acsacw69556.2025.00054) |
| IntelForge: Multi-Agent LLM Framework for Cyber Threat Intelligence  | 2025 | 2025 Annual Computer Security Appl | EC1: ACSAC *workshop* paper; CTI enrichment | [10.1109/acsacw69556.2025.00047](https://doi.org/10.1109/acsacw69556.2025.00047) |
| Leveraging Large Language Models for Scalable and Explainable Cybers | 2025 | Journal of Cybersecurity and Priva | EC4/EC3: LLM log classification (no agent); evaluated on a vulnerability-detection task | [10.3390/jcp5030055](https://doi.org/10.3390/jcp5030055) |
| LLMs in the SOC: An Empirical Study of Human-AI Collaboration in Sec | 2026 | 2026 IEEE Symposium on Security an | EC4: empirical study of LLM *assistant* use by SOC analysts, no agentic system (used as context) | [10.1109/sp63933.2026.00111](https://doi.org/10.1109/sp63933.2026.00111) |
| LLM-Assisted Joint Ticket and Log Analysis for Incident Triage in In | 2026 | Proceedings of the 41st IEEE/ACM I | EC3: vehicle software incident triage (operational, not security) | [10.1145/3832783.3834521](https://doi.org/10.1145/3832783.3834521) |
| GALA: Graph-Augmented LLM Agents for Root Cause Analysis and Inciden | 2026 | Proceedings of the 41st IEEE/ACM I | EC3: microservice reliability RCA (operational, not security) | [10.1145/3832783.3834335](https://doi.org/10.1145/3832783.3834335) |
| MORPH-IDS: A context-driven Multi-Agent Reinforcement Learning frame | 2026 | Computer Networks | EC4: MARL moving-target defence of the IDS itself (detection robustness, not incident response) | [10.1016/j.comnet.2026.112541](https://doi.org/10.1016/j.comnet.2026.112541) |
| Evidence-borne prompt injection in LLM-assisted textual evidence tri | 2026 | Forensic Science International: Di | EC4/EC3: attack on LLM-assisted forensic text triage (assistant, not SOC IR agent) - cited as context | [10.1016/j.fsidi.2026.302187](https://doi.org/10.1016/j.fsidi.2026.302187) |
| Agentic Intelligence for Unified Cyber Defense: A Self-Adaptive Fram | 2026 | IEEE Access | EC4: agentic controller only re-trains a detector (detection, no response) | [10.1109/access.2026.3650833](https://doi.org/10.1109/access.2026.3650833) |

---

## 10. Research Gaps and Future Directions

**Gap 1 — Autonomy without operational evidence.**
*Evidence.* All 12 fully autonomous (A4) agents were evaluated only in simulators or emulated testbeds; no included study reports a production SOC deployment (DP = 2 for 0/26; mean DP 0.50). The most realistic evaluations (real attack datasets) concern assistive or bounded investigation agents [P09, P21, P23, P24].
*Future directions.* Staged deployment protocols — *shadow mode* (agent decides, humans act), then *canary autonomy* on low-impact actions, then bounded autonomy — reported with SOC KPIs (mean time to contain, false-action rate, analyst hours saved); sim-to-real transfer studies that quantify the gap between simulator and emulation results, building on simulation-plus-emulation methodology [P02, P06].

**Gap 2 — Safety and governance are optional and rarely verified.**
*Evidence.* 7/26 report no safety mechanism, six of them A3/A4; only three studies have verified or gated execution [P12, P15, P18], one keeps a human approval step [P12], and none reports audit, authorisation tiers or rollback (SAL4 empty).
*Future directions.* Require a **safety case** for every agent: action taxonomy by impact, admissible-action constraints, pre-condition verification for high-impact actions (as in [P15]), human approval tiers, reversible-action preference and rollback, tamper-evident audit logs; verification of learned policies [P18] and safe-RL objectives [P25] as standard.

**Gap 3 — No shared, SOC-realistic benchmark across agent paradigms.**
*Evidence.* Evaluations are split across simulators (10), offline datasets (9) and testbeds (7) with incomparable metrics (reward, F1, recovery time, availability, safety cost). Only one study includes human-expert evaluation [P08]; LLM and RL agents are compared only within CAGE-2-style simulators [P11].
*Future directions.* A common benchmark with realistic SOC telemetry (SIEM alerts, EDR/provenance logs, tickets), multi-stage campaigns, ground-truth response plans, and metrics for time-to-contain, collateral damage, false actions and explanation quality; evaluation tracks for both RL and LLM agents.

**Gap 4 — Piecemeal task automation; triage and reporting neglected.**
*Evidence.* Containment 18/26; triage 2; reporting 2; planning 2; no end-to-end lifecycle agent (§5.2).
*Future directions.* Orchestrated multi-agent pipelines that hand off from triage to investigation to containment to reporting with explicit state and accountability; reporting agents that generate auditable incident records; evaluation of hand-off failures.

**Gap 5 — Adversarial robustness of LLM agents is untested.**
*Evidence.* No included LLM agent reports evaluation against prompt injection, tool misuse or poisoned retrieval, although SOC agents ingest attacker-controlled content and evidence-borne prompt injection has been demonstrated in LLM-assisted triage [C2]; the threat landscape is surveyed in [R11]. RL robustness is studied only for model misspecification and topology change [P07, P14, P19].
*Future directions.* Red-team suites for SOC agents (injection via logs, emails, filenames, CTI feeds), privilege separation between reading untrusted data and invoking actuators, provenance-aware context handling, and adversarial training of RL defenders against telemetry manipulation [P16].

**Gap 6 — Shallow integration with real SOC tooling and standards.**
*Evidence.* SIEM/SOAR integration appears in 3/26 studies [P04, P08, P12]; actuators are mostly SDN controllers in simulation [P01, P03, P10]; standards-based integration (STIX/TAXII, OpenC2, CACAO) appears only in a below-threshold study (Table 9).
*Future directions.* Reference architectures that expose SOAR/EDR/firewall actions to agents through typed, permissioned tool interfaces; use of OpenC2 for actions and CACAO for machine-readable playbooks; evaluations on open SOC stacks (e.g., Wazuh/Elastic + SOAR).

**Gap 7 — Human factors and reproducibility.**
*Evidence.* Mean RP 0.81/2; human evaluation in 1/26; analysts in practice use LLMs as aids rather than decision-makers [C1]; 6 of 26 included studies are coded from TL;DRs because abstracts are not openly available, underscoring limited openness.
*Future directions.* Controlled user studies with SOC analysts (trust calibration, workload, over-reliance), release of environments, agent code and incident datasets, and reporting checklists for agentic IR experiments.

---

## 11. Contribution Statement

**What is new.**
1. A **peer-reviewed-only, venue-restricted, DOI-verified** synthesis of agentic AI for SOC incident response (2021–2026).
2. A **unified autonomy scale (A1–A4)** applied to both RL-based autonomous cyber-defence agents and LLM agents, revealing the inverse relation between autonomy and evaluation realism.
3. **ATLAS-IR**, a five-axis taxonomy with graded **Safety-Assurance Levels (SAL0–SAL4)**, showing that SAL4 is empty and that only three studies combine bounded or full autonomy with verified or gated execution.
4. **Quantified evidence** that no included study evaluates in a production SOC, automates the full IR lifecycle, or tests LLM agents against prompt injection.
5. A **reproducible pipeline** (search, screening, extraction, scoring) with archived data.

**How it differs from existing surveys.** Versus broad LLM-in-security reviews [R03–R06]: agent- and IR-specific, quality-graded. Versus the LLM-agent SLR [R10]: excludes preprints, adds RL-based agents, restricts to defensive IR, and grades safety and deployment per study. Versus the IoT agentic survey [R08]: SOC IR scope, six publishers, quality gate. Versus the SIEM–SOAR SLR [R09]: architecture-level autonomy and safety grading of agents rather than an integration lens. Versus the IRS-for-CPS survey [R02]: covers LLM agents and SOC-wide IR.

**Academic value.** A common vocabulary (autonomy × safety assurance) for positioning new agentic IR work; seven research agendas grounded in the evidence. **Practical value.** For SOC leaders and vendors: a maturity checklist (autonomy level vs safety-assurance level) for procuring or piloting agentic IR, and identification of designs with the strongest assurance evidence (verify-before-act, verified policies, safe RL).

---

## 12. Limitations

### 12.1 Limitations of this SLR
- **Source coverage.** Searches ran on Crossref only (IEEE Xplore, Scopus, Web of Science and other publisher portals were not reachable from the review environment). Crossref covers all six permitted publishers, but its relevance ranking and the 200-record cap per string can miss records; Boolean strings for a confirmatory run are provided (§4.1).
- **Title-based filtering.** Records were kept only if the title matched agent and security-response patterns; papers describing agentic IR only in the abstract may be under-represented.
- **Semantic-search discovery.** Five SciSpace searches were used to discover candidates; all were verified in Crossref and subjected to identical criteria, but this step is less reproducible than the scripted searches.
- **Abstract-level extraction.** For 6 of 26 included studies (mostly Elsevier), abstracts were unavailable through open APIs and coding relied on TL;DRs and titles (*CANDIDATE coding*). Claims of absence (e.g., no prompt-injection evaluation, no audit logging) are based on abstracts and should be confirmed on full texts.
- **Single reviewer.** Screening, extraction and scoring were performed by one reviewer with deterministic scripts; a second reviewer on ≥ 20% of records with Cohen's κ is recommended before submission.
- **Inclusion of RL agents.** We treat RL-based autonomous cyber-defence agents as agentic (§2.1). Readers who restrict "agentic AI" to LLM agents should use the LLM subset (13 studies: P08–P15, P20, P21, P23, P24, P26), which is below the 25-study minimum on its own.
- **Venue rules.** Strict main-track rules excluded relevant workshop papers (e.g., AgentNIRS and IntelForge at ACSAC 2025 workshops) and venues such as IEEE NOMS, CNS, MILCOM and AAAI symposia, where much agentic IR work appears.
- **Quartiles** were applied from a whitelist and must be re-confirmed; *Internet of Things and Cyber-Physical Systems* [R04] and *Array* [R09] in particular should be checked.
- **Recency.** 54% of included studies are from 2026; the field is moving faster than the review cycle.

### 12.2 Limitations of the included studies
Simulator-bound evaluation; bespoke environments; incomparable metrics; scarce human evaluation; limited code/environment release; little adversarial testing; safety mechanisms rarely evaluated quantitatively.

### 12.3 Limitations of the field
No shared SOC-IR benchmark; limited researcher access to production SOC telemetry; immature governance frameworks for autonomous security actions; legal and liability uncertainty for automated containment; rapid model turnover that ages LLM-agent results quickly.

---

## 13. Conclusion

**Key findings.** Across 26 quality-assessed studies (2021–2026), agentic SOC incident response is split evenly between RL-based and LLM-based/hybrid agents and is dominated by automated containment. Full autonomy is the most common level (46%) but exists only in simulation or emulation; agents tested on real attack data are assistive or bounded investigators. A quarter of studies have no safety mechanism, one keeps a human approval step, one includes expert evaluation, and none tests LLM agents against prompt injection or operates in a production SOC.

**Gaps.** (1) Autonomy without operational evidence; (2) optional, rarely verified safety and governance; (3) no shared SOC-realistic benchmark; (4) piecemeal task automation; (5) untested adversarial robustness of LLM agents; (6) shallow integration with SOC tooling and standards; (7) weak human-factors evaluation and reproducibility.

**Future directions.** Staged shadow-to-bounded-autonomy deployments with SOC KPIs; mandatory safety cases with verify-before-act gating; cross-paradigm benchmarks; end-to-end orchestrated lifecycle agents; red-teaming against prompt injection; standards-based tool interfaces; analyst-centred user studies.

**Contribution.** A verified, reproducible evidence base and the ATLAS-IR taxonomy with autonomy and safety-assurance levels, offering researchers and SOC practitioners a shared yardstick for moving agentic incident response from capable-in-simulation to trustworthy-in-operation.

---

## 8. Reference List

*(Section 8 is placed at the end, per the output-format requirement for a closing reference list.)*

**Verification legend.** **[VERIFIED]** — authors, title, venue, year and DOI confirmed in Crossref on 14 Nov 2026; extraction from the full abstract. **[VERIFIED metadata · CANDIDATE coding]** — metadata confirmed in Crossref; extraction from TL;DR/metadata, to be checked against the full text. No preprints or arXiv-only works are cited. Venue strings are Crossref container titles.

### 8.1 Primary studies (n = 26)

[P01] Trung V. Phan, Thomas Bauschert, “DeepAir: Deep Reinforcement Learning for Adaptive Intrusion Response in Software-Defined Networks,” *IEEE Transactions on Network and Service Management*, 2022. DOI: 10.1109/tnsm.2022.3158468. Link: https://doi.org/10.1109/tnsm.2022.3158468 [VERIFIED]

[P02] Kim Hammar, Rolf Stadler, “Intrusion Prevention Through Optimal Stopping,” *IEEE Transactions on Network and Service Management*, 2022. DOI: 10.1109/tnsm.2022.3176781. Link: https://doi.org/10.1109/tnsm.2022.3176781 [VERIFIED]

[P03] Stephen Raio, Kevin Corder, Travis W. Parker et al., “Reinforcement Learning as a Path to Autonomous Intelligent Cyber-Defense Agents in Vehicle Platforms,” *Applied Sciences*, 2023. DOI: 10.3390/app132111621. Link: https://doi.org/10.3390/app132111621 [VERIFIED]

[P04] Xiaoyu Wang, Xiaobo Yang, Xueping Liang et al., “Combating alert fatigue with AlertPro: Context-aware alert prioritization using reinforcement learning for multi-step attack detection,” *Computers & Security*, 2024. DOI: 10.1016/j.cose.2023.103583. Link: https://doi.org/10.1016/j.cose.2023.103583 [VERIFIED metadata · CANDIDATE coding]

[P05] Hao Chen, Yingxu Lai, Jing Liu et al., “Interpretable Cross-Layer Intrusion Response System Based on Deep Reinforcement Learning for Industrial Control Systems,” *IEEE Transactions on Industrial Informatics*, 2024. DOI: 10.1109/tii.2024.3388672. Link: https://doi.org/10.1109/tii.2024.3388672 [VERIFIED]

[P06] Kim Hammar, Rolf Stadler, “Learning Near-Optimal Intrusion Responses Against Dynamic Attackers,” *IEEE Transactions on Network and Service Management*, 2024. DOI: 10.1109/tnsm.2023.3293413. Link: https://doi.org/10.1109/tnsm.2023.3293413 [VERIFIED]

[P07] Kim Hammar, Tao Li, Rolf Stadler et al., “Adaptive Security Response Strategies Through Conjectural Online Learning,” *IEEE Transactions on Information Forensics and Security*, 2025. DOI: 10.1109/tifs.2025.3558600. Link: https://doi.org/10.1109/tifs.2025.3558600 [VERIFIED]

[P08] Amine Tellache, Abdelaziz Amara Korba, Amdjed Mokhtari et al., “Advancing Autonomous Incident Response: Leveraging LLMs and Cyber Threat Intelligence,” *GLOBECOM 2025 - 2025 IEEE Global Communications Conference*, 2025. DOI: 10.1109/globecom59602.2025.11432623. Link: https://doi.org/10.1109/globecom59602.2025.11432623 [VERIFIED]

[P09] Abdullah Aldaihan, Fahad Alotaibi, Sergio Maffeis, “Clouseau: A Hierarchical Multi-Agent Approach for Autonomous Attack Investigation,” *2025 IEEE Annual Computer Security Applications Conference (ACSAC)*, 2025. DOI: 10.1109/acsac67867.2025.00051. Link: https://doi.org/10.1109/acsac67867.2025.00051 [VERIFIED]

[P10] Johannes Loevenich, Erik Adler, Tobias Hürten et al., “Design and evaluation of an Autonomous Cyber Defence agent using DRL and an augmented LLM,” *Computer Networks*, 2025. DOI: 10.1016/j.comnet.2025.111162. Link: https://doi.org/10.1016/j.comnet.2025.111162 [VERIFIED metadata · CANDIDATE coding]

[P11] Hamoun Mohammadi, Jonathan J. Davis, Mitchell Kiely, “Leveraging Large Language Models for Autonomous Cyber Defense: Insights from CAGE-2 Simulations,” *IEEE Intelligent Systems*, 2025. DOI: 10.1109/mis.2025.3568209. Link: https://doi.org/10.1109/mis.2025.3568209 [VERIFIED]

[P12] Ismail, Rahmat Kurnia, Zilmas Arjuna Brata et al., “Toward Robust Security Orchestration and Automated Response in Security Operations Centers with a Hyper-Automation Approach Using Agentic Artificial Intelligence,” *Information*, 2025. DOI: 10.3390/info16050365. Link: https://doi.org/10.3390/info16050365 [VERIFIED]

[P13] Md. Shamim Towhid, Shahrear Iqbal, Euclides Carlos Pinto Neto et al., “Cyber Task Automation With Knowledge-Infused Reinforcement Learning and LLM-Guided Policies,” *IEEE Transactions on Network Science and Engineering*, 2026. DOI: 10.1109/tnse.2026.3715407. Link: https://doi.org/10.1109/tnse.2026.3715407 [VERIFIED]

[P14] Yixiao Peng, Hao Hu, Feiyang Li et al., “Enhancing Cloud Network Resilience via a Robust LLM-Empowered Multi-Agent Reinforcement Learning Framework,” *IEEE Transactions on Dependable and Secure Computing*, 2026. DOI: 10.1109/tdsc.2026.3694417. Link: https://doi.org/10.1109/tdsc.2026.3694417 [VERIFIED]

[P15] Haozhe Zhou, Hang Lei, Maolin Yang, “EviGuard: Machine-Verifiable Evidence Grounding for LLM-Based Industrial Incident Reasoning,” *Applied Sciences*, 2026. DOI: 10.3390/app16188925. Link: https://doi.org/10.3390/app16188925 [VERIFIED]

[P16] Yiyao Zhang, Diksha Goel, Hussain Ahmad, “Explainable autonomous cyber defense using adversarial multi-agent reinforcement learning,” *Expert Systems with Applications*, 2026. DOI: 10.1016/j.eswa.2026.132741. Link: https://doi.org/10.1016/j.eswa.2026.132741 [VERIFIED]

[P17] Fatih Şahin, “FedMARL-LTI: Federated Multi-Agent Reinforcement Learning with LLM-Compatible Threat Intelligence for Cooperative Cyber Defense,” *Applied Sciences*, 2026. DOI: 10.3390/app16168278. Link: https://doi.org/10.3390/app16168278 [VERIFIED]

[P18] Laurin Holz, Johannes Loevenich, Roberto Rigolin F. Lopes et al., “Formal Modeling and Verification of Deep Reinforcement Learning Agents for Secure and Available Autonomous Cyber Defense,” *IEEE Transactions on Dependable and Secure Computing*, 2026. DOI: 10.1109/tdsc.2026.3738256. Link: https://doi.org/10.1109/tdsc.2026.3738256 [VERIFIED metadata · CANDIDATE coding]

[P19] Isaiah J. King, Benjamin Bowman, H. Howie Huang, “Generalizable Graph-based Reinforcement Learning Agents for Automated Cyber Defense,” *2026 56th Annual IEEE International Conference on Dependable Systems and Networks (DSN)*, 2026. DOI: 10.1109/dsn69566.2026.00079. Link: https://doi.org/10.1109/dsn69566.2026.00079 [VERIFIED]

[P20] Kim Hammar, Tansu Alpcan, Emil Lupu et al., “Incident Response Planning Using a Lightweight Large Language Model with Reduced Hallucination,” *Proceedings 2026 Network and Distributed System Security Symposium*, 2026. DOI: 10.14722/ndss.2026.240358. Link: https://doi.org/10.14722/ndss.2026.240358 [VERIFIED metadata · CANDIDATE coding]

[P21] Kai Cheng, Dongkun Li, Weidong Tang et al., “Insider Threat Detection and Evidence-Grounded Triage Using a Heterogeneous Dual-Branch Network and a Constrained LLM Agent,” *Applied Sciences*, 2026. DOI: 10.3390/app16147054. Link: https://doi.org/10.3390/app16147054 [VERIFIED]

[P22] Mohamed Chahine Ghanem, Dominik Wojtczak, Elhadj Benkhelifa et al., “Leveraging reinforcement learning for an efficient windows registry analysis during cyber incident response,” *Scientific Reports*, 2026. DOI: 10.1038/s41598-026-57787-6. Link: https://doi.org/10.1038/s41598-026-57787-6 [VERIFIED]

[P23] Sunghun Jang, MyoungRak Lee, Taeshik Shon, “Local LLM-Based Cyber Incident Analysis in Air-Gapped Networks via Teacher–Student Knowledge Distillation and Agentic Orchestration,” *Electronics*, 2026. DOI: 10.3390/electronics15132949. Link: https://doi.org/10.3390/electronics15132949 [VERIFIED]

[P24] Jiahui Wang, Zhenyuan Li, Zhengkai Wang et al., “Minos: A Multi-agent Collaborative Framework for Provenance-Based Backward Tracking,” *ESORICS 2026 (LNCS)*, 2026. DOI: 10.1007/978-3-032-38692-2_19. Link: https://doi.org/10.1007/978-3-032-38692-2_19 [VERIFIED metadata · CANDIDATE coding]

[P25] Lin Chen, Yingxu Lai, Peng Zhao et al., “Safety-Aware Intrusion Response System Based on Safe Reinforcement Learning for Cyber-Physical Systems,” *IEEE Transactions on Consumer Electronics*, 2026. DOI: 10.1109/tce.2026.3674866. Link: https://doi.org/10.1109/tce.2026.3674866 [VERIFIED]

[P26] Muhammad Omer Farooq, “Towards generic defensive cyber agents: Leveraging large language models and RAG-based few-shot learning,” *Computer Networks*, 2026. DOI: 10.1016/j.comnet.2026.112349. Link: https://doi.org/10.1016/j.comnet.2026.112349 [VERIFIED metadata · CANDIDATE coding]

### 8.2 Secondary studies: surveys and SLRs (n = 11)

[R01] Chadni Islam, Muhammad Ali Babar, Surya Nepal, “A Multi-Vocal Review of Security Orchestration,” *ACM Computing Surveys*, 2019. DOI: 10.1145/3305268. Link: https://doi.org/10.1145/3305268 [VERIFIED]

[R02] May Bashendy, Ashraf Tantawy, Abdelkarim Erradi, “Intrusion response systems for cyber-physical systems: A comprehensive survey,” *Computers & Security*, 2023. DOI: 10.1016/j.cose.2022.102984. Link: https://doi.org/10.1016/j.cose.2022.102984 [VERIFIED]

[R03] Ismayil Hasanov, Seppo Virtanen, Antti Hakkala et al., “Application of Large Language Models in Cybersecurity: A Systematic Literature Review,” *IEEE Access*, 2024. DOI: 10.1109/access.2024.3505983. Link: https://doi.org/10.1109/access.2024.3505983 [VERIFIED]

[R04] Mohamed Amine Ferrag, Fatima Alwahedi, Ammar Battah et al., “Generative AI in cybersecurity: A comprehensive review of LLM applications and vulnerabilities,” *Internet of Things and Cyber-Physical Systems*, 2025. DOI: 10.1016/j.iotcps.2025.01.001. Link: https://doi.org/10.1016/j.iotcps.2025.01.001 [VERIFIED]

[R05] Weiping Ding, Mohamed Abdel-Basset, Ahmed M. Ali et al., “Large language models for cyber resilience: A comprehensive review, challenges, and future perspectives,” *Applied Soft Computing*, 2025. DOI: 10.1016/j.asoc.2024.112663. Link: https://doi.org/10.1016/j.asoc.2024.112663 [VERIFIED]

[R06] Jie Zhang, Haoyu Bu, Hui Wen et al., “When LLMs meet cybersecurity: a systematic literature review,” *Cybersecurity*, 2025. DOI: 10.1186/s42400-025-00361-w. Link: https://doi.org/10.1186/s42400-025-00361-w [VERIFIED]

[R07] Andreas Ekelhart, Sebastian Schrittwieser, Gerald Sendera et al., “A survey of Large Language Models in Cyber Threat Intelligence: Toward a regulation-aware architecture for secure ICT systems,” *ICT Express*, 2026. DOI: 10.1016/j.icte.2026.09.017. Link: https://doi.org/10.1016/j.icte.2026.09.017 [VERIFIED]

[R08] Vinoth Nageshwaran, Soundararajan Ezekiel, “Agentic AI and Large Language Models for Autonomous IoT Cybersecurity: A Systematic Survey, Taxonomy, and Research Roadmap,” *Electronics*, 2026. DOI: 10.3390/electronics15122740. Link: https://doi.org/10.3390/electronics15122740 [VERIFIED]

[R09] Issa Ahmad El-Attar, Ali Attar, Mohammed El-Hajj, “From alert fatigue to autonomous defense: A systematic literature review of AI-driven SIEM–SOAR integration in security operations centers,” *Array*, 2026. DOI: 10.1016/j.array.2026.101367. Link: https://doi.org/10.1016/j.array.2026.101367 [VERIFIED]

[R10] George Fatouros, Konstantinos Mavrogiorgos, Georgios Makridis et al., “LLM-Based Agents for Cybersecurity: A Systematic Review of Architectures, Applications, and Open Challenges,” *Journal of Cybersecurity and Privacy*, 2026. DOI: 10.3390/jcp6050159. Link: https://doi.org/10.3390/jcp6050159 [VERIFIED]

[R11] Vincenzo Sammartino, “Vulnerabilities in autonomous execution: A survey of security threats and defenses in LLM-driven agentic and multi-agent systems,” *Knowledge-Based Systems*, 2026. DOI: 10.1016/j.knosys.2026.117001. Link: https://doi.org/10.1016/j.knosys.2026.117001 [VERIFIED]

### 8.3 Contextual studies (not primary studies)

[C1] Ronal Singh, Shahroz Tariq, Fatemeh Jalalvand et al., “LLMs in the SOC: An Empirical Study of Human-AI Collaboration in Security Operations Centres,” *2026 IEEE Symposium on Security and Privacy (SP)*, 2026. DOI: 10.1109/sp63933.2026.00111. Link: https://doi.org/10.1109/sp63933.2026.00111 [VERIFIED; contextual, not a primary study]

[C2] Dongho Kim, Damin Kim, Moohong Min, “Evidence-borne prompt injection in LLM-assisted textual evidence triage,” *Forensic Science International: Digital Investigation*, 2026. DOI: 10.1016/j.fsidi.2026.302187. Link: https://doi.org/10.1016/j.fsidi.2026.302187 [VERIFIED; contextual, not a primary study]

### 8.4 Methodological references

[M1] M. J. Page, J. E. McKenzie, P. M. Bossuyt, I. Boutron et al., "The PRISMA 2020 statement: an updated guideline for reporting systematic reviews," *BMJ*, 372:n71, 2021. DOI: 10.1136/bmj.n71. Link: https://doi.org/10.1136/bmj.n71 [VERIFIED]

[M2] B. Kitchenham, O. Pearl Brereton, D. Budgen, M. Turner et al., "Systematic literature reviews in software engineering – A systematic literature review," *Information and Software Technology*, 51(1), 2009. DOI: 10.1016/j.infsof.2008.09.009. Link: https://doi.org/10.1016/j.infsof.2008.09.009 [VERIFIED]

### 8.5 Candidate publications (not cited as evidence; require confirmation before any use)
The following were found during the search but **failed the venue rules** (workshops or non-top-tier conferences) or could not be confirmed as peer-reviewed in an eligible venue. They are listed only so readers can see what was excluded; they are **not** part of the evidence base.

| Title | Venue (per Crossref) | Reason | DOI |
|---|---|---|---|
| AgentNIRS: An LLM-Driven Agent for Network Intrusion Response | ACSAC 2025 Workshops | Workshop (EC1) | [10.1109/acsacw69556.2025.00054](https://doi.org/10.1109/acsacw69556.2025.00054) |
| IntelForge: Multi-Agent LLM Framework for CTI Enrichment | ACSAC 2025 Workshops | Workshop (EC1) | [10.1109/acsacw69556.2025.00047](https://doi.org/10.1109/acsacw69556.2025.00047) |
| Hallucination-Resistant Security Planning with a Large Language Model | IEEE NOMS 2026 | Conference not in top-tier list | [10.1109/noms69089.2026.11668410](https://doi.org/10.1109/noms69089.2026.11668410) |
| In-Context Autonomous Network Incident Response: An End-to-End LLM Agent Approach | Proc. AAAI Symposium Series 2026 | Symposium, not in list | [10.1609/aaaiss.v9i1.42938](https://doi.org/10.1609/aaaiss.v9i1.42938) |
| Large Language Models are Autonomous Cyber Defenders | IEEE CAI 2025 | Conference not in list | [10.1109/cai64502.2025.00195](https://doi.org/10.1109/cai64502.2025.00195) |
| Explaining Hybrid RL Agents for Cyber Defense using SHAP and Reward Decomposition | IEEE MILCOM 2025 | Conference not in list | [10.1109/milcom64451.2025.11310039](https://doi.org/10.1109/milcom64451.2025.11310039) |
| DeepStage: Learning Autonomous Defense Policies Against Multi-Stage APT Campaigns | IEEE CSR 2026 | Conference not in list | [10.1109/csr69374.2026.11759781](https://doi.org/10.1109/csr69374.2026.11759781) |
| Enhancing Security Operation Center: Wazuh Security Event Response with RAG-Driven Copilot | *Sensors* 2025 | Eligible venue; excluded as an assistant/copilot (EC4) — borderline, reviewer judgement | [10.3390/s25030870](https://doi.org/10.3390/s25030870) |
