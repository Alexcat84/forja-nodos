# -*- coding: utf-8 -*-
"""LA MEDICION DEL DIA de los tres capitulos que un nodo declara NO MINADOS.

El recuento se GENERA DEL DATO, nunca leyendo la tabla que corrijo (REMEDIO 2,
ACTA 31). Dos piezas, y las dos salen de un fichero:

  1. el mapa CAPITULO DEL LIBRO -> FICHERO, leido de la cabecera 'unidad:' de
     cada fuentes/scott_radical_candor/cap_NN.md. El libro numera sus capitulos
     con TRES unidades de frente (Preface, Introduction, How to Use This Book),
     asi que 'chapter eight' NO es cap_08.md.
  2. los nodos y pasos que cada fichero tiene YA en el grafo, contados por la
     ruta que cada nodo cita en su resumen_teorico.
"""
import glob, io, os, re, sys, collections
sys.path.insert(0, ".")
from src import comun

ORD = {"1": "uno", "2": "dos", "3": "tres", "4": "cuatro", "5": "cinco",
       "6": "seis", "7": "siete", "8": "ocho"}
mapa = {}
for ruta in sorted(glob.glob("fuentes/scott_radical_candor/cap_*.md")):
    with io.open(ruta, encoding="utf-8", errors="replace") as fh:
        cab = fh.read(400)
    m = re.search(r"^unidad:\s*Cap\.\s*(\d+)", cab, re.M)
    if m:
        mapa[ORD[m.group(1)]] = os.path.basename(ruta)[:-3]

RX = re.compile(r"fuentes/scott_radical_candor/(cap_\d\d)\.md")
nodos = comun.leer_jsonl(comun.RUTA_DATASET)
porcap = collections.defaultdict(lambda: [0, 0])
for n in nodos:
    for c in set(RX.findall(n.get("resumen_teorico") or "")):
        porcap[c][0] += 1
        porcap[c][1] += len(n.get("pasos_accionables") or [])

print("poblacion: %d nodos de dataset/nodos.jsonl (el arbol entero)" % len(nodos))
print("mapa leido de la cabecera 'unidad:' de fuentes/scott_radical_candor/cap_*.md")
print()
print("| lo que la linea 95 nombra | fichero del capitulo | nodos en el grafo | pasos en el grafo | la afirmacion del nodo |")
print("|---|---|---:|---:|---|")
filas = [("capitulo ocho", "1:1 Conversations"),
         ("capitulo seis", "Soliciting Impromptu Guidance"),
         ("capitulo siete", "las conversaciones de carrera")]
tn = tp = 0
for orden, rotulo in filas:
    f = mapa[orden.split()[1]]
    nn, pp = porcap.get(f, [0, 0])
    tn += nn; tp += pp
    juicio = "**FALSA**" if nn else "cierta"
    print("| **%s** (%s) | `%s` | **%d** | **%d** | %s |" % (orden, rotulo, f, nn, pp, juicio))
print("| **los tres** | | **%d** | **%d** | |" % (tn, tp))
