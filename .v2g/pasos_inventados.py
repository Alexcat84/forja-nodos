# -*- coding: utf-8 -*-
"""PASOS INVENTADOS POR UNIDAD (AUDITOR_FORJA.md 8.3, D.30), VUELTA 2 DEL FRENTE.

EL DENOMINADOR SALE DEL DATO: cuenta pasos_accionables fichero a fichero de la bandeja.
EL NUMERADOR LO PONE EL EXTRACTOR LEYENDO, porque ninguna maquina lo puede poner (D.30),
y aqui viene de .v2g/fidelidad.py, que es donde esta la relectura paso a paso con su cita
pegada.

La columna de reescritos NO es el numerador: son los puentes que se cazaron y se
corrigieron ANTES de que el candidato contara como escrito, y se publican porque un cero
sin su historia no dice si hubo trabajo o si no hubo mirada.

Y EL REMEDIO BLOQUEANTE HEREDADO (PARA_ALEXIS.md 4): la cifra se publica con el ROTULO de
la poblacion que se midio. La poblacion de esta tabla son LOS 15 CANDIDATOS QUE ESTA
VUELTA ESCRIBIO DE cap_03. No es el grafo, no es el capitulo entero del libro y no es la
bandeja del libro, que hoy tiene 23 ficheros porque arrastra los 8 de la vuelta 1.
"""
import glob
import io
import json
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

BANDEJA = "cuarentena/grove_high_output/%s.json"

TANDA = {
    "cap_03": ["elegir_cinco_indicadores_diarios_fabrica",
               "emparejar_indicadores_efecto_contraefecto",
               "elegir_indicador_salida_trabajo_administrativo",
               "representar_actividad_caja_negra_ventanas",
               "construir_indicador_linealidad_alerta_temprana",
               "construir_indicador_tendencia_patron",
               "construir_grafico_escalonado_pronosticos",
               "archivar_indicadores_resolver_problemas",
               "elegir_fabricar_pedido_pronostico",
               "casar_flujo_fabricacion_flujo_ventas",
               "dimensionar_plantilla_administrativa_pronostico",
               "decidir_aceptar_rechazar_material_defectuoso",
               "elegir_inspeccion_barrera_monitorizacion",
               "variar_frecuencia_inspeccion_nivel_calidad",
               "simplificar_trabajo_reducir_numero_pasos"],
}
# EL NUMERADOR, PUESTO POR MI LEYENDO CADA PASO CONTRA SU PARRAFO (.v2g/fidelidad.py)
PUENTES = {"cap_03": 0}
# PUENTES CAZADOS Y REESCRITOS EN EL ACTO, ANTES DE CONTAR COMO ESCRITOS (D.30)
REESCRITOS = {"cap_03": 2}

print("| capitulo | nodos | **pasos escritos** | **PUENTE** | **PASOS INVENTADOS** | puentes reescritos en el acto |")
print("|---|---:|---:|---:|---:|---:|")
total_nodos = total_pasos = total_puentes = total_reescritos = 0
peor = 0.0
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
    peor = max(peor, 100.0 * puentes / pasos)
    print("| **`%s`** (lote 7, `grove_high_output`), los candidatos de ESTA vuelta | %d | **%d** | **%d** | **%s por ciento** | %d |"
          % (unidad, len(TANDA[unidad]), pasos, puentes,
             ("%.2f" % (100.0 * puentes / pasos)).replace(".", ","), REESCRITOS[unidad]))
print("| **total del tramo de esta vuelta**, y no del libro ni del grafo | %d | **%d** | **%d** | **%s por ciento** | %d |"
      % (total_nodos, total_pasos, total_puentes,
         ("%.2f" % (100.0 * total_puentes / total_pasos)).replace(".", ","), total_reescritos))
print("")
print("EL PEOR CAPITULO, que es sobre el que se decide la escalada: %s por ciento"
      % ("%.2f" % peor).replace(".", ","))
print("TOPE                                                       : 10")
print("ESCALADA                                                   : %s"
      % ("SI" if peor > 10 else "NO"))
print("")
print("LA POBLACION DE ESTA TABLA, DICHA ENTERA (remedio bloqueante de PARA_ALEXIS.md 4)")
bandeja = len([r for r in glob.glob("cuarentena/grove_high_output/*.json")])
minados = sum(len(v) for v in TANDA.values())
print("  candidatos releidos en esta tabla          : %d" % minados)
print("  ficheros en la bandeja del libro hoy       : %d   (arrastra los 8 de la vuelta 1)"
      % bandeja)
print("  unidades del libro minadas hasta hoy       : 3 de 18   (cap_01, cap_02 y cap_03)")
