# -*- coding: utf-8 -*-
"""Imprime los pasos de los dos nodos del par que la aduana levanto en 62.4."""
import json
for f in ("detectar_arreglar_fallo_etapa_menor_valor",
          "supervisar_tarea_delegada_etapa_menor_valor"):
    d = json.load(open("cuarentena/grove_high_output/%s.json" % f, encoding="utf-8"))
    print("=" * 78)
    print(f, "|", d["titulo"])
    print("dominio            :", d["dominio"])
    print("activacion         :", d["condiciones_activacion"])
    print("entregable         :", d["entregable_esperado"])
    for n, p in enumerate(d["pasos_accionables"], 1):
        print("  paso %d: %s" % (n, p))
    print("origen             :", d["resumen_teorico"].split(".")[0])
