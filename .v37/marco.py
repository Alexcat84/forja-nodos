# -*- coding: utf-8 -*-
"""Los dos sitios donde el libro dice cosas distintas sobre las casillas del marco."""
import io
import json

for linea in io.open("dataset/nodos.jsonl", encoding="utf-8"):
    d = json.loads(linea)
    if d["id"] == "desplegar_marco_franqueza_radical":
        print("desplegar_marco_franqueza_radical P8: %s" % d["pasos_accionables"][7])
        print("desplegar_marco_franqueza_radical entregable: ... %s"
              % d["entregable_esperado"].split(", y")[-1].strip())
