# -*- coding: utf-8 -*-
"""LA TANDA DE LA VUELTA 31, CONTADA DEL DATO Y NO DE MI MEMORIA.

Para cada candidato del tramo, en el orden del libro: si vive en el grafo, cuantos
vecinos le levanto la aduana, que veredicto lleva cada uno, y cuantas aristas quedan
cableadas. Todo sale de `dataset/nodos.jsonl` y de `bitacora/VEREDICTOS.jsonl`.
"""
import glob
import json
import os

TANDA = [
    "decidir_quien_comunica_cada_cuanto",
    "montar_reuniones_solas_mentalidad_frecuencia",
    "preguntar_seguimiento_hallar_huecos",
    "nutrir_ideas_nuevas_reunion_solas",
    "leer_seniales_fallo_jefe_reunion_solas",
    "conducir_reunion_equipo_agenda_tres_bloques",
    "escribir_apuntes_sala_estudio_equipo",
    "montar_reunion_gran_debate",
    "montar_reunion_gran_decision",
    "montar_reunion_general_presentaciones_preguntas",
    "pelear_proliferacion_reuniones_bloquear_ejecucion",
]
HOY = "2026-09-16"
# LA FECHA NO BASTA PARA SEPARAR MI VUELTA DE LA ANTERIOR: la vuelta 30 corrio el
# MISMO DIA, asi que filtrar por fecha me contaba nueve aristas suyas como mias.
# Lo que separa las dos es la LINEA: la bitacora tenia 375 al abrir mi turno
# (.v31/apertura_tabla.txt), asi que lo mio empieza en la 376.
LINEAS_AL_ABRIR = 375

grafo = {}
for linea in open("dataset/nodos.jsonl", encoding="utf-8"):
    datos = json.loads(linea)
    grafo[datos["id"]] = datos

veredictos = []
for numero, linea in enumerate(open("bitacora/VEREDICTOS.jsonl", encoding="utf-8"), 1):
    registro = json.loads(linea)
    registro["_linea"] = numero
    veredictos.append(registro)

print("LA TANDA DE cap_11, UNO POR VEZ Y EN EL ORDEN DEL LIBRO")
print()
print("| # | id | en el grafo | vecinos que levanto la aduana | veredictos escritos | aristas cableadas |")
print("|---:|---|---|---|---|---|")
for indice, identificador in enumerate(TANDA, 1):
    vive = "SI" if identificador in grafo else "**NO**"
    lineas = [v for v in veredictos
              if v.get("candidato") == identificador and v.get("fecha") == HOY
              and not v.get("arista_en_cola")]
    conjuez = [v for v in lineas if v.get("levantada_por") != ["lectura declarada"]]
    clases = ", ".join("`%s` %s" % (v["veredicto"], v["vecino"]) for v in conjuez) or "cola vacia"
    nodo = grafo.get(identificador, {})
    salientes = nodo.get("nodos_siguientes") or []
    entrantes = nodo.get("nodos_previos") or []
    aristas = (("madre de %d" % len(salientes)) if salientes else "") \
        + (" / " if salientes and entrantes else "") \
        + (("hija de %d" % len(entrantes)) if entrantes else "")
    print("| %d | `%s` | **%s** | **%d** | %s | %s |"
          % (indice, identificador, vive, len(conjuez), clases, aristas or "ninguna"))

print()
print("| | |")
print("|---|---:|")
print("| candidatos del tramo | **%d** |" % len(TANDA))
print("| **de ellos, dentro del grafo** | **%d** |"
      % sum(1 for i in TANDA if i in grafo))
print("| **de ellos, archivados en `cuarentena/_insertados/`** | **%d** |"
      % sum(1 for i in TANDA
            if os.path.exists("cuarentena/_insertados/scott_radical_candor/%s.json" % i)))
print("| **de ellos, que siguen en bandeja** | **%d** |"
      % sum(1 for i in TANDA
            if os.path.exists("cuarentena/scott_radical_candor/%s.json" % i)))
vecinos = sum(1 for v in veredictos if v.get("fecha") == HOY
              and v.get("candidato") in TANDA
              and v.get("levantada_por") != ["lectura declarada"]
              and not v.get("arista_en_cola"))
print("| vecinos levantados y juzgados en la tanda | **%d** |" % vecinos)
lectura = [v for v in veredictos if v["_linea"] > LINEAS_AL_ABRIR
           and v.get("levantada_por") == ["lectura declarada"]]
print("| **aristas declaradas por LECTURA en esta vuelta** (`forja.py arista`) | **%d** |"
      % len(lectura))
print("| lineas nuevas de `bitacora/VEREDICTOS.jsonl` | **%d** |"
      % (len(veredictos) - LINEAS_AL_ABRIR))
print("| nodos en el grafo | **%d** |" % len(grafo))
print("| bandeja del lote 4 | **%d** |"
      % len(glob.glob("cuarentena/scott_radical_candor/*.json")))
print("| archivados del lote 4 | **%d** |"
      % len(glob.glob("cuarentena/_insertados/scott_radical_candor/*.json")))
