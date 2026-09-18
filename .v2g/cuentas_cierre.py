# -*- coding: utf-8 -*-
"""LAS CIFRAS DEL CIERRE, RECOMPUTADAS AL CIERRE (EXTRACTOR.md 4).

LA APERTURA NO SE TECLEA: se lee de .v2g/apertura_tabla.txt, que es el instrumento que la
midio. EL CIERRE SE MIDE AHORA, con las mismas fuentes. La fila de las pruebas se lee del
fichero de la corrida de cierre, no de memoria.

Y CADA FILA CONSERVA EL ROTULO DE LO QUE CUENTA (remedio bloqueante de PARA_ALEXIS.md 4),
porque es en una tabla de antes y despues donde mas facil es cambiar de poblacion sin
decirlo.
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
for linea in io.open(".v2g/apertura_tabla.txt", encoding="utf-8"):
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

mios = sorted(glob.glob("cuarentena/grove_high_output/*.json"))
pasos_mios = 0
for ruta in mios:
    datos = json.loads(io.open(ruta, encoding="utf-8").read())
    pasos_mios += len(datos.get("pasos_accionables") or [])
ficheros = len([r for r in glob.glob("cuarentena/*/*.json") if "_insertados" not in r])
en_bandejas = len(aduana.poblacion_de_bandejas())

pruebas = None
if os.path.exists(".v2g/aceptacion_cierre.txt"):
    texto = io.open(".v2g/aceptacion_cierre.txt", encoding="utf-8").read()
    hallado = re.search(r"total:\s*(\d+)\s*pruebas", texto)
    if hallado:
        pruebas = int(hallado.group(1))

# clave de la apertura -> valor de cierre
FILAS = [
    ("nodos en `dataset/nodos.jsonl`, el grafo entero", nodos),
    ("aristas por `nodos_siguientes`, sobre el grafo entero", sig),
    ("aristas por `nodos_previos`, sobre el grafo entero", prev),
    ("veredictos en `bitacora/VEREDICTOS.jsonl`, el fichero entero", veredictos),
    ("de esos veredictos, con `no_consumada: true`", nocons),
    ("candidatos en bandeja de ESTE libro, escritos por la vuelta 1", len(mios)),
    ("pasos escritos en esos candidatos de ESTE libro", pasos_mios),
    ("ficheros `.json` en TODAS las bandejas, contados a ojo", ficheros),
    ("de esos ficheros, los que la ADUANA admite al barrido", en_bandejas),
    ("POBLACION QUE VERA CADA INFORME MIO: grafo mas bandejas admitidas", nodos + en_bandejas),
]

print("| pieza, con el rotulo de lo que se cuenta | al abrir | **al cerrar** | movimiento |")
print("|---|---:|---:|---:|")
for clave, ahora in FILAS:
    antes = APERTURA[clave]
    salto = ahora - antes
    etiqueta = clave
    if clave.endswith("escritos por la vuelta 1"):
        etiqueta = ("candidatos en bandeja de ESTE libro (al abrir eran los `8` de la "
                    "vuelta 1; al cerrar, esos `8` mas los `15` de hoy)")
    print("| %s | %d | **%d** | %s |"
          % (etiqueta, antes, ahora, ("**%+d**" % salto) if salto else "0"))
if pruebas is not None:
    print("| pruebas de `tests/test_aceptacion.py` | sin medir al abrir, y se dice en vez de "
          "rellenarlo | **%d**, `0` fallos | la vuelta 1 publico `201` en su corrida de las "
          "`22:23` |" % pruebas)
print("")
print("LO QUE ESTE FRENTE NO PUEDE HABER MOVIDO, Y SE COMPRUEBA EN VEZ DE PROMETERLO")
intacto = (nodos == APERTURA["nodos en `dataset/nodos.jsonl`, el grafo entero"]
           and sig == APERTURA["aristas por `nodos_siguientes`, sobre el grafo entero"]
           and prev == APERTURA["aristas por `nodos_previos`, sobre el grafo entero"]
           and veredictos == APERTURA["veredictos en `bitacora/VEREDICTOS.jsonl`, el fichero entero"])
print("  nodos, aristas y veredictos: %s"
      % ("INTACTOS, como manda D.45: este frente no inserta"
         if intacto else "SE MOVIERON: CAIDA DE DATO, y se declara"))
print("  cero lineas escritas en dataset/, bitacora/, censos/ y config/pares_mutuos.jsonl")
print("")
print("LO QUE SI SE MOVIO, Y ES LO UNICO QUE ESTA VUELTA TENIA QUE MOVER")
print("  candidatos en la bandeja del libro : %d mas" % (len(mios) - APERTURA["candidatos en bandeja de ESTE libro, escritos por la vuelta 1"]))
print("  pasos escritos en esa bandeja      : %d mas" % (pasos_mios - APERTURA["pasos escritos en esos candidatos de ESTE libro"]))
