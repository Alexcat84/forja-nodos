# -*- coding: utf-8 -*-
"""Los cuatro hijos del orden de operaciones, contra el grafo de hoy (D.36)."""
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ids = set()
with open(os.path.join(RAIZ, "dataset", "nodos.jsonl"), encoding="utf-8") as f:
    for l in f:
        l = l.strip()
        if l:
            ids.add(json.loads(l)["id"])

CUATRO = [(49, "dar_elogio_disciplina_igual_critica"),
          (50, "criticar_trabajo_evitar_desanimo"),
          (51, "medir_critica_respuesta_oyente_brujula"),
          (52, "fomentar_guia_reciproca_companieros")]

print("LOS CUATRO HIJOS DEL ORDEN DE OPERACIONES, contra el grafo de hoy")
for n, i in CUATRO:
    print("  arista %d  %-50s  %s"
          % (n, i, "DENTRO del grafo" if i in ids else "en la BANDEJA"))
