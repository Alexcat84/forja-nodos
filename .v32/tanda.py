# -*- coding: utf-8 -*-
"""LA TANDA DE INSERCION DE LA VUELTA 32, CONTADA DE SUS PROPIOS FICHEROS.

Cada fila se lee de la salida que la corrida dejo en `.v32/`, no de la memoria:
el saldo del informe en seco, el veredicto que se escribio, y si el nodo vive hoy
en `dataset/nodos.jsonl` y esta archivado en `cuarentena/_insertados/`.
"""
import io
import json
import os
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

ARCHIVO = "cuarentena/_insertados/scott_radical_candor/%s.json"
BANDEJA = "cuarentena/scott_radical_candor/%s.json"

TANDA = [
    (12, "montar_tablero_kanban_medir_actividades", ".v32/informe_01.txt", ".v32/insertar_01.txt"),
    (13, "pasear_organizacion_hallar_problemas_pequenios", ".v32/informe_02.txt", ".v32/insertar_02.txt"),
    (14, "debatir_decidir_asuntos_cultura_evitar_delegar", ".v32/informe_03.txt", ".v32/insertar_03.txt"),
]

GRAFO = {}
for linea in io.open("dataset/nodos.jsonl", encoding="utf-8"):
    datos = json.loads(linea)
    GRAFO[datos["id"]] = datos

CABEZA = "decidir_quien_comunica_cada_cuanto"
HIJOS = set(GRAFO[CABEZA].get("nodos_siguientes") or [])


def saldo(ruta):
    texto = io.open(ruta, encoding="utf-8").read()
    if "[BLOQUEARIA]" in texto:
        vecinos = texto.count("      similitud_texto")
        return "**BLOQUEARIA**, %d vecino" % vecinos
    if "[ENTRARIA]" in texto:
        return "**ENTRARIA sin leer nada**, 0 vecinos"
    return "**no se pudo leer**"


def nodos_tras(ruta):
    for linea in io.open(ruta, encoding="utf-8"):
        if "nodos en el grafo:" in linea:
            return linea.split(":")[1].strip()
    return "?"


print("| # | id | informe en seco | el grafo tras insertarlo | vive hoy | archivado | arista de cabeza |")
print("|---:|---|---|---:|---|---|---|")
for numero, identificador, informe, insercion in TANDA:
    vive = "**SI**" if identificador in GRAFO else "**NO**"
    archivado = "**SI**" if os.path.exists(ARCHIVO % identificador) else "**NO**"
    en_bandeja = os.path.exists(BANDEJA % identificador)
    if en_bandeja:
        archivado += " **y SIGUE EN BANDEJA**"
    arista = "**CABLEADA hoy**" if identificador in HIJOS else "**no lleva, y se dice por que**"
    print("| %d | `%s` | %s | %s | %s | %s | %s |"
          % (numero, identificador, saldo(informe), nodos_tras(insercion), vive, archivado, arista))

pasos = sum(len(GRAFO[i]["pasos_accionables"]) for _n, i, _a, _b in TANDA if i in GRAFO)
print()
print("| | |")
print("|---|---:|")
print("| corridas de `forja.py informe` de un candidato suelto | **%d** |" % len(TANDA))
print("| corridas de `forja.py insertar`, una por candidato | **%d** |" % len(TANDA))
print("| cargas masivas | **0** |")
print("| nodos que entraron | **%d** |" % sum(1 for _n, i, _a, _b in TANDA if i in GRAFO))
print("| pasos que entraron con ellos | **%d** |" % pasos)
print("| archivados en `cuarentena/_insertados/scott_radical_candor/` | **%d** |"
      % sum(1 for _n, i, _a, _b in TANDA if os.path.exists(ARCHIVO % i)))
print("| aristas de cabeza declaradas en el acto | **%d** |"
      % sum(1 for _n, i, _a, _b in TANDA if i in HIJOS))
