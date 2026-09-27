# secciones.py adaptado de .v1g_auditor/secciones.py (sede del auditor, no se toca) para
# el bloque G5 de esta vuelta, contra docs/loop/REPORTE.md. Toda referencia G5.x que el
# bloque escribe, contra los encabezados que el propio bloque tiene. CERO CONSTANTES: el
# inicio del bloque se busca por su propio encabezado de vuelta y las referencias salen por
# patron. EXTRACTOR.md 2.2 de esta vuelta: es el mismo instrumento de 14 lineas, corrido
# sobre otro bloque, no maquinaria nueva.
import re, sys
texto = open('docs/loop/REPORTE.md', encoding='utf-8', errors='replace').read().splitlines()
ini = max(i for i, l in enumerate(texto) if l.startswith('# FRENTE `gerber_emyth`, VUELTA 5'))
bloque = texto[ini:]
print("el bloque del frente empieza en la linea", ini + 1, "de docs/loop/REPORTE.md")
encabezados = set()
for l in bloque:
    m = re.match(r'^#{2,4}\s+(G5\.[0-9]+(?:\.[a-z])?)\.', l)
    if m: encabezados.add(m.group(1))
refs = {}
for n, l in enumerate(bloque):
    for m in re.finditer(r'`(G5\.[0-9]+(?:\.[a-z])?)`', l):
        refs.setdefault(m.group(1), []).append(ini + n + 1)
print("secciones que el bloque TIENE      :", len(encabezados), " ", " ".join(sorted(encabezados)))
print("secciones que el bloque CITA       :", len(refs), " ", " ".join(sorted(refs)))
falta = sorted(r for r in refs if r not in encabezados)
print("CITADAS Y QUE NO EXISTEN           :", len(falta))
for f in falta:
    print("   ", f, "citada en la(s) linea(s)", refs[f])
