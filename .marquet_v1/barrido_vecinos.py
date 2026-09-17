# -*- coding: utf-8 -*-
"""CERO CONSTANTES TECLEADAS: no hay ni una lista de ids dentro. La poblacion y
los candidatos a barrer salen los dos del dato (glob sobre cuarentena/ y lectura
de dataset/nodos.jsonl). Es el REMEDIO 4 de la ACTA 30 aplicado a mi propio
instrumento: el barrido de la vuelta 21 llevaba `.lote_v21_auditor.txt` dentro.

Barrido de vecinos D.38.4 (GRAFO MAS BANDEJAS), leave-one-out.
Usa src.aduana.buscar_vecinos, el instrumento de la casa. CERO ESCRITURAS.

    python .marquet_v1/barrido_vecinos.py cuarentena/marquet_turn_the_ship
"""
import io, json, glob, os, sys
sys.path.insert(0, os.path.abspath('.'))
from src import aduana, comun, config as modulo_config

comun.salida_utf8()
umbrales = modulo_config.cargar()

nodos = [json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
bandeja = []
for p in sorted(glob.glob('cuarentena/*/*.json')):
    q = p.replace(chr(92), '/')
    if '_insertados' in q or '_derivadas' in q:
        continue
    bandeja.append((q, json.load(io.open(p, encoding='utf-8'))))

print("POBLACION DEL BARRIDO (D.38.4)")
print("  grafo dataset/nodos.jsonl : %d" % len(nodos))
print("  bandejas cuarentena/*/    : %d" % len(bandeja))
print("  TOTAL                     : %d" % (len(nodos) + len(bandeja)))
print("  umbrales: sim %s | fam %s | paso %s"
      % (umbrales.get('umbral_similitud_texto'), umbrales.get('umbral_familia_id'),
         umbrales.get('umbral_paso_contra_nodo')))
print("")

objetivo = sys.argv[1].replace(chr(92), '/').rstrip('/')
aBarrer = [(r, c) for r, c in bandeja if r.startswith(objetivo + '/')]
print("candidatos a barrer en %s: %d (todos los de la carpeta, sin lista teclada)"
      % (objetivo, len(aBarrer)), flush=True)
print("")
poblacion = nodos + [n for _, n in bandeja]
for ruta, cand in aBarrer:
    otros = [n for n in poblacion if n is not cand]
    vecinos = aduana.buscar_vecinos(cand, otros, umbrales)
    print("### %s   (contra %d)" % (os.path.basename(ruta), len(otros)))
    if not vecinos:
        print("    SIN VECINOS: ninguna senial levanta nada")
    for v in vecinos:
        s = v["senales"]
        print("    vecino %s  [levantada por: %s]"
              % (v["id"], ", ".join(v["levantada_por"])))
        print("      similitud_texto %s | familia_id %s | paso_contra_nodo %s"
              % (s.get("similitud_texto"), s.get("familia_id"), s.get("paso_contra_nodo")))
        if v.get("detalle_paso"):
            print("      %s" % v["detalle_paso"])
    print("", flush=True)
