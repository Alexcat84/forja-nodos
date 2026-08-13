# -*- coding: utf-8 -*-
"""Carga de config/umbrales.json.

Los umbrales son editables a mano: son la perilla de la cola de lectura,
no una autoridad. El aviso del manual viaja dentro del propio archivo y
tambien esta escrito en src/aduana.py, donde se usa.
"""

from . import comun

POR_DEFECTO = {
    "umbral_similitud_texto": 0.45,
    "umbral_familia_id": 0.5,
    "umbral_paso_contra_nodo": 0.55,
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
