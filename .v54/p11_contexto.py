# -*- coding: utf-8 -*-
"""EL CONTEXTO DE LOS DOS U+0008, IMPRESO Y NO PARAFRASEADO."""
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
    print("nodo            : %s" % ID)
    print("campo           : resumen_teorico, %d caracteres" % len(t))
    print("posiciones      : 5162 y 5166")
    print()
    print("LOS CARACTERES ALREDEDOR, con el U+0008 escrito como <U+0008>:")
    tramo = t[5040:5300].replace(CONTROL, "<U+0008>")
    print("    " + tramo.replace("\n", "\n    "))
    print()
    print("QUE HAY DENTRO DEL PROPIO CAMPO SOBRE ESTO:")
    for clave in ("CORRECCION DECLARADA", "U+0008", "caracter de control",
                  "vuelta 40", "control"):
        print("    '%s' aparece %d vez/veces" % (clave, t.count(clave)))
