# -*- coding: utf-8 -*-
"""Lector del libro que SANEA LOS GUIONES AL ESCRIBIR.

Es el remedio que la `ACTA 25` `11` dejo y que la vuelta 27 volvio a romper: un
instrumento mio que vuelca texto del libro al arbol **sanea al salir**, en el
punto donde se escribe, y no despues con el barrido.
"""
import io, sys, re

def sanear(texto):
    # LOS GUIONES SE CONSTRUYEN POR PUNTO DE CODIGO, NO SE TECLEAN: el barrido de
    # esta casa es sobre el repo ENTERO, y una tabla con el caracter literal
    # dentro tumba el commit del propio instrumento que los sanea. Caida mia de
    # la vuelta 28, y es la segunda vez que este lector la paga.
    for punto, bueno in ((0x2014, " "), (0x2013, " "), (0x2012, " "),
                         (0x2010, "-"), (0x2011, "-"), (0x2212, "-")):
        texto = texto.replace(chr(punto), bueno)
    return texto

def main():
    ruta, desde, hasta = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    salida = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    lineas = io.open(ruta, encoding="utf-8").read().splitlines()
    for n in range(desde, min(hasta, len(lineas)) + 1):
        salida.write("%d: %s\n" % (n, sanear(lineas[n - 1])))
    salida.flush()

main()
