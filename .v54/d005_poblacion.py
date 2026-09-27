# -*- coding: utf-8 -*-
"""LA POBLACION DE HOY CONTRA LA QUE MIDIO LOS 15 INFORMES DE cap_03.

Usa la funcion de la casa (src.aduana.poblacion_de_bandejas) y no una cuenta
de ficheros propia. Imprime la diferencia con sus dos extremos nombrados.
"""
import os
import sys

sys.path.insert(0, os.path.abspath("."))
from src import aduana  # noqa: E402

bandejas = aduana.poblacion_de_bandejas()
if isinstance(bandejas, list):
    bandejas = len(bandejas)
bandejas = int(bandejas)

grafo = sum(1 for l in open("dataset/nodos.jsonl", encoding="utf-8") if l.strip())
hoy = grafo + bandejas

print("LA POBLACION DEL BARRIDO, HOY Y ENTONCES")
print("  grafo de hoy                              : %d  (lineas de dataset/nodos.jsonl)" % grafo)
print("  bandejas de hoy                           : %d  (src.aduana.poblacion_de_bandejas)" % bandejas)
print("  poblacion del barrido de hoy              : %d  (suma de los dos de arriba)" % hoy)
print()
print("  poblacion de los 15 informes de .v2g/     : 358 a 371  (leida de sus propias cabeceras)")
print("  documentos NUEVOS desde entonces          : %d contra el mayor, %d contra el menor"
      % (hoy - 371, hoy - 358))
print("    numerador   %d  documentos de la poblacion de hoy" % hoy)
print("    denominador %d  documentos de la poblacion mayor de aquellos informes" % 371)
