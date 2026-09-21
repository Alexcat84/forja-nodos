# -*- coding: utf-8 -*-
"""VERIFICACION PROPIA DEL AUDITOR (ACTA 56): la frontera de cap_11, cap_12 y cap_13.

Leo las filas de la tabla QUE EL REPORTE PUBLICA, recompongo cada cifra contra el
fichero fuente con mis propios comandos, y comparo. No importo nada de .v57ext/.
"""
import io
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

REPORTE = "docs/loop/REPORTE.md"
lineas_rep = io.open(REPORTE, encoding="utf-8").read().split("\n")
# la vuelta 57 empieza en la cabecera de nivel 1 que la nombra
ini = max(i for i, l in enumerate(lineas_rep) if l.startswith("# VUELTA 57,"))
bloque = lineas_rep[ini:]

FILA = re.compile(r"^\| `L(\d+) a L(\d+)` \| (\d+) \| \*\*(\d+)\*\* \|")

tablas = {}
unidad = None
for l in bloque:
    m = re.search(r"LA TABLA DE (cap_\d+), IMPRESA", l)
    if m:
        unidad = m.group(1)
        tablas[unidad] = []
        continue
    if unidad:
        f = FILA.match(l)
        if f:
            tablas[unidad].append((int(f.group(1)), int(f.group(2)),
                                   int(f.group(3)), int(f.group(4))))

TOTAL = re.compile(r"^\| \| \*\*(\d+)\*\* \| \*\*(\d+)\*\* \| \*\*el cuerpo entero de (cap_\d+)")
totales = {}
for l in bloque:
    t = TOTAL.match(l)
    if t:
        totales[t.group(3)] = (int(t.group(1)), int(t.group(2)))

print("=" * 78)
print("VERIFICACION PROPIA DE LA FRONTERA, FILA A FILA CONTRA EL FICHERO")
print("=" * 78)

gran_total_nodos = 0
for unidad in ("cap_11", "cap_12", "cap_13"):
    ruta = "fuentes/grove_high_output/%s.md" % unidad
    lineas = io.open(ruta, encoding="utf-8").read().split("\n")

    # la cabecera acaba en el SEGUNDO guion triple, localizado y no tecleado
    guiones = [i for i, l in enumerate(lineas) if l.strip() == "---"]
    fin_cabecera = guiones[1] + 1

    def palabras(desde, hasta):
        return len(" ".join(lineas[desde - 1:hasta]).split())

    cuerpo = len(" ".join(lineas[fin_cabecera:]).split())
    caracteres = len("\n".join(lineas[fin_cabecera:]))
    fichero = len(" ".join(lineas).split())
    con_contenido = [i + 1 for i, l in enumerate(lineas)
                     if i >= fin_cabecera and l.strip()]

    filas = tablas[unidad]
    cubiertas = []
    for d, h, _p, _n in filas:
        cubiertas.extend(range(d, h + 1))
    sin_cubrir = [n for n in con_contenido if n not in cubiertas]
    solapes = sorted(set(n for n in cubiertas if cubiertas.count(n) > 1))

    suma = sum(palabras(d, h) for d, h, _p, _n in filas)
    nodos = sum(n for _d, _h, _p, n in filas)

    discrepan = [(d, h, p, palabras(d, h)) for d, h, p, _n in filas
                 if p != palabras(d, h)]

    print("")
    print("--- %s" % unidad)
    print("  cabecera acaba en la linea            : %d" % (guiones[1] + 1))
    print("  filas de la tabla del reporte         : %d" % len(filas))
    print("  lineas con contenido tras la cabecera : %d" % len(con_contenido))
    print("  lineas NO cubiertas                   : %d  %s" % (len(sin_cubrir), sin_cubrir))
    print("  SOLAPES                               : %d  %s" % (len(solapes), solapes))
    print("  suma de las filas (contada por mi)    : %d palabras" % suma)
    print("  cuerpo medido aparte                  : %d palabras" % cuerpo)
    print("  CARACTERES DE CUERPO                  : %d" % caracteres)
    print("  fichero entero                        : %d palabras" % fichero)
    print("  IGUALES                               : %s" % (suma == cuerpo))
    print("  nodos que la tabla declara            : %d" % nodos)
    print("  FILAS CUYA CIFRA DE PALABRAS NO ME SALE: %d  %s"
          % (len(discrepan), discrepan))
    tot = totales.get(unidad)
    print("  fila TOTAL del reporte                : %s   (mia: %d, %d)"
          % (str(tot), suma, nodos))
    gran_total_nodos += nodos

print("")
print("NODOS DE LAS TRES UNIDADES, CONTADOS POR MI: %d" % gran_total_nodos)
