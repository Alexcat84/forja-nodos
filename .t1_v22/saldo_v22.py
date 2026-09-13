# -*- coding: utf-8 -*-
"""EL SALDO DE LA VUELTA 22, LEIDO DE LOS DIECISIETE INFORMES Y NO DE CABEZA.

Nace el 13 sep 2026 con la decision del fundador sobre la parada de la vuelta 22,
punto 2: **las tres cifras falsas se corrigen POR REGENERACION, no a mano.**

Dos de las tres son esta: el reporte publico `10 ENTRARIA` y `7 BLOQUEARIA` donde
los ficheros de la maquina dicen `9` y `8`, y conto `11` pares distintos donde hay
`12`. **Las dos salen de la misma causa: la pieza 14 se leyo como ENTRARIA cuando
su propio informe dice BLOQUEARIA.**

LEE `.aduana_v22/*.txt`, que son los diecisiete informes de un candidato que la
vuelta corrio en el acto de escribir cada uno. **No recomputa la aduana: lee lo
que la aduana escribio.**
"""
import glob
import os
import re

CARPETA = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "..", ".aduana_v22")
SALIDA = re.compile(r"^\[(ENTRARIA|BLOQUEARIA|CAERIA|CHOCA)\]\s+(\S+)")
VECINO = re.compile(r"^\s+vecino\s+(\S+)\s+\[levantada por:\s*([^\]]*)\]")


def leer():
    saldo = {"ENTRARIA": 0, "BLOQUEARIA": 0, "CAERIA": 0, "CHOCA": 0}
    filas = []
    for ruta in sorted(glob.glob(os.path.join(CARPETA, "*.txt"))):
        actual = None
        for linea in open(ruta, encoding="utf-8"):
            encaje = SALIDA.match(linea)
            if encaje:
                saldo[encaje.group(1)] += 1
                actual = encaje.group(2)
                continue
            encaje = VECINO.match(linea)
            if encaje and actual:
                filas.append((actual, encaje.group(1), encaje.group(2).strip()))
    return saldo, filas


def main():
    saldo, filas = leer()
    # UN PAR ES DOS NODOS, NO UNA FLECHA. `montar_reunion_gran_debate` contra
    # `montar_reunion_gran_decision` se levanta por los dos lados, y contarlo dos
    # veces convertiria una lectura en dos. Sin esta linea el instrumento decia
    # 13 donde la ACTA 22 leyo 12, y la que tenia razon era el acta.
    pares = sorted(set(tuple(sorted((c, v))) for c, v, _s in filas))
    print("=" * 76)
    print("1. EL SALDO DE LOS DIECISIETE INFORMES, CONTADO DE SUS FICHEROS")
    print("=" * 76)
    print("informes leidos en .aduana_v22/ : %d" % sum(saldo.values()))
    for clase in ("ENTRARIA", "BLOQUEARIA", "CAERIA", "CHOCA"):
        print("  %-12s : %d" % (clase, saldo[clase]))
    print("")
    print("filas de vecino levantadas      : %d" % len(filas))
    print("pares DISTINTOS (candidato, vecino): %d" % len(pares))
    print("")
    print("=" * 76)
    print("2. LA TABLA, IMPRESA Y NO TECLEADA")
    print("=" * 76)
    print("| | |")
    print("|---|---|")
    print("| **informes de un candidato corridos** | **%d, uno por candidato y en el "
          "acto de escribirlo**. Saldo: **%d `ENTRARIA`, %d `BLOQUEARIA`, %d "
          "`CAERIA`** |" % (sum(saldo.values()), saldo["ENTRARIA"],
                            saldo["BLOQUEARIA"], saldo["CAERIA"]))
    print("| **filas de vecino levantadas** | **%d**, que son **%d pares distintos** |"
          % (len(filas), len(pares)))
    print("")
    print("=" * 76)
    print("3. LOS PARES, UNO A UNO, PARA QUE LA CUENTA SE PUEDA RECONTAR")
    print("=" * 76)
    for numero, (candidato, vecino) in enumerate(pares, 1):
        print("  %2d  %-46s  contra  %s" % (numero, candidato[:46], vecino))


if __name__ == "__main__":
    main()
