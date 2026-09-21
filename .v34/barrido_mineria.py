# -*- coding: utf-8 -*-
"""ENCARGO V34 2.b: BARRIDO DEL DATASET ENTERO buscando nodos que afirmen
ESTADO DE MINERIA (el estado de la campania) dentro de su propio texto.

Un nodo describe CONOCIMIENTO, no el estado de la campania. La familia se busca
por patron sobre TODO campo de texto del nodo, y cada coincidencia se publica
con su CAMPO y su frase, para que quien relea separe el falso positivo del
ejemplar: un barrido que solo se cuenta cuando encuentra algo no es un barrido.
"""
import io, re, sys
sys.path.insert(0, ".")
from src import comun

PATRONES = [
    ("no estan minados",      r"\bno\s+est[ae]n?\s+minad"),
    ("sin minar",             r"\bsin\s+minar\b"),
    ("pendiente de minar",    r"\bpendiente[s]?\s+de\s+minar\b"),
    ("por minar",             r"\b(por|falta[n]?\s+por)\s+minar\b"),
    ("minado / minar / mineria", r"\b(minad[oa]s?|minar|mineria)\b"),
    ("queda por extraer",     r"\bqueda[n]?\s+por\s+extraer\b"),
    ("sin extraer",           r"\bsin\s+extraer\b"),
    ("pendiente de extraccion", r"\b(pendiente[s]?\s+de\s+extra|extraccion\s+pendiente)"),
    ("no extraido",           r"\bno\s+(se\s+ha\s+)?extraid"),
    ("en bandeja",            r"\ben\s+bandeja\b"),
    ("en cuarentena",         r"\ben\s+cuarentena\b"),
    ("sin insertar / no insertado", r"\b(sin\s+insertar|no\s+insertad|pendiente[s]?\s+de\s+inserc)"),
    ("lote abierto / lote N", r"\blote\s+(abierto|cerrado|\d)"),
    ("ruta de cuarentena",    r"\bcuarentena/"),
]
RX = [(n, re.compile(p, re.I)) for n, p in PATRONES]


def textos(n):
    """Todo campo de texto del nodo, con su nombre, incluidos los anidados."""
    for k, v in n.items():
        if isinstance(v, str):
            yield k, v
        elif isinstance(v, list):
            for i, e in enumerate(v):
                if isinstance(e, str):
                    yield "%s[%d]" % (k, i), e
                elif isinstance(e, dict):
                    for k2, v2 in e.items():
                        if isinstance(v2, str):
                            yield "%s[%d].%s" % (k, i, k2), v2
        elif isinstance(v, dict):
            for k2, v2 in v.items():
                if isinstance(v2, str):
                    yield "%s.%s" % (k, k2), v2
                elif isinstance(v2, list):
                    for i, e in enumerate(v2):
                        if isinstance(e, str):
                            yield "%s.%s[%d]" % (k, k2, i), e


nodos = comun.leer_jsonl(comun.RUTA_DATASET)
hits = []
for n in nodos:
    for campo, txt in textos(n):
        for nombre, rx in RX:
            m = rx.search(txt)
            if m:
                ini = max(0, m.start() - 105)
                fin = min(len(txt), m.end() + 105)
                hits.append((n["id"], campo, nombre, txt[ini:fin]))

print("BARRIDO: nodos que afirman ESTADO DE MINERIA dentro de su texto")
print("  poblacion : %d nodos de dataset/nodos.jsonl (el arbol entero, sin filtrar)"
      % len(nodos))
print("  patrones  : %d de la familia" % len(PATRONES))
print("  campos    : TODO campo de texto del nodo, incluidos los anidados")
print("-" * 78)
for nid, campo, nombre, frase in hits:
    print("NODO  %s" % nid)
    print("  campo  : %s" % campo)
    print("  patron : %s" % nombre)
    print("  frase  : ...%s..." % frase)
    print()
print("-" * 78)
print("coincidencias : %d" % len(hits))
print("nodos tocados : %d de %d" % (len(set(h[0] for h in hits)), len(nodos)))
