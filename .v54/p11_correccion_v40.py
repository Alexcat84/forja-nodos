# -*- coding: utf-8 -*-
"""LO QUE LA VUELTA 40 ESCRIBIO POR ANEXION SOBRE LOS DOS U+0008."""
import json

RUTA = "dataset/nodos.jsonl"
ID = "pedir_critica_primero_crear_seguridad_psicologica"
CONTROL = chr(8)

for cruda in open(RUTA, encoding="utf-8"):
    if not cruda.strip():
        continue
    o = json.loads(cruda)
    if o.get("id") != ID:
        continue
    t = o["resumen_teorico"]
    donde = t.find("U+0008")
    print("la mencion de U+0008 empieza en la posicion %d del campo" % donde)
    print("y los dos caracteres vivos estan en 5162 y 5166:")
    print("  la correccion va %d caracteres DESPUES del defecto que describe"
          % (donde - 5162))
    print()
    print("EL TEXTO DE LA CORRECCION, IMPRESO ENTERO:")
    print("    " + t[donde - 700:donde + 700].replace(CONTROL, "<U+0008>")
          .replace("\n", "\n    "))
