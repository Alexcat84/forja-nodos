# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 78 de .v76ext/r9.py, con la poblacion cambiada a los pasos que .v78ext/fidelidad.tsv marca T en las 20
fichas de cuarentena/marquet_turn_the_ship/, y el patron de la 76 sin tocar; nada mas cambiado. Lo que decia la de la 76: COPIA DE LA VUELTA 76 de .v75ext/r9.py (R9 de la ACTA 73 seccion 73.11), con la poblacion cambiada: no un nodo del grafo sino
los pasos que .v76ext/fidelidad.tsv marca T en las 22 fichas de cuarentena/gerber_emyth/. EL PATRON SE ENSANCHA, y es lo que pide el
encargo de la 76 (TAREA 2.2, ACTA 74 74.4): demostr (que el de la 75 no veia), y las comparaciones que el de la 75 no tenia: mejor,
peor, mayor, menor, tan ... como, en lugar de, compar, supera. Imprime cada paso T que casa, con lo que casa y con la nota de su
fila, para leer si la nota pega el tramo literal que lo sostiene. Solo lee."""
import io, json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
PAT = re.compile(r"\by [^,.:;]{1,40}? no\b|\bmas [^,.:;]{0,40}?\bque\b|\bmenos [^,.:;]{0,40}?\bque\b|\ben vez de\b|\ba diferencia de\b|\bno solo\b|\bsino\b|\bigual de\b|\blo contrario\b"
                 r"|\bha medido\b|\bmedid[oa]s?\b|\bmidi[oa]\b|\bdemuestr\w*|\bdemostr\w*|\bprobad[oa]\b|\bcomprob\w*|\bestudi\w*|\binvestig\w*|\bdatos?\b|\bel texto dice\b"
                 r"|\bmejor\b|\bpeor\b|\bmayor\b|\bmenor\b|\btan [^,.:;]{0,40}?\bcomo\b|\ben lugar de\b|\bcompar\w*|\bsuper[oa]\w*", re.I)
filas = [[c.strip() for c in l.rstrip('\n').split('|')]
         for l in io.open('.v78ext/fidelidad.tsv', encoding='utf-8') if l.strip() and not l.startswith('#')]
fichas = {}
casan = t = 0
for i, n, marca, linea, nota in filas:
    if marca != 'T':
        continue
    t += 1
    if i not in fichas:
        fichas[i] = json.load(io.open('cuarentena/marquet_turn_the_ship/%s.json' % i, encoding='utf-8'))['pasos_accionables']
    p = fichas[i][int(n) - 1]
    m = [x.group(0) for x in PAT.finditer(p)]
    if m:
        casan += 1
        print('%s paso %s | casa: %s' % (i, n, ' / '.join(m)))
        print('    paso: %s' % p)
        print('    nota: %s %s' % (linea, nota))
print('pasos T: %d | pasos T que casan: %d | pasos T sin ninguna clausula del patron: %d' % (t, casan, t - casan))
