# -*- coding: utf-8 -*-
"""EL CERROJO, PROBADO POR MUTACION Y DEVUELTO TAL CUAL.

Cosecha 7.C: una guarda publicada como mordiendo que no muerde es cifra falsa,
asi que toda guarda que el acta declare se re corre. El cerrojo es una de las
cuatro que bloquean (D.55), y hoy hay un fichero de cerrojo puesto, de un
proceso del 18 sep que ya no vive. Este script no lo rompe a mano: intenta
tomarlo por la puerta normal, deja que src/cerrojo.py decida, y RESTAURA el
fichero byte a byte al salir.
"""

import io
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import cerrojo, comun


def main():
    ruta = cerrojo.ruta_de(comun.RUTA_DATASET)
    if not os.path.exists(ruta):
        print("no hay cerrojo puesto sobre este dataset: nada que probar")
        print("VERDE por ausencia, y se declara")
        return

    copia = io.open(ruta, encoding="utf-8").read()
    dueno = json.loads(copia)
    print("dueno declarado : %s" % dueno)
    print("edad en segundos: %d" % int(time.time() - dueno["desde"]))
    print("TOPE_DE_HUERFANO: %s" % cerrojo.TOPE_DE_HUERFANO)
    print("_vive(pid)      : %s" % cerrojo._vive(dueno.get("pid")))
    print("")

    avisos = []
    try:
        with cerrojo.tomar(comun.RUTA_DATASET, avisar=avisos.append):
            print("LO TOMO: si, el huerfano no bloquea")
    except cerrojo.CerrojoOcupado as ocupado:
        print("NO LO TOMO, y eso seria ROJO: %s" % ocupado)
    for aviso in avisos:
        print("aviso: %s" % aviso)

    io.open(ruta, "w", encoding="utf-8").write(copia)
    print("")
    print("fichero restaurado byte a byte: %s"
          % (io.open(ruta, encoding="utf-8").read() == copia))


if __name__ == "__main__":
    main()
