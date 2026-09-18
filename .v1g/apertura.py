# -*- coding: utf-8 -*-
"""LA APERTURA DE LA VUELTA 1 DEL FRENTE grove_high_output, MEDIDA ANTES DE LA
PRIMERA OPERACION DE EXTRACCION (EXTRACTOR.md 4).

CERO CELDAS TECLEADAS DENTRO DEL INSTRUMENTO: las dos unicas constantes que este
fichero contiene son la clave del libro y las dos cifras que el encargo publica y
que aqui se CONTRASTAN, no se copian, y van nombradas en la primera linea de la
salida (caida de la vuelta 31).
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
ENCARGO_UNIDADES = 18        # constante del encargo, para CONTRASTE
ENCARGO_PALABRAS = 64862     # constante del encargo, para CONTRASTE


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
palabras_fichero = palabras_cuerpo = 0
for ruta in unidades:
    texto = io.open(ruta, encoding="utf-8").read().split("\n")
    palabras_fichero += len(" ".join(texto).split())
    palabras_cuerpo += len(" ".join(texto[7:]).split())

# LA POBLACION NO LA CUENTO YO A OJO: LA PIDO A LA ADUANA, que es quien la
# construye (src/aduana.py poblacion_de_bandejas). Mi primer recuento conto los
# ficheros de cuarentena/*/*.json y dio 241, y el informe de la aduana dice 78:
# los 163 de cuarentena/ensayo_referencia_163/ quedan fuera porque su clave
# quality_is_free_the NO esta en fuentes/FUENTES_CANONICAS.json. Publicar 241
# habria sido una cifra tecleada por mi contra la que mide el instrumento.
poblacion_bandejas = aduana.poblacion_de_bandejas()
en_bandejas = len(poblacion_bandejas)
bandejas = collections.Counter(f["clave"] for n in poblacion_bandejas
                               for f in (n.get("fuentes") or []))
ficheros_en_cuarentena = len([r for r in glob.glob("cuarentena/*/*.json")
                              if "_insertados" not in r])

print("LA APERTURA DE LA VUELTA 1 DEL FRENTE %s" % CLAVE)
print("CONSTANTES DEL ENCARGO QUE ESTE INSTRUMENTO SOLO CONTRASTA: unidades=%d, palabras=%d"
      % (ENCARGO_UNIDADES, ENCARGO_PALABRAS))
print()
filas = [
    ("rama", "`" + git("rev-parse", "--abbrev-ref", "HEAD") + "`",
     "`git rev-parse --abbrev-ref HEAD`"),
    ("commit al abrir mi turno", "`" + git("rev-parse", "--short", "HEAD") + "`",
     "`git rev-parse --short HEAD`"),
    ("nodos en `dataset/nodos.jsonl`", "**%d**" % nodos, "`dataset/nodos.jsonl`"),
    ("aristas por `nodos_siguientes`", "**%d**" % sig, "`dataset/nodos.jsonl`"),
    ("aristas por `nodos_previos`", "**%d**" % prev, "`dataset/nodos.jsonl`"),
    ("veredictos en `bitacora/VEREDICTOS.jsonl`", "**%d**" % lineas("bitacora/VEREDICTOS.jsonl"),
     "`bitacora/VEREDICTOS.jsonl`"),
    ("de ellos, con `no_consumada: true`", "**%d**" % nocons, "`bitacora/VEREDICTOS.jsonl`"),
    ("unidades de `%s`" % CLAVE, "**%d**" % len(unidades),
     "PATRON: `fuentes/%s/cap_*.md`" % CLAVE),
    ("palabras de fichero, las 18 unidades", "**%s**" % "{:,}".format(palabras_fichero).replace(",", "."),
     "PATRON: `fuentes/%s/cap_*.md`" % CLAVE),
    ("palabras de cuerpo, de `L8` en adelante", "**%s**" % "{:,}".format(palabras_cuerpo).replace(",", "."),
     "PATRON: `fuentes/%s/cap_*.md`" % CLAVE),
    ("candidatos en bandeja de este libro", "**%d**" % bandejas.get(CLAVE, 0),
     "PATRON: `cuarentena/%s/*.json`. VACIA A PROPOSITO: es la vuelta 1 del frente "
     "y la bandeja se abre hoy" % CLAVE),
    ("ficheros `.json` en las bandejas, contados a ojo", "**%d**" % ficheros_en_cuarentena,
     "PATRON: `cuarentena/*/*.json`"),
    ("de ellos, poblacion que la ADUANA admite al barrido", "**%d**" % en_bandejas,
     "`src/aduana.py`, `poblacion_de_bandejas()`"),
    ("poblacion que vera cada informe mio", "**%d**" % (nodos + en_bandejas),
     "`dataset/nodos.jsonl` mas `src/aduana.py`, `poblacion_de_bandejas()`"),
]
print("| pieza | valor | de donde sale |")
print("|---|---:|---|")
for a, b, c in filas:
    print("| %s | %s | %s |" % (a, b, c))
print()
print("CONTRASTE CONTRA EL ENCARGO (EXTRACTOR.md 5: si discrepan, se declara)")
print("  unidades : encargo %d, medido %d, %s"
      % (ENCARGO_UNIDADES, len(unidades),
         "IGUALES" if ENCARGO_UNIDADES == len(unidades) else "DISCREPAN"))
print("  palabras : encargo %d, medido de fichero %d, %s"
      % (ENCARGO_PALABRAS, palabras_fichero,
         "IGUALES" if ENCARGO_PALABRAS == palabras_fichero else "DISCREPAN"))
print("  y la ficha canonica dice 64.372 de CUERPO; medido de cuerpo %d" % palabras_cuerpo)
print()
print("REPARTO DE LA POBLACION DE BANDEJAS, que es lo que D.38.5 manda citar con su reparto")
for k, v in sorted(bandejas.items()):
    print("  %-28s %4d" % (k, v))
print("  y FUERA DEL BARRIDO             %4d   (los de cuarentena/ensayo_referencia_163/,"
      % (ficheros_en_cuarentena - en_bandejas))
print("                                        clave quality_is_free_the, no canonica)")
