# -*- coding: utf-8 -*-
"""La correccion de la ficha de la madre de P27 ANIADE y no borra (manual principio 6).
Un `M` de git no lo dice por si solo: hay que comparar el campo contra su version
del commit de apertura. Comparo campo a campo y compruebo que el texto viejo esta
entero dentro del nuevo."""
import json, io, sys, subprocess

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

P = "cuarentena/grove_high_output/transmitir_objetivos_prioridades_preferencias.json"
APERTURA = "327d969"

viejo = json.loads(subprocess.run(["git", "show", APERTURA + ":" + P],
                                  capture_output=True).stdout.decode("utf-8"))
nuevo = json.load(open(P, encoding="utf-8"))

for k in nuevo:
    if viejo.get(k) != nuevo.get(k):
        print("campo que cambia:", k)

a = viejo["resumen_teorico"]
b = nuevo["resumen_teorico"]
print("el texto viejo esta entero dentro del nuevo:", b.startswith(a))
print("largo viejo:", len(a), " largo nuevo:", len(b), " anadido:", len(b) - len(a))
print("LO ANADIDO, literal:")
print("   ", b[len(a):].strip()[:600])
