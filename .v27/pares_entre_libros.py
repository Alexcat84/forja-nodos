# -*- coding: utf-8 -*-
import io, json, glob, subprocess, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
idx={}
for l in io.open("dataset/nodos.jsonl",encoding="utf-8"):
    if l.strip():
        d=json.loads(l); idx[d["id"]]=d
def clave(i):
    d=idx.get(i)
    if not d: return "?"
    fs=d.get("fuentes",[]) or []
    return fs[0].get("clave","?") if fs else "?"
viejas=set(l.strip() for l in subprocess.run(["git","show","f52f77e:bitacora/VEREDICTOS.jsonl"],
    capture_output=True).stdout.decode("utf-8").split("\n") if l.strip())
nuevas=[json.loads(l) for l in io.open("bitacora/VEREDICTOS.jsonl",encoding="utf-8")
        if l.strip() and l.strip() not in viejas]
print("PARES DE LA TANDA CUYO VECINO ES DE OTRO LIBRO:")
n=0
for v in nuevas:
    c=v.get("candidato"); ve=v.get("vecino")
    if clave(c)!=clave(ve):
        n+=1
        print("  %s [%s]  contra  %s [%s]   -> %s" % (c,clave(c),ve,clave(ve),v.get("veredicto")))
print("TOTAL: %d" % n)
print("\nARISTAS DEL GRAFO QUE CRUZAN DE LIBRO:")
cruce=0; total=0
for d in idx.values():
    for h in d.get("nodos_siguientes",[]) or []:
        total+=1
        if clave(d["id"])!=clave(h):
            cruce+=1; print("  %s [%s] > %s [%s]" % (d["id"],clave(d["id"]),h,clave(h)))
print("aristas declaradas por nodos_siguientes: %d, de ellas entre libros: %d" % (total,cruce))
