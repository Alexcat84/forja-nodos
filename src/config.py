# -*- coding: utf-8 -*-
"""Carga de config/umbrales.json.

Los umbrales son editables a mano: son la perilla de la cola de lectura,
no una autoridad. El aviso del manual viaja dentro del propio archivo y
tambien esta escrito en src/aduana.py, donde se usa.
"""

from . import comun

POR_DEFECTO = {
    "umbral_similitud_texto": 0.35,
    "umbral_familia_id": 0.3,
    "umbral_paso_contra_nodo": 0.6,
    "maximo_vecinos_reportados": 25,
    "solo_dominio_y_nucleo": False,
    "dominios_nucleo": [],
}


def cargar(ruta=None):
    valores = dict(POR_DEFECTO)
    try:
        crudo = comun.leer_json(ruta or comun.RUTA_UMBRALES)
    except (IOError, ValueError):
        return valores
    for clave, valor in crudo.items():
        if clave.startswith("_"):
            continue
        valores[clave] = valor
    return valores


def cargar_pares_mutuos(ruta=None):
    """La lista blanca de enlaces mutuos declarados (adjudicacion A.1,
    docs/BANCO_DE_REGLAS.md). El gate solo perdona una vuelta en un par que
    esta lista cubra tras resolver: todo lo demas sigue siendo fallo.
    comun.leer_jsonl ya devuelve lista vacia si el archivo no existe todavia
    (nadie ha declarado un enlace mutuo aun); un jsonl mal formado SI se deja
    romper, para que el fallo se vea en vez de tragarse en silencio."""
    return comun.leer_jsonl(ruta or comun.RUTA_PARES_MUTUOS)
