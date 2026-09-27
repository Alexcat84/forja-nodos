# -*- coding: utf-8 -*-
"""Huella de texto (comun.huella_de_nodo, la de D.15) de una ficha de bandeja en un commit y hoy."""
import io, os, subprocess, sys, json
sys.path.insert(0, os.getcwd())
from src import comun, aduana
commit, ruta = sys.argv[1], sys.argv[2]
antes = json.loads(subprocess.run(["git", "show", "%s:%s" % (commit, ruta)], capture_output=True, text=True, encoding="utf-8").stdout)
for nombre, bruto in (("en " + commit, antes), ("hoy", comun.leer_json(ruta))):
    c, _ = aduana.normalizar_candidato(bruto)
    print("%-12s %s" % (nombre, comun.huella_de_nodo(c)))
