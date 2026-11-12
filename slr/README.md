# SLR: Machine Learning for Ransomware Detection (2016–2026)

- `ransomware-ml-slr.md` — the full systematic literature review (PRISMA 2020).
- `scripts/` — the re-runnable pipeline: `search.py` (Crossref harvest, 27 strings) → `screen.py` (type/venue screen)
  → `lookup.py` (snowball title look-ups) → `extract.py` (eligibility + extraction coding) → `analyze.py` (QA gate, statistics)
  → `taxonomy.py` (XL/DRL levels) → `tables.py` (markdown tables and references).
- `data/` — raw Crossref pool, screened sets, abstracts used for extraction, and `analysis.json` (final coded evidence base).

Re-run (needs network access to api.crossref.org and api.semanticscholar.org):
```
cd slr/data && python3 ../scripts/search.py pool.json && python3 ../scripts/screen.py pool.json eligible.json
cp ../scripts/extract.py . && python3 ../scripts/analyze.py "$PWD" && python3 ../scripts/taxonomy.py "$PWD" && python3 ../scripts/tables.py "$PWD"
```
Note: `selected.json` (which records were kept at title/abstract screening, plus the Semantic Scholar abstracts) is a manual-screening
artefact and is archived here rather than regenerated.
