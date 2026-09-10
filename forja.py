# -*- coding: utf-8 -*-
"""forja.py: la unica puerta de entrada de la forja.

    python forja.py insertar candidato.json     la aduana (manual seccion 3)
    python forja.py informe candidato.json      la aduana EN SECO, cero inserciones
    python forja.py arista --madre A --hijo B --paso N --razon R   D.37
    python forja.py gate                        el gate de integridad
    python forja.py guiones [ruta ...]          el barrido de estilo
    python forja.py rancios                     el bloque de vigencia (D.15)
    python forja.py resolutor [id ...]          el resolutor de ids
    python forja.py censos                      crea las plantillas de censo
    python forja.py ayuda
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src import (aduana, arista, censos, comun, gate, guiones, informe,  # noqa: E402
                 resolutor, vigencia)

AYUDA = __doc__


def main(argumentos):
    comun.salida_utf8()
    if not argumentos or argumentos[0] in ("ayuda", "-h", "--help", "help"):
        print(AYUDA)
        return 0
    comando, resto = argumentos[0], argumentos[1:]

    if comando == "insertar":
        return aduana.main(resto)
    if comando == "arista":
        return arista.main(resto)
    if comando == "informe":
        return informe.main(resto)
    if comando == "gate":
        return gate.main(resto)
    if comando == "guiones":
        return guiones.main(resto)
    if comando == "rancios":
        return vigencia.main(resto)
    if comando == "resolutor":
        instancia = resolutor.Resolutor.desde_dataset()
        if resto:
            codigo = 0
            for identificador in resto:
                resuelto = instancia.resolver(identificador)
                print("%s resuelve a %s (cadena: %s)"
                      % (identificador, resuelto or "NADA",
                         " > ".join(instancia.cadena(identificador))))
                if resuelto is None:
                    codigo = 1
            return codigo
        print(resolutor.informe())
        return 0
    if comando == "censos":
        creados = censos.crear_plantillas()
        print("plantillas de censo creadas: %s" % (", ".join(creados) if creados
                                                   else "ninguna, ya estaban todas"))
        return 0

    print("comando desconocido: %s" % comando)
    print(AYUDA)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
