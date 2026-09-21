# -*- coding: utf-8 -*-
"""LOS 14 DE cap_12 Y cap_13 INSERTADOS. Todo se lee de la salida de las 14
corridas de `forja.py insertar` guardadas en .v37/informes/, y la cuenta de pasos
del fichero ya archivado en _insertados. Ninguna celda se teclea."""
import json
import os
import re

ORDEN = [
    ("a01_desplegar_plan",       "cap_12", "L13"),
    ("a02_contar_historias",     "cap_12", "L17"),
    ("b03_mejorar_consciencia",  "cap_13", "L17"),
    ("b04_contar_cuatro",        "cap_13", "L41"),
    ("b05_triangulo",            "cap_13", "L59"),
    ("c06_pedir_critica_primero", "cap_13", "L73"),
    ("c07_elegir_pregunta",      "cap_13", "L115"),
    ("c08_resolver_dudas",       "cap_13", "L167"),
    ("c09_abrazar",              "cap_13", "L187"),
    ("d10_escuchar",             "cap_13", "L199"),
    ("d11_premiar",              "cap_13", "L215"),
    ("d12_integrar",             "cap_13", "L235"),
    ("d13_dar_elogio",           "cap_13", "L247"),
    ("e14_medir_critica",        "cap_13", "L289"),
]
ARCHIVO = "cuarentena/_insertados/scott_radical_candor/%s.json"


def uno(patron, texto, por_defecto="0"):
    hallado = re.search(patron, texto)
    return hallado.group(1) if hallado else por_defecto


print("| # | cap | candidato | linea | pasos | nodos tras entrar | levantados | por lectura | aristas |")
print("|---:|---|---|---:|---:|---:|---:|---:|---:|")
tp = tl = td = ta = tc = 0
ultimo = "?"
for indice, (salida, cap, linea) in enumerate(ORDEN, 1):
    texto = open(os.path.join(".v37", "informes", salida + ".txt"), encoding="utf-8").read()
    nid = re.search(r"candidato '([a-z0-9_]+)'", texto).group(1)
    pasos = len(json.load(open(ARCHIVO % nid, encoding="utf-8"))["pasos_accionables"])
    nodos = uno(r"nodos en el grafo: (\d+)", texto, "?")
    ultimo = nodos
    lev = int(uno(r"VECINOS POR ENCIMA DE UMBRAL: (\d+)", texto))
    dec = int(uno(r"DECLARADOS POR LECTURA: (\d+)", texto))
    cab = len(re.findall(r"arista madre-hijo cableada", texto))
    cola = int(uno(r"ARISTAS EN COLA, sin cablear: (\d+)", texto))
    tp += pasos
    tl += lev
    td += dec
    ta += cab
    tc += cola
    marca = "%d" % cab
    if cola:
        marca = "%d mas %d EN COLA" % (cab, cola)
    print("| %d | `%s` | `%s` | %s | %d | **%s** | %d | %d | %s |"
          % (indice, cap, nid, linea, pasos, nodos, lev, dec, marca))
print("| | | **TOTAL del tramo** | | **%d** | **%s** | **%d** | **%d** | **%d mas %d EN COLA** |"
      % (tp, ultimo, tl, td, ta, tc))
