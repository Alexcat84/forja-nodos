# -*- coding: utf-8 -*-
"""QUE PASOS CAEN EN LA CLASE QUE EL ENCARGO MANDA RELEER ENTERA.

`TAREA 2` de la vuelta 39: *cuando un paso nombre una persona, una cuenta, un
escalon o un adjetivo de sentimiento, lee la linea entera antes de marcarlo
TRANSCRIPCION*. Esto NO juzga: solo **marca** los pasos de esa clase, para que
la cuenta que publico de cuantos relei enteros se pueda recontar.
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CUENTA = re.compile(
    r"\b(un|una|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|trece|"
    r"catorce|quince|veinte|treinta|cien|ciento|doscientos|cincuenta|ochenta|mil|"
    r"primero|primera|segundo|segunda|tercero|tercera|cuarto|cuarta|quinto|quinta|"
    r"ambos|cada|\d+)\b", re.I)
PERSONA = re.compile(
    r"\b(Amy|Edmondson|Google|Harvard|Carol|Dweck|Kim|Jason|Ann|Sheryl|Sandberg|"
    r"Bob|Chicago|Apple)\b")
ESCALON = re.compile(
    r"\b(consejero delegado|jefes intermedios|jefe|jefa|lider|lideres|empleado|"
    r"empleados|equipo|equipos|niveles|companiero|persona a tu cargo|mayores|"
    r"participantes|alumnos|crio)\b", re.I)
SENTIMIENTO = re.compile(
    r"\b(memorable|memorables|comodo|comoda|comodas|incomod\w*|miedo|temes|teme|"
    r"seguro|segura|seguridad|sincero|sincera|dispuesta|arrogantes|flustered|"
    r"preocupa|util|natural|rancia|dificil|facil|normal|fantastico|desastre|"
    r"humano|exito|dolor|duele|silencio)\b", re.I)

ESPECIES = (("persona", PERSONA), ("cuenta", CUENTA), ("escalon", ESCALON),
            ("sentimiento", SENTIMIENTO))

LOTE = ("pedir_critica_primero_crear_seguridad_psicologica",
        "elegir_pregunta_recurrente_pedir_critica",
        "resolver_dudas_frecuentes_pedir_critica")

print("LOS PASOS DE LA CLASE QUE EL ENCARGO MANDA RELEER ENTERA (TAREA 2)")
print("  marcados por el instrumento; el veredicto de cada uno lo pone la lectura")
total_pasos = 0
total_clase = 0
for cid in LOTE:
    ruta = os.path.join(RAIZ, "cuarentena", "scott_radical_candor", "%s.json" % cid)
    with io.open(ruta, encoding="utf-8") as f:
        pasos = json.load(f)["pasos_accionables"]
    marcados = []
    for i, paso in enumerate(pasos, 1):
        especies = [n for n, rx in ESPECIES if rx.search(paso)]
        if especies:
            marcados.append((i, especies))
    total_pasos += len(pasos)
    total_clase += len(marcados)
    print()
    print("  %s" % cid)
    print("    pasos: %d | de la clase: %d" % (len(pasos), len(marcados)))
    for i, especies in marcados:
        print("      P%02d  %s" % (i, ", ".join(especies)))
    fuera = [i for i in range(1, len(pasos) + 1)
             if i not in [m[0] for m in marcados]]
    print("    FUERA de la clase: %s" % (", ".join("P%02d" % i for i in fuera) or "ninguno"))
print()
print("  TOTAL del tramo: %d pasos, %d de la clase" % (total_pasos, total_clase))
