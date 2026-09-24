# -*- coding: utf-8 -*-
"""PASOS INVENTADOS POR CAPITULO, VUELTA 3 DEL FRENTE marquet_turn_the_ship.

D.47 manda cero instrumentos nuevos: este es el mismo instrumento que ya usan
`.v33/pasos_inventados.py` y sus hermanos, apuntado a los ficheros de esta vuelta.

EL DENOMINADOR SALE DEL DATO: cuenta pasos_accionables fichero a fichero, leyendo
los JSON de cuarentena tal como estan HOY (tras pagar el puente de la TAREA 2).

EL NUMERADOR LO PONE EL EXTRACTOR LEYENDO (D.30): ninguna maquina distingue una
TRANSCRIPCION de un PUENTE. La tabla PUENTES_POR_NODO es la relectura de fidelidad
publicada en el reporte (TAREA 2, TAREA 4, seccion 5.a.3 y 5.b.3), no un conteo
automatico.
"""
import io
import json
import os
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANDEJA = os.path.join(RAIZ, "cuarentena", "marquet_turn_the_ship")

# capitulo -> [(archivo_json, puentes_leidos), ...]
CAPITULOS = {
    "cap_04": [("informar_cierre_jornada_conservar_propiedad_trabajo.json", 0)],
    "cap_06 (HOY, tras pagar el puente y releer sus 51 filas)": [
        ("aplicar_ejercicio_codigo_genetico_control.json", 0),
        ("asignar_responsable_unico_evolucion_planificada.json", 0),
    ],
    "cap_07": [("declarar_intencion_reemplazar_peticion_permiso.json", 0)],
    "cap_08": [("resistir_dar_solucion_clasificar_decision_urgencia.json", 0)],
}


def pasos(archivo):
    with io.open(os.path.join(BANDEJA, archivo), encoding="utf-8") as f:
        datos = json.load(f)
    return len(datos["pasos_accionables"])


def fila(etiqueta, nodos_n, p, b):
    if p == 0:
        print("| %s | %d | 0 | 0 | **SIN SUPERFICIE (0 / 0)** |" % (etiqueta, nodos_n))
    else:
        porciento = ("%.2f" % (100.0 * b / p)).replace(".", ",")
        print("| %s | %d | %d | %d | **%s por ciento (%d / %d)** |"
              % (etiqueta, nodos_n, p, b, porciento, b, p))


print("| capitulo | nodos | pasos escritos | PUENTE | PASOS INVENTADOS |")
print("|---|---:|---:|---:|---:|")

tramo_pasos = 0
tramo_puentes = 0
tramo_nodos = 0
for capitulo, nodos in CAPITULOS.items():
    p = sum(pasos(archivo) for archivo, _ in nodos)
    b = sum(puentes for _, puentes in nodos)
    fila("`%s`" % capitulo, len(nodos), p, b)
    if capitulo in ("cap_07", "cap_08"):
        tramo_pasos += p
        tramo_puentes += b
        tramo_nodos += len(nodos)

fila("EL TRAMO DE ESTA VUELTA (`cap_07` + `cap_08`)", tramo_nodos, tramo_pasos, tramo_puentes)
