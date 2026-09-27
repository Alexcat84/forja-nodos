# -*- coding: utf-8 -*-
"""LAS CITAS DE LINEA DE LA TANDA DE LA VUELTA 48, IMPRESAS POR EL INSTRUMENTO.

D.35: ninguna cita de linea se teclea en una tabla del reporte sin que la salida
literal de sed -n '<n>p' quede pegada al lado. Aqui la imprime el instrumento, que
es el mismo remedio mecanico llevado a su sede.
"""
import io
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

RUTA = "fuentes/grove_high_output/cap_04.md"

CITAS = [
    ("P34a", 273, "usar_calendario_herramienta_planificacion_produccion"),
    ("P34a", 275, "usar_calendario_herramienta_planificacion_produccion"),
    ("P34a", 279, "la cabecera que numera las dos responsabilidades, de los DOS"),
    ("P34a", 281, "usar_calendario_herramienta_planificacion_produccion"),
    ("P34b", 277, "decir_no_trabajo_excede_capacidad"),
    ("P34b", 283, "decir_no_trabajo_excede_capacidad"),
    ("P34b", 285, "decir_no_trabajo_excede_capacidad"),
    ("P36", 289, "llevar_inventario_proyectos_discrecionales"),
    ("P38", 293, "dimensionar_numero_subordinados_medio_dia_semanal"),
    ("P38", 295, "dimensionar_numero_subordinados_medio_dia_semanal"),
    ("P38", 297, "dimensionar_numero_subordinados_medio_dia_semanal"),
    ("P38", 299, "dimensionar_numero_subordinados_medio_dia_semanal"),
    ("P38", 301, "dimensionar_numero_subordinados_medio_dia_semanal"),
    ("P39", 303, "buscar_regularidad_bloques_iguales_trabajo_mando"),
    ("P39", 305, "buscar_regularidad_bloques_iguales_trabajo_mando"),
    ("P39", 307, "buscar_regularidad_bloques_iguales_trabajo_mando"),
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
                              (0x2018, "'"), (0x2014, ", "), (0x2013, ", "),
                              (0x2026, "...")):
        texto = texto.replace(chr(codigo), sustituto)
    print("| %d | `%s` | L%d | `%d:%s` | `%s` |" % (i, tramo, n, n, texto[:82], quien))
print("")
print("renglones citados: %d, de %d tramos distintos" % (len(CITAS), len(set(c[0] for c in CITAS))))
