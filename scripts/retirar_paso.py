# -*- coding: utf-8 -*-
"""UN PASO RETIRADO POR DECLARACION SE RETIRA DEL CAMPO (D.54, 17 sep 2026).

    python scripts/retirar_paso.py --ver
        mide que nodos declaran una retirada que sigue viva en `pasos_accionables`

    python scripts/retirar_paso.py --nodo <id> --paso N --razon "..."
        la aplica: el paso sale del campo y su retirada queda escrita con su cita

POR QUE HIZO FALTA ESCRIBIRLO, y lo dice el propio nodo que lo obligo:

    esta casa no da ninguna via que reescriba un paso de un nodo ya insertado:
    src/correccion.py solo toca el resumen_teorico por decision escrita, e
    insertar rechaza un id que ya vive.

**POR ESO LA RETIRADA SE QUEDABA EN LA PROSA.** No fue descuido: **no habia por donde.**
Y un nodo tiene dos lectores: quien lee el `resumen_teorico` se entera de que el paso esta
retirado, **quien lee `pasos_accionables` se lleva el puente entero**, que es ademas el
campo que la maquina consume.

LO QUE HACE AL APLICARLA, y las tres cosas van en el mismo acto:

  1. **saca el paso de `pasos_accionables`**, por su numero de orden;
  2. **escribe la retirada dentro del propio nodo**, con la fecha, la razon y el texto
     literal del paso retirado, para que **no se pierda lo que decia**;
  3. **escribe bajo cerrojo** (`D.44`), porque toca `dataset/nodos.jsonl`.

NO BORRA: TACHA Y DEJA EL TEXTO AL LADO. El paso sale de la lista que la maquina lee y
**su literal queda escrito en el nodo**, que es como corrige esta casa desde `D.13`.
"""

import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)

from src import cerrojo, comun  # noqa: E402

# La forma con la que esta casa declara una retirada dentro del resumen.
RETIRADA = re.compile(
    r"(?:paso|P)\s*(\d+)[^.\n]{0,120}?\bretirad[oa]\b"
    r"|\bretirad[oa]\b[^.\n]{0,120}?(?:paso|P)\s*(\d+)", re.I)


# LA MARCA QUE DEJA UNA RETIRADA YA APLICADA. Sin ella el medidor no distingue
# "declarada y pendiente" de "declarada y hecha": el resumen sigue diciendo que el paso
# N esta retirado, y el nodo sigue teniendo N pasos o mas, porque tenia mas de N.
# **Un medidor que no sabe decir cuando ya se hizo no mide: acusa siempre.**
APLICADA = "SALE DE pasos_accionables EN ESTE ACTO"


def pendientes(nodos=None):
    """`[(id, numero, total, frase)]` de cada retirada declarada que sigue en el campo."""
    nodos = comun.leer_jsonl(comun.RUTA_DATASET) if nodos is None else nodos
    casos = []
    for nodo in nodos:
        resumen = nodo.get("resumen_teorico") or ""
        pasos = nodo.get("pasos_accionables") or []
        if APLICADA in resumen:
            continue
        for encaje in RETIRADA.finditer(resumen):
            numero = int(encaje.group(1) or encaje.group(2))
            if 1 <= numero <= len(pasos):
                casos.append((nodo.get("id", "?"), numero, len(pasos),
                              encaje.group(0).strip()))
                break
    return casos


def retirar(id_nodo, numero, razon, nodos=None):
    """Saca el paso `numero` de ese nodo y deja su retirada escrita. Devuelve el texto."""
    propios = nodos is None
    nodos = comun.leer_jsonl(comun.RUTA_DATASET) if propios else nodos
    for nodo in nodos:
        if nodo.get("id") != id_nodo:
            continue
        pasos = nodo.get("pasos_accionables") or []
        if not (1 <= numero <= len(pasos)):
            raise ValueError("el nodo '%s' tiene %d paso(s) y se pidio el %d"
                             % (id_nodo, len(pasos), numero))
        retirado = pasos[numero - 1]
        nodo["pasos_accionables"] = pasos[:numero - 1] + pasos[numero:]
        nodo["resumen_teorico"] = (nodo.get("resumen_teorico") or "").rstrip() + (
            " CORRECCION DECLARADA (17 sep 2026, D.54): EL PASO %d SALE DE "
            "pasos_accionables EN ESTE ACTO, y no solo de esta prosa. %s "
            "SU TEXTO LITERAL, QUE NO SE PIERDE: \"%s\" LOS PASOS PASAN DE %d A %d."
            % (numero, razon, retirado, len(pasos), len(pasos) - 1))
        return nodos, retirado
    raise ValueError("no hay ningun nodo con id '%s'" % id_nodo)


def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos if argumentos is not None else sys.argv[1:])

    if "--ver" in argumentos or not argumentos:
        casos = pendientes()
        print("RETIRADAS DECLARADAS QUE SIGUEN VIVAS EN EL CAMPO (D.54)")
        print("  poblacion: %s, sin filtrar" % comun.relativa(comun.RUTA_DATASET))
        print("  encontradas: %d" % len(casos))
        for id_nodo, numero, total, frase in casos:
            print("    %s, paso %d de %d" % (id_nodo, numero, total))
            print("       el resumen dice: %s" % frase[:90])
        return 0 if not casos else 1

    def valor(bandera):
        return argumentos[argumentos.index(bandera) + 1] if bandera in argumentos else None

    id_nodo, numero, razon = valor("--nodo"), valor("--paso"), valor("--razon")
    if not (id_nodo and numero and razon):
        print("faltan argumentos: --nodo <id> --paso N --razon \"...\"")
        return 2

    with cerrojo.tomar(comun.RUTA_DATASET, avisar=lambda m: print("  " + m)):
        nodos, retirado = retirar(id_nodo, int(numero), razon)
        comun.escribir_jsonl(comun.RUTA_DATASET, nodos)

    print("RETIRADO del campo (D.54): %s, paso %s" % (id_nodo, numero))
    print("  su texto queda escrito en el nodo y no se pierde:")
    print("    \"%s\"" % retirado[:160])
    return 0


if __name__ == "__main__":
    sys.exit(main())
