# -*- coding: utf-8 -*-
"""CERO CONSTANTES TECLEADAS DENTRO: ni una lista de ids, ni un nombre de fichero.
La carpeta llega por argumento y el resto sale del dato. REMEDIO 4 de la ACTA 30.

Cuenta pasos, unidad de origen y lineas citadas de cada candidato de una bandeja.
La UNIDAD y las LINEAS se sacan del propio resumen_teorico con una expresion, no
de una tabla mia. CERO ESCRITURAS.

    python .marquet_v1/censo_pasos.py cuarentena/marquet_turn_the_ship
"""
import io, json, glob, os, re, sys
sys.path.insert(0, os.path.abspath('.'))
from src import comun

comun.salida_utf8()
carpeta = sys.argv[1].replace(chr(92), '/').rstrip('/')

UNIDAD = re.compile(r"UNIDAD DE ORIGEN:\s*([^,]+)")
# DOS FORMAS, Y LA SEGUNDA ME FALTABA: los resumenes escriben `linea 29` y tambien
# `L27`. Con solo la primera, la correccion declarada de esta vuelta (paso 4 de L27
# mas L29) no salia en la columna, y la columna promete TODAS las lineas citadas.
LINEA = re.compile(r"(?:linea[s]?\s+|\bL)(\d+)")

total = 0
filas = []
for ruta in sorted(glob.glob(carpeta + '/*.json')):
    d = json.load(io.open(ruta, encoding='utf-8'))
    pasos = d.get('pasos_accionables') or []
    resumen = d.get('resumen_teorico') or ''
    u = UNIDAD.search(resumen)
    unidad = os.path.basename(u.group(1).strip()) if u else '(sin UNIDAD DE ORIGEN)'
    lineas = sorted(set(int(x) for x in LINEA.findall(resumen)))
    total += len(pasos)
    filas.append((os.path.basename(ruta)[:-5], unidad, len(pasos), lineas,
                  len(d.get('denominaciones', {}).get('otros_idiomas') or []),
                  d.get('fuentes')[0].get('fecha') if d.get('fuentes') else ''))

print("BANDEJA %s : %d candidatos" % (carpeta, len(filas)))
print("")
print("%-52s %-12s %5s %4s %-10s %s" % ('id', 'unidad', 'pasos', 'den', 'fecha', 'lineas citadas en el resumen'))
for i, u, n, l, den, fecha in filas:
    print("%-52s %-12s %5d %4d %-10s %s" % (i, u, n, den, fecha, l))
print("")
print("PASOS ESCRITOS EN LA BANDEJA: %d" % total)
por_unidad = {}
for _i, u, n, _l, _d, _f in filas:
    por_unidad[u] = por_unidad.get(u, 0) + n
for u in sorted(por_unidad):
    print("  %-14s %4d pasos" % (u, por_unidad[u]))
