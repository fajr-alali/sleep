"""Render markdown tables and references from analysis.json -> tables.md."""
import json, sys
d = sys.argv[1]; a = json.load(open(d + "/analysis.json")); sel = json.load(open(d + "/selected.json"))
P, Q, E, S = a["P"], a["Q"], a["E"], a["S"]
AUT = {"A1": "A1 Assist", "A2": "A2 HITL", "A3": "A3 Bounded", "A4": "A4 Full"}
def L(x): return x.replace(" ", ", ") or "—"
o = ["<!-- extraction -->", "| ID | Year | Venue | Architecture | Autonomy | SOC tasks | Evaluation | Tool / data integration | Safety & governance |", "|---|---|---|---|---|---|---|---|---|"]
for r in P:
    o.append(f"| {r['sid']} | {r['year']} | {r['venue'][:34]} | {r['arch']} | {AUT[r['aut']]} | {L(r['task'])} | {L(r['ev'])} | {L(r['tool'])} | {L(r['safe'])} |")
o += ["", "<!-- notes -->", "| ID | Short title | Key characteristics (from abstract) |", "|---|---|---|"]
for r in P: o.append(f"| {r['sid']} | {r['title'][:60]}{'…' if len(r['title'])>60 else ''} | {r.get('note') or '—'} |")
o += ["", "<!-- qa -->", "| ID | Short title | AU | ER | RP | SF | DP | Total /10 | Extraction basis |", "|---|---|---|---|---|---|---|---|---|"]
for r in P:
    au, er, rp, sf, dp = r["qa"]
    o.append(f"| {r['sid']} | {r['title'][:52]}{'…' if len(r['title'])>52 else ''} | {au} | {er} | {rp} | {sf} | {dp} | **{r['tot']}** | {'abstract' if r['conf']=='A' else 'TLDR/metadata [CANDIDATE coding]'} |")
o += ["", "<!-- qa_out -->", "| Title | Year | Venue | Arch / autonomy | QA | DOI |", "|---|---|---|---|---|---|"]
for r in sorted(Q, key=lambda r: (r["year"], r["title"])):
    o.append(f"| {r['title'][:68]} | {r['year']} | {r['venue'][:34]} | {r['arch']} / {r['aut']} | {r['tot']} | [{r['doi']}](https://doi.org/{r['doi']}) |")
o += ["", "<!-- excluded -->", "| Title | Year | Venue | Reason | DOI |", "|---|---|---|---|---|"]
for r in sorted(E, key=lambda r: r["year"]):
    o.append(f"| {r['title'][:68]} | {r['year']} | {r['venue'][:34]} | {r['reason']} | [{r['doi']}](https://doi.org/{r['doi']}) |")
o += ["", "<!-- refs_primary -->"]
for r in P:
    tag = "[VERIFIED]" if r["conf"] == "A" else "[VERIFIED metadata · CANDIDATE coding]"
    o += [f"[{r['sid']}] {r['authors']}, “{r['title']},” *{r['venue']}*, {r['year']}. DOI: {r['doi']}. Link: https://doi.org/{r['doi']} {tag}", ""]
o += ["", "<!-- refs_surveys -->"]
for k, r in enumerate(S, 1):
    o += [f"[R{k:02d}] {r['authors']}, “{r['title']},” *{r['venue']}*, {r['year']}. DOI: {r['doi']}. Link: https://doi.org/{r['doi']} [VERIFIED]", ""]
o += ["", "<!-- refs_context -->"]
for k, i in enumerate([2, 50], 1):
    s = sel[i]; au = [x.strip() for x in s.get("authors", []) if x.strip()]
    au = (", ".join(au[:3]) + (" et al." if len(au) > 3 else "")) if au else "[authors: see DOI]"
    o += [f"[C{k}] {au}, “{s['title']},” *{s['venue']}*, {s['year']}. DOI: {s['doi']}. Link: https://doi.org/{s['doi']} [VERIFIED; contextual, not a primary study]", ""]
open(d + "/tables.md", "w").write("\n".join(o)); print("ok")
