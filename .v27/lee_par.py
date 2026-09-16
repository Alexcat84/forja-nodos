# -*- coding: utf-8 -*-
"""Imprime los pasos ENTEROS de los dos lados de un par. HEREDADO 3 punto 1:
una arista se decide con los dos lados impresos, no con la madre sola."""
import io, json, os, sys
sys.path.insert(0, os.path.abspath("."))
from src import informe

def cargar():
    por = {}
    for l in io.open("dataset/nodos.jsonl", encoding="utf-8"):
        if l.strip():
            d = json.loads(l); por[d["id"]] = ("GRAFO", d)
    for d in informe.poblacion_de_bandejas():
        por.setdefault(d.get("id"), ("BANDEJA", d))
    return por

POR = cargar()

def muestra(i):
    if i not in POR:
        print("!! %s NO ESTA" % i); return
    sede, d = POR[i]
    print("=" * 78)
    print("%s   [%s]" % (i, sede))
    print("  nombre_largo : %s" % d.get("denominaciones", {}).get("nombre_largo", ""))
    print("  activacion   : %s" % d.get("condiciones_activacion", ""))
    print("  entregable   : %s" % d.get("entregable_esperado", ""))
    fu = d.get("fuentes", [{}])[0]
    print("  fuente       : %s" % fu.get("clave", ""))
    for c in d.get("citas", []) or []:
        print("  cita         : %s" % json.dumps(c, ensure_ascii=False))
    print("  PASOS (%d):" % len(d.get("pasos_accionables", [])))
    for n, p in enumerate(d.get("pasos_accionables", []), 1):
        print("   %2d. %s" % (n, p))
    print("  previos    : %s" % d.get("nodos_previos"))
    print("  siguientes : %s" % d.get("nodos_siguientes"))

for i in sys.argv[1:]:
    muestra(i)
