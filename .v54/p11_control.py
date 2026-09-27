# -*- coding: utf-8 -*-
"""EL EJEMPLAR DE LA PREGUNTA 11, PUESTO DELANTE Y NO CITADO DE MEMORIA.

Barre dataset/nodos.jsonl y cuarentena/ buscando CARACTERES DE CONTROL dentro
de los campos ya escritos: lo que la pregunta 11 llama un defecto de dato que
no es cifra falsa ni veredicto mal puesto.

Imprime la cuenta con su numerador y su denominador NOMBRADOS (D.59).

    python .v54/p11_control.py
"""
import json
import os
import sys
import unicodedata

# Control de C0 y C1, menos los tres que un texto normal si puede llevar.
PERMITIDOS = ("\t", "\n", "\r")


def sospechosos(texto):
    malos = []
    for posicion, letra in enumerate(texto):
        if letra in PERMITIDOS:
            continue
        if unicodedata.category(letra) == "Cc" or letra in ("​", "﻿"):
            malos.append((posicion, letra))
    return malos


def barrer_json(ruta, obj, encontrados):
    def hundir(nodo, camino):
        if isinstance(nodo, dict):
            for clave, valor in nodo.items():
                hundir(valor, camino + "." + str(clave))
        elif isinstance(nodo, list):
            for indice, valor in enumerate(nodo):
                hundir(valor, camino + "[%d]" % indice)
        elif isinstance(nodo, str):
            for posicion, letra in sospechosos(nodo):
                encontrados.append((ruta, camino, posicion,
                                    "U+%04X" % ord(letra)))
    hundir(obj, "")


def main():
    encontrados = []
    campos = 0
    nodos = 0

    ruta = os.path.join("dataset", "nodos.jsonl")
    with open(ruta, encoding="utf-8") as mano:
        for cruda in mano:
            if not cruda.strip():
                continue
            nodos += 1
            obj = json.loads(cruda)
            campos += 1
            barrer_json("%s:%s" % (ruta, obj.get("id")), obj, encontrados)

    fichas = 0
    for base, _, nombres in os.walk("cuarentena"):
        if "_derivadas" in base:
            continue
        for nombre in sorted(nombres):
            if not nombre.endswith(".json"):
                continue
            entera = os.path.join(base, nombre)
            fichas += 1
            with open(entera, encoding="utf-8") as mano:
                barrer_json(entera, json.load(mano), encontrados)

    print("BARRIDO DE CARACTERES DE CONTROL (pregunta 11 de la cola de doctrina)")
    print("  nodos del grafo barridos              : %d  (lineas de %s)" % (nodos, ruta))
    print("  fichas de cuarentena barridas         : %d  (ficheros .json bajo cuarentena/)" % fichas)
    print("  caracteres de control ENCONTRADOS     : %d" % len(encontrados))
    print("    numerador   %d  cadenas con un caracter de control dentro" % len(encontrados))
    print("    denominador %d  documentos barridos (nodos del grafo mas fichas de cuarentena)"
          % (nodos + fichas))
    for fila in encontrados:
        print("    %s  campo %s  posicion %d  %s" % fila)
    if not encontrados:
        print("    (ninguno: el barrido no devuelve una sola coincidencia)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
