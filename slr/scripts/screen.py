"""Venue/publisher eligibility screen (EC-venue) over pool.json -> eligible.json."""
import json, re, sys, html

pool = json.load(open(sys.argv[1]))
# Journals judged Q1/Q2 (SJR, Computer Science / security categories) from allowed publishers.
JOURNALS = {
    "ieee access", "computers & security", "sensors", "applied sciences", "information",
    "scientific reports", "electronics", "international journal of information security",
    "concurrency and computation: practice and experience", "expert systems with applications",
    "future internet", "cluster computing", "ieee transactions on information forensics and security",
    "journal of network and computer applications", "wireless personal communications",
    "forensic science international: digital investigation", "journal of computer virology and hacking techniques",
    "the journal of supercomputing", "computer networks", "journal of king saud university - computer and information sciences",
    "digital threats: research and practice", "future generation computer systems", "ict express",
    "acm computing surveys", "engineering applications of artificial intelligence", "ieee transactions on computers",
    "computers and electrical engineering", "mathematics", "egyptian informatics journal",
    "big data and cognitive computing", "ieee transactions on dependable and secure computing",
    "ieee internet of things journal", "acm transactions on privacy and security",
    "journal of information security and applications", "internet of things", "applied soft computing",
    "knowledge-based systems", "information sciences", "neural computing and applications",
    "ieee communications surveys & tutorials", "ieee transactions on emerging topics in computing",
    "ieee transactions on network and service management", "computer communications",
    "security and communication networks", "journal of systems architecture", "ieee transactions on industrial informatics",
    "ieee transactions on services computing", "ieee transactions on cloud computing", "applied intelligence",
    "multimedia tools and applications", "digital investigation", "journal of cybersecurity", "symmetry",
    "complex & intelligent systems", "ieee transactions on network science and engineering",
    "computer science review", "ieee transactions on sustainable computing", "ieee transactions on cybernetics",
    "ieee transactions on circuits and systems ii: express briefs", "ieee transactions on computer-aided design of integrated circuits and systems",
    "acm transactions on storage", "ieee transactions on consumer electronics", "journal of big data",
    "ieee open journal of the communications society", "ieee transactions on reliability", "artificial intelligence review",
    "machine learning with applications", "array", "heliyon", "alexandria engineering journal",
}
CONF = re.compile(r"(security and privacy|usenix security|computer and communications security|\bccs\b|ndss|network and distributed system|"
                  r"annual computer security applications|acsac|dimva|detection of intrusions and malware|raid|recent advances in intrusion|"
                  r"esorics|european symposium on research in computer security|icse|international conference on software engineering|"
                  r"automated software engineering|foundations of software engineering|icassp|acoustics, speech|globecom|"
                  r"dependable systems and networks|\bdsn\b|infocom|asia conference on computer and communications security|asiaccs)", re.I)
out = []
for r in pool.values():
    v = html.unescape(r["venue"] or "").strip()
    r["venue"] = v
    if r["type"] == "journal-article" and v.lower() in JOURNALS:
        r["route"] = "journal"; out.append(r)
    elif r["type"] == "proceedings-article" and CONF.search(v):
        r["route"] = "conference"; out.append(r)
out.sort(key=lambda r: (r["route"], r["venue"], r["year"] or 0))
json.dump(out, open(sys.argv[2], "w"), indent=1)
for i, r in enumerate(out):
    print(i, r["year"], r["cites"], "|", r["venue"][:40], "|", html.unescape(r["title"])[:140])
print(len(out), file=sys.stderr)
