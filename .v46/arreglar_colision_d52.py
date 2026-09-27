# -*- coding: utf-8 -*-
"""LA COLISION DE D.52 CON D.41: un solo fichero de salida para todas las vueltas.

scripts/tabla_de_cierre.py --escribir escribe SIEMPRE en docs/loop/TABLA_DE_CIERRE.txt, y
el tallado de D.41 compara TODA tabla del reporte contra el fichero que esa tabla nombra.
Dos vueltas no pueden estar verdes a la vez: la que escribe deja en rojo a la anterior.

SE REPARA SIN TECLEAR NI BORRAR: la salida de la vuelta 42 se saca de git BYTE A BYTE
(git show HEAD:docs/loop/TABLA_DE_CIERRE.txt, hash c33bec5) y se archiva, y la linea de
su reporte que nombraba la ruta viva pasa a nombrar la archivada, con la correccion
declarada al lado. El fichero canonico se queda con la tabla de la vuelta que cierra hoy,
que es lo que D.52 manda.
"""
import io

R = "docs/loop/REPORTE.md"
t = io.open(R, encoding="utf-8").read()

VIEJO = (u"## ED.8. **LA TABLA DE CIERRE DE TAREAS** (`D.52`)\n"
         u"\n"
         u"*Salida de `python scripts/tabla_de_cierre.py --escribir`, pegada de "
         u"`docs/loop/TABLA_DE_CIERRE.txt`.*\n")

NUEVO = (u"## ED.8. **LA TABLA DE CIERRE DE TAREAS** (`D.52`)\n"
         u"\n"
         u"*Salida de `python scripts/tabla_de_cierre.py --escribir`, pegada de\n"
         u"`docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_v42.txt`.*\n"
         u"\n"
         u"> **CORRECCION DECLARADA de la vuelta 46, y no toca ni una celda de esta tabla.**\n"
         u"> Esta linea decia `docs/loop/TABLA_DE_CIERRE.txt`, que es la ruta VIVA del\n"
         u"> instrumento. **`scripts/tabla_de_cierre.py --escribir` escribe siempre en esa misma\n"
         u"> ruta**, asi que la vuelta siguiente que cierre su tabla deja a esta en rojo sin que\n"
         u"> nadie haya tocado el reporte: **dos vueltas no pueden estar verdes contra un solo\n"
         u"> fichero de salida.** Paso en esta vuelta 46, con esta salida pegada tal cual:\n"
         u">\n"
         u">     DIFIERE  docs/loop/REPORTE.md linea 42364\n"
         u">       declara: docs/loop/TABLA_DE_CIERRE.txt\n"
         u">       5 fila(s) distintas de su instrumento\n"
         u">\n"
         u"> **LA SALIDA DE LA VUELTA 42 NO SE TECLEO NI SE PERDIO: SE SACO DE GIT BYTE A BYTE**\n"
         u"> (`git show HEAD:docs/loop/TABLA_DE_CIERRE.txt`, `git hash-object` da `c33bec5` antes\n"
         u"> y despues) y se archivo en la ruta que esta linea nombra ahora. **La ruta viva se\n"
         u"> queda con la tabla de la vuelta que cierra**, que es lo que `D.52` manda.\n")

assert VIEJO in t, "la linea de la vuelta 42 no esta donde se esperaba"
io.open(R, "w", encoding="utf-8", newline="\n").write(t.replace(VIEJO, NUEVO))
print("colision declarada y reparada")
