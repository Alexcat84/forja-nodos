# -*- coding: utf-8 -*-
"""Ensambla docs/loop/APERTURA_CIEGA.md desde .v63aud/plantilla.md.

Cada linea de la plantilla que sea exactamente  {{$ <comando>}}  se sustituye por el
bloque pegado: la linea '    $ <comando>' y debajo, sangrada, la salida LITERAL que el
comando imprime ahora (R5 de la ACTA 61: el bloque contiene lo que el comando imprimio
y nada mas). Si una salida pasa de TOPE lineas, se corta POR EL FINAL y se dice
'(recortado, entero en <fichero>)', con la salida entera guardada en ese fichero.

Si al terminar queda un '{{' en la pagina, NO se escribe: una pagina con un hueco sin
rellenar fue lo que tumbo el sello de la segunda fase ciega de esta vuelta.
"""
import io, os, re, subprocess, sys, hashlib

TOPE = 40
# El Git Bash por su ruta: 'bash' a secas resuelve en Windows al de WSL.
BASH = r'C:\Program Files\Git\usr\bin\bash.exe'
plantilla = io.open('.v63aud/plantilla.md', encoding='utf-8').read().split('\n')
salida = []
for linea in plantilla:
    m = re.match(r'^\{\{\$ (.+)\}\}$', linea.strip())
    if not m:
        salida.append(linea)
        continue
    cmd = m.group(1)
    r = subprocess.run([BASH, '-c', cmd], capture_output=True, text=True, encoding='utf-8')
    texto = (r.stdout + r.stderr).rstrip('\n')
    lineas = texto.split('\n') if texto else []
    salida.append('    $ ' + cmd)
    if len(lineas) > TOPE:
        nombre = '.v63aud/pegado_%s.txt' % hashlib.sha1(cmd.encode('utf-8')).hexdigest()[:8]
        io.open(nombre, 'w', encoding='utf-8').write(texto + '\n')
        lineas = lineas[:TOPE] + ['(recortado, entero en %s)' % nombre]
    salida += ['    ' + x if x else '' for x in lineas]
pagina = '\n'.join(salida)
if '{{' in pagina:
    sys.exit('QUEDA UN HUECO SIN RELLENAR: no se escribe la pagina')
io.open('docs/loop/APERTURA_CIEGA.md', 'w', encoding='utf-8', newline='\n').write(pagina)
print('escrita docs/loop/APERTURA_CIEGA.md, %d lineas' % len(salida))
