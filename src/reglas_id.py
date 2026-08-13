# -*- coding: utf-8 -*-
"""Reglas de id escritas y ejecutables (manual seccion 2).

La version en prosa, con ejemplos validos e invalidos, vive en
docs/REGLAS_DE_ID.md. Este modulo es la misma ley en codigo: si las dos
se separan, manda el documento y este archivo esta roto.
"""

import re

from . import comun

PATRON = re.compile(r"^[a-z][a-z0-9_]*$")

# Preposiciones y articulos: prohibidos como pieza de un id.
PALABRAS_VACIAS = {
    "a", "al", "ante", "bajo", "con", "contra", "de", "del", "desde", "durante",
    "el", "en", "entre", "hacia", "hasta", "la", "las", "lo", "los", "mediante",
    "para", "por", "que", "segun", "sin", "so", "sobre", "tras", "un", "una",
    "unas", "unos", "y", "o", "u", "e",
}

# Lexico ajeno al castellano que aparece con mas frecuencia en esta forja.
# Un solo idioma en los ids: el termino en otro idioma viaja como
# denominacion (manual seccion 3.1), jamas como id paralelo.
LEXICO_AJENO = {
    "and", "audit", "book", "chapter", "check", "data", "edge", "extract",
    "extraction", "for", "framework", "gate", "graph", "guide", "knowledge",
    "loop", "merge", "node", "nodes", "of", "pipeline", "process", "review",
    "rule", "rules", "schema", "scope", "source", "sources", "step", "steps",
    "the", "to", "tool", "tools", "with", "workflow",
}


def piezas(identificador):
    return [p for p in identificador.split("_") if p]


def familia(identificador):
    """Clave de familia de un id (señal 2 de la aduana y guarda del gate).

    Normaliza sufijos numericos, preposiciones, articulos, plurales y el
    orden de las palabras. Dos ids con la misma clave son la misma familia:
    o son el mismo nodo, o merecen revision antes de existir.
    """
    piezas_normalizadas = set()
    for pieza in piezas(comun.normalizar_texto(identificador.replace("_", " ")).replace(" ", "_")):
        pieza = re.sub(r"\d+$", "", pieza)
        if not pieza or pieza in PALABRAS_VACIAS:
            continue
        # Plural y singular han de caer en la MISMA pieza. Se quita la ese
        # final y despues la e final, en ese orden: asi 'fuentes' y 'fuente'
        # dan los dos 'fuent', que es lo unico que importa aqui. Si solo se
        # quitara la ese, 'fuentes' daria 'fuente' y 'fuente' daria 'fuente'
        # en unos casos y 'fuent' en otros, y la familia dejaria de agrupar.
        if len(pieza) > 3 and pieza.endswith("s"):
            pieza = pieza[:-1]
        if len(pieza) > 4 and pieza.endswith("e"):
            pieza = pieza[:-1]
        if pieza:
            piezas_normalizadas.add(pieza)
    return frozenset(piezas_normalizadas)


def similitud_familia(id_a, id_b):
    familia_a, familia_b = familia(id_a), familia(id_b)
    if not familia_a or not familia_b:
        return 0.0
    interseccion = len(familia_a & familia_b)
    union = len(familia_a | familia_b)
    return float(interseccion) / float(union)


def validar(identificador, campo="id", es_alias=False):
    """Devuelve la lista de fallos del id. Lista vacia es verde.

    Los ids_alias son ids MUERTOS: se les exige forma (snake_case, sin
    rayas) pero no doctrina (un alias existe justamente porque alguna vez
    se escribio mal). Al id canonico se le exige todo.
    """
    fallos = []
    if not isinstance(identificador, str) or not identificador:
        return ["%s: id vacio" % campo]
    if not PATRON.match(identificador):
        fallos.append("%s '%s': solo minusculas, digitos y guion bajo, empezando por letra"
                      % (campo, identificador))
        return fallos
    if "__" in identificador:
        fallos.append("%s '%s': guion bajo doble" % (campo, identificador))
    if es_alias:
        return fallos
    trozos = piezas(identificador)
    if re.search(r"_\d+$", identificador):
        fallos.append("%s '%s': sufijo numerico prohibido (regla 2 de docs/REGLAS_DE_ID.md)"
                      % (campo, identificador))
    vacias = [t for t in trozos if t in PALABRAS_VACIAS]
    if vacias:
        fallos.append("%s '%s': preposicion o articulo prohibido: %s (regla 3)"
                      % (campo, identificador, ", ".join(sorted(set(vacias)))))
    ajenas = [t for t in trozos if t in LEXICO_AJENO]
    if ajenas:
        fallos.append("%s '%s': palabra fuera del castellano: %s (regla 1). "
                      "El termino en otro idioma va en denominaciones.otros_idiomas"
                      % (campo, identificador, ", ".join(sorted(set(ajenas)))))
    if len(trozos) < 2:
        fallos.append("%s '%s': un id nombra un procedimiento, no una palabra suelta "
                      "(regla 5: verbo mas objeto)" % (campo, identificador))
    return fallos


def normalizar(bruto):
    """Lleva un id de entrada humana a la forma de la casa.

    No inventa doctrina: baja a minusculas, quita acentos, convierte
    espacios y rayas en guion bajo. Si despues de eso el id sigue
    rompiendo una regla, la aduana lo rechaza en vez de maquillarlo.
    """
    texto = comun.sin_acentos((bruto or "").strip().lower())
    for guion in comun.GUIONES_PROHIBIDOS:
        texto = texto.replace(guion, "_")
    texto = texto.replace("-", "_")
    texto = re.sub(r"[^a-z0-9_]+", "_", texto)
    texto = re.sub(r"_+", "_", texto)
    return texto.strip("_")
