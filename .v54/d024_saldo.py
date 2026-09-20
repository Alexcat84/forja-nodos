# -*- coding: utf-8 -*-
"""d024 PAGADA: el saldo de los 7 de cap_02, leido de sus 7 informes de hoy.

No teclea ni un veredicto: los saca de los ficheros que forja.py informe
escribio en .v54/. Toda cifra derivada lleva numerador y denominador
NOMBRADOS (D.59).
"""
import glob
import os
import re

RELOJ = ".v54/d024_reloj.txt"
segundos = {}
for linea in open(RELOJ, encoding="utf-8"):
    trozo = linea.split()
    if len(trozo) == 2 and trozo[1].isdigit():
        segundos[trozo[0]] = int(trozo[1])

filas = []
for ruta in sorted(glob.glob(".v54/d024_*.txt")):
    # EXCLUYO MIS PROPIAS SALIDAS: el glob d024_*.txt se incluia a si mismo
    # (d024_saldo.txt y d024_reloj.txt), que es la especie de d038.
    if os.path.basename(ruta) in ("d024_reloj.txt", "d024_saldo.txt"):
        continue
    texto = open(ruta, encoding="utf-8", errors="replace").read()
    nombre = os.path.basename(ruta)[len("d024_"):-len(".txt")]
    poblacion = re.search(r"poblacion del barrido\s*:\s*(\d+)", texto)
    veredicto = re.search(r"^\[(ENTRARIA|BLOQUEARIA|CAERIA)\]", texto, re.M)
    vecinos = re.findall(r"vecino (\S+)\s+\[levantada por: ([^\]]+)\]", texto)
    filas.append((nombre, veredicto.group(1) if veredicto else "?",
                  poblacion.group(1) if poblacion else "?", vecinos,
                  segundos.get(nombre, 0)))

bloquean = [f for f in filas if f[1] == "BLOQUEARIA"]
entran = [f for f in filas if f[1] == "ENTRARIA"]
caen = [f for f in filas if f[1] == "CAERIA"]

print("d024: LOS 7 DE cap_02 DE grove, CON SU INFORME POR CANDIDATO, CORRIDO HOY")
print("  informes corridos hoy, uno por candidato : %d" % len(filas))
print("  poblacion del barrido de cada uno        : %s"
      % ", ".join(sorted(set(f[2] for f in filas))))
print()
print("  ENTRARIAN   : %d" % len(entran))
print("  BLOQUEARIAN : %d" % len(bloquean))
print("  CAERIAN     : %d" % len(caen))
print("    numerador   %d  candidatos que BLOQUEARIAN" % len(bloquean))
print("    denominador %d  candidatos de cap_02 con informe corrido hoy" % len(filas))
print()
total = sum(f[4] for f in filas)
print("  RELOJ: %d s en total sobre %d pasadas" % (total, len(filas)))
print("    segundos por pasada : %.1f s" % (total / float(len(filas))))
print("      numerador   %d  suma de segundos de las pasadas de hoy" % total)
print("      denominador %d  pasadas lanzadas hoy" % len(filas))
print()
print("LA LISTA, CANDIDATO POR CANDIDATO, CON SU VECINDAD")
for nombre, veredicto, poblacion, vecinos, seg in filas:
    print("  [%s] %s   (poblacion %s, reloj %d s)" % (veredicto, nombre, poblacion, seg))
    for vecino, senal in vecinos:
        print("       vecino %s  [%s]" % (vecino, senal))
    if not vecinos:
        print("       (cero vecinos levantados)")
