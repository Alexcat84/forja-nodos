# -*- coding: utf-8 -*-
"""IMPRIME LA TABLA EN MARKDOWN, YA TALLADA, PARA PEGARLA SIN TOCARLA.

REMEDIO DE ESTA VUELTA, contra mi propia caida de la vuelta anterior: mi tabla
de la APERTURA_CIEGA de la vuelta 33 decia 'PEGADA DE .v33a/mis_clases.txt SIN
TOCARLA' y aquel fichero no imprimia ninguna tabla, solo una lista. D.41 en
estricto lo pone en ROJO y con razon. Este instrumento IMPRIME LA TABLA.

MIS CLASES SE TECLEAN AQUI Y SOLO AQUI, y se teclean a ciegas: este fichero se
escribe ANTES de leer ni una razon de bitacora/VEREDICTOS.jsonl. La columna 'la
de la vuelta' la lee el propio instrumento del fichero, para que la comparacion
no la haga mi mano.
"""
import io, json, re, sys

BASE = 410
# MI CLASE, adjudicada leyendo los dos pasos y con la vara de AUDITOR_FORJA.md 6.
MIAS = {
    412: 'SANO', 413: 'SANO', 414: 'SANO', 415: 'SANO', 416: 'SANO',
    417: 'SANO', 418: 'SANO', 419: 'SANO', 420: 'SANO', 421: 'SANO',
    422: 'SANO', 423: 'CONTINUA', 411: 'CORREGIDO',
}

ver = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()]
print('| # | candidato | vecino | senial que la levanta | **MI CLASE, a ciegas** | la de la vuelta | |')
print('|---:|---|---|---|---|---|---|')
ok = 0
for n, v in enumerate(ver[BASE:], BASE + 1):
    suya = v.get('veredicto') or '(ninguna)'
    mia = MIAS.get(n, '(no adjudicada)')
    igual = 'COINCIDE' if mia == suya else '**DISCREPA**'
    ok += 1 if mia == suya else 0
    s = v.get('senales') or {}
    marca = ', '.join(v.get('levantada_por') or [])
    cifra = ('%.3f' % s['similitud_texto']) if 'similitud_texto' in s else '.'
    pcn = ('%.3f' % s['paso_contra_nodo']) if 'paso_contra_nodo' in s else '.'
    print('| %d | `%s` | `%s` | %s (txt %s, pcn %s) | **%s** | %s | %s |'
          % (n, v['candidato'], v['vecino'], marca, cifra, pcn, mia, suya, igual))
print()
print('lineas comparadas: %d   COINCIDEN: %d   DISCREPAN: %d' % (len(ver) - BASE, ok, len(ver) - BASE - ok))
print('lineas nuevas SIN razon escrita (D.8): %d de %d'
      % (sum(1 for v in ver[BASE:] if not (v.get('razon') or '').strip()), len(ver) - BASE))
