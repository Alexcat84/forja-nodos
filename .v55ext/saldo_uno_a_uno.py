# -*- coding: utf-8 -*-
"""EL SALDO DE LA ADUANA EN SECO, CANDIDATO A CANDIDATO, LEIDO DE SUS PROPIOS FICHEROS.

Cada fila sale del fichero `.v55ext/aduana_<tag>.txt` que produjo `python forja.py informe`
sobre ESE candidato, en el mismo acto en que se escribio (`EXTRACTOR.md` 16). Aqui no se
recomputa nada: **se lee la salida y se tabula**, con el reloj de cada pasada, que es la cifra
que `D.43` pedia que nadie firmara a ciegas.

CERO CIFRAS TECLEADAS: el veredicto, la poblacion, los vecinos y el reloj se sacan de la
salida con una expresion regular, y el numero de pasos del JSON del candidato.
"""
import io
import json
import os
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

ORDEN = [
    ("cap_07", "P5", "planificar_tres_pasos_demanda_estado_brecha", None),
    ("cap_07", "P8", "definir_entorno_grupo_clientes_proveedores_competidores", "p8"),
    ("cap_07", "P9", "examinar_entorno_expectativas_tecnologia_proveedores_grupos", "p9"),
    ("cap_07", "P10", "examinar_demanda_entorno_dos_marcos_temporales", "p10"),
    ("cap_07", "P12", "determinar_estado_presente_capacidades_proyectos_merma", "p12"),
    ("cap_07", "P14", "cerrar_brecha_dos_preguntas_estrategia", "p14"),
    ("cap_07", "P22", "fijar_horizonte_ventana_replanificacion", "p22"),
    ("cap_07", "P27", "contestar_dos_preguntas_direccion_objetivos", "p27"),
    ("cap_07", "P29", "fijar_periodo_direccion_objetivos_retroalimentacion", "p29"),
    ("cap_10", "P17", "repartir_supervision_puesto_funcional_mision", "c10p17"),
]

RE_VER = re.compile(r"^\[(ENTRARIA|BLOQUEARIA|CAERIA)\]", re.M)
RE_POB = re.compile(r"poblacion del barrido\s*:\s*(\d+)\s*\((\d+) del grafo mas (\d+)")
RE_VEC = re.compile(r"vecinos levantados en total\s*:\s*(\d+)")
RE_REL = re.compile(r"^real\s+(\d+)m([\d.]+)s", re.M)
RE_CAE = re.compile(r"CAERIAN por una guarda\s*:\s*(\d+)")

print("| capitulo | pieza | candidato | pasos | veredicto en seco | poblacion | vecinos | reloj |")
print("|---|---|---|---:|---|---:|---:|---:|")
segundos, corridas, caidas, bloqueos = 0.0, 0, 0, 0
for cap, pieza, cid, tag in ORDEN:
    ruta = "cuarentena/grove_high_output/%s.json" % cid
    pasos = len(json.load(io.open(ruta, encoding="utf-8"))["pasos_accionables"])
    if tag is None:
        print("| `%s` | `%s` | `%s` | %d | escrito y pasado por la VUELTA 53, no por esta | | | |"
              % (cap, pieza, cid, pasos))
        continue
    salida = ".v55ext/aduana_%s.txt" % tag
    if not os.path.exists(salida):
        print("| `%s` | `%s` | `%s` | %d | **SIN CORRER** | | | |" % (cap, pieza, cid, pasos))
        continue
    crudo = io.open(salida, encoding="utf-8").read()
    ver = RE_VER.search(crudo)
    pob = RE_POB.search(crudo)
    vec = RE_VEC.search(crudo)
    rel = RE_REL.search(crudo)
    cae = RE_CAE.search(crudo)
    seg = (int(rel.group(1)) * 60 + float(rel.group(2))) if rel else 0.0
    segundos += seg
    corridas += 1
    if cae and int(cae.group(1)):
        caidas += 1
    if ver and ver.group(1) == "BLOQUEARIA":
        bloqueos += 1
    print("| `%s` | `%s` | `%s` | %d | **%s** | %s (%s mas %s) | %s | %s s |"
          % (cap, pieza, cid, pasos, ver.group(1) if ver else "?",
             pob.group(1) if pob else "?", pob.group(2) if pob else "?",
             pob.group(3) if pob else "?",
             vec.group(1) if vec else "0",
             ("%.1f" % seg).replace(".", ",")))
print("")
print("    PASADAS DE ADUANA CORRIDAS EN ESTA VUELTA, una por candidato nuevo : %d" % corridas)
print("    CANDIDATOS QUE CAERIAN POR UNA GUARDA                              : %d" % caidas)
print("    CANDIDATOS QUE BLOQUEARIAN (cola de lectura, no rechazo)           : %d" % bloqueos)
print("    RELOJ SUMADO DE LAS PASADAS                                        : %s s"
      % ("%.1f" % segundos).replace(".", ","))
print("    RELOJ MEDIO POR PASADA                                             : %s s"
      % ("%.1f" % (segundos / corridas if corridas else 0)).replace(".", ","))
