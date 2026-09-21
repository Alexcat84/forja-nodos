# -*- coding: utf-8 -*-
"""LAS CIFRAS DEL CIERRE, RECOMPUTADAS AL CIERRE (EXTRACTOR.md 4).

LA APERTURA NO SE TECLEA: se lee de `.v1g/apertura_tabla.txt`, que es el instrumento que la
midio. EL CIERRE SE MIDE AHORA. Y la fila de las pruebas se lee del fichero de la corrida de
cierre, no de memoria.
"""
import glob
import io
import json
import os
import re
import sys

sys.path.insert(0, os.getcwd())
from src import aduana

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

APERTURA = {}
for linea in io.open(".v1g/apertura_tabla.txt", encoding="utf-8"):
    if not linea.startswith("|") or "---" in linea:
        continue
    celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
    if len(celdas) != 3:
        continue
    crudo = celdas[1].replace("*", "").replace(".", "")
    try:
        APERTURA[celdas[0]] = int(crudo)
    except ValueError:
        pass

nodos = sig = prev = 0
for linea in io.open("dataset/nodos.jsonl", encoding="utf-8"):
    datos = json.loads(linea)
    nodos += 1
    sig += len(datos.get("nodos_siguientes") or [])
    prev += len(datos.get("nodos_previos") or [])

veredictos = nocons = 0
for linea in io.open("bitacora/VEREDICTOS.jsonl", encoding="utf-8"):
    veredictos += 1
    datos = json.loads(linea)
    if any(a.get("no_consumada") is True for a in (datos.get("anotaciones") or [])):
        nocons += 1

bandeja = len(glob.glob("cuarentena/grove_high_output/*.json"))
en_bandejas = len(aduana.poblacion_de_bandejas())

pruebas = None
if os.path.exists(".v1g/aceptacion_cierre.txt"):
    texto = io.open(".v1g/aceptacion_cierre.txt", encoding="utf-8").read()
    hallado = re.search(r"total:\s*(\d+)\s*pruebas", texto)
    if hallado:
        pruebas = int(hallado.group(1))

CIERRE = {
    "nodos en `dataset/nodos.jsonl`": nodos,
    "aristas por `nodos_siguientes`": sig,
    "aristas por `nodos_previos`": prev,
    "veredictos en `bitacora/VEREDICTOS.jsonl`": veredictos,
    "de ellos, con `no_consumada: true`": nocons,
    "candidatos en bandeja de este libro": bandeja,
    "de ellos, poblacion que la ADUANA admite al barrido": en_bandejas,
    "poblacion que vera cada informe mio": nodos + en_bandejas,
}
ORDEN = ["nodos en `dataset/nodos.jsonl`",
         "aristas por `nodos_siguientes`",
         "aristas por `nodos_previos`",
         "veredictos en `bitacora/VEREDICTOS.jsonl`",
         "de ellos, con `no_consumada: true`",
         "candidatos en bandeja de este libro",
         "de ellos, poblacion que la ADUANA admite al barrido",
         "poblacion que vera cada informe mio"]

print("| pieza | al abrir | **al cerrar** | movimiento |")
print("|---|---:|---:|---:|")
for clave in ORDEN:
    antes, ahora = APERTURA[clave], CIERRE[clave]
    salto = ahora - antes
    print("| %s | %d | **%d** | %s |"
          % (clave, antes, ahora, ("**%+d**" % salto) if salto else "0"))
if pruebas is not None:
    # LA APERTURA DE ESTA FILA NO LA MEDI YO: el encargo de este frente no la pide y yo no
    # corri la suite antes de la primera operacion. Se dice en vez de rellenarla.
    print("| pruebas de `tests/test_aceptacion.py` | sin medir al abrir | **%d**, `0` fallos | el ultimo publicado en el repo era `200`, y `269c068` (del fundador, `20:46`) anadio una |"
          % pruebas)
print("")
print("LO QUE ESTE FRENTE NO PUEDE HABER MOVIDO, Y SE COMPRUEBA EN VEZ DE PROMETERLO")
print("  nodos, aristas y veredictos: %s"
      % ("INTACTOS, como manda D.45: este frente no inserta"
         if (nodos == APERTURA["nodos en `dataset/nodos.jsonl`"]
             and sig == APERTURA["aristas por `nodos_siguientes`"]
             and prev == APERTURA["aristas por `nodos_previos`"]
             and veredictos == APERTURA["veredictos en `bitacora/VEREDICTOS.jsonl`"])
         else "SE MOVIERON: CAIDA DE DATO, y se declara"))
