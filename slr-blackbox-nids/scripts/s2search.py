"""Semantic Scholar bulk search (title+abstract) with a search log. Usage: s2search.py <tag> <query> <out.json>"""
import json, sys, time, datetime, urllib.parse, urllib.request
tag, q, out = sys.argv[1], sys.argv[2], sys.argv[3]
base = "https://api.semanticscholar.org/graph/v1/paper/search/bulk?"
params = {"query": q, "year": "2020-2026", "fields": "title,abstract,venue,year,publicationTypes,externalIds,journal,publicationDate,authors"}
res, token, total = [], None, None
while True:
    p = dict(params); 
    if token: p["token"] = token
    for a in range(8):
        try: d = json.load(urllib.request.urlopen(base + urllib.parse.urlencode(p), timeout=90)); break
        except Exception as e: time.sleep(10 * (a + 1))
    else: raise SystemExit("failed")
    total = d.get("total"); res += d.get("data", []); token = d.get("token")
    if not token: break
    time.sleep(2)
json.dump(res, open(out, "w"))
log = dict(source="Semantic Scholar Graph API /paper/search/bulk (fields searched: title+abstract)", tag=tag, query=q,
           executed=datetime.datetime.utcnow().isoformat() + "Z", date_filter="year=2020-2026", doc_type_filter="none at query time (applied in screening)",
           results_returned=total, results_exported=len(res), export_format="JSON", cap="none (paged to completion)")
open("search_log.jsonl", "a").write(json.dumps(log) + "\n"); print(tag, total, len(res))
