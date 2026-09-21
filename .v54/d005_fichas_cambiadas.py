# -*- coding: utf-8 -*-
"""MI PROPIA AFIRMACION, MORDIDA: el 6 solo es SUELO si las fichas no cambiaron.

Un candidato pierde vecinos si SU PROPIO texto cambia (es lo que d056 midio:
11 de 34 pares dejaron de levantar). Asi que compruebo, ficha a ficha, si las
15 de cap_03 se han tocado desde que sus informes corrieron.
"""
import glob
import os
import subprocess

INFORMES = sorted(glob.glob(".v2g/informe_*.txt"))
SALTAR = ("informe_lote_grove.txt", "informe_01.txt", "informe_02.txt")

# El commit en que el frente grove dejo sus informes: el de la ficha mas vieja.
CORTE = subprocess.check_output(
    ["git", "log", "-1", "--format=%h %ad", "--date=short", "--", ".v2g/"],
    text=True).strip()
print("ultimo commit que toco .v2g/ : %s" % CORTE)
print()

tocadas, intactas = [], []
for ruta in INFORMES:
    if os.path.basename(ruta) in SALTAR:
        continue
    nombre = os.path.basename(ruta)[len("informe_"):-len(".txt")]
    ficha = "cuarentena/grove_high_output/%s.json" % nombre
    if not os.path.exists(ficha):
        tocadas.append((nombre, "LA FICHA NO ESTA EN ESA RUTA"))
        continue
    salida = subprocess.check_output(
        ["git", "log", "--format=%h %ad %s", "--date=short", "-3", "--", ficha],
        text=True).strip().splitlines()
    ultimo = salida[0] if salida else "(sin commits)"
    (tocadas if len(salida) > 1 else intactas).append((nombre, ultimo))

print("LAS 15 FICHAS DE cap_03, CON SU ULTIMO COMMIT")
print("  con MAS de un commit (o sea, tocadas despues de nacer) : %d" % len(tocadas))
print("  con UN solo commit (nacieron y no se tocaron)          : %d" % len(intactas))
print("    numerador   %d  fichas con mas de un commit" % len(tocadas))
print("    denominador %d  fichas de cap_03 con informe en .v2g/" % (len(tocadas) + len(intactas)))
print()
for nombre, ultimo in tocadas:
    print("  TOCADA   %-50s %s" % (nombre, ultimo))
for nombre, ultimo in intactas:
    print("  INTACTA  %-50s %s" % (nombre, ultimo))
