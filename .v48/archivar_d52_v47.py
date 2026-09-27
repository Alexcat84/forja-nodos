# -*- coding: utf-8 -*-
"""LA COLISION DE D.52 CON D.41, RESUELTA COMO LA RESOLVIERON LAS VUELTAS 46 Y 47 (d030).

scripts/tabla_de_cierre.py --escribir escribe SIEMPRE en docs/loop/TABLA_DE_CIERRE.txt, y
el tallado de D.41 compara TODA tabla del reporte contra el fichero que esa tabla nombra.
Dos vueltas no pueden estar verdes a la vez: la que escribe deja en rojo a la anterior.

SE REPARA SIN TECLEAR NI BORRAR: la salida de la vuelta 47 se saca de git BYTE A BYTE y se
archiva; la linea de su reporte que nombraba la ruta viva pasa a nombrar la archivada, con
la correccion declarada al lado; y la ruta viva se queda con la tabla de la vuelta que
cierra hoy, que es lo que D.52 manda.

ES EL CUARTO EJEMPLAR SEGUIDO (42, 46, 47 y hoy la 48), y por eso es deuda de maquinaria
y no descuido: d030 la tiene abierta y la moratoria de EXTRACTOR.md 13 con D.45 me dejan
fuera de arreglar el script.
"""
import io

R = "docs/loop/REPORTE.md"
t = io.open(R, encoding="utf-8").read()

VIEJO = (u"### II.4.c. **LA TABLA DE CIERRE DE TAREAS** (`D.52`)\n"
         u"\n"
         u"*Salida de `python scripts/tabla_de_cierre.py --escribir`, pegada de\n"
         u"`docs/loop/TABLA_DE_CIERRE.txt`.*\n")

NUEVO = (u"### II.4.c. **LA TABLA DE CIERRE DE TAREAS** (`D.52`)\n"
         u"\n"
         u"*Salida de `python scripts/tabla_de_cierre.py --escribir`, pegada de\n"
         u"`docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_v47.txt`.*\n"
         u"\n"
         u"> **CORRECCION DECLARADA de la vuelta 48, y no toca ni una celda de esta tabla.**\n"
         u"> Esta linea decia `docs/loop/TABLA_DE_CIERRE.txt`, que es la ruta VIVA del\n"
         u"> instrumento, **y es la misma colision que esta misma seccion declaro contra la\n"
         u"> vuelta 46**: la vuelta siguiente que cierre su tabla deja a esta en rojo sin que\n"
         u"> nadie toque el reporte. **La vuelta 48 le hace a la 47 exactamente lo que la 47 le\n"
         u"> hizo a la 46 y la 46 a la 42.**\n"
         u">\n"
         u"> **LA SALIDA DE LA VUELTA 47 NO SE TECLEO NI SE PERDIO: SE SACO DE GIT BYTE A BYTE**\n"
         u"> (`git show HEAD:docs/loop/TABLA_DE_CIERRE.txt`, con el mismo `git hash-object`\n"
         u"> antes y despues, sellado en `.v48/sello_v47.txt`) y se archivo en la ruta que esta\n"
         u"> linea nombra ahora. **La ruta viva se queda con la tabla de la vuelta que cierra**,\n"
         u"> que es lo que `D.52` manda.\n"
         u">\n"
         u"> **Y ES EL CUARTO EJEMPLAR SEGUIDO DE LA MISMA AVERIA**, que es lo que la convierte\n"
         u"> en deuda de maquinaria y no en descuido de nadie: `d030` la tiene abierta desde la\n"
         u"> `ACTA 46` y la moratoria de `EXTRACTOR.md` 13 con `D.45` me dejan fuera de arreglar\n"
         u"> el script. **Lo que hago es el remedio a mano que el encargo me manda volver a\n"
         u"> usar.**\n")

assert VIEJO in t, "la linea de la vuelta 47 no esta donde se esperaba"
io.open(R, "w", encoding="utf-8", newline="\n").write(t.replace(VIEJO, NUEVO, 1))
print("colision declarada y reparada")
