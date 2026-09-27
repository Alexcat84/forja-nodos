# -*- coding: utf-8 -*-
"""Verificacion del auditor, vuelta 26. Lee del arbol, no del reporte."""
import io, json, subprocess, sys, collections
sys.stdout.reconfigure(encoding="utf-8")

def jl(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]

nodos = jl("dataset/nodos.jsonl")
ver = jl("bitacora/VEREDICTOS.jsonl")
print("nodos en el grafo                 : %d" % len(nodos))
print("veredictos en bitacora            : %d" % len(ver))

def git_show(rev, path):
    return subprocess.run(["git","show","%s:%s" % (rev,path)],capture_output=True).stdout.decode("utf-8")

antes_n = [json.loads(l) for l in git_show("f52f77e","dataset/nodos.jsonl").split("\n") if l.strip()]
antes_v = [json.loads(l) for l in git_show("f52f77e","bitacora/VEREDICTOS.jsonl").split("\n") if l.strip()]
print("nodos en f52f77e (antes de la 26) : %d" % len(antes_n))
print("veredictos en f52f77e             : %d" % len(antes_v))
print("NUEVOS NODOS                      : %d" % (len(nodos)-len(antes_n)))
print("NUEVAS LINEAS DE BITACORA         : %d" % (len(ver)-len(antes_v)))

def aristas(ns):
    s = set()
    for n in ns:
        for h in n.get("nodos_siguientes",[]) or []:
            s.add((n["id"],h))
        for m in n.get("nodos_previos",[]) or []:
            s.add((m,n["id"]))
    return s

a0, a1 = aristas(antes_n), aristas(nodos)
print("aristas antes                     : %d" % len(a0))
print("aristas ahora                     : %d" % len(a1))
print("NUEVAS ARISTAS                    : %d" % len(a1-a0))
for m,h in sorted(a1-a0): print("   %s > %s" % (m,h))
print("RETIRADAS                         : %d" % len(a0-a1))

nuevos = [n["id"] for n in nodos if n["id"] not in {x["id"] for x in antes_n}]
print("\nLOS NUEVOS (%d):" % len(nuevos))
for i in sorted(nuevos): print("   %s" % i)

# lineas nuevas de bitacora, por candidato y por forma
viejas = set()
for l in git_show("f52f77e","bitacora/VEREDICTOS.jsonl").split("\n"):
    if l.strip(): viejas.add(l.strip())
nuevas = [json.loads(l) for l in io.open("bitacora/VEREDICTOS.jsonl",encoding="utf-8") if l.strip() and l.strip() not in viejas]
print("\nLINEAS NUEVAS DE BITACORA: %d" % len(nuevas))
porforma = collections.Counter()
porcand = collections.Counter()
for v in nuevas:
    tipo = v.get("veredicto") or v.get("clase") or "?"
    porforma[tipo]+=1
    porcand[v.get("candidato") or v.get("id") or "?"]+=1
print("  por veredicto:", dict(porforma))
for k in sorted(porcand): print("   %-46s %d" % (k, porcand[k]))
