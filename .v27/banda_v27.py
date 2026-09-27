# -*- coding: utf-8 -*-
"""Recomputo de la banda de la señal 1 sobre los 35 pares de la tanda (T.3.e)."""
import io, json, subprocess, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
viejas=set(l.strip() for l in subprocess.run(["git","show","f52f77e:bitacora/VEREDICTOS.jsonl"],
    capture_output=True).stdout.decode("utf-8").split("\n") if l.strip())
nuevas=[json.loads(l) for l in io.open("bitacora/VEREDICTOS.jsonl",encoding="utf-8")
        if l.strip() and l.strip() not in viejas]
def sen(v):
    s=v.get("seniales") or v.get("señales") or v.get("senales") or {}
    return s
lev=collections.Counter(); banda=collections.Counter(); altos=[]
pares=0; declaradas=0
for v in nuevas:
    s=sen(v); lv=v.get("levantada_por") or v.get("levantada") or ""
    if isinstance(lv,str) and "lectura" in lv.lower():
        declaradas+=1; continue
    pares+=1
    ls = lv if isinstance(lv,list) else [x.strip() for x in str(lv).split(",") if x.strip()]
    for x in ls: lev[x]+=1
    sim = float(s.get("similitud_texto",0) or 0)
    if sim>=0.40: banda["0.40 en adelante"]+=1; altos.append((sim,v.get("candidato"),v.get("vecino")))
    elif sim>=0.35: banda["0.35 a 0.40"]+=1
    else: banda["por debajo de 0.35"]+=1
print("lineas nuevas                       : %d" % len(nuevas))
print("  de ellas ARISTA POR LECTURA       : %d" % declaradas)
print("PARES LEIDOS DE LA ADUANA           : %d" % pares)
print("\nQUE SENIAL LOS LEVANTA")
for k,n in sorted(lev.items(), key=lambda x:-x[1]): print("  %-20s: %d" % (k,n))
print("\nEN QUE BANDA DE SIMILITUD CAEN")
for k in ["0.35 a 0.40","0.40 en adelante","por debajo de 0.35"]:
    print("  %-22s: %d" % (k,banda[k]))
print("\nLOS QUE PASAN DE 0.40")
for s,c,ve in sorted(altos, reverse=True): print("  %.3f  %s contra %s" % (s,c,ve))
print("MAYOR SIMILITUD DE LA VUELTA        : %.3f" % max(float(sen(v).get("similitud_texto",0) or 0) for v in nuevas))
