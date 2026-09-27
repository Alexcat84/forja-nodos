# -*- coding: utf-8 -*-
"""LAS CIFRAS DEL CIERRE, RECOMPUTADAS AL CIERRE (EXTRACTOR.md 4).

*El estado al cierre se mide al cierre. Toda cifra que describa el estado al cerrar
se RECOMPUTA si algo de la propia vuelta pudo haberla movido.*

Es el instrumento de la vuelta 32 (`.v32/cuentas_cierre.py`) apuntado a esta: `D.47`
manda cero instrumentos nuevos, y este no lo es. Lo unico que cambia respecto de aquel
es que **el total del lote 4 tampoco se teclea**: sale de sumar bandeja mas archivo.
"""
import glob
import io
import json
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

# LA APERTURA SALE DE .v33/apertura_tabla.txt, que es el instrumento que la midio,
# no de la memoria.
APERTURA = {}
for linea in io.open(".v33/apertura_tabla.txt", encoding="utf-8"):
    if not linea.startswith("|") or "---" in linea:
        continue
    celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
    if len(celdas) != 3:
        continue
    crudo = celdas[1].replace("*", "").replace(",", ".")
    try:
        APERTURA[celdas[0]] = float(crudo) if "." in crudo else int(crudo)
    except ValueError:
        pass


def pruebas_de(ruta):
    for linea in io.open(ruta, encoding="utf-8"):
        if "total:" in linea:
            return int(linea.split("total:")[1].split("pruebas")[0].strip())
    raise SystemExit("no encuentro el total de pruebas en %s" % ruta)


APERTURA["pruebas de `tests/test_aceptacion.py`"] = pruebas_de(".v33/aceptacion_apertura.txt")

sig = prev = nodos = 0
for linea in io.open("dataset/nodos.jsonl", encoding="utf-8"):
    datos = json.loads(linea)
    nodos += 1
    sig += len(datos.get("nodos_siguientes") or [])
    prev += len(datos.get("nodos_previos") or [])

veredictos = nocons = 0
for linea in io.open("bitacora/VEREDICTOS.jsonl", encoding="utf-8"):
    veredictos += 1
    datos = json.loads(linea)
    if any(a.get("no_consumada") is True for a in (datos.get("anotaciones") or [])):
        nocons += 1

bandeja4 = len(glob.glob("cuarentena/scott_radical_candor/*.json"))
insertados = len(glob.glob("cuarentena/_insertados/scott_radical_candor/*.json"))
total4 = bandeja4 + insertados

CIERRE = {
    "nodos en `dataset/nodos.jsonl`": nodos,
    "veredictos en `bitacora/VEREDICTOS.jsonl`": veredictos,
    "de ellos, con alguna anotacion `no_consumada: true`": nocons,
    "aristas por `nodos_siguientes`": sig,
    "aristas por `nodos_previos`": prev,
    "candidatos en bandeja, lote 4": bandeja4,
    "insertados y archivados, lote 4": insertados,
    "candidatos en bandeja, lote 5":
        len(glob.glob("cuarentena/marquet_turn_the_ship/*.json")),
    "pruebas de `tests/test_aceptacion.py`": pruebas_de(".v33/aceptacion_cierre.txt"),
}

ORDEN = ["nodos en `dataset/nodos.jsonl`",
         "aristas por `nodos_siguientes`",
         "aristas por `nodos_previos`",
         "veredictos en `bitacora/VEREDICTOS.jsonl`",
         "de ellos, con alguna anotacion `no_consumada: true`",
         "candidatos en bandeja, lote 4",
         "insertados y archivados, lote 4",
         "candidatos en bandeja, lote 5",
         "pruebas de `tests/test_aceptacion.py`"]

print("| pieza | al abrir | **al cerrar** | movimiento |")
print("|---|---:|---:|---:|")
for clave in ORDEN:
    antes, ahora = APERTURA[clave], CIERRE[clave]
    salto = ahora - antes
    print("| %s | %d | **%d** | %s |"
          % (clave, antes, ahora, ("**%+d**" % salto) if salto else "0"))

antes = APERTURA["lote 4 insertado sobre `%d`, por ciento" % total4]
ahora = 100.0 * insertados / total4
print("| lote 4 insertado sobre `%d`, por ciento | %s | **%s** | **%s** |"
      % (total4,
         ("%.1f" % antes).replace(".", ","),
         ("%.1f" % ahora).replace(".", ","),
         ("%+.1f" % (ahora - antes)).replace(".", ",")))
