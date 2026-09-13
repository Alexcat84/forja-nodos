# -*- coding: utf-8 -*-
"""LA TABLA DEL SALDO DE LOS TRECE INFORMES, IMPRESA Y NO TECLEADA (`EXTRACTOR.md` 5).

Lee los trece ficheros de `.aduana_v21/final/`, saca de cada uno su dictamen, su
poblacion con su reparto y sus vecinos levantados, y los cuenta. **No decide nada:
transcribe lo que cada informe dice.**

Y publica aparte la cifra que `D.41` dice que un informe de uno en uno NO PUEDE VER:
`CHOCAN entre si dentro del lote`. Los trece la imprimen como `0`, y ese `0` es
**estructural y no medido**, porque de uno en uno nunca hay dos candidatos.
"""
import glob
import os
import re

TRECE = [
    ("P7",         "conversar_historia_vida_descubrir_motivadores"),
    ("P8",         "conversar_suenios_cruzar_habilidades"),
    ("P9",         "trazar_plan_dieciocho_meses_aprendizaje"),
    ("P13 a P17",  "armar_plan_anual_crecimiento_equipo"),
    ("P19 y P21",  "montar_proceso_contratacion_reducir_sesgo"),
    ("P24",        "facilitar_despido_tres_cosas"),
    ("P25",        "admitir_pronto_mal_desempenio_cuatro_razones"),
    ("P26",        "calibrar_decision_despido_documentarla"),
    ("P27",        "sopesar_consejo_legal_despedir_humildad"),
    ("P28",        "contactar_despedido_mes_despues"),
    ("P30",        "calibrar_ascensos_evitar_politica"),
    ("P33",        "evitar_obsesion_ascenso_estatus"),
    ("P34 a P36",  "reconocer_excelencia_trayectoria_gradual"),
]

print('| # | pieza | id | dictamen | poblacion (grafo mas bandejas) | vecinos levantados |')
print('|---:|---|---|---|---|---|')
cuenta = {'ENTRARIA': 0, 'BLOQUEARIA': 0, 'CAERIA': 0}
vecinos_total = 0
for i, (pieza, ident) in enumerate(TRECE, 1):
    ruta = '.aduana_v21/final/%s.txt' % ident
    if not os.path.exists(ruta):
        print('| %d | `%s` | `%s` | **FALTA EL FICHERO** | | |' % (i, pieza, ident))
        continue
    texto = open(ruta, encoding='utf-8').read()
    m = re.search(r'^\[(\w+)\]', texto, re.M)
    dictamen = m.group(1) if m else 'SIN DICTAMEN'
    cuenta[dictamen] = cuenta.get(dictamen, 0) + 1
    p = re.search(r'poblacion del barrido\s+:\s+(\d+)\s+\((\d+) del grafo mas (\d+)', texto)
    pob = '**%s** (%s mas %s)' % (p.group(1), p.group(2), p.group(3)) if p else '?'
    vec = re.findall(r'vecino (\S+)\s+\[levantada por: ([^\]]+)\]', texto)
    vecinos_total += len(vec)
    lista = '; '.join('`%s` por `%s`' % (v, s) for v, s in vec) or 'ninguno'
    print('| %d | `%s` | `%s` | **%s** | %s | %s |' % (i, pieza, ident, dictamen, pob, lista))
print('| | | **trece informes** | **%d ENTRARIA, %d BLOQUEARIA, %d CAERIA** | | **%d filas de vecino** |'
      % (cuenta.get('ENTRARIA', 0), cuenta.get('BLOQUEARIA', 0), cuenta.get('CAERIA', 0),
         vecinos_total))
print('')
choques = set()
for _p, ident in TRECE:
    ruta = '.aduana_v21/final/%s.txt' % ident
    if os.path.exists(ruta):
        for m in re.finditer(r'CHOCAN entre si dentro del lote\s+:\s+(\d+)', open(ruta, encoding='utf-8').read()):
            choques.add(m.group(1))
print('valor de CHOCAN entre si dentro del lote en los trece : %s' % sorted(choques))
print('  ES ESTRUCTURAL Y NO MEDIDO (D.41): de uno en uno nunca hay dos candidatos.')
print('')
print('ficheros de informe de esta vuelta:')
print('  .aduana_v21/final/   : %d' % len(glob.glob('.aduana_v21/final/*.txt')))
print('  .aduana_v21/ (raiz)  : %d' % len(glob.glob('.aduana_v21/*.txt')))
