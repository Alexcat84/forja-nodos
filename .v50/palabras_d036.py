# -*- coding: utf-8 -*-
"""d036: LAS OCHO CIFRAS DE FRONTERA, RECONTADAS POR MI ANTES DE ESCRIBIR NINGUNA CORRECCION.

El recuento es el mismo de .v46/frontera.py linea 136 (palabras separadas por espacios sobre
el rango de lineas que la ficha declara). La columna 'dice' se LEE de la propia ficha con una
expresion regular, no se teclea. La columna 'HH.2.c' se LEE de la tabla de frontera publicada
en docs/loop/REPORTE.md, no se teclea.

SI MI RECUENTO NO COINCIDIERA CON LA FRONTERA EN LAS OCHO, ESTO PARA Y SE TRAE
(encargo de la vuelta 50, TAREA 3.a: no se inventa una tercera cifra).
"""
import io
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

LIBRO = "fuentes/grove_high_output/cap_04.md"
REPORTE = "docs/loop/REPORTE.md"

FICHAS = [
    ("reunir_informacion_gerencial_vias_variadas", "P7"),
    ("escalonar_fuentes_informacion_gerencial", "P9"),
    ("programar_visita_area_observar_despachar", "P10"),
    ("transmitir_objetivos_prioridades_preferencias", "P11"),
    ("empujar_persona_reunion_direccion_preferida", "P13"),
    ("subir_productividad_gerencial_tres_vias", "P18"),
    ("buscar_actividad_alta_palanca_tres_vias", "P19"),
    ("elegir_momento_actividad_palanca_maxima", "P20"),
]

lineas = io.open(LIBRO, encoding="utf-8").read().split("\n")


def palabras(desde, hasta):
    return len(" ".join(lineas[desde - 1:hasta]).split())


# LA FRONTERA SE LEE DE SU TABLA PUBLICADA, fila a fila, y no se teclea.
frontera = {}
for l in io.open(REPORTE, encoding="utf-8"):
    m = re.match(r"\| `L(\d+) a L(\d+)` \| (\d+) \| \*\*\d\*\* \| (P\d+) ", l)
    if m:
        frontera[m.group(4)] = (int(m.group(1)), int(m.group(2)), int(m.group(3)))

print("ficha                                          pieza rango        dice  HH.2.c  cuento  veredicto")
filas = []
discrepan = 0
for fid, pieza in FICHAS:
    texto = io.open("cuarentena/grove_high_output/%s.json" % fid, encoding="utf-8").read()
    m = re.search(r"PIEZA %s de la frontera[^.]*?L(\d+) a L(\d+), (\d+) palabras" % pieza, texto)
    desde, hasta, dice = int(m.group(1)), int(m.group(2)), int(m.group(3))
    fdesde, fhasta, fdice = frontera[pieza]
    cuento = palabras(desde, hasta)
    bien = (cuento == fdice) and (desde, hasta) == (fdesde, fhasta)
    if cuento != dice:
        discrepan += 1
    filas.append((fid, pieza, desde, hasta, dice, fdice, cuento))
    print("%-46s %-5s L%d a L%-5d %4d  %4d    %4d    %s"
          % (fid, pieza, desde, hasta, dice, fdice, cuento,
             "la frontera manda" if bien else "PARADA: mi recuento no es el de la frontera"))

print("")
print("fichas leidas: %d ; mi recuento coincide con la frontera en %d ; cifras declaradas que discrepan: %d"
      % (len(filas), sum(1 for f in filas if f[6] == f[5]), discrepan))
