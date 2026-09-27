# -*- coding: utf-8 -*-
"""LAS ARISTAS QUE LAS CINCO FICHAS DE HOY DECLARAN POR LECTURA, SACADAS DE SUS FICHAS.

El encargo 2.c manda que las aristas declaradas por lectura vivan DENTRO de la ficha,
que es donde sobreviven al reporte, y que se cablen el dia que el lote cierre. Ninguna
se puede cablear hoy con `forja.py arista`, porque esa orden escribe en el grafo y
estos cinco nodos siguen en cuarentena (la puerta de D.39 mide cerrada, JJ.0).

Esto no las cablea: las LISTA, para que la tabla del reporte salga de las fichas y no
de mi memoria. Cada una se cuenta con su clase (D.37 cabeza, D.29 madre, hermano o
pariente) y con el id o el tramo al que apunta.
"""
import io
import json
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

TANDA = [
    ("P34a", "usar_calendario_herramienta_planificacion_produccion"),
    ("P34b", "decir_no_trabajo_excede_capacidad"),
    ("P36", "llevar_inventario_proyectos_discrecionales"),
    ("P38", "dimensionar_numero_subordinados_medio_dia_semanal"),
    ("P39", "buscar_regularidad_bloques_iguales_trabajo_mando"),
]

# (N) D.NN, CLASE destino, ...   hasta el punto que cierra la frase
LINEA = re.compile(r"\((\d)\) (D\.\d\d), ([A-Z ]+?) ([a-z0-9_]+),")

print("| # | ficha de hoy | clase | a quien apunta |")
print("|---:|---|---|---|")
n = 0
por_clase = {}
for tramo, ident in TANDA:
    d = json.load(io.open("cuarentena/grove_high_output/%s.json" % ident, encoding="utf-8"))
    for m in LINEA.finditer(d["resumen_teorico"]):
        n += 1
        clase = "%s %s" % (m.group(2), m.group(3).strip())
        por_clase[clase] = por_clase.get(clase, 0) + 1
        print("| %d | `%s` (`%s`) | `%s` | `%s` |" % (n, ident, tramo, clase, m.group(4)))
print("| | | **%d aristas** | |" % n)
print("")
for k in sorted(por_clase):
    print("   %-28s %d" % (k, por_clase[k]))
print("")
print("NINGUNA SE CABLEA HOY: forja.py arista escribe en el grafo y los cinco nodos")
print("siguen en cuarentena. Viven dentro de su ficha y se cablean el dia del lote.")
