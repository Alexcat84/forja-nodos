# -*- coding: utf-8 -*-
"""7.C de la cosecha: toda guarda que el reporte declare mordiendo se re corre
POR MUTACION. Aqui se muta un candidato REAL (sobre una copia en memoria, el
arbol no se toca) y se comprueba que la guarda CAE."""
import json, sys, copy
sys.path.insert(0, ".")
sys.stdout.reconfigure(encoding='utf-8')
from src import aduana

RUTA = "cuarentena/grove_high_output/variar_frecuencia_inspeccion_nivel_calidad.json"
base = json.load(open(RUTA, encoding="utf-8"))

def probar(nombre, mutar):
    c = copy.deepcopy(base)
    mutar(c)
    try:
        c, _avisos = aduana.normalizar_candidato(c)
        fallos = aduana.validar_candidato(c)
    except Exception as e:
        fallos = ["EXCEPCION: %s" % e]
    veredicto = "CAE" if fallos else "PASA"
    print("  %-46s -> %s   %s" % (nombre, veredicto, (fallos[0][:90] if fallos else "")))
    return bool(fallos)

print("$ python .v3g/mutacion.py   (el arbol NO se toca: se muta una copia en memoria)")
print("fichero mutado: %s" % RUTA)
print()
print("CONTROL, sin mutar:")
probar("el candidato tal como esta en la bandeja", lambda c: None)
print()
print("MUTACIONES, y cada una tiene que CAER:")
r = []
r.append(probar("id con preposicion y articulo (regla 3)", lambda c: c.__setitem__("id", "gestion_de_la_calidad")))
r.append(probar("id de una palabra suelta (regla 5)", lambda c: c.__setitem__("id", "inspeccion")))
print("  NOTA: un id con mayusculas y espacios NO se prueba aqui: D.7 manda que la")
print("        aduana lo NORMALICE (forma), no que lo rechace. Probarlo seria pedirle")
print("        a la guarda que muerda donde la doctrina dice que no muerda.")
r.append(probar("sin fuentes", lambda c: c.__setitem__("fuentes", [])))
r.append(probar("fuente con clave no canonica", lambda c: c["fuentes"][0].__setitem__("clave", "libro_que_no_existe")))
r.append(probar("sin pasos accionables", lambda c: c.__setitem__("pasos_accionables", [])))
# El guion largo NO se teclea aqui: este fichero vive en el repo y el barrido de
# guiones lo leeria. Se construye por su punto de codigo, que es lo mismo para la
# guarda y no deja el caracter escrito en el arbol.
GUION_LARGO = chr(0x2014)
r.append(probar("un guion largo dentro de un paso", lambda c: c["pasos_accionables"].__setitem__(0, c["pasos_accionables"][0] + " " + GUION_LARGO + " colado")))
r.append(probar("se le quita el entregable", lambda c: c.__setitem__("entregable_esperado", "")))
print()
print("MUTACIONES QUE CAEN: %d de %d" % (sum(r), len(r)))
print("LA GUARDA MUERDE" if sum(r) == len(r) else "HAY AL MENOS UNA QUE NO MUERDE, Y ESO ES CIFRA (cosecha 7.C)")
