# -*- coding: utf-8 -*-
"""BARRIDO DE VECINOS DE LA APERTURA CIEGA (D.38.4 y D.38.5).

POBLACION: dataset/nodos.jsonl MAS todo lo que espera en cuarentena/<libro>/,
por el instrumento de la casa `aduana.poblacion_de_bandejas`, que descarta
`_insertados`, `_derivadas` y lo que no tenga fuente canonica. MENOS el propio
candidato (correccion de la ACTA 18: un nodo no es vecino de si mismo).

Este fichero no teclea ninguna cifra: todas salen de `aduana.buscar_vecinos`
con `config/umbrales.json` sin tocar.
"""
import io, json, os, sys
sys.path.insert(0, os.path.abspath("."))
from src import aduana, comun

FECHA = "2026-09-16"
TABLA = comun.leer_json(comun.RUTA_FUENTES)

grafo = [json.loads(l) for l in io.open("dataset/nodos.jsonl", encoding="utf-8") if l.strip()]
bandejas = aduana.poblacion_de_bandejas(fecha=FECHA, tabla_fuentes=TABLA)
poblacion = list(grafo) + list(bandejas)
vivos = set(d.get("id") for d in grafo)

print("poblacion del barrido : %d   (%d del grafo mas %d que esperan en bandejas)"
      % (len(poblacion), len(grafo), len(bandejas)))
print("umbrales              : %s" % json.dumps(
    {k: v for k, v in comun.leer_json("config/umbrales.json").items() if k.startswith("umbral_")},
    sort_keys=True))
print("")

for ruta in sys.argv[1:]:
    if ruta.endswith(".json"):
        bruto = comun.leer_json(ruta)
    else:  # un id que ya vive en el grafo
        bruto = next(d for d in grafo if d.get("id") == ruta)
    cand, _ = aduana.normalizar_candidato(bruto, FECHA)
    vecinos = aduana.buscar_vecinos(cand, poblacion)
    print("=" * 86)
    print("CANDIDATO : %s   (%d pasos)" % (cand.get("id"), len(cand.get("pasos_accionables") or [])))
    print("VECINOS QUE SUPERAN UMBRAL : %d   sobre una poblacion de %d"
          % (len(vecinos), len(poblacion) - 1))
    for v in vecinos:
        vid = v.get("id") or v.get("nodo")
        senales = ", ".join("%s=%s" % (k, s) for k, s in sorted(v["senales"].items())
                            if k in (v["levantada_por"] or []))
        print("   - %-52s %-8s [%s]" % (vid, "GRAFO" if vid in vivos else "BANDEJA", senales))
    if not vecinos:
        print("   (ninguno)")
print("=" * 86)
