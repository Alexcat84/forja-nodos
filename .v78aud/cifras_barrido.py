# -*- coding: utf-8 -*-
"""Fase ciega de la 78 (la idea de .v76aud/normal/cifras_barrido.py, escrita de nuevo para esta tanda): las cifras que la
LECTURA de la seccion 4 de mi apertura cita, contadas sobre mis .v78aud/vecinos_<id>.json y no a ojo (D.38.3): filas por senial
que levanta, nodos de fuera con su libro, fichas que no levantan a nadie y fichas a las que no levanta nadie, y la banda de
similitud_texto de las filas que esa senial levanta. Cada reparto con su suma (R7). Solo lee."""
import io, json, glob, os, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
tanda = [l.strip() for l in io.open('.v78aud/las20.txt', encoding='utf-8') if l.strip()]
libro = {}
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l); libro[d['id']] = (d.get('fuentes') or [{}])[0].get('clave')
senial = collections.Counter(); fuera = {}; levanta = collections.Counter(); levantada = collections.Counter(); texto = []
for i in tanda:
    d = json.load(io.open('.v78aud/vecinos_%s.json' % i, encoding='utf-8'))
    for v in d['vecinos']:
        senial['+'.join(v['levantada_por'])] += 1
        levanta[i] += 1; levantada[v['id']] += 1
        if v['id'] not in tanda: fuera[v['id']] = libro.get(v['id'])
        if v['levantada_por'] == ['similitud_texto']: texto.append(v['senales']['similitud_texto'])
print('filas por senial: %s | suma: %d' % (dict(senial), sum(senial.values())))
pl = collections.Counter(fuera.values())
print('nodos de fuera: %d | por libro: %s | suma: %d' % (len(fuera), dict(pl), sum(pl.values())))
nada = [i for i in tanda if not levanta[i]]; nadie = [i for i in tanda if not levantada[i]]
print('fichas que no levantan a nadie: %d %s' % (len(nada), nada))
print('fichas a las que no levanta nadie: %d %s' % (len(nadie), nadie))
print('similitud_texto en las filas que levanta solo esa senial: filas %d | menor %.3f | mayor %.3f' % (len(texto), min(texto), max(texto)))
