# -*- coding: utf-8 -*-
"""QUE ENTRO EN MIS COMMITS QUE NO ERA MIO.

La poblacion son los commits de esta vuelta cuyo asunto empieza por una marca mia, y la
pregunta es cual de sus ficheros cae FUERA de las sedes que EXTRACTOR.md 14 me da.

MIS SEDES: docs/loop/REPORTE.md, y lo que escribe la aduana por mi mano
(dataset/, bitacora/, censos/, cuarentena/), mas mi carpeta de instrumentos .v33/.
TODO LO DEMAS NO ES MIO en esta vuelta, y el encargo lo repite: src/, el banco, el arnes
y los protocolos estan bajo la moratoria de D.45 mientras el frente grove este vivo.
"""
import subprocess
import sys

MIAS = ("docs/loop/REPORTE.md", "dataset/", "bitacora/", "censos/", "cuarentena/", ".v33/")
MARCAS = ("V.33 ", "Apertura de la vuelta 33")

log = subprocess.check_output(
    ["git", "log", "--format=%h|%s", "ef3e7f9..HEAD"]).decode("utf-8", "replace")

filas = []
for linea in log.strip().split("\n"):
    corto, asunto = linea.split("|", 1)
    if not asunto.startswith(MARCAS):
        continue
    ficheros = subprocess.check_output(
        ["git", "show", "--pretty=", "--name-only", corto]).decode("utf-8", "replace")
    ajenos = [f for f in ficheros.strip().split("\n")
              if f and not f.startswith(MIAS)]
    filas.append((corto, asunto, ajenos))

print("| commit mio | ficheros que NO son de mis sedes |")
print("|---|---|")
total = 0
for corto, _asunto, ajenos in reversed(filas):
    total += len(ajenos)
    print("| `%s` | %s |"
          % (corto, ", ".join("`%s`" % f for f in ajenos) if ajenos else "**ninguno**"))
print("| **%d commits mios** | **%d ficheros ajenos arrastrados** |" % (len(filas), total))
