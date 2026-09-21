# -*- coding: utf-8 -*-
"""LA COLISION DE D.52 CON D.41, RESUELTA COMO LA RESOLVIERON LAS VUELTAS 46, 47, 48 Y 49 (d030).

scripts/tabla_de_cierre.py --escribir escribe SIEMPRE en docs/loop/TABLA_DE_CIERRE.txt, y el
tallado de D.41 compara TODA tabla del reporte contra el fichero que esa tabla nombra. Dos
vueltas no pueden estar verdes a la vez: la que escribe deja en rojo a la anterior.

SE REPARA SIN TECLEAR NI BORRAR: la salida de la vuelta 49 se saca de git BYTE A BYTE y se
archiva; la linea de su reporte que nombraba la ruta viva pasa a nombrar la archivada, con la
correccion declarada al lado; y la ruta viva se queda con la tabla de la vuelta que cierra hoy.

ES EL SEXTO EJEMPLAR SEGUIDO (42, 46, 47, 48, 49 y hoy la 50), y por eso es deuda de maquinaria
y no descuido: d030 la tiene abierta y D.45 con la moratoria de EXTRACTOR.md 13 me dejan fuera
de arreglar el script.
"""
import io

R = "docs/loop/REPORTE.md"
t = io.open(R, encoding="utf-8").read()

VIEJO = (u"### KK.5.c. **LA TABLA DE CIERRE DE TAREAS** (`D.52`)\n"
         u"\n"
         u"*Salida de `python scripts/tabla_de_cierre.py --escribir`, pegada de\n"
         u"`docs/loop/TABLA_DE_CIERRE.txt`.*\n")

NUEVO = (u"### KK.5.c. **LA TABLA DE CIERRE DE TAREAS** (`D.52`)\n"
         u"\n"
         u"*Salida de `python scripts/tabla_de_cierre.py --escribir`, pegada de\n"
         u"`docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_v49.txt`.*\n"
         u"\n"
         u"> **CORRECCION DECLARADA de la vuelta 50, y no toca ni una celda de esta tabla.**\n"
         u"> Esta linea decia `docs/loop/TABLA_DE_CIERRE.txt`, que es la ruta VIVA del\n"
         u"> instrumento, **y es la misma colision que esta misma seccion declaro contra la\n"
         u"> vuelta 48**: la vuelta siguiente que cierre su tabla deja a esta en rojo sin que\n"
         u"> nadie toque el reporte. **La vuelta 50 le hace a la 49 exactamente lo que la 49 le\n"
         u"> hizo a la 48, la 48 a la 47, la 47 a la 46 y la 46 a la 42.**\n"
         u">\n"
         u"> **LA SALIDA DE LA VUELTA 49 NO SE TECLEO NI SE PERDIO: SE SACO DE GIT BYTE A BYTE**\n"
         u"> (`git show HEAD:docs/loop/TABLA_DE_CIERRE.txt`), **con el mismo `git hash-object`\n"
         u"> en los dos lados**, que es lo que prueba que la copia es la salida y no una\n"
         u"> transcripcion. **El sello esta pegado en `LL.5.c`.**\n")

if VIEJO not in t:
    raise SystemExit("PARADA: la cabecera de KK.5.c no esta tal cual en el reporte")
if NUEVO in t:
    raise SystemExit("YA ESTABA ARCHIVADA: no la toco")

io.open(R, "w", encoding="utf-8", newline="\n").write(t.replace(VIEJO, NUEVO, 1))
print("KK.5.c pasa a nombrar docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_v49.txt")
print("sexto ejemplar seguido de la colision d030, pagado a mano otra vez")
