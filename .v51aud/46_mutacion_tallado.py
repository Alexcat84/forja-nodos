# -*- coding: utf-8 -*-
"""LA GUARDA QUE EL REPORTE DECLARA MORDIENDO (MM.4.k), VUELTA A MORDER POR
MUTACION. Se cambia UNA celda de la tabla D.52 de MM.4.j en una COPIA del
reporte fuera del arbol vivo, y el tallado tiene que CAER sobre esa copia."""
import io, os, sys, tempfile
sys.path.insert(0, "scripts")
import tallar_reporte as T

texto = io.open(T.RUTA_REPORTE, encoding="utf-8").read()

# La celda que muto: el `CERRADA ENTERA en MM.2` de la fila 2 de la tabla D.52.
AGUJA = "**CERRADA ENTERA en `MM.2`**: `6` de `6` escritos y pasados"
assert texto.count(AGUJA) == 1, "la aguja tiene que ser unica: %d" % texto.count(AGUJA)
mutado = texto.replace(AGUJA, "**CERRADA ENTERA en `MM.2`**: `7` de `7` escritos y pasados")

tmp = tempfile.mkdtemp(prefix="tallado_mutado_")
os.makedirs(os.path.join(tmp, "docs", "loop"))
destino = os.path.join(tmp, "docs", "loop", "REPORTE.md")

for etiqueta, contenido in (("SIN MUTAR", texto), ("CON UNA CELDA MUTADA", mutado)):
    io.open(destino, "w", encoding="utf-8").write(contenido)
    dictamenes = T.revisar(ruta_reporte=destino, raiz=T.RAIZ)
    difieren = [d for d in dictamenes if d.get("estado") == "DIFIERE"]
    print("%-22s tablas comprobadas %3d   DIFIEREN %d"
          % (etiqueta, len(dictamenes), len(difieren)))
    for d in difieren:
        print("      DIFIERE en la linea %s" % d["tabla"].get("linea"))
os.remove(destino)
