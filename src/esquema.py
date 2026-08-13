# -*- coding: utf-8 -*-
"""Validador de JSON Schema minimo, solo con libreria estandar.

Cubre el subconjunto que usa esquema/nodo.schema.json: type, required,
properties, additionalProperties, items, minItems, minLength, pattern,
uniqueItems, enum. No pretende ser un validador general: pretende ser el
validador de ESTE esquema, y fallar ruidosamente si el esquema crece.
"""

import json
import re

from . import comun

TIPOS = {
    "object": dict,
    "array": list,
    "string": str,
    "number": (int, float),
    "integer": int,
    "boolean": bool,
    "null": type(None),
}

CLAVES_CONOCIDAS = {
    "$schema", "$id", "title", "description", "type", "required", "properties",
    "additionalProperties", "items", "minItems", "minLength", "pattern",
    "uniqueItems", "enum", "examples",
}


def _tipo_ok(valor, tipo):
    if tipo == "integer":
        return isinstance(valor, int) and not isinstance(valor, bool)
    if tipo == "number":
        return isinstance(valor, (int, float)) and not isinstance(valor, bool)
    if tipo == "boolean":
        return isinstance(valor, bool)
    esperado = TIPOS.get(tipo)
    if esperado is None:
        raise ValueError("tipo de esquema no soportado: %s" % tipo)
    if tipo != "boolean" and isinstance(valor, bool) and esperado in (int, float):
        return False
    return isinstance(valor, esperado)


def validar(dato, esquema, ruta="$"):
    """Devuelve una lista de fallos legibles. Lista vacia es verde."""
    fallos = []

    desconocidas = set(esquema.keys()) - CLAVES_CONOCIDAS
    if desconocidas:
        raise ValueError("el esquema usa claves que este validador no cubre: %s"
                         % ", ".join(sorted(desconocidas)))

    tipo = esquema.get("type")
    if tipo is not None:
        tipos = tipo if isinstance(tipo, list) else [tipo]
        if not any(_tipo_ok(dato, t) for t in tipos):
            fallos.append("%s: se esperaba %s y llego %s"
                          % (ruta, "/".join(tipos), type(dato).__name__))
            return fallos

    if "enum" in esquema and dato not in esquema["enum"]:
        fallos.append("%s: valor fuera de la lista permitida %s" % (ruta, esquema["enum"]))

    if isinstance(dato, str):
        if "minLength" in esquema and len(dato.strip()) < esquema["minLength"]:
            fallos.append("%s: texto vacio o mas corto de %d caracteres"
                          % (ruta, esquema["minLength"]))
        if "pattern" in esquema and not re.search(esquema["pattern"], dato):
            fallos.append("%s: no cumple el patron %s" % (ruta, esquema["pattern"]))

    if isinstance(dato, list):
        if "minItems" in esquema and len(dato) < esquema["minItems"]:
            fallos.append("%s: necesita al menos %d elementos y trae %d"
                          % (ruta, esquema["minItems"], len(dato)))
        if esquema.get("uniqueItems"):
            vistos = []
            for elemento in dato:
                clave = json.dumps(elemento, sort_keys=True, ensure_ascii=False)
                if clave in vistos:
                    fallos.append("%s: elemento repetido %s" % (ruta, clave))
                vistos.append(clave)
        sub = esquema.get("items")
        if sub:
            for indice, elemento in enumerate(dato):
                fallos.extend(validar(elemento, sub, "%s[%d]" % (ruta, indice)))

    if isinstance(dato, dict):
        propiedades = esquema.get("properties", {})
        for requerida in esquema.get("required", []):
            if requerida not in dato:
                fallos.append("%s: falta el campo obligatorio %s" % (ruta, requerida))
        if esquema.get("additionalProperties") is False:
            for clave in sorted(dato.keys()):
                if clave not in propiedades:
                    fallos.append("%s: campo no previsto en el esquema: %s" % (ruta, clave))
        for clave, subesquema in sorted(propiedades.items()):
            if clave in dato:
                fallos.extend(validar(dato[clave], subesquema, "%s.%s" % (ruta, clave)))

    return fallos


def cargar():
    return comun.leer_json(comun.RUTA_ESQUEMA)
