# -*- coding: utf-8 -*-
"""EL CIERRE DE UNA VUELTA, COMPROBADO POR CODIGO (D.41).

    python scripts/cerrar_reporte.py            el cierre entero de una vuelta
    python scripts/cerrar_reporte.py --hook     lo que corre en cada commit

POR QUE HAY DOS MODOS, y no es una comodidad. **El cierre de vuelta es estricto:
toda tabla que diga venir de un instrumento tiene que poder enseñarlo**, porque
ese es el momento en que el extractor todavia tiene sus instrumentos en el arbol.
**El hook es el modo corto**: corre en cada commit, decenas de veces por vuelta,
y solo puede permitirse lo barato.

LO QUE EL HOOK NO HACE, Y ES DELIBERADO: no corre instrumentos. `--regenerar` es
una orden explicita que se da a mano. Los instrumentos de una vuelta **escriben**
en `cuarentena/` y **llaman a la aduana**, que cuesta minutos por candidato: un
hook que re ejecuta lo que encuentra escrito en un documento no es una guarda.

LO QUE SI HACE EL HOOK: comparar, celda a celda, toda tabla del reporte que diga
ser la salida de un instrumento contra el fichero de salida de ese instrumento.
**Una tabla que difiere ABORTA el commit nombrando la fila.** Cuesta menos de un
segundo porque solo lee ficheros que ya estan escritos.
"""

import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TALLADOR = os.path.join("scripts", "tallar_reporte.py")
CENSO = os.path.join("scripts", "censar_rutas.py")


def _correr(titulo, orden):
    print("[cierre] %s" % titulo)
    proceso = subprocess.Popen(orden, cwd=RAIZ)
    proceso.communicate()
    return proceso.returncode == 0


def main(argumentos=None):
    argumentos = list(argumentos if argumentos is not None else sys.argv[1:])
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8")
        except Exception:
            pass
    solo_hook = "--hook" in argumentos

    pasos = [("tallado del reporte (D.41)",
              [sys.executable, TALLADOR] + ([] if solo_hook else ["--estricto"])),
             # D.42 VA EN LOS DOS MODOS Y SIN VARIANTE: solo lee ficheros que ya
             # estan escritos, cuesta menos de un segundo, y caza la especie que
             # tumbo la racha REPORTE en la vuelta 25.
             ("censo de rutas (D.42)", [sys.executable, CENSO])]
    if not solo_hook:
        # EL CIERRE DE VUELTA CORRE TODAS LAS GUARDAS, no solo la nueva. Una
        # guarda nueva que desplaza a las viejas no suma: sustituye.
        # La vigencia va aparte, mas abajo, y la razon esta escrita alli.
        pasos.extend([
            ("gate de integridad", [sys.executable, "forja.py", "gate"]),
            ("barrido de guiones", [sys.executable, "forja.py", "guiones"]),
            ("prueba de aceptacion",
             [sys.executable, os.path.join("tests", "test_aceptacion.py")]),
        ])

    caidos = []
    for titulo, orden in pasos:
        if not _correr(titulo, orden):
            caidos.append(titulo)
            if solo_hook:
                break

    # CORRECCION DECLARADA DEL 16 SEP 2026 (ACTA 27 5.3.a): LA VIGENCIA SALE DE
    # LA LISTA DE ARRIBA Y NO DEVUELVE ROJO.
    #
    # Estuvo entre las guardas cuyo fallo devuelve CIERRE EN ROJO, y `D.15` dice
    # lo contrario con estas palabras: *se relee con el texto de hoy, o se declara
    # por que sigue valiendo. Las dos cosas las hace una persona, y por eso esto NO
    # pone el gate en rojo: el gate vigila lo que es cierto o falso hoy; esto
    # vigila lo que fue cierto ayer y nadie ha vuelto a mirar.*
    #
    # ENTRE UNA REGLA ESCRITA Y UN CODIGO QUE LA CONTRADICE MANDA LA REGLA, y el
    # codigo se corrige declarandolo, que es lo que hace este parrafo.
    #
    # Y NO SE AFLOJA: `rancios` SIGUE CORRIENDO, SIGUE IMPRIMIENDO SUS HALLAZGOS Y
    # EL CIERRE SIGUE PUBLICANDO SU CUENTA. *La guarda que no muerde es cifra*
    # (cosecha 7.C). Lo unico que cambia es que **contar una cola no es caerse.**
    if not solo_hook:
        print("[cierre] vigencia de los veredictos (D.15): COLA DE TRABAJO, no guarda")
        proceso = subprocess.Popen([sys.executable, "forja.py", "rancios"], cwd=RAIZ)
        proceso.communicate()
        if proceso.returncode != 0:
            print("")
            print("LA VIGENCIA TIENE COLA, Y ESO NO PONE EL CIERRE EN ROJO (D.15).")
            print("Un rancio no se cita como vigente: se relee con el texto de hoy,")
            print("o se declara por que sigue valiendo. Las dos cosas las hace una")
            print("persona, y por eso esto no pone nada en rojo.")

    print("")
    if caidos:
        print("CIERRE EN ROJO. No pasa: %s" % ", ".join(caidos))
        if any("censo" in c for c in caidos):
            print("")
            print("Si lo que cayo es el censo, la ruta se arregla de una de estas")
            print("tres formas, y solo de estas tres:")
            print("  1. regenerando el fichero, que es lo que casi siempre toca;")
            print("  2. escribiendo en la MISMA celda 'VACIA A PROPOSITO: <motivo>';")
            print("  3. si era un conjunto, escribiendola como 'PATRON: <glob>'.")
        if any("tallado" in c for c in caidos):
            print("")
            print("Si lo que cayo es el tallado, la tabla NO se corrige tecleando:")
            print("  python scripts/tallar_reporte.py --arreglar")
            print("y se escribe al lado de que caida sale (correccion declarada).")
        return 1
    print("CIERRE VERDE: %s." % ("el tallado y el censo de rutas" if solo_hook
                                 else "las cuatro guardas que muerden, el tallado y el "
                                      "censo. La vigencia corrio y publico su cuenta "
                                      "arriba: es cola, no guarda (D.15)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
