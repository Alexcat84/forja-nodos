# -*- coding: utf-8 -*-
"""TAREA BLOQUEANTE DE LA ACTA 41: toda seccion que me cito A MI MISMO existe en MI fichero.

Una remision es AJENA si su propia linea nombra otro documento (AUDITOR_FORJA.md,
EXTRACTOR.md, el manual, una ACTA anterior, una regla D.x o la cosecha). El resto son
PROPIAS y son las que hay que comprobar. Los numeros con separador de millares
(23.357) no son remisiones y se descartan por su forma.
"""
import io, re, sys
ruta = sys.argv[1]
ini = sys.argv[2] if len(sys.argv) > 2 else None
txt = io.open(ruta, encoding='utf-8').read()
if ini:
    txt = txt[txt.index(ini):]
sec = set()
for m in re.finditer(r'(?m)^#{1,6}\s+([0-9]+(?:\.[0-9a-z]+)*)\.', txt):
    sec.add(m.group(1))
    p = m.group(1).split('.')
    for i in range(1, len(p)):
        sec.add('.'.join(p[:i]))
AJENO = re.compile(r'AUDITOR_FORJA|EXTRACTOR\.md|MANUAL_|manual |cosecha|ACTA \d|`D\.\d|CALIBRACION|REPORTE\.md|de mi protocolo|ED\.')
MILLAR = re.compile(r'^\d+\.\d{3}$')
propias, vacias = [], []
for linea in txt.splitlines():
    for m in re.finditer(r'`([0-9]+(?:\.[0-9a-z]+)*)`|seccion\s+([0-9]+(?:\.[0-9a-z]+)*)', linea):
        r = m.group(1) or m.group(2)
        if MILLAR.match(r) or '.' not in r and not re.search(r'seccion|apertura|acta', linea, re.I):
            continue
        if AJENO.search(linea):
            continue
        if not re.search(r'\.', r) and not re.search(r'seccion', linea):
            continue
        propias.append(r)
        if r not in sec:
            vacias.append((r, linea.strip()[:90]))
print('secciones que este fichero tiene       :', len(sec))
print('remisiones PROPIAS comprobadas         :', len(propias))
print('apuntan a una seccion que NO existe    :', len(vacias))
for r, l in vacias:
    print('   %-6s  %s' % (r, l))
