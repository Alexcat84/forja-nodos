# -*- coding: utf-8 -*-
"""CERO CONSTANTES TECLEADAS DENTRO: ni un termino, ni un id, ni un nombre de fichero.
Los terminos salen de denominaciones.otros_idiomas de cada candidato y la unidad sale
de su propio resumen_teorico. REMEDIO 4 de la ACTA 30. CERO ESCRITURAS sobre el arbol.

Comprueba si cada termino extranjero que un candidato publica aparece de verdad en la
unidad de la que el candidato dice salir.

    python .marquet_v1/denominaciones.py cuarentena/marquet_turn_the_ship
"""
import io, json, glob, os, re, sys
sys.path.insert(0, os.path.abspath('.'))
from src import comun

comun.salida_utf8()
carpeta = sys.argv[1].replace(chr(92), '/').rstrip('/')
UNIDAD = re.compile(r"UNIDAD DE ORIGEN:\s*(\S+)")

print("%-46s %-28s %-12s %s" % ('candidato', 'termino', 'en su unidad', 'lineas'))
faltan = total = 0
for ruta in sorted(glob.glob(carpeta + '/*.json')):
    d = json.load(io.open(ruta, encoding='utf-8'))
    m = UNIDAD.search(d.get('resumen_teorico') or '')
    fuente = m.group(1).rstrip(',') if m else None
    texto = (io.open(fuente, encoding='utf-8').read().split('\n')
             if fuente and os.path.exists(fuente) else [])
    for t in (d.get('denominaciones', {}).get('otros_idiomas') or []):
        term = t.get('termino', '')
        total += 1
        hits = [n for n, l in enumerate(texto, 1) if term.lower() in l.lower()]
        if not hits:
            faltan += 1
        print("%-46s %-28s %-12s %s"
              % (d['id'][:46], term, 'SI' if hits else 'NO', hits[:5]))
print("")
print("TERMINOS COMPROBADOS                          : %d" % total)
print("TERMINOS QUE NO APARECEN EN SU PROPIA UNIDAD  : %d" % faltan)
