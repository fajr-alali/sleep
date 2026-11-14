"""Eligibility + extraction coding (index = position in selected.json).
arch: LLM-SA single LLM agent | LLM-MA multi-agent LLM | RAG retrieval-augmented LLM pipeline | HYB LLM+RL hybrid |
      DRL single-agent deep RL | MARL multi-agent RL | GT game-theoretic/optimal-stopping RL | PLAN MDP/DP planner | NS neuro-symbolic/verifier
aut:  A1 assistance/recommendation | A2 human-in-the-loop (agent proposes, human approves/acts) | A3 bounded autonomy (executes within
      explicit constraints/gates) | A4 full autonomy (executes without human approval; typically in simulation)
task: TRI triage/prioritisation | INV investigation/hunting/reconstruction | CON containment/mitigation | REM remediation/recovery |
      PLN response planning | REP reporting/explanation
eval: SIM simulator/gym | EMU emulation/testbed | DS offline dataset | HUM human-expert evaluation | PROD production/real SOC
tool: FW firewall/ACL | SDN | SIEM SIEM/SOAR/IDS alerts | CTI CTI platforms/feeds | LOG host/provenance logs | KG knowledge graph/vector store | DT digital twin
safe: CONSTR action constraints/allow-list | VER formal/deterministic verification or gate | SRL safe/constrained RL | XAI explanations |
      ABST abstention/consistency check | GRD evidence grounding/RAG | PRIV privacy/DP/federated | HUM human approval | ROB robustness eval
QA (0-2): AU autonomy, ER evaluation rigour, RP reproducibility, SF safety, DP deployment readiness.  conf A=abstract, B=TLDR/metadata.
"""
X = {}
def inc(i, arch, aut, task, ev, tool, safe, au, er, rp, sf, dp, conf, note=""):
    X[i] = dict(inc=True, arch=arch, aut=aut, task=task, ev=ev, tool=tool, safe=safe, qa=(au, er, rp, sf, dp), conf=conf, note=note)
def exc(i, reason): X[i] = dict(inc=False, reason=reason)
exc(0, "EC1: ACSAC *workshop* paper (main-track only)")
exc(1, "EC1: ACSAC *workshop* paper; CTI enrichment")
exc(2, "EC4: empirical study of LLM *assistant* use by SOC analysts, no agentic system (used as context)")
inc(3, "RAG", "A1", "INV PLN", "DS HUM", "SIEM CTI KG", "GRD", 0, 2, 0, 1, 1, "A", "hybrid CTI retrieval + external CTI platform queries; expert cross-validation")
inc(4, "HYB", "A1", "PLN REM", "DS", "LOG KG", "ABST GRD", 1, 2, 2, 2, 1, "B", "fine-tuned lightweight LLM + retrieval + lookahead planning; up to 22% shorter recovery")
exc(5, "EC3: vehicle software incident triage (operational, not security)")
exc(6, "EC3: microservice reliability RCA (operational, not security)")
inc(7, "DRL", "A4", "CON", "EMU", "SDN", "", 2, 2, 1, 0, 1, "A", "CAN-bus agent on PASTA hardware testbed; 90% cyber resilience")
inc(8, "DRL", "A4", "CON REM", "DS", "SIEM", "", 1, 1, 0, 0, 0, "A")
inc(9, "MARL", "A4", "CON", "SIM", "CTI", "PRIV ROB", 1, 2, 0, 2, 0, "A", "LLM-summarised DP semantic embeddings; Byzantine robustness")
inc(10, "LLM-SA", "A1", "TRI INV", "DS", "LOG KG", "GRD CONSTR", 0, 2, 1, 1, 0, "A", "constrained ReAct-style agent; CERT r4.2")
inc(11, "NS", "A3", "INV CON", "EMU", "LOG KG", "VER GRD CONSTR", 2, 2, 0, 2, 1, "A", "LLM proposes hypotheses; deterministic verifiers; response gate")
inc(12, "DRL", "A4", "CON", "SIM", "", "", 1, 1, 0, 0, 0, "B")
inc(13, "HYB", "A3", "CON REP", "SIM", "SDN KG", "CONSTR XAI", 1, 1, 1, 1, 0, "B", "DRL actuation + LLM + rule-based; KG chatbot for human experts")
inc(14, "MARL", "A4", "CON", "SIM", "", "", 1, 1, 0, 0, 0, "B")
inc(15, "LLM-MA", "A1", "INV REP", "DS", "LOG", "GRD CONSTR", 0, 1, 1, 1, 1, "A", "air-gapped local LLM; agent orchestration suppresses hallucination; Atomic Red Team")
inc(16, "MARL", "A3", "INV CON", "DS", "LOG", "CONSTR XAI", 1, 2, 1, 2, 0, "A", "causal DAG restricts admissible responses")
inc(17, "MARL", "A4", "CON", "SIM", "", "", 1, 1, 0, 0, 0, "A")
inc(18, "DRL", "A3", "CON", "SIM", "", "SRL", 1, 2, 0, 2, 0, "A", "CMDP safety cost; safety cost 5.07 -> 0")
inc(19, "DRL", "A4", "CON", "SIM", "", "VER", 1, 2, 1, 2, 0, "B", "probabilistic model checking of DRL ACD policies")
inc(20, "DRL", "A3", "CON", "SIM", "", "XAI CONSTR", 1, 1, 0, 2, 0, "A", "DRL distilled into decision trees; physical-domain policies")
inc(21, "DRL", "A4", "CON", "EMU", "SDN", "CONSTR", 1, 2, 0, 1, 1, "A", "minimises benign-traffic impact; ~85% attack packets dropped")
inc(22, "LLM-SA", "A3", "INV CON REM", "EMU", "SIEM", "VER HUM", 1, 1, 0, 1, 1, "A", "agentic-LLM SOAR; IVAM investigation-validation-active monitoring")
exc(23, "EC4/EC3: LLM log classification (no agent); evaluated on a vulnerability-detection task")
inc(24, "DRL", "A4", "INV", "SIM", "LOG", "", 1, 1, 0, 0, 0, "B")
inc(25, "MARL", "A4", "TRI CON", "SIM", "SIEM", "", 1, 1, 1, 0, 0, "A")
inc(26, "PLAN", "A2", "INV", "DS", "LOG", "CONSTR", 1, 1, 0, 1, 1, "A", "DP planner with bounded RL refinement for forensic registry analysis")
inc(27, "DRL", "A4", "CON", "SIM", "", "XAI", 1, 1, 0, 1, 0, "A", "adaptive deception control")
inc(28, "LLM-MA", "A4", "CON", "DS", "", "PRIV", 0, 1, 1, 1, 0, "A", "conceptual; only detector implemented")
inc(35, "GT", "A4", "CON", "EMU", "", "", 2, 2, 2, 0, 1, "A", "optimal stopping; simulation + emulation system")
inc(36, "GT", "A4", "CON", "EMU", "", "", 2, 2, 2, 0, 1, "A", "fictitious self-play vs dynamic attacker")
inc(37, "GT", "A4", "CON REM", "EMU", "", "ROB", 2, 2, 2, 1, 1, "A", "conjectural online learning under model misspecification; testbed")
inc(43, "LLM-MA", "A3", "INV", "DS", "LOG", "", 2, 2, 1, 0, 1, "A", "hierarchical agents; DARPA OpTC + ATLAS; F1 99.78% single-host")
inc(44, "DRL", "A4", "CON", "SIM", "", "ROB", 1, 2, 1, 0, 0, "A", "graph observations; zero-shot transfer to new networks")
inc(45, "DRL", "A4", "CON", "DS", "FW", "", 1, 1, 0, 0, 0, "B")
inc(46, "DRL", "A4", "CON", "SIM", "", "", 1, 1, 0, 0, 0, "B")
exc(47, "EC4: MARL moving-target defence of the IDS itself (detection robustness, not incident response)")
inc(48, "DRL", "A2", "TRI", "DS", "SIEM", "", 1, 2, 1, 0, 1, "B", "RL alert prioritisation; +30% attack discovery; <0.5 s")
inc(49, "DRL", "A1", "INV", "DS", "LOG", "", 0, 2, 1, 0, 0, "B")
exc(50, "EC4/EC3: attack on LLM-assisted forensic text triage (assistant, not SOC IR agent) - cited as context")
exc(51, "EC4: agentic controller only re-trains a detector (detection, no response)")
inc(52, "DRL", "A4", "CON", "SIM", "", "", 1, 1, 0, 0, 0, "A")
inc(53, "DRL", "A4", "CON", "EMU", "SDN", "", 1, 1, 0, 0, 1, "B")
inc(54, "DRL", "A3", "CON", "SIM", "DT", "VER", 1, 1, 0, 1, 0, "B", "digital-twin-guided mitigation")
inc(55, "HYB", "A4", "CON", "SIM", "", "", 1, 2, 1, 0, 0, "A", "LLM-guided RL; >75% faster convergence")
inc(56, "HYB", "A4", "CON", "SIM", "KG", "GRD", 1, 2, 1, 0, 0, "B", "RAG over RL observation-action tuples; few-shot")
inc(57, "HYB", "A4", "CON REM", "SIM", "", "ROB", 1, 2, 0, 1, 0, "A", "LLM-empowered MARL; +68.5% availability")
inc(58, "LLM-SA", "A4", "CON", "SIM", "", "XAI", 1, 1, 1, 1, 0, "A", "LLM agent on CAGE-2; par with best RL agent")
inc(59, "MARL", "A4", "CON", "SIM", "CTI", "", 1, 1, 0, 0, 0, "B")
inc(60, "LLM-MA", "A3", "INV", "DS", "LOG", "", 2, 2, 1, 0, 0, "B", "provenance backward tracking; 14 scenarios, 5 public datasets")
