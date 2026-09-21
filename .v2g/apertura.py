# -*- coding: utf-8 -*-
"""LA APERTURA DE LA VUELTA 2 DEL FRENTE grove_high_output, MEDIDA ANTES DE LA
PRIMERA OPERACION DE EXTRACCION (EXTRACTOR.md 4).

CERO CELDAS TECLEADAS DENTRO DEL INSTRUMENTO.

Y EL REMEDIO BLOQUEANTE QUE ESTA VUELTA HEREDA (PARA_ALEXIS.md 4, ultimo bloque,
D.38.3 ensanchada por extension de su propio motivo): TODA CIFRA DE POBLACION SE
PUBLICA CON EL ROTULO DE LA POBLACION QUE EL INSTRUMENTO MIDIO. Por eso cada fila
de poblacion de esta tabla dice, en su propia celda, SOBRE QUE conjunto se conto,
y ninguna dice "en el grafo" ni "capitulo entero" sin que eso sea lo medido.
"""
import collections
import glob
import io
import json
import os
import subprocess
import sys

sys.path.insert(0, os.getcwd())
from src import aduana          # SOLO PARA LEER: la poblacion la define la aduana

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

CLAVE = "grove_high_output"


def git(*args):
    return subprocess.check_output(("git",) + args).decode("utf-8", "replace").strip()


def lineas(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return sum(1 for _ in f)


nodos = sig = prev = 0
for linea in io.open("dataset/nodos.jsonl", encoding="utf-8"):
    datos = json.loads(linea)
    nodos += 1
    sig += len(datos.get("nodos_siguientes") or [])
    prev += len(datos.get("nodos_previos") or [])

nocons = 0
for linea in io.open("bitacora/VEREDICTOS.jsonl", encoding="utf-8"):
    datos = json.loads(linea)
    if any(a.get("no_consumada") is True for a in (datos.get("anotaciones") or [])):
        nocons += 1

unidades = sorted(glob.glob("fuentes/%s/cap_*.md" % CLAVE))
palabras_cuerpo = 0
for ruta in unidades:
    texto = io.open(ruta, encoding="utf-8").read().split("\n")
    palabras_cuerpo += len(" ".join(texto[7:]).split())

poblacion_bandejas = aduana.poblacion_de_bandejas()
en_bandejas = len(poblacion_bandejas)
bandejas = collections.Counter(f["clave"] for n in poblacion_bandejas
                               for f in (n.get("fuentes") or []))
ficheros_en_cuarentena = len([r for r in glob.glob("cuarentena/*/*.json")
                              if "_insertados" not in r])
mios = sorted(glob.glob("cuarentena/%s/*.json" % CLAVE))
pasos_mios = 0
capitulos_minados = collections.Counter()
for ruta in mios:
    datos = json.loads(io.open(ruta, encoding="utf-8").read())
    pasos_mios += len(datos.get("pasos_accionables") or [])
    resumen = datos.get("resumen_teorico") or ""
    for cap in ("cap_%02d" % n for n in range(1, 19)):
        if cap + ".md" in resumen:
            capitulos_minados[cap] += 1
            break

print("LA APERTURA DE LA VUELTA 2 DEL FRENTE %s" % CLAVE)
print("CADA FILA DE POBLACION LLEVA EL ROTULO DE LO QUE SE CONTO (remedio bloqueante)")
print()
filas = [
    ("rama", "`" + git("rev-parse", "--abbrev-ref", "HEAD") + "`",
     "`git rev-parse --abbrev-ref HEAD`"),
    ("commit al abrir mi turno, ya intermedio", "`" + git("rev-parse", "--short", "HEAD") + "`",
     "`git rev-parse --short HEAD`"),
    ("nodos en `dataset/nodos.jsonl`, el grafo entero", "**%d**" % nodos,
     "`dataset/nodos.jsonl`"),
    ("aristas por `nodos_siguientes`, sobre el grafo entero", "**%d**" % sig,
     "`dataset/nodos.jsonl`"),
    ("aristas por `nodos_previos`, sobre el grafo entero", "**%d**" % prev,
     "`dataset/nodos.jsonl`"),
    ("veredictos en `bitacora/VEREDICTOS.jsonl`, el fichero entero",
     "**%d**" % lineas("bitacora/VEREDICTOS.jsonl"), "`bitacora/VEREDICTOS.jsonl`"),
    ("de esos veredictos, con `no_consumada: true`", "**%d**" % nocons,
     "`bitacora/VEREDICTOS.jsonl`"),
    ("unidades del libro `%s`, las 18 del fichero" % CLAVE, "**%d**" % len(unidades),
     "PATRON: `fuentes/%s/cap_*.md`" % CLAVE),
    ("palabras de cuerpo de esas 18 unidades, de `L8` en adelante",
     "**%s**" % "{:,}".format(palabras_cuerpo).replace(",", "."),
     "PATRON: `fuentes/%s/cap_*.md`" % CLAVE),
    ("candidatos en bandeja de ESTE libro, escritos por la vuelta 1", "**%d**" % len(mios),
     "PATRON: `cuarentena/%s/*.json`" % CLAVE),
    ("pasos escritos en esos candidatos de ESTE libro", "**%d**" % pasos_mios,
     "PATRON: `cuarentena/%s/*.json`" % CLAVE),
    ("ficheros `.json` en TODAS las bandejas, contados a ojo",
     "**%d**" % ficheros_en_cuarentena, "PATRON: `cuarentena/*/*.json`"),
    ("de esos ficheros, los que la ADUANA admite al barrido", "**%d**" % en_bandejas,
     "`src/aduana.py`, `poblacion_de_bandejas()`"),
    ("POBLACION QUE VERA CADA INFORME MIO: grafo mas bandejas admitidas",
     "**%d**" % (nodos + en_bandejas),
     "`dataset/nodos.jsonl` mas `src/aduana.py`, `poblacion_de_bandejas()`"),
]
print("| pieza, con el rotulo de lo que se conto | valor | de donde sale |")
print("|---|---:|---|")
for a, b, c in filas:
    print("| %s | %s | %s |" % (a, b, c))
print()
print("REPARTO DE LA POBLACION DE BANDEJAS, con su reparto (D.38.5)")
for k, v in sorted(bandejas.items()):
    print("  %-28s %4d" % (k, v))
print("  FUERA DEL BARRIDO               %4d   (cuarentena/ensayo_referencia_163/,"
      % (ficheros_en_cuarentena - en_bandejas))
print("                                        clave quality_is_free_the, no canonica)")
print()
print("REPARTO DE MI PROPIA BANDEJA POR UNIDAD DE ORIGEN, leido del resumen_teorico")
for k, v in sorted(capitulos_minados.items()):
    print("  %-28s %4d" % (k, v))
print("  SIN MINAR TODAVIA               %4d unidades de las %d"
      % (len(unidades) - len(capitulos_minados), len(unidades)))
