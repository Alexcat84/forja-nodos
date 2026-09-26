# -*- coding: utf-8 -*-
"""Fase ciega de la 75: la TAREA 2 de mi encargo (la bloqueante heredada, ACTA 73 73.6) medida sobre el DATO, sin git y
sin el reporte. Los pasos viejos de dar_elogio_disciplina_igual_critica son los que imprimi en mi fase ciega de la 74 con
.v67aud/normal/pasos_ciego.py (.v74aud/pasos_tres.txt, 20 pasos); los de hoy, del grafo. Mide: (1) que los de hoy son los
viejos sin el 8 y sin el 17, en su orden, texto a texto; (2) que los dos literales que el resumen dice retirados son el 8 y
el 17 viejos; (3) que las tres correcciones del 26 sep estan en el orden que el encargo pedia (corregir, retirar 17,
retirar 8); (4) que la correccion declarada trae lo que el encargo le pidio, frase por frase, buscando cada una literal;
(5) que las lineas del libro que pega estan, tramo a tramo, en su linea de fuentes/scott_radical_candor/cap_13.md.
Reparte con su suma (R7). NO imprime ninguna clave de relacion (R6). Solo lee."""
import io, re, json, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
DE = 'dar_elogio_disciplina_igual_critica'
viejos = []; dentro = False
for l in io.open('.v74aud/pasos_tres.txt', encoding='utf-8'):
    if l.startswith('====='): dentro = l.split()[1] == DE; continue
    m = re.match(r'^  P(\d+)\. (.*)$', l.rstrip('\n'))
    if dentro and m: viejos.append(m.group(2))
d = [json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if json.loads(l)['id'] == DE][0]
hoy = d['pasos_accionables']; r = d['resumen_teorico']
print('pasos viejos (.v74aud/pasos_tres.txt): %d | pasos hoy en el grafo: %d' % (len(viejos), len(hoy)))
print('(1) los de hoy son los viejos sin el 8 y sin el 17, en su orden y texto a texto: %s' % ('SI' if hoy == [p for n, p in enumerate(viejos, 1) if n not in (8, 17)] else 'NO'))
ret = dict((int(n), t) for n, t in re.findall(r'EL PASO (\d+) SALE DE pasos_accionables EN ESTE ACTO.*?SU TEXTO LITERAL, QUE NO SE PIERDE: "(.*?)" LOS PASOS', r))
print('(2) literal retirado del paso 17 igual al 17 viejo: %s | del paso 8 igual al 8 viejo: %s' % (
    'SI' if ret.get(17) == viejos[16] else 'NO', 'SI' if ret.get(8) == viejos[7] else 'NO'))
marcas = [('corregir', r.find('CORRECCION DECLARADA (26 sep 2026')), ('retirar 17', r.find('EL PASO 17 SALE DE pasos_accionables')), ('retirar 8', r.find('EL PASO 8 SALE DE pasos_accionables'))]
print('(3) posicion en el resumen: %s | en el orden corregir, 17, 8: %s' % (', '.join('%s %d' % m for m in marcas), 'SI' if 0 < marcas[0][1] < marcas[1][1] < marcas[2][1] else 'NO'))
cor = r[marcas[0][1]:marcas[1][1]]
PIDE = [('los dos pasos declarados PUENTE de clausula', 'LOS PASOS 8 Y 17 DE ESTE NODO SON PUENTE DE CLAUSULA'),
        ('la ACTA 73 73.5 citada', 'ACTA 73 seccion 73.5'),
        ('la linea 273 del libro', '273:Also, praise helps people focus on their strengths'),
        ('la linea 283 del libro', '283:We'),
        ('lo que del paso 8 es del libro', 'LO QUE DEL PASO 8 SI ES DEL LIBRO: el elogio ayuda a la gente a centrarse en sus fuerzas y a hacer mas del trabajo que disfruta y menos del que odia'),
        ('lo que del paso 17 es del libro', 'LO QUE DEL PASO 17 SI ES DEL LIBRO: en ese ejercicio la gente sale sintiendose vista, conectada e inspirada'),
        ('la cuenta 18 y 2 en lugar de 20 y 0', 'donde arriba dice 20 pasos, 20 TRANSCRIPCION, 0 PUENTE, vale 20 pasos, 18 TRANSCRIPCION, 2 PUENTE'),
        ('la tabla, del 1 al 7', 'los pasos 1 a 7 no se mueven'),
        ('la tabla, del 9 al 16', 'del 9 al 16 pasan a ser del 8 al 15'),
        ('la tabla, del 18 al 20', 'del 18 al 20 pasan a ser del 16 al 18'),
        ('la numeracion vieja para lo citado antes', 'va con la numeracion vieja')]
c = collections.Counter()
for q, t in PIDE:
    c['esta' if t in cor else 'NO ESTA'] += 1
    if t not in cor: print('    NO ESTA en la correccion: %s' % q)
print('(4) lo que el encargo pedia a la correccion, frase por frase: %s | suma: %d' % (dict(c), sum(c.values())))
libro = io.open('fuentes/scott_radical_candor/cap_13.md', encoding='utf-8').read().split('\n')
pegado = cor[cor.index('grep -n -o'):cor.index('POR QUE EL PASO 8')]
tramos = re.findall(r'(\d+):(.*?)(?= \| \d+:| POR QUE|$)', pegado.split('cap_13.md:', 1)[1].strip())
c = collections.Counter()
for n, t in tramos: c['en su linea' if t.strip() in libro[int(n) - 1] else 'NO esta en su linea'] += 1
print('(5) tramos del libro pegados en la correccion: %d, lineas %s | por estado: %s | suma: %d' % (len(tramos), [int(n) for n, t in tramos], dict(c), sum(c.values())))
razon = [r[marcas[1][1]:marcas[2][1]], r[marcas[2][1]:]]
print('    las dos razones de retirar_paso.py traen la fecha de hoy y la ACTA 73 73.5: %s' % ['SI' if ('26 sep 2026' in x and '73.5' in x) else 'NO' for x in razon])
