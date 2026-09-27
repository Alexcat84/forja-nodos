# secciones.py: toda referencia G1.x que el bloque del frente escribe, contra los
# encabezados que el bloque tiene. CERO CONSTANTES: el inicio del bloque se busca
# por su propio encabezado de vuelta y las referencias salen por patron.
import re, sys
texto = open('docs/loop/REPORTE.md', encoding='utf-8', errors='replace').read().splitlines()
ini = max(i for i, l in enumerate(texto) if l.startswith('# FRENTE `gerber_emyth`, VUELTA 1'))
bloque = texto[ini:]
print("el bloque del frente empieza en la linea", ini + 1, "de docs/loop/REPORTE.md")
encabezados = set()
for l in bloque:
    m = re.match(r'^#{2,4}\s+(G1\.[0-9]+(?:\.[a-z])?)\.', l)
    if m: encabezados.add(m.group(1))
refs = {}
for n, l in enumerate(bloque):
    for m in re.finditer(r'`(G1\.[0-9]+(?:\.[a-z])?)`', l):
        refs.setdefault(m.group(1), []).append(ini + n + 1)
print("secciones que el bloque TIENE      :", len(encabezados), " ", " ".join(sorted(encabezados)))
print("secciones que el bloque CITA       :", len(refs), " ", " ".join(sorted(refs)))
falta = sorted(r for r in refs if r not in encabezados)
print("CITADAS Y QUE NO EXISTEN           :", len(falta))
for f in falta:
    print("   ", f, "citada en la(s) linea(s)", refs[f])
