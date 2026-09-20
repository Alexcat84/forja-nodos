# -*- coding: utf-8 -*-
"""La medicion que sostiene la segunda mitad de la pregunta 11: quitar los dos
U+0008 NO mueve la huella de D.15, asi que no invalida ninguna lectura emitida."""
import json, sys, copy
sys.path.insert(0, ".")
from src import comun
nodo = None
for line in open("dataset/nodos.jsonl", encoding="utf-8"):
    d = json.loads(line)
    if d["id"] == "pedir_critica_primero_crear_seguridad_psicologica":
        nodo = d; break
crudo = nodo.get("titulo", "") + nodo.get("resumen_teorico", "") + "".join(
    p if isinstance(p, str) else json.dumps(p, ensure_ascii=False)
    for p in nodo.get("pasos_accionables", []))
comp = comun.texto_comparable(nodo)
limpio = copy.deepcopy(nodo)
limpio["resumen_teorico"] = limpio["resumen_teorico"].replace("\x08", "")
h1, h2 = comun.huella_de_nodo(nodo), comun.huella_de_nodo(limpio)
print("U+0008 en crudo                  : %d" % crudo.count("\x08"))
print("U+0008 en texto_comparable       : %d        largo comparable %d" % (comp.count("\x08"), len(comp)))
print("huella con los dos controles     : %s" % h1)
print("huella SIN los dos controles     : %s" % h2)
print("cambia la huella al quitarlos?   : %s" % ("SI" if h1 != h2 else "NO"))
