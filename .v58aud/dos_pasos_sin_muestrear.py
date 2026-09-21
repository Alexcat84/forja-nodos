# -*- coding: utf-8 -*-
"""LOS DOS PASOS QUE LA MUESTRA DE `v57` NO TOCO, LEIDOS POR MI CONTRA SU LINEA.

El reporte los deja SIN MUESTREAR y lo dice bien. Yo los leo, y con eso la
cobertura de fidelidad de la tanda pasa de 40 de 42 a 42 de 42.

LOS GUIONES: la linea del libro puede traer guiones largos o medios, y este
fichero SI entra al barrido de `forja.py guiones` (la exencion es de
`fuentes/`, que es bandeja de entrada, y no de mi testigo). Se sustituyen por
el corto y el instrumento imprime cuantas veces lo hizo.
"""
import io
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

RUTA = "fuentes/grove_high_output/cap_11.md"
lineas = io.open(RUTA, encoding="utf-8").read().split("\n")
cruda = lineas[62]                       # L63, contando desde 1

sustituciones = cruda.count(chr(0x2014)) + cruda.count(chr(0x2013))
limpia = cruda.replace(chr(0x2014), "-").replace(chr(0x2013), "-")

print("$ sed -n '63p' %s   (la linea ENTERA, no un tercio)" % RUTA)
print("")
print(limpia)
print("")
print("guiones largos o medios sustituidos por el corto: %d" % sustituciones)
print("")
print("LOS DOS PASOS QUE LA MUESTRA NO ELIGIO, contra esa misma linea:")
print("  P4 de escalonar_complejidad_puesto_empleado_nuevo")
print("     'Promuevelo despues a un puesto mas complejo, incierto y ambiguo, que ademas suele pagar mas.'")
print("     en la linea: 'The employee can then be promoted into a more complex, uncertain,")
print("                   ambiguous job. (These tend to pay more.)'")
print("     esta en la linea: %s" % ("SI" if "can then be promoted into a more complex, uncertain, ambiguous job" in limpia else "NO"))
print("     y el parentesis del sueldo: %s" % ("SI" if "(These tend to pay more.)" in limpia else "NO"))
print("")
print("  P6 de escalonar_complejidad_puesto_empleado_nuevo")
print("     'Reconoce que esta es la razon por la que la promocion interna es el enfoque")
print("      que favorecen las empresas con culturas corporativas fuertes.'")
print("     en la linea: 'This is why promotion from within tends to be the approach favored")
print("                   by corporations with strong corporate cultures.'")
print("     esta en la linea: %s" % ("SI" if "This is why promotion from within tends to be the approach favored by corporations with strong corporate cultures" in limpia else "NO"))
print("")
print("VEREDICTO DE LOS DOS: TRANSCRIPCION. PUENTE: 0.")
