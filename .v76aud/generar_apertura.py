# Fase ciega de la 76 (copia de .v75aud/generar_apertura.py con la ruta cambiada): arma docs/loop/APERTURA_CIEGA.md desde .v76aud/apertura_plantilla.md, sustituyendo cada
# linea @@RUN:<n>:<fichero>:<comando>@@ por un bloque con '$ <comando>' y la salida LITERAL de correrlo ahora
# (R5: el bloque contiene lo que el comando imprime y nada mas; si n > 0 se corta por el final, dentro del bloque,
# con '(recortado, entero en <fichero>)'). No escribe nada mas que ese fichero.
import io, os, re, subprocess, sys
BASH = 'C:/Program Files/Git/usr/bin/bash.exe'  # el bash de Git Bash; el 'bash' a secas de Windows es el de WSL
sys.stdout.reconfigure(encoding="utf-8")
env = dict(os.environ, PYTHONIOENCODING='utf-8')
out = []
for l in io.open('.v76aud/apertura_plantilla.md', encoding='utf-8'):
    m = re.match(r'^@@RUN:(\d+):([^:]*):(.*)@@\s*$', l)
    if not m:
        out.append(l); continue
    n, fich, cmd = int(m.group(1)), m.group(2), m.group(3)
    r = subprocess.run([BASH, '-c', cmd], capture_output=True, text=True, encoding='utf-8', env=env)
    salida = (r.stdout + r.stderr).rstrip('\n').split('\n')
    out.append('    $ %s\n' % cmd)
    corte = n > 0 and len(salida) > n
    for s in (salida[:n] if corte else salida):
        out.append(('    ' + s).rstrip() + '\n')
    if corte:
        out.append('    (recortado, entero en %s)\n' % fich)
io.open('docs/loop/APERTURA_CIEGA.md', 'w', encoding='utf-8', newline='\n').write(''.join(out))
print('escrito docs/loop/APERTURA_CIEGA.md: %d lineas' % sum(o.count('\n') for o in out))
