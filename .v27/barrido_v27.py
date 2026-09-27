# -*- coding: utf-8 -*-
"""BARRIDO DE VECINOS DEL AUDITOR, vuelta 27, fase ciega.

D.38.4: la poblacion es GRAFO MAS BANDEJAS (dataset/nodos.jsonl mas
cuarentena/<libro>/*.json), descartando _insertados y _derivadas.
D.38.5: es la misma poblacion que mide el informe de la casa.

Corre con los instrumentos de la casa: aduana.buscar_vecinos y
informe.poblacion_de_bandejas. No reimplementa ninguna senial.
"""
import io, json, os, sys
sys.path.insert(0, os.path.abspath("."))
from src import aduana, informe, config as modulo_config

umbrales = modulo_config.cargar()
nodos = [json.loads(l) for l in io.open("dataset/nodos.jsonl", encoding="utf-8") if l.strip()]
bandejas = informe.poblacion_de_bandejas()
poblacion = nodos + bandejas
print("POBLACION DEL BARRIDO (D.38.4)")
print("  grafo    : %d" % len(nodos))
print("  bandejas : %d" % len(bandejas))
print("  total    : %d" % len(poblacion))
print("  umbrales : similitud %.2f | familia %.2f | paso_contra_nodo %.2f"
      % (umbrales["umbral_similitud_texto"], umbrales["umbral_familia_id"],
         umbrales["umbral_paso_contra_nodo"]))
print()

DOCE = sys.argv[1:]
por_id = {}
for n in poblacion:
    por_id.setdefault(n.get("id"), n)

# veredictos escritos, SOLO el par: no leo razon ni veredicto
pares_escritos = {}
for l in io.open("bitacora/VEREDICTOS.jsonl", encoding="utf-8"):
    if not l.strip(): continue
    d = json.loads(l)
    pares_escritos.setdefault(d["candidato"], set()).add(d["vecino"])
    pares_escritos.setdefault(d["vecino"], set()).add(d["candidato"])

total_v = 0
for cid in DOCE:
    cand = por_id.get(cid)
    if cand is None:
        print("%s : NO ESTA EN LA POBLACION" % cid); continue
    vecinos = aduana.buscar_vecinos(cand, poblacion, umbrales)
    total_v += len(vecinos)
    escritos = pares_escritos.get(cid, set())
    print("%s : %d vecinos por encima de umbral" % (cid, len(vecinos)))
    for v in vecinos:
        s = v["senales"]
        marca = "con veredicto" if v["id"] in escritos else "*** SIN VEREDICTO ***"
        print("    %-58s fam %.3f pxn %.3f sim %.3f  [%s]  %s"
              % (v["id"], s.get("familia_id",0), s.get("paso_contra_nodo",0),
                 s.get("similitud_texto",0), ",".join(v["levantada_por"]), marca))
    if not vecinos:
        print("    (ninguno)")
print()
print("TOTAL DE VECINOS LEVANTADOS EN ESTE BARRIDO: %d" % total_v)
