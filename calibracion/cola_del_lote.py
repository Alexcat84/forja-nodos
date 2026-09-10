# -*- coding: utf-8 -*-
"""CUANTA LECTURA CUESTA UN LOTE CUANDO EL GRAFO YA ESTA LLENO.

    python calibracion/cola_del_lote.py [--cuantos 12]

EL INFORME DEL ESTRENO (calibracion/SALIDA_ESTRENO.txt) corrio contra el grafo
real de la forja, que hoy tiene DOS nodos, asi que dio CERO bloqueos. Eso es
cierto y es lo que el fundador va a ver manana, pero no dice lo que costara el
mismo lote cuando el grafo tenga miles.

Esto lo mide DIRECTAMENTE: los mismos candidatos, contra los 3.169 vivos del
catalogo limpio. Es el control de la cifra 2,4 vecinos falsos por candidato que
docs/CALIBRACION_D4.md estimo de forma analitica para el umbral 0,60.

Es caro (cada candidato se compara con 3.169 nodos, unos cuatro minutos), por
eso corre sobre una submuestra y publica su tamaño. NO INSERTA NADA.
"""

import io
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calibracion import preparar_ensayo, referencia  # noqa: E402
from src import comun, informe  # noqa: E402


def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos or sys.argv[1:])
    cuantos = 12
    if "--cuantos" in argumentos:
        cuantos = int(argumentos[argumentos.index("--cuantos") + 1])

    lote = os.path.join(comun.RAIZ, "cuarentena", preparar_ensayo.LOTE_POR_DEFECTO)
    rutas = sorted(os.path.join(lote, f) for f in os.listdir(lote)
                   if f.lower().endswith(".json"))
    if not rutas:
        print("el lote de ensayo no esta depositado: corre preparar_ensayo.py")
        return 1

    ref = referencia.Referencia()
    vivos = [i for i in ref.nodos if ref.nodos[i].get("estado", "vivo") == "vivo"]

    taller = os.path.join(comun.RAIZ, "cuarentena", "_derivadas")
    if not os.path.isdir(taller):
        os.makedirs(taller)
    grafo = os.path.join(taller, "CATALOGO_COMPLETO.jsonl")
    with io.open(grafo, "w", encoding="utf-8") as fichero:
        for identificador in sorted(vivos):
            fichero.write(json.dumps(ref.nodos[identificador],
                                     ensure_ascii=False) + u"\n")
    tabla = os.path.join(taller, "FUENTES_DEL_CONTROL.json")
    comun.escribir_texto(tabla, json.dumps(ref.tabla_de_fuentes(),
                                           ensure_ascii=False))

    # Los candidatos de la submuestra NO pueden estar en el grafo de destino, o
    # cada uno se encontraria a si mismo. Se quitan de la copia y se dice.
    elegidos = rutas[::max(1, len(rutas) // cuantos)][:cuantos]
    ids_elegidos = set(os.path.splitext(os.path.basename(r))[0] for r in elegidos)
    with io.open(grafo, "w", encoding="utf-8") as fichero:
        for identificador in sorted(vivos):
            if identificador in ids_elegidos:
                continue
            fichero.write(json.dumps(ref.nodos[identificador],
                                     ensure_ascii=False) + u"\n")
    destino = len(vivos) - len(ids_elegidos & set(vivos))

    print("=" * 74)
    print("CONTROL DIRECTO DE COLA: el lote contra un grafo LLENO")
    print("=" * 74)
    print("candidatos medidos : %d de %d del lote de ensayo" % (len(elegidos), len(rutas)))
    print("grafo de destino   : %d vivos del catalogo limpio" % destino)
    print("                     (cada candidato se retira de su propio destino)")
    print("umbral vigente     : paso contra nodo 0,60")
    print("")
    sys.stdout.flush()

    arranque = time.time()
    dictamenes, cuantos_nodos, umbrales, _archivados = informe.revisar(
        elegidos, ruta_dataset=grafo, tabla_fuentes=comun.leer_json(tabla))

    colas = []
    for dictamen in dictamenes:
        vecinos = dictamen.get("vecinos") or []
        colas.append(len(vecinos))
        print("  %-52s %3d vecinos  [%s]"
              % (dictamen["id"][:52], len(vecinos), dictamen["salida"]))
    colas.sort()
    print("")
    print("LA CIFRA")
    print("  vecinos totales levantados : %d" % sum(colas))
    print("  media por candidato        : %.2f" % (float(sum(colas)) / len(colas)))
    print("  mediana                    : %d" % colas[len(colas) // 2])
    print("  maximo                     : %d" % colas[-1])
    print("  candidatos con cola vacia  : %d de %d"
          % (len([c for c in colas if c == 0]), len(colas)))
    print("")
    print("  estimacion analitica de docs/CALIBRACION_D4.md : 2,4 por candidato")
    print("  corrida en %.1f segundos" % (time.time() - arranque))
    print("")
    print("NADA SE INSERTO.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
