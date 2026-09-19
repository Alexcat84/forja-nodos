# -*- coding: utf-8 -*-
"""LAS CITAS DE LINEA DE LA TANDA DE LA VUELTA 50, IMPRESAS POR EL INSTRUMENTO.

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
    ("P41", 315, "preparar_respuestas_estandar_interrupciones_repetidas"),
    ("P42", 317, "agrupar_interrupciones_subordinados_reuniones_regulares"),
    ("P44", 321, "canalizar_interrupciones_cartel_hora_oficina"),
    ("P44", 323, "canalizar_interrupciones_cartel_hora_oficina"),
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
print("renglones citados: %d, de %d tramos distintos"
      % (len(CITAS), len(set(c[0] for c in CITAS))))
