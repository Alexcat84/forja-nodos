# -*- coding: utf-8 -*-
"""ACTA 77: PASOS INVENTADOS POR CAPITULO de las 20 de Marquet, contado por mi desde los dos ficheros de fila: la marca suya sobre el
texto de AL ABRIR (.v78ext/fidelidad.tsv) y la mia sobre el texto de HOY (.v78aud/fidelidad.tsv, sellada, con mis dos D adjudicadas T
en la ACTA 77 77.5). El capitulo, de mi fila; su titulo, de la cabecera de su fichero. Toda linea que reparte trae su suma (R7). Solo lee."""
import io, re, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
cap, mia, suya = {}, {}, {}
for l in io.open('.v78aud/fidelidad.tsv', encoding='utf-8'):
    c = l.rstrip('\r\n').split('\t')
    if len(c) < 6 or c[0] == 'id': continue
    cap[(c[0], int(c[1]))] = c[3]; mia[(c[0], int(c[1]))] = 'T' if c[2] == 'D' else c[2]
for l in io.open('.v78ext/fidelidad.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    c = [x.strip() for x in l.split('|')]
    suya[(c[0], int(c[1]))] = c[2]
por = collections.defaultdict(lambda: collections.Counter()); cands = collections.defaultdict(set)
for k, ch in cap.items():
    cands[ch].add(k[0]); por[ch]['pasos'] += 1
    por[ch]['P al abrir'] += suya[k] == 'P'; por[ch]['P hoy'] += mia[k] == 'P'
tot = collections.Counter()
for ch in sorted(por):
    t = re.search(r'^titulo_textual: (.*)$', io.open('fuentes/marquet_turn_the_ship/%s.md' % ch, encoding='utf-8').read(), re.M).group(1).strip()
    p = por[ch]; tot.update(p)
    print('%s | %s | candidatos %d | pasos %d | PUENTE sobre el texto de al abrir %d = %.2f por ciento | PUENTE en el texto de hoy %d' % (
        ch, t, len(cands[ch]), p['pasos'], p['P al abrir'], 100.0 * p['P al abrir'] / p['pasos'], p['P hoy']))
print('lote: candidatos %d | pasos %d | PUENTE al abrir %d = %.2f por ciento | PUENTE hoy %d | suma de pasos por capitulo: %d' % (
    sum(len(v) for v in cands.values()), tot['pasos'], tot['P al abrir'], 100.0 * tot['P al abrir'] / tot['pasos'], tot['P hoy'], sum(p['pasos'] for p in por.values())))
