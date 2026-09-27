# -*- coding: utf-8 -*-
"""La identidad se lee de git, nunca se teclea (EXTRACTOR.md 5)."""
import subprocess
def git(*a): return subprocess.check_output(["git"]+list(a)).decode("utf-8","replace").strip()
APERTURA = "6315b30"
log = git("log", "--format=%h|%ad|%s", "--date=format:%Y-%m-%d %H:%M:%S", "%s^..HEAD" % APERTURA)
filas = [l.split("|", 2) for l in log.split("\n") if l.strip()][::-1]
mios = [f for f in filas if f[2].startswith("V.34") or f[2].startswith("Apertura de la vuelta 34")]
print("| pieza | valor | de donde sale |")
print("|---|---|---|")
print("| rama | `%s` | `git rev-parse --abbrev-ref HEAD` |" % git("rev-parse","--abbrev-ref","HEAD"))
print("| commit que abrio mi turno | `%s` | `git log` |" % APERTURA)
print("| commit al escribir este bloque | `%s` | `git log` |" % git("rev-parse","--short","HEAD"))
print("| commits en la ventana de mi turno | **%d** | `git log` |" % len(filas))
print("| de ellos, MIOS | **%d** | el asunto empieza por `V.34` o por la apertura |" % len(mios))
print("| de ellos, de otra sesion | **%d** | `git log` |" % (len(filas)-len(mios)))
print("")
print("    LA VENTANA ENTERA, DEL PRIMERO AL ULTIMO. `>` marca los que NO son mios:")
for h, f, s in filas:
    marca = "  " if (s.startswith("V.34") or s.startswith("Apertura de la vuelta 34")) else "> "
    print("    %s%s  %s  %s" % (marca, h, f, s[:96]))
