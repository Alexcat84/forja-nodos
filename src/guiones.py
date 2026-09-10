# -*- coding: utf-8 -*-
"""El barrido de guiones: hook de estilo de la casa (manual seccion 2).

Cero guiones largos y cero guiones medios en TODO el repo. El guion corto
normal es legal. Lo corre el pre-commit y lo corre el gate sobre los textos
de los nodos.
"""

import os

from . import comun

EXTENSIONES_DE_TEXTO = {
    ".md", ".py", ".json", ".jsonl", ".txt", ".sh", ".yml", ".yaml", ".cfg", ".toml", ""
}


def barrer_texto(texto, etiqueta):
    return ["%s linea %d columna %d: %s"
            % (etiqueta, linea, columna, comun.nombrar_guion(caracter))
            for linea, columna, caracter, nombre in comun.buscar_guiones(texto)]


def barrer_archivo(ruta):
    try:
        texto = comun.leer_texto(ruta)
    except (UnicodeDecodeError, IOError):
        return []
    return barrer_texto(texto, comun.relativa(ruta))


def barrer_repo(raiz=None, rutas=None):
    """Devuelve la lista de hallazgos. Lista vacia es verde."""
    if rutas is None:
        rutas = [r for r in comun.archivos_del_repo(raiz)
                 if os.path.splitext(r)[1].lower() in EXTENSIONES_DE_TEXTO]
    hallazgos = []
    for ruta in rutas:
        hallazgos.extend(barrer_archivo(ruta))
    return hallazgos


def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos or [])
    rutas = [a for a in argumentos if not a.startswith("--")] or None
    hallazgos = barrer_repo(rutas=rutas)
    if hallazgos:
        print("BARRIDO DE GUIONES EN ROJO: %d hallazgo(s)" % len(hallazgos))
        for hallazgo in hallazgos:
            print("  " + hallazgo)
        print("Regla: cero guiones largos y cero guiones medios en todo el repo "
              "(manual seccion 2). Usa el guion corto normal.")
        return 1
    print("BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.")
    return 0
