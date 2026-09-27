import json, glob, os, re, collections
LIBRO = "grove_high_output"
filas = []
# bandeja
for p in sorted(glob.glob(f"cuarentena/{LIBRO}/*.json")):
    d = json.load(open(p, encoding="utf-8"))
    filas.append(("bandeja", os.path.basename(p), d))
# grafo
for ln in open("dataset/nodos.jsonl", encoding="utf-8"):
    ln = ln.strip()
    if not ln: continue
    d = json.loads(ln)
    txt = json.dumps(d, ensure_ascii=False)
    if LIBRO in txt:
        filas.append(("grafo", d.get("id", "?"), d))

def cap_de(d):
    txt = json.dumps(d, ensure_ascii=False)
    m = re.findall(r"cap_(\d{2})", txt)
    return "cap_" + m[0] if m else None

por_cap = collections.defaultdict(lambda: [0, 0])
sin_cap = 0
tot_c = tot_p = 0
band_c = band_p = 0
graf_c = graf_p = 0
for sede, nom, d in filas:
    pasos = len(d.get("pasos_accionables") or [])
    c = cap_de(d)
    if c is None:
        sin_cap += 1
    else:
        por_cap[c][0] += 1
        por_cap[c][1] += pasos
    tot_c += 1; tot_p += pasos
    if sede == "bandeja": band_c += 1; band_p += pasos
    else: graf_c += 1; graf_p += pasos; print("   grafo:", nom, pasos, "pasos", c)

caps = sorted(glob.glob(f"fuentes/{LIBRO}/cap_*.md"))
print("capitulos del libro (ficheros cap_*.md) :", len(caps))
print("candidatos en la bandeja                :", band_c)
print("pasos_accionables en la bandeja         :", band_p)
print("insertados en el grafo                  :", graf_c)
print("pasos en los insertados                 :", graf_p)
print("TOTAL cosechado del libro               :", tot_c)
print("TOTAL pasos cosechados del libro        :", tot_p)
print("POR CAPITULO:")
todos = sorted(set([os.path.basename(c)[:-3] for c in caps]) | set(por_cap))
con = cero = 0
sc = sp = 0
for c in todos:
    n, p = por_cap.get(c, [0, 0])
    sc += n; sp += p
    marca = "   <- DIO CERO" if n == 0 else ""
    print(f"   {c}: {n:2d} candidato(s), {p:3d} paso(s){marca}")
    if n: con += 1
    else: cero += 1
print("capitulos CON al menos un candidato:", con)
print("capitulos que DIERON CERO          :", cero, sorted([c for c in todos if por_cap.get(c,[0,0])[0]==0]))
print("suma de control (por capitulo)     :", sc, "candidatos,", sp, "pasos")
print("fichas sin capitulo legible        :", sin_cap)
