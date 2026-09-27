# -*- coding: utf-8 -*-
"""Las DOS preguntas que la vuelta 38 sube a la cola de doctrina (D.53).

TAREA 4 del encargo: se escriben en el tablero y se sigue. NO se resuelven aqui,
y ninguna de las dos bloquea.
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA = os.path.join(RAIZ, "config", "frentes.json")

NUEVAS = [
    {"n": 7,
     "pregunta": "El propio libro se contradice y ningun nodo lo dice: cap_12 L21 invita a "
                 "copiar el marco y llevar ahi la cuenta de quien te dice que, y cap_01 "
                 "prohibe escribir nombres en las casillas. Los dos pasos son transcripcion "
                 "fiel de su linea y ninguno es PUENTE. Se toca alguno de los dos nodos?",
     "medida_en": "REPORTE.md AC.7 (vuelta 37) y BC.7 (vuelta 38); encargo de la vuelta 38, tarea 4.1",
     "bloquea": False},
    {"n": 8,
     "pregunta": "La senial 1 compara titulo mas resumen_teorico mas pasos, y en un lote "
                 "escrito de una sentada eso mide la formula del extractor tanto como el "
                 "contenido del nodo. Lo midieron dos instrumentos por separado. Ningun "
                 "umbral se toca en ninguna vuelta: la pregunta es que se hace con eso.",
     "medida_en": "APERTURA_CIEGA.md 13.2 y ACTA 36 7; encargo de la vuelta 38, tarea 4.2",
     "bloquea": False},
]

with io.open(RUTA, encoding="utf-8") as f:
    datos = json.load(f)

cola = datos["cola_de_doctrina"]
tenidas = set(p["n"] for p in cola["preguntas"])
for nueva in NUEVAS:
    if nueva["n"] in tenidas:
        print("la pregunta %d ya estaba: no se duplica" % nueva["n"])
        continue
    cola["preguntas"].append(nueva)
    print("pregunta %d anexada a la cola de doctrina" % nueva["n"])

with io.open(RUTA, "w", encoding="utf-8", newline="\n") as f:
    json.dump(datos, f, ensure_ascii=False, indent=2)
    f.write(u"\n")

print("la cola queda en %d pregunta(s), %d bloquea(n)"
      % (len(cola["preguntas"]),
         len([p for p in cola["preguntas"] if p.get("bloquea")])))
