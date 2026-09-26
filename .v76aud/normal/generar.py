# ACTA 75: pega la salida literal de cada bloque `$`. En la plantilla, una linea "    $ <comando>" seguida de una linea
# "    {{SALIDA}}" se sustituye por el comando y lo que imprime al correrlo ahora, sangrado con cuatro espacios. Uso:
#     python .v76aud/normal/generar.py <plantilla> <salida>
import io, subprocess, sys
BASH = r"C:\Program Files\Git\usr\bin\bash.exe"  # el bash de Git, no el de WSL
ent, sal = sys.argv[1:3]
L = io.open(ent, encoding="utf-8").read().split("\n")
out = []; i = 0
while i < len(L):
    l = L[i]
    if l.startswith("    $ ") and i + 1 < len(L) and L[i + 1].strip() == "{{SALIDA}}":
        r = subprocess.run([BASH, "-c", l[6:]], capture_output=True)
        txt = (r.stdout + r.stderr).decode("utf-8", "replace").replace("\r", "").rstrip("\n")
        out.append(l)
        out += ["    " + x if x else "" for x in txt.split("\n")] if txt else []
        i += 2; continue
    out.append(l); i += 1
io.open(sal, "w", encoding="utf-8", newline="\n").write("\n".join(out))
