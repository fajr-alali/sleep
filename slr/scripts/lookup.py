"""Title lookup in Crossref; prints top match per title (for snowballing known works)."""
import json, sys, urllib.parse, urllib.request, time, html, difflib

titles = [l.strip() for l in open(sys.argv[1]) if l.strip()]
res = []
for t in titles:
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode({
        "query.bibliographic": t, "rows": 3, "mailto": "slr-bot@example.org",
        "select": "DOI,title,container-title,type,published,author,publisher,is-referenced-by-count"})
    items = json.load(urllib.request.urlopen(url, timeout=60))["message"]["items"]
    best = max(items, key=lambda it: difflib.SequenceMatcher(None, t.lower(), html.unescape((it.get("title") or [""])[0]).lower()).ratio())
    bt = html.unescape((best.get("title") or [""])[0])
    sim = difflib.SequenceMatcher(None, t.lower(), bt.lower()).ratio()
    rec = {"query": t, "sim": round(sim, 2), "doi": best["DOI"].lower(), "title": bt,
           "venue": html.unescape((best.get("container-title") or [""])[0]), "type": best.get("type"),
           "publisher": best.get("publisher"),
           "year": (best.get("published", {}).get("date-parts") or [[None]])[0][0],
           "authors": ["%s %s" % (a.get("given", ""), a.get("family", "")) for a in best.get("author", [])],
           "cites": best.get("is-referenced-by-count", 0)}
    res.append(rec)
    print(rec["sim"], rec["year"], rec["doi"], "|", rec["venue"][:50], "|", bt[:100])
    time.sleep(0.5)
json.dump(res, open(sys.argv[2], "w"), indent=1)
