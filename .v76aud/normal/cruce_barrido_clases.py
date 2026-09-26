# ACTA 75: (1) su barrido (.v76ext/vecinos_<id>.json) contra el mio sellado (.v76aud/vecinos_<id>.json), fila dirigida a fila
# dirigida, con sede, seniales, levantada_por y detalle; (2) sus lineas listas (.v76ext/veredictos_listos.txt) contra mis clases
# selladas (.v76aud/mis_clases.tsv), par a par, clase y madre. Solo lee. Toda linea que reparte trae su suma (R7).
import collections, io, json, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
L22 = [l.strip() for l in open(".v76aud/las22.txt", encoding="utf-8") if l.strip()]
def filas(d):
    r = {}
    for c in L22:
        j = json.load(open(f"{d}/vecinos_{c}.json", encoding="utf-8"))
        for v in j["vecinos"]:
            r[(c, v["id"])] = (v["sede"], json.dumps(v["senales"], sort_keys=True), tuple(v["levantada_por"]), v.get("detalle_paso"))
        r[(c, "__pob")] = (j["grafo"], j["bandejas"])
    return r
S, M = filas(".v76ext"), filas(".v76aud")
k_s = {k for k in S if k[1] != "__pob"}; k_m = {k for k in M if k[1] != "__pob"}
st = collections.Counter()
for k in k_s | k_m:
    st["en las dos, igual" if (k in S and k in M and S[k] == M[k]) else ("en las dos, DISTINTA" if (k in S and k in M) else ("solo suya" if k in S else "solo mia"))] += 1
print("(1) filas dirigidas suyas:", len(k_s), "| mias:", len(k_m), "|", dict(st), "| suma:", sum(st.values()))
pob = collections.Counter((S[(c, "__pob")], M[(c, "__pob")]) for c in L22)
print("    poblacion (grafo, bandejas) suya y mia por candidato:", {str(k): v for k, v in pob.items()}, "| suma:", sum(pob.values()))
# (2)
lin = {}; cand = None; dis = 0
for l in open(".v76ext/veredictos_listos.txt", encoding="utf-8"):
    l = l.rstrip("\r\n")
    if l.startswith("## "):
        cand = l[3:].strip(); continue
    if not l.strip() or l.startswith("#"):
        continue
    p = l.split("|")
    madre = p[2][6:] if p[2].startswith("madre=") else ""
    lin[(cand, p[0])] = (p[1], madre)
    if "DISCUTIBLE" in l: dis += 1
print("(2) lineas suyas:", len(lin), "| con DISCUTIBLE:", dis, "| las mismas filas dirigidas que mi barrido:", set(lin) == k_m)
mc = {}
for l in open(".v76aud/mis_clases.tsv", encoding="utf-8"):
    c = l.rstrip("\r\n").split("\t")
    if c[0] == "a": continue
    mc[frozenset((c[0], c[1]))] = (c[2], c[3])
cl = collections.Counter(); cls = collections.Counter()
for (a, b), (k, m) in sorted(lin.items()):
    mine = mc.get(frozenset((a, b)))
    cls[k] += 1
    if mine is None:
        cl["sin fila mia"] += 1; print("   SIN FILA MIA", a, b); continue
    igual = (k == mine[0]) and (k != "CONTINUA" or m == mine[1])
    cl["igual clase y madre" if igual else "DISTINTA"] += 1
    if not igual:
        print("   DISTINTA", a, "~", b, "| suya", k, m, "| mia", mine[0], mine[1])
print("    sus clases:", dict(cls), "| suma:", sum(cls.values()))
print("    contra mis clases:", dict(cl), "| suma:", sum(cl.values()))
