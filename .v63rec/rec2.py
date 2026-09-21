# -*- coding: utf-8 -*-
"""Que candidato de la bandeja de grove tiene ya un veredicto de aduana corrido.

NO cuenta que su nombre aparezca en un fichero. Cuenta UNA SOLA COSA:
que exista la linea que forja.py informe imprime en LA LISTA COMPLETA,

    [BLOQUEARIA] <id>   (<id>.json)

que es la unica sede donde la aduana se pronuncia sobre un candidato.
Se anota ademas la POBLACION del barrido que lo produjo, porque un informe
corrido contra 414 no es el mismo que uno corrido contra 440.
"""
import glob, io, os, re

os.chdir("C:/Users/AlexDesk/Documents/forja-nodos")

ids = sorted(os.path.basename(p)[:-5]
             for p in glob.glob("cuarentena/grove_high_output/*.json"))

VEREDICTO = re.compile(r"^\[(BLOQUEARIA|ENTRARIA|CAERIA)\]\s+(\S+)", re.M)
POBLACION = re.compile(r"poblacion del barrido\s*:\s*(\d+)")

tiene = {}
for p in glob.glob(".v*/**/*", recursive=True):
    if not os.path.isfile(p) or os.path.getsize(p) > 4_000_000:
        continue
    try:
        txt = io.open(p, encoding="utf-8", errors="replace").read()
    except Exception:
        continue
    fallos = VEREDICTO.findall(txt)
    if not fallos:
        continue
    pobs = POBLACION.findall(txt)
    pob = max(int(x) for x in pobs) if pobs else 0
    for veredicto, cid in fallos:
        if cid in ids:
            # se queda el de POBLACION mayor, que es el mas reciente y el mas ancho
            if cid not in tiene or pob > tiene[cid][1]:
                tiene[cid] = (veredicto, pob, p.replace("\\", "/"))

faltan = [i for i in ids if i not in tiene]

print("BANDEJA DE grove_high_output : %d candidatos" % len(ids))
print("CON VEREDICTO DE ADUANA YA CORRIDO : %d" % len(tiene))
print("SIN VEREDICTO, HAY QUE CORRERLOS   : %d" % len(faltan))
print()
from collections import Counter
print("por poblacion del barrido que lo produjo:")
for pob, n in sorted(Counter(v[1] for v in tiene.values()).items()):
    print("   poblacion %3d : %2d candidato(s)" % (pob, n))
print()
print("por veredicto:")
for v, n in sorted(Counter(v[0] for v in tiene.values()).items()):
    print("   %-12s : %2d" % (v, n))

lineas = []
lineas.append("LOS %d QUE YA TIENEN VEREDICTO DE ADUANA CORRIDO" % len(tiene))
lineas.append("%-58s %-12s %5s  %s" % ("candidato", "veredicto", "pobl", "fichero"))
for i in sorted(tiene):
    v, pob, p = tiene[i]
    lineas.append("%-58s %-12s %5d  %s" % (i, v, pob, p))
lineas.append("")
lineas.append("LOS %d QUE FALTAN POR CORRER" % len(faltan))
for i in faltan:
    lineas.append("  %s" % i)
io.open(".v63rec/veredictos_de_aduana.txt", "w", encoding="utf-8",
        newline=chr(10)).write(chr(10).join(lineas) + chr(10))
io.open(".v63rec/faltan_informe.txt", "w", encoding="utf-8",
        newline=chr(10)).write(chr(10).join(faltan) + chr(10))
print()
print("LOS QUE FALTAN:")
for i in faltan:
    print("  %s" % i)
