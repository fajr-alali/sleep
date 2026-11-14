"""Crossref harvest for the agentic-AI SOC incident-response SLR. Writes pool.json."""
import json, re, time, urllib.parse, urllib.request, sys, html
OUT = sys.argv[1]
QUERIES = [
 "agentic artificial intelligence cyber defense",
 "intrusion response system deep reinforcement learning",
 "automated intrusion response optimal policy",
 "autonomous security operations center",
 "LLM agent security alert investigation",
 "large language model incident response automation",
 "cyber defense agent CybORG reinforcement learning",
 "multi-agent reinforcement learning network defense",
 "self-adaptive security response attack mitigation reinforcement learning",
 "moving target defense reinforcement learning autonomous",
 "large language model SOC analyst",
 "AI agents security orchestration playbooks",
 "autonomous response advanced persistent threat reinforcement learning",
 "LLM digital forensics incident investigation agent",
 "reinforcement learning cyber attack mitigation software defined network",
]
KEEP_A = re.compile(r"agent|autonom|llm|large language|gpt|generative|soar|orchestrat|copilot|reinforcement|self-healing|chatbot|language model", re.I)
KEEP_B = re.compile(r"incident|\bsoc\b|security operation|cyber.?defen|response|alert|triage|threat hunt|intrusion|cyber.?security|network defen|attack|threat", re.I)
FILTER = "from-pub-date:2021-01-01,until-pub-date:2026-12-31"
pool = {}
for q in QUERIES:
    for offset in (0, 100):
        url = ("https://api.crossref.org/works?" + urllib.parse.urlencode({
            "query.bibliographic": q, "filter": FILTER, "rows": 100, "offset": offset,
            "select": "DOI,title,container-title,type,published,author,publisher,is-referenced-by-count",
            "mailto": "slr-bot@example.org"}))
        for _ in range(3):
            try: data = json.load(urllib.request.urlopen(url, timeout=60)); break
            except Exception as e: print("retry", e, file=sys.stderr); time.sleep(5)
        else: continue
        for it in data["message"]["items"]:
            t = html.unescape((it.get("title") or [""])[0])
            if not (KEEP_A.search(t) and KEEP_B.search(t)): continue
            d = it["DOI"].lower()
            rec = pool.setdefault(d, {"doi": d, "title": t, "venue": html.unescape((it.get("container-title") or [""])[0]),
                "type": it.get("type"), "publisher": it.get("publisher"),
                "year": (it.get("published", {}).get("date-parts") or [[None]])[0][0],
                "authors": ["%s %s" % (a.get("given", ""), a.get("family", "")) for a in it.get("author", [])],
                "cites": it.get("is-referenced-by-count", 0), "queries": []})
            rec["queries"].append(q)
        time.sleep(1)
    print(q, len(pool), file=sys.stderr)
json.dump(pool, open(OUT, "w"), indent=1); print("total", len(pool))
