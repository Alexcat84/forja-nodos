# -*- coding: utf-8 -*-
"""CORRECCION DECLARADA sobre bitacora/VEREDICTOS.jsonl (vuelta 17, TAREA 2.c.2).

ACTA 16 seccion 8.1 midio que `src/aduana.py` daba por hecho que el candidato es
siempre el HIJO. Cuando el candidato es la MADRE, el campo `arista` escribia
`X > X` y perdia el nombre del hijo. La linea de codigo esta arreglada en esta
misma vuelta, con su prueba que cae con el codigo viejo.

LAS DOCE LINEAS VIEJAS NO SE REESCRIBEN NI SE BORRAN (principio 6 del manual, y
el encargo lo repite con esas palabras). En un jsonl no hay tachado, asi que se
les ANIADE UN CAMPO NUEVO, `arista_corregida`, con la arista verdadera, y el
campo `arista` se queda exactamente donde esta y diciendo lo que decia.

ESTO NO ES UNA EDICION A MANO: es una operacion escrita, con su simulacion antes
de escribir y su comprobacion despues, que es la forma que EXTRACTOR.md 2 exige
para tocar una sede por una via que no sea su instrumento.

La arista verdadera NO se deduce del texto roto: se lee del GRAFO, que es la
sede donde la arista si esta bien puesta por los dos lados (ACTA 16 1.2 midio
que las 79 aristas estan completas). Si el grafo no la confirma por los dos
extremos, la linea NO se toca y se declara.

    python .correccion_arista_v17.py            <- simulacion, no escribe
    python .correccion_arista_v17.py --escribir <- escribe
"""

import io
import json
import sys

RUTA_VEREDICTOS = "bitacora/VEREDICTOS.jsonl"
RUTA_DATASET = "dataset/nodos.jsonl"
CAMPO_NUEVO = "arista_corregida"


def leer(ruta):
    return [json.loads(l) for l in io.open(ruta, encoding="utf-8") if l.strip()]


def main():
    escribir = "--escribir" in sys.argv
    nodos = {n["id"]: n for n in leer(RUTA_DATASET)}
    lineas = io.open(RUTA_VEREDICTOS, encoding="utf-8").read().splitlines()

    tocadas, saltadas, salida = 0, 0, []
    for numero, cruda in enumerate(lineas, 1):
        if not cruda.strip():
            salida.append(cruda)
            continue
        registro = json.loads(cruda)
        arista = registro.get("arista") or ""
        extremos = arista.split(" > ")
        es_auto = (registro.get("veredicto") == "CONTINUA"
                   and len(extremos) == 2 and extremos[0] == extremos[1])
        if not es_auto or CAMPO_NUEVO in registro:
            salida.append(cruda)
            continue

        candidato, vecino = registro["candidato"], registro["vecino"]
        # La verdad se lee del grafo, por los DOS extremos, o no se escribe.
        siguientes = (nodos.get(candidato, {}).get("nodos_siguientes") or [])
        previos = (nodos.get(vecino, {}).get("nodos_previos") or [])
        if vecino in siguientes and candidato in previos:
            verdadera = "%s > %s" % (candidato, vecino)
        else:
            print("  L%-4d NO SE TOCA: el grafo no confirma %s > %s por los dos "
                  "extremos" % (numero, candidato, vecino))
            saltadas += 1
            salida.append(cruda)
            continue

        registro[CAMPO_NUEVO] = verdadera
        # sort_keys=True es lo que usa comun.agregar_jsonl: la linea corregida
        # sale con la misma forma que si la hubiera escrito el instrumento.
        salida.append(json.dumps(registro, ensure_ascii=False, sort_keys=True))
        tocadas += 1
        print("  L%-4d %-62s ->  %s" % (numero, arista, verdadera))

    print("")
    print("lineas en la bitacora        : %d" % len(lineas))
    print("lineas con el campo anadido  : %d" % tocadas)
    print("lineas saltadas y declaradas : %d" % saltadas)
    if not escribir:
        print("SIMULACION: no se ha escrito nada. Anade --escribir.")
        return 0
    with io.open(RUTA_VEREDICTOS, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(salida) + "\n")
    print("ESCRITO en %s" % RUTA_VEREDICTOS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
