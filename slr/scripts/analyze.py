"""Apply QA threshold, compute RQ statistics, emit markdown tables + JSON for the report."""
import json, html, re, sys, collections
sys.path.insert(0, sys.argv[1])
from extract import X

sel = json.load(open(sys.argv[1] + "/selected.json"))
QA_MIN = 4
def clean(t): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html.unescape(t))).replace("N-gram", "N-gram").strip()
def authors(s):
    a = s.get("authors") or [x["name"] for x in (s.get("s2") or {}).get("authors", [])]
    a = [x.strip() for x in a if x.strip()]
    return (", ".join(a[:3]) + (" et al." if len(a) > 3 else "")) if a else "[authors: see DOI]"

VENUE_FIX = {"10.1007/978-3-030-00470-5_6": "RAID 2018 (LNCS 11050)",
             "10.1007/978-3-030-88418-5_12": "ESORICS 2021 (LNCS 12972)",
             "10.1007/978-3-319-66332-6_5": "RAID 2017 (LNCS 10453)"}
prim, qa_out, excl = [], [], []
for i, s in enumerate(sel):
    if s["role"] != "primary": continue
    x = X.get(i)
    if x is None: raise SystemExit(f"uncoded #{i} {s['title']}")
    rec = dict(idx=i, doi=s["doi"], title=clean(s["title"]), year=s["year"],
               venue=VENUE_FIX.get(s["doi"], html.unescape(s["venue"])), authors=authors(s))
    if not x["inc"]:
        excl.append(dict(rec, reason=x["reason"])); continue
    rec.update(x); rec["qa_total"] = sum(x["qa"])
    (prim if rec["qa_total"] >= QA_MIN else qa_out).append(rec)

prim.sort(key=lambda r: (r["year"], r["title"]))
for k, r in enumerate(prim, 1): r["sid"] = f"S{k:02d}"
surveys = [dict(idx=i, doi=s["doi"], title=clean(s["title"]), year=s["year"], venue=html.unescape(s["venue"]),
                authors=authors(s)) for i, s in enumerate(sel) if s["role"] == "survey"]
surveys.sort(key=lambda r: (r["year"], r["title"]))

N = len(prim)
def pct(n): return f"{n} ({100*n/N:.0f}%)"
C = collections.Counter
stats = {}
stats["n_primary"] = N; stats["n_qa_out"] = len(qa_out); stats["n_excl"] = len(excl); stats["n_surveys"] = len(surveys)
stats["year"] = dict(sorted(C(r["year"] for r in prim).items()))
stats["stage"] = C(t for r in prim for t in r["stage"].split())
stats["stage_combo"] = C(r["stage"] for r in prim)
stats["input"] = C(t for r in prim for t in r["input"].split())
stats["model"] = C(t for r in prim for t in r["model"].split())
stats["xai_any"] = sum(1 for r in prim if r["xai"])
stats["xai"] = C(t for r in prim for t in r["xai"].split())
stats["xev"] = C(r["xev"] or "none" for r in prim if r["xai"])
stats["flags"] = {f: sum(1 for r in prim if f in r["flags"]) for f in "PCUTLORFE"}
stats["platform"] = C(r["plat"] for r in prim)
stats["conf"] = C(r["conf"] for r in prim)
stats["qa_mean"] = [round(sum(r["qa"][j] for r in prim) / N, 2) for j in range(5)]
stats["qa_total_mean"] = round(sum(r["qa_total"] for r in prim) / N, 2)
stats["dp2"] = sum(1 for r in prim if r["qa"][4] == 2)
stats["early_and_xai"] = [r["sid"] for r in prim if r["xai"] and ("AT" in r["stage"] or "PRE" in r["stage"])]
stats["early_xai_deploy"] = [r["sid"] for r in prim if r["xai"] and ("AT" in r["stage"] or "PRE" in r["stage"]) and r["qa"][4] >= 1]
stats["xai_and_L"] = [r["sid"] for r in prim if r["xai"] and "L" in r["flags"]]
stats["model_by_stage"] = {st: dict(C(t for r in prim if st in r["stage"].split() for t in r["model"].split())) for st in ["PRE", "AT", "POST", "ENC"]}
stats["input_by_stage"] = {st: dict(C(t for r in prim if st in r["stage"].split() for t in r["input"].split())) for st in ["PRE", "AT", "POST", "ENC"]}
stats["U_and_T"] = [r["sid"] for r in prim if "U" in r["flags"] and "T" in r["flags"]]
stats["R_and_O"] = [r["sid"] for r in prim if "R" in r["flags"] or "O" in r["flags"]]
stats["xai_sids"] = {r["sid"]: r["xai"] for r in prim if r["xai"]}
json.dump(dict(stats=stats, prim=prim, qa_out=qa_out, excl=excl, surveys=surveys),
          open(sys.argv[1] + "/analysis.json", "w"), indent=1, default=list)
for k, v in stats.items(): print(k, ":", v)
print("QA-out:", [(r["idx"], r["qa_total"], r["title"][:50]) for r in qa_out])
