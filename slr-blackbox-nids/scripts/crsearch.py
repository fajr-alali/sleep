"""Crossref complementary searches with log (query.bibliographic: title/author/venue metadata, not full text)."""
import json, sys, time, datetime, urllib.parse, urllib.request, html
QS = ["black-box adversarial attack network intrusion detection", "evasion attack network intrusion detection machine learning",
      "adversarial examples intrusion detection deep learning", "transferability adversarial network intrusion detection",
      "adversarial botnet detection evasion", "adversarial traffic generation intrusion detection GAN evasion",
      "defense adversarial attacks network intrusion detection", "query-based attack intrusion detection system"]
pool = {}
for q in QS:
    got = 0
    for off in (0, 100):
        url = "https://api.crossref.org/works?" + urllib.parse.urlencode({"query.bibliographic": q, "filter": "from-pub-date:2020-01-01,type:journal-article",
              "rows": 100, "offset": off, "mailto": "slr-review@example.org", "select": "DOI,title,container-title,published,ISSN,author,type,relation"})
        d = json.load(urllib.request.urlopen(url, timeout=90))["message"]; total = d["total-results"]
        for it in d["items"]:
            pool.setdefault(it["DOI"].lower(), dict(doi=it["DOI"].lower(), title=html.unescape((it.get("title") or [""])[0]),
                 venue=html.unescape((it.get("container-title") or [""])[0]), issn=it.get("ISSN"), year=(it.get("published", {}).get("date-parts") or [[None]])[0][0],
                 authors=["%s %s" % (a.get("given", ""), a.get("family", "")) for a in it.get("author", [])], relation=it.get("relation")))
            got += 1
        time.sleep(1)
    open("search_log.jsonl", "a").write(json.dumps(dict(source="Crossref REST API /works (query.bibliographic; metadata fields, not abstracts/full text)", tag="CR", query=q,
        executed=datetime.datetime.now(datetime.UTC).isoformat(), date_filter="from-pub-date:2020-01-01", doc_type_filter="type:journal-article",
        results_returned=total, results_exported=got, export_format="JSON", cap="first 200 by relevance")) + "\n")
    print(q, total, got)
json.dump(pool, open("crossref_pool.json", "w")); print(len(pool))
