# -*- coding: utf-8 -*-
"""LAS CIFRAS DE APERTURA Y CIERRE DE LA VUELTA 34, RECONTADAS POR MI DEL FICHERO.

La columna 'yo' sale de contar dataset/nodos.jsonl, bitacora/VEREDICTOS.jsonl y las
carpetas de cuarentena; NUNCA de leer la tabla del reporte. La columna 'el reporte'
la tecleo yo del documento que audito, que es lo unico que se puede hacer con una
afirmacion ajena, y por eso la columna que manda es la mia.

La base es b698aef, ultimo commit antes de la primera tarea; el cierre es HEAD.
"""
import io, json, os, subprocess, sys
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

BASE = "b698aef"

def _texto(ref, ruta):
    if ref is None:
        return io.open(ruta, encoding="utf-8").read()
    return subprocess.check_output(["git", "show", "%s:%s" % (ref, ruta)]).decode("utf-8")

def _cuenta_dir(ref, ruta):
    if ref is None:
        return len([f for f in os.listdir(ruta) if f.endswith(".json")])
    salida = subprocess.check_output(["git", "ls-tree", "--name-only", ref, ruta + "/"])
    return len([l for l in salida.decode("utf-8").split("\n") if l.endswith(".json")])

def medidas(ref):
    nodos = [json.loads(l) for l in _texto(ref, "dataset/nodos.jsonl").split("\n") if l.strip()]
    ver = [json.loads(l) for l in _texto(ref, "bitacora/VEREDICTOS.jsonl").split("\n") if l.strip()]
    ins = _cuenta_dir(ref, "cuarentena/_insertados/scott_radical_candor")
    return {
        "nodos en `dataset/nodos.jsonl`": len(nodos),
        "pasos del grafo entero": sum(len(n["pasos_accionables"]) for n in nodos),
        "lineas en `bitacora/VEREDICTOS.jsonl`": len(ver),
        "de ellas, `consumada: false`": sum(1 for v in ver if v.get("consumada") is False),
        "aristas por `nodos_siguientes`": sum(len(n.get("nodos_siguientes", [])) for n in nodos),
        "aristas por `nodos_previos`": sum(len(n.get("nodos_previos", [])) for n in nodos),
        "candidatos en bandeja, lote 4": _cuenta_dir(ref, "cuarentena/scott_radical_candor"),
        "insertados y archivados, lote 4": ins,
        "candidatos en bandeja, lote 5": _cuenta_dir(ref, "cuarentena/marquet_turn_the_ship"),
        "lote 4 insertado sobre `142`, por ciento": round(100.0 * ins / 142, 1),
    }

# LO QUE EL REPORTE PUBLICA, tecleado por mi de AA.0 y de AA.5 para poder enfrentarlo.
SUYO_ABRE = [282, None, 410, 14, 107, 107, 63, 79, 3, 55.6]
SUYO_CIERRA = [297, None, 423, 14, 108, 108, 48, 94, 3, 66.2]

a, c = medidas(BASE), medidas(None)
filas = list(a.keys())
print("| pieza | **yo, sobre `%s`** | el reporte, `AA.0` | **yo, sobre `HEAD`** | el reporte, `AA.5` | |" % BASE)
print("|---|---:|---:|---:|---:|---|")
caen = 0
for i, k in enumerate(filas):
    sa, sc = SUYO_ABRE[i], SUYO_CIERRA[i]
    if sa is None:
        print("| %s | **%s** | . | **%s** | . | *no lo publica* |" % (k, a[k], c[k]))
        continue
    bien = (a[k] == sa) and (c[k] == sc)
    caen += 0 if bien else 1
    print("| %s | **%s** | %s | **%s** | %s | %s |"
          % (k, a[k], sa, c[k], sc, "AL DIGITO" if bien else "**DISCREPA**"))
print()
print("filas comparables: %d   AL DIGITO: %d   DISCREPAN: %d" % (len(SUYO_ABRE) - 1, len(SUYO_ABRE) - 1 - caen, caen))
print("142 de la tabla del lote: %d en bandeja mas %d archivados = %d"
      % (c["candidatos en bandeja, lote 4"], c["insertados y archivados, lote 4"],
         c["candidatos en bandeja, lote 4"] + c["insertados y archivados, lote 4"]))
