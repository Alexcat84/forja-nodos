# -*- coding: utf-8 -*-
"""HASTA DONDE LLEGA EL DEFECTO: se cuela el U+0008 en lo que la senial compara?

Usa la MISMA funcion de la aduana (src.comun.texto_comparable) sobre el nodo
del ejemplar, y cuenta los controles antes y despues de normalizar.
"""
import json
import os
import sys

sys.path.insert(0, os.path.abspath("."))
from src import comun  # noqa: E402

RUTA = "dataset/nodos.jsonl"
ID = "pedir_critica_primero_crear_seguridad_psicologica"
CONTROL = chr(8)

for cruda in open(RUTA, encoding="utf-8"):
    if not cruda.strip():
        continue
    o = json.loads(cruda)
    if o.get("id") != ID:
        continue
    crudo = " ".join([o.get("titulo") or "", o.get("resumen_teorico") or ""]
                     + list(o.get("pasos_accionables") or []))
    comparable = comun.texto_comparable(o)
    print("EL EJEMPLAR: %s" % ID)
    print("  U+0008 en el texto CRUDO (titulo+resumen+pasos) : %d"
          % crudo.count(CONTROL))
    print("  U+0008 en texto_comparable, la del aduana        : %d"
          % comparable.count(CONTROL))
    print("  largo crudo %d, largo comparable %d" % (len(crudo), len(comparable)))
    print()
    print("  Y LA HUELLA DE D.15, que es la que dice si una lectura sigue viva:")
    print("    huella_de_nodo : %s" % comun.huella_de_nodo(o))
    limpio = json.loads(json.dumps(o).replace("\u0008", ""))
    print("    la misma huella SIN los dos controles : %s"
          % comun.huella_de_nodo(limpio))
    print("    cambia la huella al quitarlos? %s"
          % ("SI" if comun.huella_de_nodo(o) != comun.huella_de_nodo(limpio)
             else "NO"))
