# -*- coding: utf-8 -*-
"""EL CASO POSITIVO DE LA TAREA 2: el arnes entrega lo que el acta ESCRIBE.

Corre el extractor de `src/herencia.py` contra las tres actas con las que se puede
probar y publica, por cada una, CUANTOS remedios entrega y CUALES, con su linea.

    python .v31/caso_positivo_herencia.py
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import herencia

ADORNO = re.compile(r"[`*~]+")
PROHIBIDAS = ("3.2", "6.1")


def titular(cuerpo):
    """La primera frase del remedio, para que la tabla quepa en una linea."""
    fila = cuerpo[-1]
    celdas = [c.strip() for c in fila.strip().strip("|").split("|")]
    texto = ADORNO.sub("", celdas[1] if len(celdas) > 1 else celdas[0])
    corte = texto.find(". ")
    if corte > 20:
        texto = texto[:corte + 1]
    return texto.strip()[:96]


def seccion(cuerpo):
    """El numero de seccion del acta donde vive la tabla: `10.` o `8.5.`."""
    crudo = ADORNO.sub("", cuerpo[0]).lstrip("# ").strip()
    encaje = re.match(r"([0-9]+(?:\.[0-9]+)*)\.?", crudo)
    return (encaje.group(1) if encaje else crudo)


print("EL ARNES ENTREGA LOS REMEDIOS QUE EL ACTA ESCRIBE, NO LOS QUE CITA")
print("caso positivo de la TAREA 2 de la vuelta 31, sobre docs/loop/ACTA_AUDITOR.md")
print()
print("| acta | remedios entregados | de que seccion salen | secciones que solo CITAN |")
print("|---|---:|---|---|")
detalle = []
for numero in ("ACTA 27", "ACTA 28", "ACTA 29"):
    datos = herencia.extraer(seleccion=numero)
    remedios = [i for i in datos["items"] if i["clase"] == "REMEDIO"]
    sedes = sorted(set(seccion(r["cuerpo"]) for r in remedios))
    citan = [s for s in sedes if s in PROHIBIDAS]
    print("| `%s` | **%d** | seccion `%s` | **%s** |"
          % (numero, len(remedios), " y ".join(sedes),
             ", ".join(citan) if citan else "NINGUNA, que es lo que se pedia"))
    detalle.append((numero, remedios))

print()
print("LOS REMEDIOS, UNO A UNO, CON SU LINEA DEL ACTA")
print()
print("| acta | # | linea | el remedio que el acta ESCRIBE |")
print("|---|---:|---:|---|")
for nombre, remedios in detalle:
    for indice, remedio in enumerate(remedios, 1):
        print("| `%s` | %d | `%d` | %s |"
              % (nombre, indice, remedio["linea"], titular(remedio["cuerpo"])))
