"""Assemble the single Stage 1-3 document from the section files and data registers."""
import csv, re, sys
D = sys.argv[1]
def body(f):
    t = open(f"{D}/{f}").read()
    t = re.sub(r'^# .*\n', '', t, count=1)
    return re.sub(r'^(#{2,5}) ', lambda m: '#' + m.group(1) + ' ', t, flags=re.M)
def esc(s): return (s or '').replace('|', '\\|').replace('\n', ' ')
out = ["# Black-Box Evasion Attacks Against ML-Based NIDS — Systematic Review: Stage 1–3 Package", "",
"**Date:** 16 November 2026  ", "**Overall status: INCOMPLETE — not a manuscript; not submission-ready.** Numbered citations [n] refer to Section 5.", "",
"| Stage | Status |", "|---|---|", "| 1 Feasibility and novelty audit | Provisional (abstracts only; comparator full texts not read) |",
"| 2 Protocol | Provisional, unregistered |", "| 3 Searches and screening | Partially completed and evidenced |",
"| 4 Full-text extraction and appraisal | Pending external access |", "| 5–7 Synthesis, manuscript, integrity audit | Not started |", "",
"## Contents", "1. Feasibility and novelty audit", "2. Review protocol", "3. Executed searches and screening", "4. Outstanding-actions register", "5. Reference list (user-supplied, verified)",
"Appendix A. Search log · Appendix B. Seed coverage test · Appendix C. Candidate register · Appendix D. Title/abstract screening log", "", "---", ""]
for n, (t, f) in enumerate([("Feasibility and Novelty Audit", "01_feasibility_and_novelty_audit.md"), ("Review Protocol", "02_protocol.md"),
        ("Executed Searches and Screening", "03_search_and_screening_report.md"), ("Outstanding-Actions Register", "04_outstanding_actions.md"),
        ("Reference List (user-supplied, verified)", "05_references.md")], 1):
    sec = body(f).strip()
    sec = re.sub(r'^### (\d+(\.\d+)?)\.? ', '### ', sec, flags=re.M)
    k = 0
    def num(m):
        global k; k += 1; return f"### {n}.{k} "
    sec = re.sub(r'^### ', num, sec, flags=re.M)
    out += [f"## {n}. {t}", "", sec, "", "---", ""]
out += ["## Appendix A. Search log (all executed searches)", "", "| Tag | Source | Exact query | Executed (UTC) | Date filter | Doc-type filter | Returned | Exported | Cap |", "|---|---|---|---|---|---|---|---|---|"]
for r in csv.DictReader(open(f"{D}/data/search_log.csv")):
    out.append(f"| {r['tag']} | {esc(r['source'])} | `{esc(r['query'])}` | {r['executed'][:19]} | {r['date_filter']} | {esc(r['doc_type_filter'])} | {r['results_returned']} | {r['results_exported']} | {esc(r['cap'])} |")
out += ["", "## Appendix B. Seed coverage test", "", "| Seed title | DOI | Venue | Verified journal seed | Found by initial queries | Found after amendment |", "|---|---|---|---|---|---|"]
for r in csv.DictReader(open(f"{D}/data/seed_coverage_test.csv")): out.append("| " + " | ".join(esc(x) for x in r.values()) + " |")
rows = list(csv.DictReader(open(f"{D}/data/candidate_register.csv")))
out += ["", f"## Appendix C. Candidate register ({len(rows)} records)", "",
"All metadata verified in Crossref on 16 Nov 2026. **For every record: journal eligibility (SJR quartile) = pending; full text retrieved = no; full text extracted = no; extraction independently checked = no.** Quartile expectations are the reviewer's unverified judgement and do not exclude any record.", "",
"| ID | Title | Journal | Online date | Vol/Issue/Pages | DOI | Source | T/A note | Quartile expectation |", "|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    vip = "/".join(x for x in [r['volume'], r['issue'], r['pages_or_article']] if x) or "—"
    out.append(f"| {r['cand_id']} | {esc(r['title'])} | {esc(r['journal'])} | {r['online_date']} | {esc(vip)} | [{r['doi']}](https://doi.org/{r['doi']}) | {esc(r['source'])} | {esc(r['ta_note'])} | {esc(r['quartile_expectation'])} |")
out += ["", "## Appendix D. Title/abstract screening log (black-box-hint subset, 129 records)", "", "| # | Year | Title | Venue (Semantic Scholar) | Decision | Reason |", "|---|---|---|---|---|---|"]
for r in csv.DictReader(open(f"{D}/data/screening_log_blackbox_subset.csv")):
    out.append(f"| {r['row']} | {r['year']} | {esc(r['title'])} | {esc(r['venue_S2'])} | {r['decision']} | {esc(r['reason']) or '—'} |")
out += ["", "---", "*Raw API exports and scripts: `slr-blackbox-nids/data/raw/` and `slr-blackbox-nids/scripts/`.*"]
open(f"{D}/blackbox-nids-slr-stage1-3.md", "w").write("\n".join(out) + "\n")
