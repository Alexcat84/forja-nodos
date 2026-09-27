# -*- coding: utf-8 -*-
"""II.2.f del reporte dice que el pariente que la ficha NO escribio es 'el mas proximo'.
Lo mido con el instrumento de la casa (src/aduana.medir), no a ojo, y publico la LISTA
ORDENADA ENTERA de los dos candidatos a pariente."""
import json, glob, io, sys, os
sys.path.insert(0, ".")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from src import aduana

def carga(ident):
    for p in (["cuarentena/grove_high_output/%s.json" % ident] +
              glob.glob("cuarentena/*/%s.json" % ident)):
        if os.path.exists(p): return json.load(open(p, encoding="utf-8"))
    for l in open("dataset/nodos.jsonl", encoding="utf-8"):
        d = json.loads(l)
        if d["id"] == ident: return d
    return None

CAND = "supervisar_tarea_delegada_etapa_menor_valor"
c = carga(CAND)
print("candidato:", CAND)
filas = []
for otro in ("detectar_arreglar_fallo_etapa_menor_valor",  # el que la senial levanto
             "elegir_inspeccion_barrera_monitorizacion"):   # el que la ficha escribio
    v = carga(otro)
    if v is None:
        print("   %-44s NO EXISTE en ninguna sede" % otro); continue
    m = aduana.medir(c, v)
    filas.append((otro, m))
print()
print("LISTA ORDENADA ENTERA, por similitud_texto:")
for otro, m in sorted(filas, key=lambda f: -float(f[1]["senales"]["similitud_texto"])):
    print("   %-44s similitud_texto %.4f | familia_id %.4f | paso_contra_nodo %.4f"
          % (otro, float(m["senales"]["similitud_texto"]), float(m["senales"]["familia_id"]),
             float(m["senales"]["paso_contra_nodo"])))
