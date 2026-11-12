"""Crossref search harvest for the ransomware-ML SLR. Writes pool.json."""
import json, time, urllib.parse, urllib.request, sys

OUT = sys.argv[1]
QUERIES = [
    "ransomware detection machine learning",
    "ransomware detection deep learning",
    "early ransomware detection",
    "ransomware early detection pre-encryption",
    "crypto-ransomware detection behavioral",
    "ransomware detection explainable artificial intelligence",
    "ransomware detection SHAP LIME explainability",
    "ransomware classification API calls",
    "ransomware detection network traffic machine learning",
    "ransomware detection hardware performance counters",
    "ransomware detection file system I/O machine learning",
    "ransomware detection entropy machine learning",
    "android ransomware detection machine learning",
    "IoT ransomware detection deep learning",
    "ransomware detection opcode static analysis",
    "ransomware detection memory forensics machine learning",
    "ransomware detection transformer LSTM",
    "ransomware detection graph neural network",
    "ransomware detection federated learning",
    "ransomware detection survey",
    "ransomware systematic literature review",
    "ransomware detection storage SSD machine learning",
    "zero-day ransomware detection",
    "ransomware family classification",
    "ransomware detection concept drift",
    "ransomware detection cloud virtual machine",
    "ransomware detection industrial control systems",
]
FILTER = "from-pub-date:2016-01-01,until-pub-date:2026-12-31"
pool = {}
for q in QUERIES:
    for offset in (0, 100):
        url = ("https://api.crossref.org/works?" + urllib.parse.urlencode({
            "query.bibliographic": q, "filter": FILTER, "rows": 100, "offset": offset,
            "select": "DOI,title,container-title,type,published,author,publisher,is-referenced-by-count",
            "mailto": "slr-bot@example.org"}))
        for attempt in range(3):
            try:
                data = json.load(urllib.request.urlopen(url, timeout=60))
                break
            except Exception as e:
                print("retry", q, e, file=sys.stderr); time.sleep(5)
        else:
            continue
        for it in data["message"]["items"]:
            title = (it.get("title") or [""])[0]
            if "ransom" not in title.lower():
                continue
            d = it["DOI"].lower()
            rec = pool.setdefault(d, {
                "doi": d, "title": title,
                "venue": (it.get("container-title") or [""])[0],
                "type": it.get("type"), "publisher": it.get("publisher"),
                "year": (it.get("published", {}).get("date-parts") or [[None]])[0][0],
                "authors": ["%s %s" % (a.get("given", ""), a.get("family", "")) for a in it.get("author", [])],
                "cites": it.get("is-referenced-by-count", 0), "queries": []})
            rec["queries"].append(q)
        time.sleep(1)
    print(q, len(pool), file=sys.stderr)
json.dump(pool, open(OUT, "w"), indent=1)
print("total", len(pool))
