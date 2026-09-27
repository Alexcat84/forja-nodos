import json, glob, os, re, collections
LIBRO="grove_high_output"
def cap_de(d):
    r=d.get("resumen_teorico","") or ""
    m=re.search(r"UNIDAD DE ORIGEN:\s*fuentes/%s/(cap_\d{2})\.md"%LIBRO, r)
    if m: return m.group(1)
    m=re.search(r"(cap_\d{2})\.md", r)
    return m.group(1) if m else None
por=collections.defaultdict(lambda:[0,0]); sin_cap=0; tot=[0,0]; band=[0,0]; graf=[0,0]
items=[]
for p in sorted(glob.glob(f"cuarentena/{LIBRO}/*.json")):
    items.append(("bandeja",os.path.basename(p)[:-5],json.load(open(p,encoding="utf-8"))))
for ln in open("dataset/nodos.jsonl",encoding="utf-8"):
    ln=ln.strip()
    if not ln: continue
    d=json.loads(ln)
    if any(f.get("clave")==LIBRO for f in (d.get("fuentes") or [])):
        items.append(("grafo",d.get("id"),d))
for sede,nom,d in items:
    n=len(d.get("pasos_accionables") or []); c=cap_de(d)
    if c is None: sin_cap+=1; print("SIN CAPITULO:",nom)
    else: por[c][0]+=1; por[c][1]+=n
    tot[0]+=1; tot[1]+=n
    (band if sede=="bandeja" else graf)[0]+=1
    (band if sede=="bandeja" else graf)[1]+=n
    if sede=="grafo": print("   en el grafo:",nom,n,"pasos,",c)
caps=sorted(os.path.basename(x)[:-3] for x in glob.glob(f"fuentes/{LIBRO}/cap_*.md"))
print("capitulos del libro                     :",len(caps))
print("candidatos en la bandeja                :",band[0])
print("pasos_accionables en la bandeja         :",band[1])
print("insertados en el grafo                  :",graf[0])
print("pasos en los insertados                 :",graf[1])
print("TOTAL cosechado del libro               :",tot[0])
print("TOTAL pasos cosechados del libro        :",tot[1])
todos=sorted(set(caps)|set(por)); sc=sp=0; con=0; ceros=[]
print("POR CAPITULO (bandeja MAS grafo, capitulo leido de UNIDAD DE ORIGEN del resumen_teorico):")
for c in todos:
    n,p=por.get(c,[0,0]); sc+=n; sp+=p
    print(f"   {c}: {n:2d} candidato(s), {p:3d} paso(s)"+("   <- DIO CERO" if n==0 else ""))
    if n: con+=1
    else: ceros.append(c)
print("capitulos CON al menos un candidato:",con)
print("capitulos que DIERON CERO          :",len(ceros),ceros)
print("suma de control (por capitulo)     :",sc,"candidatos,",sp,"pasos")
print("fichas sin capitulo legible        :",sin_cap)
