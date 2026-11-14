"""Crossref harvest for the agentic-AI SOC incident-response SLR. Writes pool.json."""
import json, re, time, urllib.parse, urllib.request, sys, html
OUT = sys.argv[1]
QUERIES = [
 "agentic AI incident response security operations center",
 "LLM agent security operations center",
 "large language model agents incident response",
 "autonomous incident response cyber security",
 "autonomous cyber defense agent reinforcement learning",
 "multi-agent system cyber incident response",
 "AI agent alert triage security operations",
 "large language model security operations center automation",
 "SOAR security orchestration automation response machine learning",
 "automated intrusion response system reinforcement learning",
 "LLM threat hunting autonomous agent",
 "retrieval augmented generation incident response cybersecurity",
 "large language model cyber threat intelligence agent",
 "autonomous cyber operations deep reinforcement learning defender",
 "human-AI teaming security operations center",
 "LLM-based agent cybersecurity tool use",
 "automated incident handling playbook generation large language model",
 "self-healing network autonomous response attack",
 "agentic AI cybersecurity survey",
 "large language models cybersecurity survey",
 "AI security operations center survey",
 "automated cyber incident response survey",
 "autonomous network defense agent",
 "LLM log analysis incident investigation",
 "generative AI security operations",
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
