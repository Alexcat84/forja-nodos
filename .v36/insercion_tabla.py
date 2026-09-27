# -*- coding: utf-8 -*-
"""LOS 14 DE cap_10 INSERTADOS. Todo se lee de la salida de las 14 corridas de
`forja.py insertar` guardadas en .v36/informes/, y la cuenta de pasos del fichero
ya archivado en _insertados. Ninguna celda se teclea."""
import json
import os
import re

ORDEN = [
    ("01_desplegar",        "L19"),
    ("02_historia",         "L47"),
    ("03_suenios",          "L61"),
    ("04_dieciocho",        "L77"),
    ("05_plan_anual",       "L93"),
    ("06_contratacion",     "L129"),
    ("07_despido_cabeza",   "L169"),
    ("08_admitir",          "L175"),
    ("09_calibrar_despido", "L181"),
    ("10_sopesar",          "L189"),
    ("11_contactar",        "L197"),
    ("12_ascensos",         "L205"),
    ("13_obsesion",         "L229"),
    ("14_reconocer",        "L239"),
]
ARCHIVO = "cuarentena/_insertados/scott_radical_candor/%s.json"


def uno(patron, texto, por_defecto="0"):
    hallado = re.search(patron, texto)
    return hallado.group(1) if hallado else por_defecto


print("| # | candidato | linea | pasos | nodos tras entrar | levantados | por lectura | aristas |")
print("|---:|---|---:|---:|---:|---:|---:|---:|")
tp = tl = td = ta = tc = 0
for indice, (salida, linea) in enumerate(ORDEN, 1):
    texto = open(os.path.join(".v36", "informes", salida + ".txt"), encoding="utf-8").read()
    nid = re.search(r"candidato '([a-z0-9_]+)'", texto).group(1)
    pasos = len(json.load(open(ARCHIVO % nid, encoding="utf-8"))["pasos_accionables"])
    nodos = uno(r"nodos en el grafo: (\d+)", texto, "?")
    lev = int(uno(r"VECINOS POR ENCIMA DE UMBRAL: (\d+)", texto))
    dec = int(uno(r"DECLARADOS POR LECTURA: (\d+)", texto))
    cab = len(re.findall(r"arista madre-hijo cableada", texto))
    cola = int(uno(r"ARISTAS EN COLA, sin cablear: (\d+)", texto))
    tp += pasos; tl += lev; td += dec; ta += cab; tc += cola
    marca = "%d" % cab
    if cola:
        marca = "%d mas %d EN COLA" % (cab, cola)
    print("| %d | `%s` | %s | %d | **%s** | %d | %d | %s |"
          % (indice, nid, linea, pasos, nodos, lev, dec, marca))
print("| | **TOTAL de `cap_10`** | | **%d** | **316** | **%d** | **%d** | **%d mas %d EN COLA** |"
      % (tp, tl, td, ta, tc))
