# -*- coding: utf-8 -*-
"""LA COLISION DE D.52 CON D.41, RESUELTA COMO LA RESOLVIO LA VUELTA 46 (encargo TAREA 4.2).

scripts/tabla_de_cierre.py --escribir escribe SIEMPRE en docs/loop/TABLA_DE_CIERRE.txt, y
el tallado de D.41 compara TODA tabla del reporte contra el fichero que esa tabla nombra.
Dos vueltas no pueden estar verdes a la vez: la que escribe deja en rojo a la anterior.

SE REPARA SIN TECLEAR NI BORRAR: la salida de la vuelta 46 se saca de git BYTE A BYTE y se
archiva; la linea de su reporte que nombraba la ruta viva pasa a nombrar la archivada, con
la correccion declarada al lado; y la ruta viva se queda con la tabla de la vuelta que
cierra hoy, que es lo que D.52 manda.
"""
import io

R = "docs/loop/REPORTE.md"
t = io.open(R, encoding="utf-8").read()

VIEJO = (u"### HH.5.g. **LA TABLA DE CIERRE DE TAREAS** (`D.52`)\n"
         u"\n"
         u"*Salida de `python scripts/tabla_de_cierre.py --escribir`, pegada de\n"
         u"`docs/loop/TABLA_DE_CIERRE.txt`.*\n")

NUEVO = (u"### HH.5.g. **LA TABLA DE CIERRE DE TAREAS** (`D.52`)\n"
         u"\n"
         u"*Salida de `python scripts/tabla_de_cierre.py --escribir`, pegada de\n"
         u"`docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_v46.txt`.*\n"
         u"\n"
         u"> **CORRECCION DECLARADA de la vuelta 47, y no toca ni una celda de esta tabla.**\n"
         u"> Esta linea decia `docs/loop/TABLA_DE_CIERRE.txt`, que es la ruta VIVA del\n"
         u"> instrumento, y **es la misma colision que esta vuelta 46 declaro en `HH.5.i` y\n"
         u"> reparo para la vuelta 42**: la vuelta siguiente que cierre su tabla deja a esta en\n"
         u"> rojo sin que nadie toque el reporte. **La vuelta 47 le hizo a la 46 exactamente lo\n"
         u"> que la 46 le hizo a la 42.**\n"
         u">\n"
         u"> **LA SALIDA DE LA VUELTA 46 NO SE TECLEO NI SE PERDIO: SE SACO DE GIT BYTE A BYTE**\n"
         u"> (`git show <commit>:docs/loop/TABLA_DE_CIERRE.txt`, con el mismo `git hash-object`\n"
         u"> antes y despues) y se archivo en la ruta que esta linea nombra ahora. **La ruta viva\n"
         u"> se queda con la tabla de la vuelta que cierra**, que es lo que `D.52` manda.\n"
         u">\n"
         u"> **Y ES EL TERCER EJEMPLAR SEGUIDO DE LA MISMA AVERIA**, que es lo que la convierte en\n"
         u"> deuda de maquinaria y no en descuido de nadie: `d022` ya dice que este instrumento\n"
         u"> localiza su tabla por un sitio fragil, y `HH.5.i` propuso que su salida lleve la\n"
         u"> vuelta en el nombre. **La vuelta 47 no lo adjudica: lo vuelve a proponer con su\n"
         u"> tercer caso delante.**\n")

assert VIEJO in t, "la linea de la vuelta 46 no esta donde se esperaba"
io.open(R, "w", encoding="utf-8", newline="\n").write(t.replace(VIEJO, NUEVO, 1))
print("colision declarada y reparada")
