# -*- coding: utf-8 -*-
"""VUELCA LAS MEDIDAS CRUDAS de las tres clases a un fichero.

    python calibracion/volcar_medidas.py

Escribe `calibracion/MEDIDAS_CRUDAS.jsonl`: una linea por par medido, con su
clase, sus dos ids y el valor de las tres señales.

POR QUE EXISTE, y no es comodidad: medir las tres señales sobre miles de pares
cuesta minutos, y **toda pregunta sobre umbrales que obligue a volver a medir es
una pregunta que nadie va a hacer dos veces.** Con el volcado, cualquier umbral
se evalua en un segundo y **cada cifra publicada se recomputa del fichero**, que
es lo que esta casa entiende por una cifra (`EJECUTOR.md` regla 5).

El fichero se commitea: es la evidencia de la calibracion, no un cache.
"""

import os
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src import aduana, comun  # noqa: E402
import referencia  # noqa: E402

SEMILLA = 20260909
MUESTRA_AJENOS = 4000
MUESTRA_JERARQUIA = 800
DESTINO = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "MEDIDAS_CRUDAS.jsonl")


def main():
    comun.salida_utf8()
    inicio = time.time()
    datos_corte = referencia.corte()
    ref = referencia.Referencia()

    import random
    azar = random.Random(SEMILLA)
    gemelos = ref.pares_gemelos()
    jerarquia = ref.pares_jerarquia()
    if len(jerarquia) > MUESTRA_JERARQUIA:
        jerarquia = azar.sample(jerarquia, MUESTRA_JERARQUIA)
    ajenos = ref.pares_ajenos(MUESTRA_AJENOS, SEMILLA)

    filas = []
    for clase, pares in (("GEMELO", gemelos), ("JERARQUIA", jerarquia),
                         ("AJENO", ajenos)):
        print("midiendo %s (%d pares) ..." % (clase, len(pares)))
        for a, b in pares:
            nodo_a, nodo_b = ref.nodos[a], ref.nodos[b]
            s1 = aduana.senal_similitud_texto(comun.texto_comparable(nodo_a),
                                              comun.texto_comparable(nodo_b))
            s2 = aduana.senal_familia_id(nodo_a.get("id"), nodo_b.get("id"))
            s3, _ = aduana.senal_paso_contra_nodo(nodo_a, nodo_b)
            fila = {"clase": clase, "a": a, "b": b}
            for nombre, valor in (("similitud_texto", s1), ("familia_id", s2),
                                  ("paso_contra_nodo", s3)):
                fila[nombre] = ("NO APLICA" if isinstance(valor, aduana.NoAplica)
                                else round(valor, 6))
            filas.append(fila)

    comun.escribir_jsonl(DESTINO, filas)
    print("")
    print("volcado en %s" % comun.relativa(DESTINO))
    print("  pares medidos : %d" % len(filas))
    print("  grafo         : %s (%s)" % (datos_corte["commit"], datos_corte["tag"]))
    print("  semilla       : %d" % SEMILLA)
    print("  corrida en %.1f segundos" % (time.time() - inicio))
    return 0


if __name__ == "__main__":
    sys.exit(main())
