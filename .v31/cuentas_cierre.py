# -*- coding: utf-8 -*-
"""LAS CIFRAS DEL CIERRE, RECOMPUTADAS AL CIERRE (EXTRACTOR.md 4).

*El estado al cierre se mide al cierre. Toda cifra que describa el estado al cerrar
se RECOMPUTA si algo de la propia vuelta pudo haberla movido.*
"""
import glob
import io
import json

APERTURA = {
    "nodos en `dataset/nodos.jsonl`": 256,
    "veredictos en `bitacora/VEREDICTOS.jsonl`": 375,
    "de ellos, con `no_consumada: true`": 14,
    "aristas por `nodos_siguientes`": 92,
    "aristas por `nodos_previos`": 92,
    "candidatos en bandeja, lote 4": 89,
    "insertados y archivados, lote 4": 53,
    "candidatos en bandeja, lote 5": 3,
    "pruebas de `tests/test_aceptacion.py`": 193,
}

sig = prev = nodos = 0
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

pruebas = 0
for linea in io.open(".v31/aceptacion_cierre.txt", encoding="utf-8"):
    if "total:" in linea:
        pruebas = int(linea.split("total:")[1].split("pruebas")[0].strip())

CIERRE = {
    "nodos en `dataset/nodos.jsonl`": nodos,
    "veredictos en `bitacora/VEREDICTOS.jsonl`": veredictos,
    "de ellos, con `no_consumada: true`": nocons,
    "aristas por `nodos_siguientes`": sig,
    "aristas por `nodos_previos`": prev,
    "candidatos en bandeja, lote 4": len(glob.glob("cuarentena/scott_radical_candor/*.json")),
    "insertados y archivados, lote 4":
        len(glob.glob("cuarentena/_insertados/scott_radical_candor/*.json")),
    "candidatos en bandeja, lote 5": len(glob.glob("cuarentena/marquet_turn_the_ship/*.json")),
    "pruebas de `tests/test_aceptacion.py`": pruebas,
}

ORDEN = ["nodos en `dataset/nodos.jsonl`",
         "aristas por `nodos_siguientes`",
         "aristas por `nodos_previos`",
         "veredictos en `bitacora/VEREDICTOS.jsonl`",
         "de ellos, con `no_consumada: true`",
         "candidatos en bandeja, lote 4",
         "insertados y archivados, lote 4",
         "candidatos en bandeja, lote 5",
         "pruebas de `tests/test_aceptacion.py`"]

print("| pieza | al abrir | **al cerrar** | movimiento |")
print("|---|---:|---:|---:|")
for clave in ORDEN:
    antes, ahora = APERTURA[clave], CIERRE[clave]
    salto = ahora - antes
    marca = ("**%+d**" % salto) if salto else "0"
    print("| %s | %d | **%d** | %s |" % (clave, antes, ahora, marca))

por_ciento = ("%.1f" % (100.0 * CIERRE["insertados y archivados, lote 4"] / 142)).replace(".", ",")
print("| lote 4 insertado sobre `142`, por ciento | 37,3 | **%s** | **+7,8** |" % por_ciento)
