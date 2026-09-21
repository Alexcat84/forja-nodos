import json,glob,re,os
ver=[json.loads(l) for l in open("bitacora/VEREDICTOS.jsonl",encoding="utf-8") if l.strip()]
nodos={json.loads(l)["id"]:json.loads(l) for l in open("dataset/nodos.jsonl",encoding="utf-8") if l.strip()}
print("ARISTAS EN COLA ESCRITAS EN LA BITACORA (campo arista_en_cola)")
n=0; ab=0
for i,v in enumerate(ver,1):
    if v.get("arista_en_cola"):
        n+=1
        a=v["arista_en_cola"]
        m=re.split(r"\s*>\s*",a) if isinstance(a,str) else None
        cab=False
        if m and len(m)==2:
            madre,hija=m
            cab = madre in nodos and hija in (nodos[madre].get("nodos_siguientes") or [])
        if not cab: ab+=1
        print("  linea %d: %s -> %s" % (i, a, "CABLEADA" if cab else "ABIERTA"))
print("  escritas: %d, cableadas: %d, abiertas: %d" % (n, n-ab, ab))
print()
p="censos/series_y_cabezas.md"
print("censos/series_y_cabezas.md existe:", os.path.exists(p), "| lineas de tabla:",
      sum(1 for l in open(p,encoding="utf-8") if l.strip().startswith("|")) if os.path.exists(p) else "-")
print()
c4=[]
for f in glob.glob("cuarentena/scott_radical_candor/*.json"):
    d=json.load(open(f,encoding="utf-8"))
    if "cap_04" in (d.get("resumen_teorico") or ""): c4.append((os.path.basename(f),len(d.get("pasos_accionables") or [])))
print("cap_04 en bandeja: %d candidatos, %d pasos" % (len(c4), sum(x[1] for x in c4)))
for x in sorted(c4): print("   ",x[0],x[1])
