# -*- coding: utf-8 -*-
"""PASOS INVENTADOS POR CAPITULO (`AUDITOR_FORJA.md` 8.3, `D.30`), VUELTA 1 DEL FRENTE.

EL DENOMINADOR SALE DEL DATO: cuenta `pasos_accionables` fichero a fichero.
EL NUMERADOR LO PONE EL EXTRACTOR LEYENDO, porque ninguna maquina lo puede poner (`D.30`), y aqui
viene de `.v1g/fidelidad.py`, que es donde esta la relectura paso a paso con su cita pegada.

La columna de reescritos NO es el numerador: son los puentes que **se cazaron y se corrigieron
antes de que el candidato contara como escrito**, y se publican porque un cero sin su historia no
dice si hubo trabajo o si no hubo mirada.
"""
import io
import json
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

BANDEJA = "cuarentena/grove_high_output/%s.json"

TANDA = {
    "cap_01": ["revisar_tres_preguntas_valor_carrera"],
    "cap_02": ["construir_flujo_produccion_paso_limitante",
               "clasificar_trabajo_proceso_montaje_prueba",
               "rehacer_flujo_paso_limitante_capacidad",
               "equilibrar_capacidad_personal_inventario_plazo",
               "preferir_inspeccion_proceso_prueba_destructiva",
               "dimensionar_inventario_materia_prima_reposicion",
               "detectar_arreglar_fallo_etapa_menor_valor"],
}
# EL NUMERADOR, PUESTO POR MI LEYENDO CADA PASO CONTRA SU PARRAFO (.v1g/fidelidad.py)
PUENTES = {"cap_01": 0, "cap_02": 0}
# PUENTES CAZADOS Y REESCRITOS EN EL ACTO, ANTES DE CONTAR COMO ESCRITOS (D.30)
REESCRITOS = {"cap_01": 0, "cap_02": 1}

print("| capitulo | nodos | **pasos escritos** | **PUENTE** | **PASOS INVENTADOS** | puentes reescritos en el acto |")
print("|---|---:|---:|---:|---:|---:|")
total_nodos = total_pasos = total_puentes = total_reescritos = 0
for unidad in sorted(TANDA):
    pasos = 0
    for identificador in TANDA[unidad]:
        datos = json.load(io.open(BANDEJA % identificador, encoding="utf-8"))
        pasos += len(datos["pasos_accionables"])
    puentes = PUENTES[unidad]
    total_nodos += len(TANDA[unidad])
    total_pasos += pasos
    total_puentes += puentes
    total_reescritos += REESCRITOS[unidad]
    print("| **`%s`** (lote 7, `grove_high_output`) | %d | **%d** | **%d** | **%s por ciento** | %d |"
          % (unidad, len(TANDA[unidad]), pasos, puentes,
             ("%.2f" % (100.0 * puentes / pasos)).replace(".", ","), REESCRITOS[unidad]))
print("| **total del tramo de esta vuelta** | %d | **%d** | **%d** | **%s por ciento** | %d |"
      % (total_nodos, total_pasos, total_puentes,
         ("%.2f" % (100.0 * total_puentes / total_pasos)).replace(".", ","), total_reescritos))
print("")
print("EL PEOR CAPITULO, que es sobre el que se decide la escalada: %s por ciento"
      % ("%.2f" % max(100.0 * PUENTES[u] / sum(len(json.load(io.open(BANDEJA % i, encoding="utf-8"))["pasos_accionables"])
                                               for i in TANDA[u]) for u in TANDA)).replace(".", ","))
print("TOPE DEL ENCARGO                                            : 10")
