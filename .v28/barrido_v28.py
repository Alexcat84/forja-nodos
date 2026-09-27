# -*- coding: utf-8 -*-
"""BARRIDO DE VECINOS DE LA APERTURA CIEGA DE LA VUELTA 28 (D.38.4).

POBLACION: el grafo mas las bandejas TAL COMO ESTABAN AL ABRIR LA VUELTA 27
(`360f941`), que es lo que el extractor tuvo delante, MENOS el propio candidato
(correccion de la ACTA 18: un nodo no es vecino de si mismo).

Instrumento de la casa: `src.aduana.buscar_vecinos`, con `config/umbrales.json`
sin tocar. Este fichero no teclea ninguna cifra.
"""
import io, json, os, sys
sys.path.insert(0, os.path.abspath("."))
from src import aduana, comun

FECHA = "2026-09-16"
TABLA = comun.leer_json(comun.RUTA_FUENTES)

grafo = [json.loads(l) for l in io.open(".v28/grafo_pre27.jsonl", encoding="utf-8") if l.strip()]
bandejas = aduana.poblacion_de_bandejas(raiz=".v28/pre27", fecha=FECHA, tabla_fuentes=TABLA)
poblacion = list(grafo) + list(bandejas)

print("poblacion del barrido       : %d   (%d del grafo mas %d que esperan en bandejas)"
      % (len(poblacion), len(grafo), len(bandejas)))
print("fuente del grafo            : git show 360f941:dataset/nodos.jsonl")
print("fuente de las bandejas      : git archive 360f941 cuarentena (sin _insertados ni _derivadas)")
print("")

CANDIDATOS = sys.argv[1:]
for ruta in CANDIDATOS:
    bruto = comun.leer_json(ruta)
    cand, _ = aduana.normalizar_candidato(bruto, FECHA)
    vecinos = aduana.buscar_vecinos(cand, poblacion)
    print("=" * 78)
    print("CANDIDATO : %s" % cand.get("id"))
    print("pasos     : %d" % len(cand.get("pasos_accionables") or []))
    print("barrido contra %d (la poblacion menos el propio candidato)" % (len(poblacion) - 1))
    print("VECINOS QUE SUPERAN UMBRAL : %d" % len(vecinos))
    for v in vecinos:
        senales = ", ".join("%s=%s" % (k, s) for k, s in sorted(v["senales"].items())
                            if k in (v["levantada_por"] or []))
        print("   - %-55s  [%s]" % (v.get("id") or v.get("nodo"), senales))
    if not vecinos:
        print("   (ninguno)")
print("=" * 78)
