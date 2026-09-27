# -*- coding: utf-8 -*-
"""CUANTO DE LA COLA LA FABRICA MI FORMULA DE REDACCION, Y NO EL CONTENIDO DEL NODO.

NO ES UN INSTRUMENTO NUEVO NI UNA GUARDA (moratoria de EXTRACTOR.md 13, austero D.47):
llama a las MISMAS funciones de la aduana que producen la senal 1,
comun.texto_comparable y aduana.senal_similitud_texto, sobre los pares que la aduana YA
levanto. No barre poblacion, no mueve ningun umbral y no decide ningun veredicto: sirve
para LEER al vecino antes de escribir la razon, que es lo que EXTRACTOR.md 2 manda cuando
la aduana bloquea.

POR QUE HACE FALTA PARA JUZGAR: comun.texto_comparable mira titulo mas resumen_teorico mas
pasos. En mi tanda el resumen_teorico es con diferencia la pieza mas larga de cada ficha y
lleva un armazon repetido en los quince (UNIDAD DE ORIGEN, POR QUE ES PROCEDIMIENTO, DE
DONDE SALE CADA PASO, RELECTURA DE FIDELIDAD, LO QUE NO ESCRIBO, DISCUTIBLE QUE MARCO). Si
la senal cae al quitar ese armazon, lo que la levanto no era el procedimiento.
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.getcwd())
from src import aduana, comun

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

BLOQUE = re.compile(r"^\[(?:BLOQUEARIA|ENTRARIA|CAERIA)\]\s+(\S+)", re.M)
PAR = re.compile(r"^\s+vecino (\S+)\s+\[levantada por: ([^\]]+)\]\s*\n"
                 r"\s+similitud_texto ([\d.]+) \|", re.M)


def cargar(identificador):
    ruta = "cuarentena/grove_high_output/%s.json" % identificador
    if os.path.exists(ruta):
        return json.loads(io.open(ruta, encoding="utf-8").read())
    for linea in io.open("dataset/nodos.jsonl", encoding="utf-8"):
        datos = json.loads(linea)
        if datos["id"] == identificador:
            return datos
    return None


def sin_armazon(nodo):
    """El mismo texto que mira la senal 1, pero SIN el resumen_teorico."""
    piezas = [nodo.get("titulo") or ""]
    piezas.extend(nodo.get("pasos_accionables") or [])
    return comun.normalizar_texto(" ".join(piezas))


pares = []
vistos = set()
for ruta in sorted(os.listdir(".v2g")):
    if not ruta.startswith("informe_") or not ruta.endswith(".txt"):
        continue
    if ruta.startswith("informe_lote") or ruta in ("informe_01.txt", "informe_02.txt"):
        continue
    texto = io.open(os.path.join(".v2g", ruta), encoding="utf-8").read()
    cabeza = BLOQUE.search(texto)
    if not cabeza:
        continue
    for vecino, _senal, medido in PAR.findall(texto):
        clave = tuple(sorted((cabeza.group(1), vecino)))
        if clave in vistos:
            continue
        vistos.add(clave)
        pares.append((cabeza.group(1), vecino, float(medido)))

print("| par que la aduana levanto | senal 1 **como la mide la aduana** | senal 1 **sin el `resumen_teorico`** | caida |")
print("|---|---:|---:|---:|")
caidas = []
for candidato, vecino, medido in pares:
    a, b = cargar(candidato), cargar(vecino)
    entero = aduana.senal_similitud_texto(comun.texto_comparable(a), comun.texto_comparable(b))
    desnudo = aduana.senal_similitud_texto(sin_armazon(a), sin_armazon(b))
    caidas.append(entero - desnudo)
    print("| `%s` con `%s` | %s | %s | **%s** |"
          % (candidato, vecino,
             ("%.3f" % entero).replace(".", ","),
             ("%.3f" % desnudo).replace(".", ","),
             ("%+.3f" % (desnudo - entero)).replace(".", ",")))
print("")
print("PARES DISTINTOS MEDIDOS                         : %d" % len(pares))
print("UMBRAL DE LA SENAL 1, QUE NO TOCO NI PROPONGO MOVER: 0,35")
bajan = sum(1 for c in caidas if c > 0)
cruzan = 0
for (candidato, vecino, _m), caida in zip(pares, caidas):
    a, b = cargar(candidato), cargar(vecino)
    entero = aduana.senal_similitud_texto(comun.texto_comparable(a), comun.texto_comparable(b))
    desnudo = aduana.senal_similitud_texto(sin_armazon(a), sin_armazon(b))
    if entero >= 0.35 > desnudo:
        cruzan += 1
print("PARES QUE BAJAN AL QUITAR EL RESUMEN            : %d de %d" % (bajan, len(pares)))
print("PARES QUE DEJARIAN DE LEVANTARSE                : %d de %d" % (cruzan, len(pares)))
print("")
print("ESTO NO ES UNA PROPUESTA DE UMBRAL NI DE CAMBIO DE FICHA. Es la medida que me")
print("hacia falta para escribir la razon de cada veredicto, y se publica entera.")
