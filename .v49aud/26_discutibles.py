# -*- coding: utf-8 -*-
"""LO QUE SOSTIENE O TUMBA CADA DISCUTIBLE MARCADO DE LA VUELTA 49."""
import io, sys, os, re, json, glob, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, 'scripts'); sys.path.insert(0, '.')
import censar_rutas as C

print("== DISCUTIBLE 6: la columna nodo(s) es el pronostico de la frontera, no lo minado")
sal = subprocess.check_output([sys.executable, '.v47aud/44_tramos.py']).decode('utf-8', 'replace')
filas = re.findall(r'^\s+(P\d+[a-z]?)\s+(\d+) palabras\s+(\d+) nodo', sal, re.M)
vistos, pron = set(), 0
for pz, w, n in filas:
    if pz in vistos:
        continue
    vistos.add(pz); pron += int(n)
print("   tramos de la frontera            : %d" % len(vistos))
print("   nodos PRONOSTICADOS por la columna: %d" % pron)
minadas = [f for f in sorted(glob.glob('cuarentena/grove_high_output/*.json'))
           if 'cap_04.md' in json.loads(io.open(f, encoding='utf-8').read()).get('resumen_teorico', '')]
print("   fichas de cap_04 en la bandeja    : %d" % len(minadas))
print("   diferencia                        : %d  (47.5.d manda P41, P42 y P44 a la vuelta 50)" % (pron - len(minadas)))

print()
print("== DISCUTIBLE 5: que hace el censo con un marcador TALLADO y con una linea de bloque")
pruebas = [
    ("marcador TALLADO tal cual", "<!-- TALLADO: parcial salida=.v49/coste.txt -->"),
    ("marcador TALLADO con comillas", "<!-- TALLADO: parcial salida=`.v49/coste.txt` -->"),
    ("linea de bloque con comando", "    $ python .v49/coste.py      (la cola del instrumento; la tabla entera va en KK.5.h)"),
    ("linea de bloque, ruta sola en comillas", "    `.v49/coste.txt`"),
    ("celda de tabla de donde sale", "| los pares | 2 | `.v49/coste.txt` |"),
]
for rotulo, linea in pruebas:
    unidades = list(C.unidades_de(linea))
    rutas = []
    for _, sitio, unidad in unidades:
        for cita in C.EN_COMILLAS.findall(unidad):
            r = C.parece_ruta(cita)
            if r is not None:
                rutas.append((r, sitio, C.es_sede(unidad, cita)))
    print("   %-40s unidades %d  rutas extraidas %s" % (rotulo, len(unidades), rutas or "ninguna"))
