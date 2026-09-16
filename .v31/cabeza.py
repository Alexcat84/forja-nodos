# -*- coding: utf-8 -*-
"""LOS DIEZ ROTULOS QUE LA CABEZA DE cap_11 ENUMERA, Y CUAL DE ELLOS ES NODO HOY.

El paso 6 de `decidir_quien_comunica_cada_cuanto` enumera las diez herramientas que
el libro lista en `L17` a `L35`, una por linea. Esta tabla dice, para cada una, si
existe como nodo y si la arista cabeza a parte esta cableada. **Comprobar cuales
existen es mirar una lista** (`EXTRACTOR.md` 15.6).
"""
import json
import os

CABEZA = "decidir_quien_comunica_cada_cuanto"

# LOS DIEZ ROTULOS EN EL ORDEN DE L17 A L35, con el nodo que los procedimenta.
# El nodo lo pongo yo leyendo; lo que la maquina pone es si vive y si esta cableado.
ROTULOS = [
    ("1:1 Conversations", "L17", "montar_reuniones_solas_mentalidad_frecuencia"),
    ("Staff Meetings", "L19", "conducir_reunion_equipo_agenda_tres_bloques"),
    ("Think Time", "L21", "bloquear_tiempo_pensar_calendario"),
    ("Big Debate Meetings", "L23", "montar_reunion_gran_debate"),
    ("Big Decision Meetings", "L25", "montar_reunion_gran_decision"),
    ("All-Hands Meetings", "L27", "montar_reunion_general_presentaciones_preguntas"),
    ("Meeting-Free Zones", "L29", ""),
    ("Kanban Boards", "L31", "montar_tablero_kanban_medir_actividades"),
    ("Walk Around", "L33", "pasear_organizacion_hallar_problemas_pequenios"),
    ("Be Conscious of Culture", "L35", "debatir_decidir_asuntos_cultura_evitar_delegar"),
]

grafo = {}
for linea in open("dataset/nodos.jsonl", encoding="utf-8"):
    datos = json.loads(linea)
    grafo[datos["id"]] = datos

hijos = set(grafo[CABEZA].get("nodos_siguientes") or [])

print("LOS DIEZ ROTULOS DE L17 A L35 QUE EL PASO 6 DE LA CABEZA ENUMERA")
print("cabeza: %s" % CABEZA)
print()
print("| # | rotulo del libro | linea | nodo que lo procedimenta | donde esta | arista cabeza a parte |")
print("|---:|---|---|---|---|---|")
for indice, (rotulo, linea, identificador) in enumerate(ROTULOS, 1):
    if not identificador:
        donde, arista = "**no hay nodo**", "**no se declara**"
        identificador = "(ninguno)"
    elif identificador in grafo:
        donde = "en el grafo"
        arista = "**CABLEADA**" if identificador in hijos else "**NO, y se dice por que**"
    elif os.path.exists("cuarentena/scott_radical_candor/%s.json" % identificador):
        donde, arista = "en bandeja", "espera a que entre"
    else:
        donde, arista = "**no esta**", "**no se puede**"
    print("| %d | %s | `%s` | `%s` | %s | %s |"
          % (indice, rotulo, linea, identificador, donde, arista))

print()
print("| | |")
print("|---|---:|")
print("| rotulos que el paso 6 enumera | **%d** |" % len(ROTULOS))
print("| **de ellos, con nodo dentro del grafo hoy** | **%d** |"
      % sum(1 for _r, _l, i in ROTULOS if i and i in grafo))
print("| **de ellos, con la arista cabeza a parte cableada** | **%d** |"
      % sum(1 for _r, _l, i in ROTULOS if i and i in hijos))
print("| de ellos, con su nodo todavia en bandeja | **%d** |"
      % sum(1 for _r, _l, i in ROTULOS if i and i not in grafo
            and os.path.exists("cuarentena/scott_radical_candor/%s.json" % i)))
print("| de ellos, sin nodo ninguno | **%d** |"
      % sum(1 for _r, _l, i in ROTULOS if not i))
print("| hijos que la cabeza declara en `nodos_siguientes` | **%d** |" % len(hijos))
