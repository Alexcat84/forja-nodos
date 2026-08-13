# -*- coding: utf-8 -*-
"""Los censos (manual seccion 3.4 a 3.6 y seccion 7.3).

Serie numerada, caso de estudio, marco legal de un pais, norma con
version, herramienta con URL, cifra de autor y denominaciones se registran
AL ENTRAR, no en una auditoria posterior. Cada censo es una tabla markdown
en censos/ que la aduana amplia con una fila por hecho.
"""

import os
import re

from . import comun

CENSOS = {
    "series_y_cabezas": {
        "titulo": "Censo de series numeradas y cabezas",
        "anclaje": "Manual seccion 3.4: un nodo por paso mas UNA cabeza, jamas dos "
                   "compresiones de la misma numeracion.",
        "columnas": ["fecha", "nodo", "serie", "papel", "cabeza", "fuente", "nota"],
    },
    "casos": {
        "titulo": "Censo de casos y estudios",
        "anclaje": "Manual seccion 3.5: el caso no es la casa. La doctrina vive en su "
                   "nodo y el caso entra como ejemplo nombrado dentro de ella. Señal "
                   "barata: el entregable del caso lleva un dato del caso.",
        "columnas": ["fecha", "nodo", "caso", "nodo_de_doctrina", "fuente", "nota"],
    },
    "marco_pais": {
        "titulo": "Censo de marco legal por pais",
        "anclaje": "Manual seccion 3.6: si cablea marco legal de un pais se registra al "
                   "entrar. Un procedimiento atado a una jurisdiccion no es universal.",
        "columnas": ["fecha", "nodo", "pais", "marco", "fuente", "nota"],
    },
    "vigencia": {
        "titulo": "Censo de vigencias y fechas de corte",
        "anclaje": "Manual principio 5: toda cifra lleva su fecha de corte, y toda glosa "
                   "lleva el corte de la cifra que interpreta.",
        "columnas": ["fecha", "nodo", "norma_o_cifra", "version", "fecha_corte", "fuente", "nota"],
    },
    "herramientas": {
        "titulo": "Censo de herramientas con URL",
        "anclaje": "Manual seccion 3.6: la herramienta con URL se registra al entrar. La "
                   "URL caduca; el censo es lo que permite revisarlas todas de una vez.",
        "columnas": ["fecha", "nodo", "herramienta", "url", "fuente", "nota"],
    },
    "denominaciones": {
        "titulo": "Censo de denominaciones",
        "anclaje": "Manual seccion 3.1 y seccion 5: nombre largo, sigla y termino en otro "
                   "idioma son TRES denominaciones aparte y cada una se registra. El alias "
                   "cubre el id, no la busqueda del lector.",
        "columnas": ["fecha", "nodo", "clase", "denominacion", "idioma", "nota"],
    },
    "atribuciones": {
        "titulo": "Censo de cifras de autor",
        "anclaje": "Manual principio 8: toda atribucion es una afirmacion que se verifica. "
                   "Una cita que admite lo que el citado prohibe es una cita falsa.",
        "columnas": ["fecha", "nodo", "cifra", "autor", "fuente", "fecha_corte"],
    },
}


def ruta(censo):
    return os.path.join(comun.DIR_CENSOS, "%s.md" % censo)


def encabezado(censo):
    ficha = CENSOS[censo]
    lineas = [
        "# %s" % ficha["titulo"],
        "",
        ficha["anclaje"],
        "",
        "Lo escribe la aduana al insertar (src/aduana.py). No se edita a mano salvo "
        "para corregir, y una correccion no borra: declara (manual principio 6).",
        "",
        "| " + " | ".join(ficha["columnas"]) + " |",
        "|" + "|".join(["---"] * len(ficha["columnas"])) + "|",
    ]
    return "\n".join(lineas) + "\n"


def crear_plantillas():
    if not os.path.isdir(comun.DIR_CENSOS):
        os.makedirs(comun.DIR_CENSOS)
    creados = []
    for censo in sorted(CENSOS):
        destino = ruta(censo)
        if not os.path.exists(destino):
            comun.escribir_texto(destino, encabezado(censo))
            creados.append(comun.relativa(destino))
    return creados


def _celda(valor):
    texto = "" if valor is None else str(valor)
    texto = texto.replace("|", "/").replace("\n", " ").strip()
    for guion in comun.GUIONES_PROHIBIDOS:
        texto = texto.replace(guion, "-")
    return texto or "-"


def registrar(censo, fila):
    """Añade una fila al censo. Devuelve la linea escrita."""
    if censo not in CENSOS:
        raise ValueError("censo desconocido: %s" % censo)
    destino = ruta(censo)
    if not os.path.exists(destino):
        crear_plantillas()
    columnas = CENSOS[censo]["columnas"]
    linea = "| " + " | ".join(_celda(fila.get(c)) for c in columnas) + " |"
    texto = comun.leer_texto(destino)
    if not texto.endswith("\n"):
        texto += "\n"
    comun.escribir_texto(destino, texto + linea + "\n")
    return linea


def filas(censo):
    """Lee las filas ya registradas, para poder comprobarlas en las pruebas."""
    destino = ruta(censo)
    if not os.path.exists(destino):
        return []
    columnas = CENSOS[censo]["columnas"]
    salida = []
    for linea in comun.leer_texto(destino).split("\n"):
        linea = linea.strip()
        if not linea.startswith("|") or re.match(r"^\|[\s\-|]+\|$", linea):
            continue
        celdas = [c.strip() for c in linea.strip("|").split("|")]
        if celdas == columnas:
            continue
        if len(celdas) == len(columnas):
            salida.append(dict(zip(columnas, celdas)))
    return salida
