# SLR: Agentic AI for Automated Incident Response in SOCs (2021–2026)

- `agentic-ai-soc-incident-response-slr.md` — the full systematic literature review (PRISMA 2020).
- `scripts/` — `search.py` / `search2.py` (Crossref harvest, 40 strings) → `screen.py` (type/venue screen) → `lookup.py`
  (known-item look-ups) → `extract.py` (eligibility + extraction coding) → `analyze.py` (QA gate + statistics) → `tables.py`.
- `data/` — raw Crossref pools, screened sets, look-up results, abstracts used for extraction, `analysis.json` (coded evidence base).

`selected.json` (records kept at title/abstract screening, with abstracts) is a manual-screening artefact and is archived rather than regenerated.
Re-run analysis: `cd slr-agentic-soc/data && cp ../scripts/extract.py . && python3 ../scripts/analyze.py "$PWD" && python3 ../scripts/tables.py "$PWD"`
