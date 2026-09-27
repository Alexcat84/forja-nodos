# -*- coding: utf-8 -*-
"""LA MORATORIA DE MAQUINARIA, MEDIDA Y NO SUPUESTA.

El reporte declara reusar .v58ext/frontera.py sin tocar su maquinaria de medir.
Un diff de texto no lo prueba, porque la tabla de tramos y el docstring cambian
por diseno. Lo que hay que comparar son las FUNCIONES, y eso se hace por arbol
sintactico: se extrae cada def y cada class de los dos ficheros y se comparan.
"""

import ast
import io
import sys


def funciones(ruta):
    fuente = io.open(ruta, encoding="utf-8").read()
    arbol = ast.parse(fuente)
    trozos = []
    for nodo in arbol.body:
        if isinstance(nodo, (ast.FunctionDef, ast.ClassDef)):
            trozos.append(ast.get_source_segment(fuente, nodo))
    return trozos


def main():
    uno, otro = sys.argv[1], sys.argv[2]
    a, b = funciones(uno), funciones(otro)
    print("%s: %d funciones/clases" % (uno, len(a)))
    print("%s: %d funciones/clases" % (otro, len(b)))
    if a == b:
        print("LAS FUNCIONES QUE MIDEN: IDENTICAS, ni una linea")
    else:
        print("LAS FUNCIONES QUE MIDEN: DIFIEREN")
        for i, (x, y) in enumerate(zip(a, b)):
            if x != y:
                print("  difiere la %d" % i)


if __name__ == "__main__":
    main()
