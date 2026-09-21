# -*- coding: utf-8 -*-
"""LA TABLA DE LA RELECTURA `D.30`, TALLADA DESDE EL DATO.

Las columnas mecanicas (candidato, paso, linea, clase, primeras palabras del paso
y de la linea del libro) **salen del fichero**. La columna del veredicto sale del
diccionario `VEREDICTOS`, que es lo unico que teclea la lectura: un paso que no
figure ahi es `TRANSCRIPCION`, y cada `PUENTE` tiene que traer su motivo escrito.

**LA CUENTA QUE PUBLICA ES LA QUE SALE DE AHI**, no una que yo teclee aparte.
"""
import io
import json
import os
import re
import subprocess
import sys

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIBRO = os.path.join(RAIZ, "fuentes", "scott_radical_candor", "cap_13.md")
LARGO = chr(0x2014)
MEDIO = chr(0x2013)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from clase import ESPECIES  # noqa: E402
from fidelidad import REPARTO  # noqa: E402

# LO UNICO QUE TECLEA LA LECTURA. Clave (candidato, numero de paso).
# Un paso ausente de este diccionario queda TRANSCRIPCION.
VEREDICTOS = {}


def linea(n):
    salida = subprocess.run(["sed", "-n", "%dp" % n, LIBRO], capture_output=True)
    crudo = salida.stdout.decode("utf-8").rstrip("\r\n")
    return crudo.replace(LARGO, "[U+2014]").replace(MEDIO, "[U+2013]")


def cortar(t, n):
    t = " ".join(t.split())
    return t if len(t) <= n else t[:n - 3] + "..."


filas = []
for cid, _rotulo, tramos in REPARTO:
    ruta = os.path.join(RAIZ, "cuarentena", "scott_radical_candor", "%s.json" % cid)
    pasos = json.load(io.open(ruta, encoding="utf-8"))["pasos_accionables"]
    for n, (desde, hasta) in tramos:
        texto_linea = linea(n)
        for i in range(desde, hasta + 1):
            paso = pasos[i - 1]
            especies = [nom for nom, rx in ESPECIES if rx.search(paso)]
            filas.append((cid, i, n, especies, paso, texto_linea))

# LAS COLUMNAS DE TEXTO NO SE REPITEN AQUI A PROPOSITO: el paso entero y la linea
# entera del libro van pegados arriba, en la salida de .v40/fidelidad.py. Esta tabla
# es el LIBRO MAYOR de la relectura, una fila por paso, y lo que aporta es el
# veredicto y la marca de clase.
# LA PRIMERA CELDA LLEVA EL CANDIDATO Y EL PASO JUNTOS, Y NO ES ADORNO: el tallado
# de D.41 casa las filas por su PRIMERA celda, y con el candidato solo hay 58 filas
# que comparten 4 claves. La caida salio en el commit y se arregla dando clave unica
# a cada fila, no tecleando la celda buena.
print("| candidato y paso | linea | de la clase | veredicto |")
print("|---|---:|---|---|")
for cid, i, n, especies, paso, texto_linea in filas:
    v = VEREDICTOS.get((cid, i), "TRANSCRIPCION")
    print("| `%s` `P%02d` | `L%d` | %s | **%s** |"
          % (cid, i, n, ", ".join(especies) if especies else "no", v))

total = len(filas)
puentes = [f for f in filas if VEREDICTOS.get((f[0], f[1]), "TRANSCRIPCION") != "TRANSCRIPCION"]
clase = [f for f in filas if f[3]]
print("")
print("LA CUENTA, SALIDA DE LA MISMA TABLA:")
print("  pasos releidos   : %d" % total)
print("  TRANSCRIPCION    : %d" % (total - len(puentes)))
print("  PUENTE           : %d" % len(puentes))
print("  marcados de la clase por el instrumento: %d de %d" % (len(clase), total))
print("  lineas distintas del libro releidas enteras: %d"
      % len(set(f[2] for f in filas)))
