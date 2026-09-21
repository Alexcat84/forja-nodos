# -*- coding: utf-8 -*-
"""QUE PASOS CAEN EN LA CLASE QUE EL ENCARGO MANDA RELEER ENTERA.

`TAREA 2` de la vuelta 40, con la misma letra que la 39: *cuando un paso nombre
una persona, una cuenta, un escalon o un adjetivo de sentimiento, lee la linea
completa antes de marcarlo TRANSCRIPCION*. Esto NO juzga: solo **marca** los
pasos de esa clase, para que la cuenta que publico de cuantos relei enteros se
pueda recontar.

HEREDA LAS CUATRO EXPRESIONES DE .v39/clase.py Y LAS AMPLIA, y la ampliacion se
dice en vez de esconderse: el vocabulario de estos cuatro candidatos trae nombres
propios que la vuelta 39 no tenia (Rick Hanson, Sara Blakely, Spanx, Hawai,
Resilient, Velcro, Teflon) y sentimientos que tampoco (enfadado, defensiva,
amenazante, agradecimiento, invisible, ignorada, antinatural, awkward). Ampliar
la expresion solo puede SUBIR la cuenta de los que relei enteros, nunca bajarla.
"""
import io
import json
import os
import re
import sys

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CUENTA = re.compile(
    r"\b(un|una|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|trece|"
    r"catorce|quince|veinte|treinta|cien|ciento|doscientos|cincuenta|ochenta|mil|"
    r"primero|primera|primeras|segundo|segunda|tercero|tercera|cuarto|cuarta|"
    r"quinto|quinta|decada|semana|semanal|anios|minutos|segundos|"
    r"ambos|cada|\b\d+)\b", re.I)
PERSONA = re.compile(
    r"\b(Amy|Edmondson|Google|Harvard|Carol|Dweck|Kim|Jason|Ann|Sheryl|Sandberg|"
    r"Bob|Chicago|Apple|Rick|Hanson|Sara|Blakely|Spanx|Hawai|Resilient|Velcro|"
    r"Teflon|Oops)\b")
ESCALON = re.compile(
    r"\b(consejero delegado|consejera delegada|directora|director|jefes intermedios|"
    r"jefe|jefa|lider|lideres|empleado|empleados|equipo|equipos|niveles|companiero|"
    r"companieros|pareja|familiar|amigo|persona a tu cargo|mayores|"
    r"participantes|alumnos|crio|poderoso|empresa)\b", re.I)
SENTIMIENTO = re.compile(
    r"\b(memorable|memorables|comodo|comoda|comodos|comodas|incomod\w*|miedo|temes|"
    r"teme|temer|seguro|segura|seguridad|sincero|sincera|dispuesta|dispuesto|"
    r"arrogantes|preocupa|util|natural|antinatural|rancia|dificil|facil|normal|"
    r"fantastico|desastre|humano|exito|dolor|duele|silencio|silenciosa|enfadado|"
    r"enfadada|enfado|defensiva|defensivo|amenazante|amenaza|agradecimiento|"
    r"agradeces|invisible|ignorada|ignorado|gusto|regalo|riesgo|perfecto|"
    r"curiosidad|compostura|gracia|apuro|patada)\b", re.I)

ESPECIES = (("persona", PERSONA), ("cuenta", CUENTA), ("escalon", ESCALON),
            ("sentimiento", SENTIMIENTO))

LOTE = ("abrazar_incomodidad_silencio_contar_seis",
        "escuchar_entender_critica_dominar_defensa",
        "premiar_franqueza_hacer_escucha_tangible",
        "integrar_peticion_critica_rutina_existente")

def main():
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
    print()
    print("  EL TRAMO ENTERO: %d pasos, %d de la clase (%s por ciento)"
          % (total_pasos, total_clase,
             ("%.1f" % (100.0 * total_clase / total_pasos)).replace('.', ',')))


if __name__ == "__main__":
    main()
