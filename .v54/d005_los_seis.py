# -*- coding: utf-8 -*-
"""d005 RELEIDA: los 6 de cap_03 que la aduana en seco bloquearia, NOMBRADOS.

Lee los 15 informes por candidato que el frente grove dejo en .v2g/ y saca de
cada uno su veredicto y sus vecinos. No teclea ningun nombre: los imprime.
"""
import glob
import os
import re

INFORMES = sorted(glob.glob(".v2g/informe_*.txt"))
SALTAR = ("informe_lote_grove.txt", "informe_01.txt", "informe_02.txt")

bloquean, entran, caen = [], [], []
for ruta in INFORMES:
    if os.path.basename(ruta) in SALTAR:
        continue
    texto = open(ruta, encoding="utf-8", errors="replace").read()
    nombre = os.path.basename(ruta)[len("informe_"):-len(".txt")]
    poblacion = re.search(r"poblacion del barrido\s*:\s*(\d+)", texto)
    vecinos = re.findall(r"vecino (\S+)\s+\[levantada por: ([^\]]+)\]", texto)
    if "[BLOQUEARIA]" in texto:
        bloquean.append((nombre, poblacion.group(1) if poblacion else "?", vecinos))
    elif "[CAERIA]" in texto:
        caen.append((nombre, poblacion.group(1) if poblacion else "?", vecinos))
    else:
        entran.append((nombre, poblacion.group(1) if poblacion else "?", vecinos))

print("d005 RELEIDA: los informes por candidato de cap_03 de grove, en .v2g/")
print("  informes por candidato leidos : %d" % (len(bloquean) + len(entran) + len(caen)))
print("  BLOQUEARIAN                   : %d" % len(bloquean))
print("  ENTRARIAN                     : %d" % len(entran))
print("  CAERIAN                       : %d" % len(caen))
print()
print("LOS QUE BLOQUEAN, NOMBRADOS UNO A UNO, CON SU POBLACION Y SUS VECINOS")
for nombre, poblacion, vecinos in bloquean:
    print("  [BLOQUEARIA] %s   (poblacion del barrido: %s)" % (nombre, poblacion))
    for vecino, senal in vecinos:
        print("       vecino %s  [%s]" % (vecino, senal))
print()
print("LOS QUE ENTRAN, NOMBRADOS IGUAL")
for nombre, poblacion, _ in entran:
    print("  [ENTRARIA]   %s   (poblacion del barrido: %s)" % (nombre, poblacion))
