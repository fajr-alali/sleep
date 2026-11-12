"""Assign Deployment Readiness Level (DRL) and Explanation Level (XL) per study; cross-tabulate with stage."""
import json, sys, collections
a = json.load(open(sys.argv[1] + "/analysis.json"))
def drl(r):
    f = r["flags"]
    if "R" in f and ("O" in f or "L" in f): return 4 if "T" in f else 3
    if "O" in f or ("L" in f and r["qa"][4] == 2): return 3
    if "L" in f: return 2
    if "U" in f or "F" in f or "T" in f: return 1
    return 0
def xl(r):
    x = r["xai"].split()
    if not x: return 0
    if "INT" in x or "UQ" in x: return 3
    if set(x) & {"SHAP", "LIME", "ATT"}: return 2
    return 1
rows = []
for r in a["prim"]:
    r["drl"], r["xl"] = drl(r), xl(r); rows.append(r)
print("DRL", sorted(collections.Counter(r["drl"] for r in rows).items()))
print("XL", sorted(collections.Counter(r["xl"] for r in rows).items()))
for lv in range(5): print("DRL", lv, [r["sid"] for r in rows if r["drl"] == lv])
for lv in range(4): print("XL", lv, [r["sid"] for r in rows if r["xl"] == lv])
first = lambda r: [s for s in ["PRE", "AT", "POST", "ENC"] if s in r["stage"].split()][0]
tab = collections.Counter((first(r), r["drl"]) for r in rows)
print("stage(earliest) x DRL")
for s in ["PRE", "AT", "POST", "ENC"]: print(s, [tab[(s, d)] for d in range(5)])
tab2 = collections.Counter((first(r), r["xl"]) for r in rows)
for s in ["PRE", "AT", "POST", "ENC"]: print(s, "XL", [tab2[(s, d)] for d in range(4)])
print("XL>=2 and DRL>=2:", [r["sid"] for r in rows if r["xl"] >= 2 and r["drl"] >= 2])
print("XL>=1 and DRL>=3:", [r["sid"] for r in rows if r["xl"] >= 1 and r["drl"] >= 3])
json.dump(a, open(sys.argv[1] + "/analysis.json", "w"), indent=1)
