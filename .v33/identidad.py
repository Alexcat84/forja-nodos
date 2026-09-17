# -*- coding: utf-8 -*-
"""LA IDENTIDAD DEL CIERRE, LEIDA DE GIT (EXTRACTOR.md 5).

*Todo hash, nombre de commit, rama o fecha de apertura o de cierre se lee de
`git rev-parse` o `git log` en esa vuelta. Una linea de identidad tecleada no se publica.*

Es el instrumento de la vuelta 32 (`.v32/identidad.py`) apuntado a esta.
"""
import io
import os
import subprocess
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def git(*args):
    return subprocess.check_output(["git"] + list(args), cwd=RAIZ).decode().strip()


APERTURA = "Apertura de la vuelta 33: el esqueleto del reporte abierto"

commits = git("log", "--format=%h|%ad|%s", "--date=format:%Y-%m-%d %H:%M:%S", "-40").split("\n")
mios = []
for linea in commits:
    hash_corto, fecha, asunto = linea.split("|", 2)
    mios.append((hash_corto, fecha, asunto))
    if asunto.startswith(APERTURA):
        break

print("| pieza | valor | de donde sale |")
print("|---|---|---|")
print("| rama | `%s` | `git rev-parse --abbrev-ref HEAD` |"
      % git("rev-parse", "--abbrev-ref", "HEAD"))
print("| commit que abrio mi turno | `%s`, %s | `git log` |" % (mios[-1][0], mios[-1][1]))
print("| commit al escribir este bloque | `%s`, %s | `git log` |" % (mios[0][0], mios[0][1]))
print("| commits de esta vuelta | **%d** | `git log` |" % len(mios))
print("")
print("LOS COMMITS DE ESTA VUELTA, DEL PRIMERO AL ULTIMO:")
for hash_corto, fecha, asunto in reversed(mios):
    print("  %s  %s  %s" % (hash_corto, fecha, asunto[:96]))
