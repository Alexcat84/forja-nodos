# -*- coding: utf-8 -*-
"""LAS CITAS DE LINEA DE LA TANDA DE LA VUELTA 47, IMPRESAS POR EL INSTRUMENTO.

D.35: ninguna cita de linea se teclea en una tabla del reporte sin que la salida
literal de sed -n '<n>p' quede pegada al lado. Aqui la imprime el instrumento, que
es el mismo remedio mecanico llevado a su sede.
"""
import io
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

RUTA = "fuentes/grove_high_output/cap_04.md"

# (tramo, linea, candidato al que sirve)
CITAS = [
    ("P21", 219, "detectar_palanca_negativa_actividad_mando"),
    ("P24", 231, "detectar_palanca_negativa_actividad_mando"),
    ("P24", 233, "detectar_palanca_negativa_actividad_mando"),
    ("P24", 235, "detectar_palanca_negativa_actividad_mando"),
    ("P27", 243, "delegar_tarea_base_comun_seguimiento"),
    ("P27", 245, "delegar_tarea_base_comun_seguimiento"),
    ("P27", 247, "delegar_tarea_base_comun_seguimiento"),
    ("P27", 249, "delegar_tarea_base_comun_seguimiento"),
    ("P29", 253, "supervisar_tarea_delegada_etapa_menor_valor"),
    ("P29", 255, "supervisar_tarea_delegada_etapa_menor_valor"),
    ("P30", 257, "supervisar_decision_delegada_preguntas_concretas"),
    ("P32", 267, "identificar_paso_limitante_jornada_desfases"),
    ("P33", 269, "agrupar_tareas_semejantes_aprovechar_preparacion"),
    ("P33", 271, "agrupar_tareas_semejantes_aprovechar_preparacion"),
    ("P34", 273, "usar_calendario_herramienta_planificacion_produccion"),
    ("P34", 275, "usar_calendario_herramienta_planificacion_produccion"),
    ("P34", 277, "decir_no_trabajo_excede_capacidad"),
    ("P34", 279, "usar_calendario... y decir_no... (la cabecera que numera las dos)"),
    ("P34", 281, "usar_calendario_herramienta_planificacion_produccion"),
    ("P34", 283, "decir_no_trabajo_excede_capacidad"),
    ("P34", 285, "decir_no_trabajo_excede_capacidad"),
]

lineas = io.open(RUTA, encoding="utf-8").read().split("\n")

print("| # | tramo | linea | la salida de `sed -n '<n>p'`, pegada y cortada a 82 | de que candidato es |")
print("|---:|---|---:|---|---|")
for i, (tramo, n, quien) in enumerate(CITAS, 1):
    texto = lineas[n - 1].replace("|", "/")
    # LOS SIGNOS TIPOGRAFICOS DEL LIBRO SE ESCRIBEN POR SU CODIGO Y NO POR SU DIBUJO:
    # el barrido de guiones muerde el guion largo y el medio en TODO el repo, incluido
    # este instrumento, asi que aqui no puede aparecer ninguno de los dos.
    for codigo, sustituto in ((0x201c, '"'), (0x201d, '"'), (0x2019, "'"),
                              (0x2018, "'"), (0x2014, ", "), (0x2013, ", ")):
        texto = texto.replace(unichr(codigo) if sys.version_info[0] == 2 else chr(codigo),
                              sustituto)
    print("| %d | `%s` | L%d | `%d:%s` | `%s` |" % (i, tramo, n, n, texto[:82], quien))
print("")
print("renglones citados: %d, de %d tramos distintos" % (len(CITAS), len(set(c[0] for c in CITAS))))
