# -*- coding: utf-8 -*-
"""Barrido de vecinos por SENIAL familia_id sobre GRAFO MAS BANDEJAS (D.38.4).
Instrumento de la casa: src.aduana.senal_familia_id / src.reglas_id.similitud_familia.
Cero escrituras fuera de su propia salida."""
import io, json, glob, os, sys
sys.path.insert(0, os.path.abspath('.'))
from src import aduana, comun, config as modulo_config

comun.salida_utf8()
umbrales = modulo_config.cargar()
U = umbrales["umbral_familia_id"]

nodos = [json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
bandeja = []
for p in sorted(glob.glob('cuarentena/*/*.json')):
    q = p.replace(chr(92), '/')
    if '_insertados' in q or '_derivadas' in q:
        continue
    bandeja.append((q, json.load(io.open(p, encoding='utf-8'))))

print("POBLACION DEL BARRIDO (D.38.4): grafo %d + bandejas %d = %d"
      % (len(nodos), len(bandeja), len(nodos) + len(bandeja)))
print("senial barrida: familia_id | umbral %s" % U)
print("")

SOLO = set(l.strip() for l in io.open('.lote16.txt', encoding='utf-8') if l.strip())
poblacion = [("GRAFO", n) for n in nodos] + [("BANDEJA", n) for _, n in bandeja]
for ruta, cand in bandeja:
    if os.path.basename(ruta)[:-5] not in SOLO:
        continue
    vec = []
    for origen, otro in poblacion:
        if otro is cand:
            continue
        v = aduana.senal_familia_id(cand.get("id") or "", otro.get("id") or "")
        if isinstance(v, aduana.NoAplica):
            continue
        if v >= U:
            vec.append((v, origen, otro.get("id")))
    vec.sort(reverse=True)
    print("### %s   (contra %d)" % (cand.get("id"), len(poblacion) - 1))
    if not vec:
        print("    SIN VECINOS por familia_id")
    for v, o, i in vec:
        print("    familia_id %.3f  [%s] %s" % (v, o, i))
    print("")
