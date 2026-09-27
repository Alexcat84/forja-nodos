# -*- coding: utf-8 -*-
"""LA TABLA DEL REPORTE, ESTA IMPRESA O ESTA TECLEADA.

La caida 58.3.a de la vuelta 59 fue texto de la mano DENTRO de un bloque que se
presentaba como salida de instrumento. La guarda barata es esta: toda fila de
tabla del tramo de la vuelta tiene que aparecer, caracter a caracter, en el
fichero de salida que el propio reporte declara con su marcador TALLADO.
"""

import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
SALIDA = os.path.join(RAIZ, ".v60ext", "frontera_v60.txt")
CABECERA_DE_LA_VUELTA = "# VUELTA 60, lote 7"


def main():
    texto = io.open(REPORTE, encoding="utf-8").read().split("\n")
    arranque = max(i for i, l in enumerate(texto)
                   if l.startswith(CABECERA_DE_LA_VUELTA))
    del_reporte = [l for l in texto[arranque:] if l.startswith("| ")]
    del_instrumento = [l for l in io.open(SALIDA, encoding="utf-8").read().split("\n")
                       if l.startswith("| ")]

    en_instrumento = set(del_instrumento)
    en_reporte = set(del_reporte)
    solo_reporte = [l for l in del_reporte if l not in en_instrumento]
    solo_instrumento = [l for l in del_instrumento if l not in en_reporte]

    print("filas de tabla en el reporte : %d" % len(del_reporte))
    print("filas de tabla en el instrum.: %d" % len(del_instrumento))
    print("filas del reporte que el instrumento NO imprime: %d" % len(solo_reporte))
    for l in solo_reporte[:10]:
        print("   REP> %s" % l[:150])
    print("filas del instrumento que el reporte NO pega   : %d" % len(solo_instrumento))
    for l in solo_instrumento[:10]:
        print("   INS> %s" % l[:150])


if __name__ == "__main__":
    main()
