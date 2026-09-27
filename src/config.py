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
    romper, para que el fallo se vea en vez de tragarse en silencio.

    LA CABECERA NO ES UNA CITA (11 sep 2026, decision del fundador 5.7). El
    fichero nace vacio, con una linea que dice que es y para que sirve, porque
    una sede que no existe y una sede vacia se parecen demasiado: la primera
    hace dudar de si el protocolo la lee, y la segunda no. Esa linea lleva
    todas sus claves con guion bajo delante, que es la misma convencion que ya
    usan fuentes/FUENTES_CANONICAS.json y los ficheros de candidato, y aqui se
    SALTA: sin esto el gate y el bloque de vigencia la tomarian por un par sin
    huellas y cantarian un fallo que no existe."""
    filas = comun.leer_jsonl(ruta or comun.RUTA_PARES_MUTUOS)
    return [f for f in filas
            if not (isinstance(f, dict) and f
                    and all(str(c).startswith("_") for c in f))]
