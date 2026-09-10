# -*- coding: utf-8 -*-
"""EL PREPARADOR DEL ESTRENO EN SECO: deposita un lote ROTULADO en la bandeja (b).

    python calibracion/preparar_ensayo.py [--cuantos 163] [--lote <nombre>]

POR QUE EXISTE, Y POR QUE NO ES MUNDO 11.

El encargo pedia correr la aduana en MODO INFORME sobre los 167 candidatos del
mundo 11 depositados en la bandeja (b). Se fue a buscarlos y NO EXISTEN COMO
CANDIDATOS: `OCR/fuentes/mundo_11/` guarda 163 recortes de capitulo en markdown
de diez libros, mas dos insumos auxiliares, y CERO ficheros de nodo. Un barrido
por `pasos_accionables` en toda esa carpeta devuelve nada. Esos 167 son BANDEJA
(a), libro crudo todavia por extraer, no bandeja (b).

Asi que el estreno se corre igual, pero DICIENDO QUE ES UN ENSAYO, a la misma
escala que el lote real (163) y por la puerta real:

    python forja.py informe --carpeta cuarentena/<lote>

El lote se construye con nodos VIVOS del catalogo limpio de referencia, que es
material auditado por humanos. Eso mide lo que hace falta medir antes de abrir
la puerta: **como se comporta el instrumento con un lote entero delante**,
cuantos entrarian de golpe, cuantos abririan cola de lectura y de que tamaño, y
cuantos caerian y por que guarda.

LO QUE ESTE ENSAYO NO MIDE, y se dice: no mide la calidad de la extraccion del
mundo 11, porque esa extraccion no se ha hecho. Cuando se haga, el mismo comando
sobre `cuarentena/mundo_11/` da el informe de verdad.

LA MORATORIA DE MAQUINARIA (EXTRACTOR.md seccion 13) permite este instrumento
porque una TAREA DEL ENCARGO lo ordena expresamente. No nace de una vuelta.

NO INSERTA NADA. Solo escribe dentro de `cuarentena/`, que git ignora.
"""

import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calibracion import referencia  # noqa: E402
from src import comun  # noqa: E402

SEMILLA_ENSAYO = 20260909
CUANTOS_POR_DEFECTO = 163  # los recortes reales del mundo 11, contados
LOTE_POR_DEFECTO = "ensayo_referencia_163"

AVISO = u"""# ESTO ES UN ENSAYO, NO ES EL MUNDO 11

Este lote lo deposito `calibracion/preparar_ensayo.py` con nodos VIVOS del
catalogo limpio de referencia (tag catalogo-limpio-v1), a la misma escala que
los recortes del mundo 11, para estrenar la aduana en seco.

**Los candidatos de verdad del mundo 11 todavia no existen.** Lo que hay en
`OCR/fuentes/mundo_11/` son 163 recortes de capitulo, que son BANDEJA (a).
Cuando se extraigan, van a `cuarentena/mundo_11/` y se corre el mismo comando.

    python forja.py informe --carpeta cuarentena/%s

Esta carpeta es material de usar y tirar. Borrarla no pierde nada: se
reconstruye con la semilla %d.
""" % (LOTE_POR_DEFECTO, SEMILLA_ENSAYO)


def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos or sys.argv[1:])
    cuantos = CUANTOS_POR_DEFECTO
    lote = LOTE_POR_DEFECTO
    if "--cuantos" in argumentos:
        cuantos = int(argumentos[argumentos.index("--cuantos") + 1])
    if "--lote" in argumentos:
        lote = argumentos[argumentos.index("--lote") + 1]

    datos_corte = referencia.corte()
    ref = referencia.Referencia()
    muestra = ref.muestra_de_vivos(cuantos, SEMILLA_ENSAYO)

    destino = os.path.join(comun.RAIZ, "cuarentena", lote)
    if not os.path.isdir(destino):
        os.makedirs(destino)

    for identificador in muestra:
        ruta = os.path.join(destino, "%s.json" % identificador)
        with io.open(ruta, "w", encoding="utf-8") as fichero:
            json.dump(ref.nodos[identificador], fichero,
                      ensure_ascii=False, indent=2, sort_keys=True)

    comun.escribir_texto(os.path.join(destino, "LEEME.md"), AVISO)

    # La tabla de fuentes DERIVADA del catalogo. Va fuera del lote, para que
    # `--carpeta` no la lea como candidato, y DENTRO de una subcarpeta, porque
    # `.gitignore` ignora `cuarentena/*/` y no los sueltos de su raiz.
    derivadas = os.path.join(comun.RAIZ, "cuarentena", "_derivadas")
    if not os.path.isdir(derivadas):
        os.makedirs(derivadas)
    tabla = os.path.join(derivadas, "FUENTES_DEL_%s.json" % lote)
    comun.escribir_texto(tabla, json.dumps(ref.tabla_de_fuentes(),
                                           ensure_ascii=False, indent=2,
                                           sort_keys=True))

    print("LOTE DE ENSAYO DEPOSITADO EN LA BANDEJA (b)")
    print("  carpeta        : cuarentena/%s" % lote)
    print("  candidatos     : %d" % len(muestra))
    print("  origen         : vivos del grafo de referencia %s (%s)"
          % (datos_corte["commit"][:12], datos_corte["tag"]))
    print("  semilla        : %d" % SEMILLA_ENSAYO)
    print("  tabla derivada : cuarentena/_derivadas/FUENTES_DEL_%s.json" % lote)
    print("")
    print("NO ES EL MUNDO 11. El mundo 11 son 163 recortes de capitulo sin")
    print("extraer, que son bandeja (a). Ver la cabecera de este fichero.")
    print("")
    print("AHORA, EL INFORME (cero inserciones):")
    print("  FORJA_FUENTES=cuarentena/_derivadas/FUENTES_DEL_%s.json \\" % lote)
    print("  python forja.py informe --carpeta cuarentena/%s" % lote)
    return 0


if __name__ == "__main__":
    sys.exit(main())
