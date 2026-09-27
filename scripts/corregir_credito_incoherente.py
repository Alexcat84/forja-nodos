# -*- coding: utf-8 -*-
"""CORRECCION DECLARADA de las filas de credito que se contradicen a si mismas.

    python scripts/corregir_credito_incoherente.py --registro <ruta> --cita <parada> [--escribir]

Sin `--escribir` solo dice lo que haria. Es la reparacion que la decision del fundador
del 22 sep 2026 (DOS SEMANAS, punto 2) manda hacer sobre las DOCE filas que
`credito.incoherentes()` destapo el 21: ocho de la serial y cuatro del frente
`marquet_turn_the_ship`.

QUE CORRIGE, Y POR QUE ESE VALOR Y NO OTRO. Cada fila declara una racha y un `cae` que
no casan: una racha que sube sin decir si cae, o un `cae` falso con la racha arriba.
**La racha declarada NO SE TOCA**: es lo que el acta adjudico, y la decision lo dice con
esas palabras, *sin reabrir rachas cerradas: son historia que el instrumento viejo no
veia, no caidas nuevas*. Lo que se corrige es la bandera, y se pone **el unico valor
coherente con la racha que la fila ya declaraba**: numerador por encima de cero es que
algo cayo, y cero es tanda limpia.

COMO SE CORRIGE, y es la forma de esta casa: **tachando, no borrando.** El valor viejo
queda en `cae_original` (o `"AUSENTE"` si la fila no lo traia), y la fila gana un campo
`correccion` con su cita. Es lo mismo que `scripts/readjudicar_aristas.py` hizo el 18 sep
con las 93 aristas: el valor anterior se conserva al lado del nuevo.

LO QUE COMPRUEBA ANTES DE ESCRIBIR, y si falla no escribe: **que el estado de cada
especie y el replay queden EXACTAMENTE como estaban.** Si corregir una bandera moviera una
racha, ya no seria corregir historia: seria reabrirla.
"""

import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)

from src import credito  # noqa: E402

AUSENTE = "AUSENTE"


def corregida(suceso, cita):
    """La fila con su `cae` coherente y el original tachado al lado. None si no toca."""
    if not credito.incoherencias(suceso):
        return None
    numero, _tope = credito._partir_racha(suceso.get("racha"))
    nueva = dict((k, v) for k, v in suceso.items() if not k.startswith("_"))
    nueva["cae_original"] = suceso["cae"] if "cae" in suceso else AUSENTE
    nueva["cae"] = bool(numero)
    nueva["correccion"] = {
        "que": "cae alineado con la racha que la fila ya declaraba; la racha no se toca",
        "cita": cita,
    }
    return nueva


def _estado(sucesos):
    return dict((k, (v.get("racha"), v.get("tanda")))
                for k, v in credito.estado(sucesos=sucesos).items())


def reparar(ruta, cita):
    """Devuelve (lineas nuevas, numero de filas corregidas, informe)."""
    crudas = io.open(ruta, encoding="utf-8").read().splitlines()
    antes = credito.leer(ruta_registro=ruta)
    salida, cambiadas = [], []
    for numero, cruda in enumerate(crudas, 1):
        if not cruda.strip():
            salida.append(cruda)
            continue
        suceso = json.loads(cruda)
        nueva = corregida(suceso, cita)
        if nueva is None:
            salida.append(cruda)
            continue
        salida.append(json.dumps(nueva, ensure_ascii=False, sort_keys=True))
        cambiadas.append((numero, suceso.get("especie"), suceso.get("tanda"),
                          suceso.get("racha"), nueva["cae_original"], nueva["cae"]))
    despues = [json.loads(l) for l in salida if l.strip()]
    for n, s in enumerate(despues, 1):
        s["_linea_del_fichero"] = n
    return salida, cambiadas, antes, despues


def main(argumentos=None):
    lector = argparse.ArgumentParser()
    lector.add_argument("--registro", required=True)
    lector.add_argument("--cita", required=True)
    lector.add_argument("--escribir", action="store_true")
    args = lector.parse_args(argumentos)

    salida, cambiadas, antes, despues = reparar(args.registro, args.cita)
    print("REGISTRO: %s" % args.registro)
    print("filas que se contradicen a si mismas: %d" % len(cambiadas))
    for numero, especie, tanda, racha, viejo, nuevo in cambiadas:
        print("  linea %3d  %-16s %-10s racha %-7s  cae %s -> %s"
              % (numero, especie, tanda, racha, viejo, nuevo))

    # LA COMPROBACION QUE DECIDE SI SE ESCRIBE
    iguales_estado = _estado(antes) == _estado(despues)
    rep_antes = len(credito.revisar(sucesos=antes))
    rep_despues = len(credito.revisar(sucesos=despues))
    quedan = len(credito.incoherentes(sucesos=despues))
    print("estado de las rachas, antes y despues   : %s"
          % ("IDENTICO" if iguales_estado else "DISTINTO"))
    print("discrepancias del replay, antes/despues : %d / %d" % (rep_antes, rep_despues))
    print("filas incoherentes que quedan           : %d" % quedan)

    if not iguales_estado or rep_despues > rep_antes or quedan:
        print("NO SE ESCRIBE: corregir la bandera moveria una racha o dejaria filas rotas,"
              " y eso ya no es corregir historia, es reabrirla.")
        return 1
    if not args.escribir:
        print("(ensayo: no se ha escrito nada; repite con --escribir)")
        return 0
    io.open(args.registro, "w", encoding="utf-8", newline="\n").write(
        "\n".join(salida) + "\n")
    print("ESCRITO: %d fila(s) corregida(s) por correccion declarada." % len(cambiadas))
    return 0


if __name__ == "__main__":
    sys.exit(main())
