# -*- coding: utf-8 -*-
"""PASOS INVENTADOS POR CAPITULO (AUDITOR_FORJA.md 8.3).

EL DENOMINADOR SALE DEL DATO: cuenta `pasos_accionables` fichero a fichero.
EL NUMERADOR LO PONE EL EXTRACTOR LEYENDO, porque ninguna maquina lo puede poner
(`D.30`: ninguna guarda de esta casa ve un paso que tu escribiste y el libro no
dice).
"""
import json

BANDEJA = "cuarentena/scott_radical_candor/%s.json"

# LA TANDA DE ESTA VUELTA, EN EL ORDEN DEL LIBRO (.v31/orden_cap11.txt)
TANDA = [
    "decidir_quien_comunica_cada_cuanto",
    "montar_reuniones_solas_mentalidad_frecuencia",
    "preguntar_seguimiento_hallar_huecos",
    "nutrir_ideas_nuevas_reunion_solas",
    "leer_seniales_fallo_jefe_reunion_solas",
    "conducir_reunion_equipo_agenda_tres_bloques",
    "escribir_apuntes_sala_estudio_equipo",
    "montar_reunion_gran_debate",
    "montar_reunion_gran_decision",
    "montar_reunion_general_presentaciones_preguntas",
    "pelear_proliferacion_reuniones_bloquear_ejecucion",
]

# EL NUMERADOR, PUESTO POR MI LEYENDO CADA PASO CONTRA SU PARRAFO.
PUENTES = dict((identificador, 0) for identificador in TANDA)

pasos = 0
for identificador in TANDA:
    datos = json.load(open(BANDEJA % identificador, encoding="utf-8"))
    pasos += len(datos["pasos_accionables"])
puentes = sum(PUENTES.values())

print("| capitulo | nodos | **pasos escritos** | **PUENTE** | **PASOS INVENTADOS** |")
print("|---|---:|---:|---:|---:|")
fila = ("| **`cap_11`** (lote 4, `scott_radical_candor`) | %d | **%d** | **%d** | "
        "**%s por ciento** |")
porciento = ("%.2f" % (100.0 * puentes / pasos)).replace(".", ",")
print(fila % (len(TANDA), pasos, puentes, porciento))
print(("| **total del tramo de esta vuelta** | %d | **%d** | **%d** | **%s por ciento** |")
      % (len(TANDA), pasos, puentes, porciento))
