# -*- coding: utf-8 -*-
"""LA MITAD BARATA DEL DICTAMEN DE LA ADUANA, CORRIDA ANTES QUE LA CARA.

NO ES UN INSTRUMENTO NUEVO (moratoria de maquinaria, EXTRACTOR.md 13): llama a las
MISMAS funciones de src/aduana.py que usa python forja.py informe para decidir CAERIA,
normalizar_candidato y validar_candidato, y a nada mas. Lo unico que NO hace es el
barrido de vecinos, que es la parte cara del informe y la que decide ENTRARIA contra
BLOQUEARIA.

PARA QUE SIRVE: el informe de un candidato tarda minutos, y una caida de guarda que se
descubre al final cuesta rehacerlos todos. Esto dice en segundos cual CAERIA, para
corregirlo antes. NO SUSTITUYE AL INFORME: el informe de cada candidato se corre igual,
uno por uno, en el mismo acto en que se escribe (EXTRACTOR.md 16), y el del lote entero
al cerrar el capitulo.
"""
import glob
import io
import json
import os
import sys

sys.path.insert(0, os.getcwd())
from src import aduana

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

FECHA = "2026-09-16"
tabla = json.loads(io.open("fuentes/FUENTES_CANONICAS.json", encoding="utf-8").read())
esquema = json.loads(io.open("esquema/nodo.schema.json", encoding="utf-8").read())

vistos = {}
malos = 0
for ruta in sorted(glob.glob("cuarentena/grove_high_output/*.json")):
    bruto = json.loads(io.open(ruta, encoding="utf-8").read())
    candidato, _avisos = aduana.normalizar_candidato(bruto, FECHA)
    try:
        aduana.validar_candidato(candidato, tabla, esquema)
        estado = "pasa las guardas"
    except aduana.Rechazo as rechazo:
        estado = "CAERIA: %s" % rechazo
        malos += 1
    identificador = candidato.get("id")
    if identificador in vistos:
        estado += " | CHOCA con %s" % vistos[identificador]
        malos += 1
    vistos[identificador] = os.path.basename(ruta)
    print("%-50s %s" % (identificador, estado))

print("")
print("POBLACION DE ESTA COMPROBACION: los %d ficheros de cuarentena/grove_high_output/,"
      % len(vistos))
print("que son los 8 de la vuelta 1 mas los 15 de la vuelta 2. NO es el grafo.")
print("CAERIAN O CHOCAN: %d" % malos)
