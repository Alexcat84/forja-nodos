# -*- coding: utf-8 -*-
"""Imprime los pasos de los candidatos de la tanda, en el orden del libro."""
import json
import sys

BANDEJA = "cuarentena/scott_radical_candor/%s.json"

for identificador in sys.argv[1:]:
    datos = json.load(open(BANDEJA % identificador, encoding="utf-8"))
    print("=== %s   (%d pasos)" % (identificador, len(datos["pasos_accionables"])))
    print("    titulo: %s" % datos["titulo"])
    for numero, paso in enumerate(datos["pasos_accionables"], 1):
        print("    P%-2d %s" % (numero, paso))
    print()
