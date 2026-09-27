# -*- coding: utf-8 -*-
"""BARRIDO DE VECINOS D.38.4: los 22 candidatos de la bandeja de grove contra
GRAFO MAS BANDEJAS, con las tres senales de la casa (src.aduana), sin escribir
ni una linea en ninguna sede."""
import json, os, sys, time
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
from src import aduana, comun, config as modulo_config

t0 = time.time()
umbrales = modulo_config.cargar()
grafo = comun.leer_jsonl(comun.RUTA_DATASET)
bandejas = aduana.poblacion_de_bandejas()
if isinstance(bandejas, dict):
    bandejas = list(bandejas.values())
poblacion = list(grafo) + list(bandejas)
print("poblacion del barrido (D.38.4)")
print("  dataset/nodos.jsonl        : %d" % len(grafo))
print("  cuarentena (todas)         : %d" % len(bandejas))
print("  POBLACION TOTAL            : %d" % len(poblacion))
print("  umbrales: similitud %s  familia_id %s  paso_contra_nodo %s"
      % (umbrales["umbral_similitud_texto"], umbrales["umbral_familia_id"],
         umbrales["umbral_paso_contra_nodo"]))
print()
BAND = os.path.join(RAIZ, "cuarentena", "grove_high_output")
nombres = sorted(n for n in os.listdir(BAND) if n.endswith(".json"))
total_vecinos = 0
for i, n in enumerate(nombres, 1):
    bruto = json.load(open(os.path.join(BAND, n), encoding="utf-8"))
    candidato, _ = aduana.normalizar_candidato(bruto, aduana._hoy())
    otros = [x for x in poblacion if x.get("id") != candidato.get("id")]
    vecinos = aduana.buscar_vecinos(candidato, otros, umbrales)
    total_vecinos += len(vecinos)
    print("%2d/%d  %-48s vecinos=%d   (%.0fs)"
          % (i, len(nombres), candidato.get("id"), len(vecinos), time.time() - t0))
    for v in vecinos:
        vid = v.get("id") if isinstance(v, dict) else getattr(v, "id", v)
        detalle = v.get("senales") if isinstance(v, dict) else None
        print("        -> %s   %s" % (vid, detalle))
    sys.stdout.flush()
print()
print("VECINOS LEVANTADOS EN TOTAL: %d sobre %d candidatos" % (total_vecinos, len(nombres)))
print("BARRIDO TERMINADO en %.0f s" % (time.time() - t0))
