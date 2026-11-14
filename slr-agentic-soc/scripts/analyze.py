"""QA gate, statistics, tables and references for the agentic-SOC SLR."""
import json, sys, re, html, collections as C
sys.path.insert(0, sys.argv[1]); from extract import X
sel = json.load(open(sys.argv[1] + "/selected.json"))
QA_MIN = 4
VENUE_FIX = {"10.1007/978-3-032-38692-2_19": "ESORICS 2026 (LNCS)"}
def clean(t): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", t))).strip()
def authors(s):
    a = [x.strip() for x in (s.get("authors") or []) if x.strip()] or [x["name"] for x in ((s.get("s2") or {}).get("authors") or [])]
    return (", ".join(a[:3]) + (" et al." if len(a) > 3 else "")) if a else "[authors: see DOI]"
P, Q, E = [], [], []
for i, s in enumerate(sel):
    if s["role"] != "primary": continue
    r = dict(idx=i, doi=s["doi"], title=clean(s["title"]), year=s["year"], venue=VENUE_FIX.get(s["doi"], clean(s["venue"])), authors=authors(s))
    x = X[i]
    if not x["inc"]: E.append(dict(r, reason=x["reason"])); continue
    r.update(x); r["tot"] = sum(x["qa"]); (P if r["tot"] >= QA_MIN else Q).append(r)
P.sort(key=lambda r: (r["year"], r["title"]))
for k, r in enumerate(P, 1): r["sid"] = f"P{k:02d}"
S = sorted([dict(doi=s["doi"], title=clean(s["title"]), year=s["year"], venue=clean(s["venue"]), authors=authors(s)) for s in sel if s["role"] == "survey"], key=lambda r: (r["year"], r["title"]))
N = len(P); ALL = P + Q
def cnt(rows, f): return C.Counter(t for r in rows for t in r[f].split())
st = dict(N=N, nQ=len(Q), nE=len(E), nS=len(S), year=dict(sorted(C.Counter(r["year"] for r in P).items())),
  arch=cnt(P, "arch"), aut=cnt(P, "aut"), task=cnt(P, "task"), ev=cnt(P, "ev"), tool=cnt(P, "tool"), safe=cnt(P, "safe"),
  no_safe=[r["sid"] for r in P if not r["safe"]], qa=[round(sum(r["qa"][j] for r in P) / N, 2) for j in range(5)], tot=round(sum(r["tot"] for r in P) / N, 2),
  llm=[r["sid"] for r in P if r["arch"] in ("LLM-SA", "LLM-MA", "RAG", "HYB", "NS")], rl=[r["sid"] for r in P if r["arch"] in ("DRL", "MARL", "GT", "PLAN")],
  aut_by_ev={a: dict(C.Counter(t for r in P if r["aut"] == a for t in r["ev"].split())) for a in ["A1", "A2", "A3", "A4"]},
  arch_by_aut={a: dict(C.Counter(r["arch"] for r in P if r["aut"] == a)) for a in ["A1", "A2", "A3", "A4"]},
  task_by_arch={t: dict(C.Counter(r["arch"] for r in P if t in r["task"].split())) for t in ["TRI", "INV", "CON", "REM", "PLN", "REP"]},
  hum=[r["sid"] for r in P if "HUM" in r["ev"].split() or "HUM" in r["safe"].split()], prod=[r["sid"] for r in P if "PROD" in r["ev"]],
  emu=[r["sid"] for r in P if "EMU" in r["ev"]], sim=[r["sid"] for r in P if r["ev"] == "SIM"],
  a34_no_safe=[r["sid"] for r in P if r["aut"] in ("A3", "A4") and not r["safe"]],
  sens_arch=cnt(ALL, "arch"), sens_aut=cnt(ALL, "aut"), sens_task=cnt(ALL, "task"), sens_ev=cnt(ALL, "ev"), sens_nosafe=sum(1 for r in ALL if not r["safe"]),
  by=lambda: None)
st.pop("by")
for f in ["arch", "aut", "task", "ev", "tool", "safe"]:
    st[f + "_ids"] = {k: [r["sid"] for r in P if k in r[f].split()] for k in st[f]}
json.dump(dict(st=st, P=P, Q=Q, E=E, S=S), open(sys.argv[1] + "/analysis.json", "w"), indent=1, default=dict)
for k, v in st.items(): print(k, ":", v)
