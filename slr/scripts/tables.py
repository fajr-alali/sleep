"""Render markdown tables from analysis.json into tables.md (pasted into the report)."""
import json, sys
a = json.load(open(sys.argv[1] + "/analysis.json"))
P, S, Q, E = a["prim"], a["surveys"], a["qa_out"], a["excl"]
ST = {"PRE": "Pre-exec", "AT": "At-exec", "POST": "Post-exec", "ENC": "Post-enc"}
def link(d): return f"https://doi.org/{d}"
o = []
o.append("<!-- TABLE: extraction -->")
o.append("| ID | Year | Venue | Stage | Input | Model | XAI | Deployment evidence |")
o.append("|---|---|---|---|---|---|---|---|")
FL = {"P": "public data", "U": "unseen-family test", "T": "temporal/drift test", "L": "latency", "O": "overhead",
      "R": "real/bare-metal or production-like env.", "F": "FPR", "E": "early-detection goal"}
for r in P:
    st = ", ".join(ST[t] for t in r["stage"].split())
    ev = "; ".join(FL[f] for f in r["flags"] if f in FL) or "—"
    o.append(f"| {r['sid']} | {r['year']} | {r['venue'][:38]} | {st} | {r['input'].replace(' ', ', ')} | "
             f"{r['model'].replace(' ', ', ')} | {r['xai'].replace(' ', ', ') or '—'} | {ev} |")
o.append("\n<!-- TABLE: qa -->")
o.append("| ID | Short title | DR | ER | RP | EX | DP | Total /10 | Extraction basis |")
o.append("|---|---|---|---|---|---|---|---|---|")
for r in P:
    dr, er, rp, ex, dp = r["qa"]
    o.append(f"| {r['sid']} | {r['title'][:55]}{'…' if len(r['title'])>55 else ''} | {dr} | {er} | {rp} | {ex} | {dp} | **{r['qa_total']}** | {'abstract' if r['conf']=='A' else 'TLDR/metadata [CANDIDATE coding]'} |")
o.append("\n<!-- TABLE: qa_out -->")
o.append("| Short title | Year | Venue | QA total | DOI |")
o.append("|---|---|---|---|---|")
for r in sorted(Q, key=lambda r: (r["year"], r["title"])):
    o.append(f"| {r['title'][:70]} | {r['year']} | {r['venue'][:40]} | {r['qa_total']} | [{r['doi']}]({link(r['doi'])}) |")
o.append("\n<!-- TABLE: excluded -->")
o.append("| Title | Year | Reason | DOI |")
o.append("|---|---|---|---|")
for r in sorted(E, key=lambda r: r["year"]):
    o.append(f"| {r['title'][:70]} | {r['year']} | {r['reason']} | [{r['doi']}]({link(r['doi'])}) |")
o.append("\n<!-- REFS: primary -->")
for r in P:
    tag = "[VERIFIED]" if r["conf"] == "A" else "[VERIFIED metadata · CANDIDATE coding]"
    o.append(f"[{r['sid']}] {r['authors']}, “{r['title']},” *{r['venue']}*, {r['year']}. DOI: {r['doi']}. Link: {link(r['doi'])} {tag}")
    o.append("")
o.append("\n<!-- REFS: surveys -->")
for k, r in enumerate(S, 1):
    o.append(f"[R{k:02d}] {r['authors']}, “{r['title']},” *{r['venue']}*, {r['year']}. DOI: {r['doi']}. Link: {link(r['doi'])} [VERIFIED]")
    o.append("")
open(sys.argv[1] + "/tables.md", "w").write("\n".join(o))
print(len(o))
