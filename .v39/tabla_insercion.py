# -*- coding: utf-8 -*-
"""La tabla de la TAREA 3, tallada de los informes de la propia aduana (D.41).

Una fila por candidato: los vecinos que la aduana levanto, cuantos veredictos quedaron
escritos, que aristas se cablearon y cuales quedaron en cola, y cuantos nodos habia en
el grafo al salir. NADA de esto se teclea: se lee de .v39/informes/.
"""
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORDEN = [
    ("1", "i01_pedir_critica_primero.txt",
     "pedir_critica_primero_crear_seguridad_psicologica", "L73"),
    ("2", "i02_elegir_pregunta.txt",
     "elegir_pregunta_recurrente_pedir_critica", "L115"),
    ("3", "i03_resolver_dudas.txt",
     "resolver_dudas_frecuentes_pedir_critica", "L167"),
]

print("| # | candidato | linea | vecinos | declarados | aristas cableadas | en cola | nodos al salir | codigo |")
print("|---:|---|---:|---:|---:|---:|---:|---:|---|")
for n, fichero, cid, linea in ORDEN:
    ruta = os.path.join(RAIZ, ".v39", "informes", fichero)
    if not os.path.exists(ruta):
        print("| %s | `%s` | `%s` | . | . | . | . | . | **NO CORRIO** |" % (n, cid, linea))
        continue
    texto = open(ruta, encoding="utf-8", errors="replace").read()
    m = re.search(r"VECINOS POR ENCIMA DE UMBRAL: (\d+)", texto)
    vecinos = m.group(1) if m else "0"
    m = re.search(r"DECLARADOS POR LECTURA: (\d+)", texto)
    declarados = m.group(1) if m else "0"
    cableadas = len(re.findall(r"arista madre-hijo cableada", texto))
    cola = len(re.findall(r"ARISTA EN COLA, no cableada", texto))
    m = re.search(r"nodos en el grafo: (\d+)", texto)
    nodos = m.group(1) if m else "."
    m = re.search(r"CODIGO DE SALIDA: (\d+)", texto)
    cod = m.group(1) if m else "."
    print("| %s | `%s` | `%s` | %s | %s | %s | %s | %s | %s |"
          % (n, cid, linea, vecinos, declarados, cableadas, cola, nodos,
             "**VERDE**" if cod == "0" else "**%s**" % cod))
