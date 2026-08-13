# -*- coding: utf-8 -*-
"""Utilidades comunes de la forja.

Anclaje: manual seccion 2 (fase cero). Aqui viven las piezas que usan el
resolutor, el gate y la aduana, para que ninguna tenga su propia version.
"""

import io
import json
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _ruta(variable, *piezas):
    """Ruta del repo, con sobreescritura por variable de entorno.

    La prueba de aceptacion corre la forja ENTERA (la aduana de verdad, el
    gate de verdad, el hook de verdad) contra un dataset de usar y tirar:
    sin esto habria que probar una copia del sistema, y una copia no
    guarda nada.
    """
    return os.environ.get(variable) or os.path.join(RAIZ, *piezas)


RUTA_ESQUEMA = _ruta("FORJA_ESQUEMA", "esquema", "nodo.schema.json")
RUTA_FUENTES = _ruta("FORJA_FUENTES", "fuentes", "FUENTES_CANONICAS.json")
RUTA_DATASET = _ruta("FORJA_DATASET", "dataset", "nodos.jsonl")
RUTA_VEREDICTOS = _ruta("FORJA_VEREDICTOS", "bitacora", "VEREDICTOS.jsonl")
RUTA_UMBRALES = _ruta("FORJA_UMBRALES", "config", "umbrales.json")
RUTA_PARES_MUTUOS = _ruta("FORJA_PARES_MUTUOS", "config", "pares_mutuos.jsonl")
DIR_CENSOS = _ruta("FORJA_CENSOS", "censos")

# Manual seccion 2: hook de estilo de la casa. Guion largo y guion medio y
# toda la familia de rayas tipograficas quedan prohibidos en TODO el repo.
# El guion corto normal (0x2D) es legal.
# Se escriben con escape unicode a proposito: si este archivo llevara los
# caracteres literales, el propio barrido tendria que dejarse pasar a si
# mismo, y una guarda con excepciones deja de ser una guarda.
GUIONES_PROHIBIDOS = {
    "\u2010": "guion tipografico",
    "\u2011": "guion corto sin corte",
    "\u2012": "guion de cifras",
    "\u2013": "guion medio",
    "\u2014": "guion largo",
    "\u2015": "raya horizontal",
    "\u2212": "signo menos",
    "\ufe58": "guion largo compatibilidad",
    "\ufe63": "guion corto compatibilidad",
    "\uff0d": "guion ancho completo",
}


def salida_utf8():
    """La consola de Windows llega en cp1252 y parte los acentos."""
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8")
        except Exception:
            pass


def leer_texto(ruta):
    with io.open(ruta, "r", encoding="utf-8") as f:
        return f.read()


def escribir_texto(ruta, texto):
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def leer_json(ruta):
    return json.loads(leer_texto(ruta))


def leer_jsonl(ruta):
    if not os.path.exists(ruta):
        return []
    filas = []
    with io.open(ruta, "r", encoding="utf-8") as f:
        for numero, linea in enumerate(f, 1):
            linea = linea.strip()
            if not linea:
                continue
            try:
                filas.append(json.loads(linea))
            except ValueError as error:
                raise ValueError("linea %d de %s ilegible: %s" % (numero, ruta, error))
    return filas


def escribir_jsonl(ruta, filas):
    partes = [json.dumps(fila, ensure_ascii=False, sort_keys=True) for fila in filas]
    escribir_texto(ruta, "\n".join(partes) + ("\n" if partes else ""))


def agregar_jsonl(ruta, fila):
    carpeta = os.path.dirname(ruta)
    if carpeta and not os.path.isdir(carpeta):
        os.makedirs(carpeta)
    with io.open(ruta, "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(fila, ensure_ascii=False, sort_keys=True) + "\n")


def sin_acentos(texto):
    descompuesto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in descompuesto if unicodedata.category(c) != "Mn")


def normalizar_texto(texto):
    """Minusculas, sin acentos, sin puntuacion, espacios colapsados."""
    texto = sin_acentos(texto or "").lower()
    texto = re.sub(r"[^a-z0-9\s]+", " ", texto)
    return re.sub(r"\s+", " ", texto).strip()


def palabras(texto):
    return [p for p in normalizar_texto(texto).split(" ") if p]


def buscar_guiones(texto):
    """Devuelve [(linea, columna, caracter, nombre)] de guiones prohibidos."""
    hallazgos = []
    for numero, linea in enumerate(texto.split("\n"), 1):
        for columna, caracter in enumerate(linea, 1):
            if caracter in GUIONES_PROHIBIDOS:
                hallazgos.append((numero, columna, caracter, GUIONES_PROHIBIDOS[caracter]))
    return hallazgos


def textos_de_nodo(nodo):
    """Todos los campos de texto libre de un nodo, para barridos."""
    campos = []
    for clave in ("id", "titulo", "resumen_teorico", "condiciones_activacion",
                  "entregable_esperado", "dominio", "escala_minima", "marco_pais",
                  "vigencia"):
        valor = nodo.get(clave)
        if isinstance(valor, str):
            campos.append((clave, valor))
    for indice, paso in enumerate(nodo.get("pasos_accionables") or []):
        if isinstance(paso, str):
            campos.append(("pasos_accionables[%d]" % indice, paso))
    denominaciones = nodo.get("denominaciones") or {}
    for clave in ("nombre_largo", "sigla"):
        valor = denominaciones.get(clave)
        if isinstance(valor, str):
            campos.append(("denominaciones.%s" % clave, valor))
    for indice, otro in enumerate(denominaciones.get("otros_idiomas") or []):
        if isinstance(otro, dict):
            for subclave, valor in sorted(otro.items()):
                if isinstance(valor, str):
                    campos.append(("denominaciones.otros_idiomas[%d].%s" % (indice, subclave), valor))
    for indice, atribucion in enumerate(nodo.get("atribuciones") or []):
        if isinstance(atribucion, dict):
            for subclave, valor in sorted(atribucion.items()):
                if isinstance(valor, str):
                    campos.append(("atribuciones[%d].%s" % (indice, subclave), valor))
    return campos


def texto_comparable(nodo):
    """Titulo mas resumen mas pasos: el texto que mira la señal 1."""
    piezas = [nodo.get("titulo") or "", nodo.get("resumen_teorico") or ""]
    piezas.extend(nodo.get("pasos_accionables") or [])
    return normalizar_texto(" ".join(piezas))


def archivos_del_repo(raiz=None, extensiones=None):
    """Recorre el arbol de trabajo saltando .git y cachés."""
    raiz = raiz or RAIZ
    saltar = {".git", "__pycache__", ".pytest_cache", ".venv", "node_modules"}
    encontrados = []
    for carpeta, subcarpetas, ficheros in os.walk(raiz):
        subcarpetas[:] = [s for s in subcarpetas if s not in saltar]
        for fichero in ficheros:
            ruta = os.path.join(carpeta, fichero)
            if extensiones is not None:
                if os.path.splitext(fichero)[1].lower() not in extensiones:
                    continue
            encontrados.append(ruta)
    return sorted(encontrados)


def relativa(ruta):
    try:
        return os.path.relpath(ruta, RAIZ).replace("\\", "/")
    except ValueError:
        return ruta
