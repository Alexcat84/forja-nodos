# -*- coding: utf-8 -*-
"""D.30 leido por el AUDITOR: cada afirmacion CUANTITATIVA de un paso contra la
linea del libro que la tiene que sostener. Si la frase inglesa no aparece en la
linea declarada, el paso es candidato a PUENTE y hay que leerlo entero."""
import io, sys, unicodedata
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
L = io.open('fuentes/scott_radical_candor/cap_14.md', encoding='utf-8').read().split('\n')

def limpia(s):
    s = s.replace('’', "'").replace('“', '"').replace('”', '"')
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()

CASOS = [
 ('montar_equipo', 11, 31, 'every three years'),
 ('montar_equipo', 10, 29, 'annually'),
 ('decidir_poner_nota', 6, 71, 'past few months'),
 ('elegir_categorias', 3, 75, 'limit yourself to three or four'),
 ('elegir_categorias', 7, 83, 'results. is the person achieving their goals'),
 ('escribir_escaleras', 2, 97, 'what teamwork means for an entry-level employee'),
 ('fijar_cuatro_notas', 1, 101, 'five to seven ratings'),
 ('fijar_cuatro_notas', 4, 105, 'about 80 percent'),
 ('fijar_cuatro_notas', 9, 111, 'top 5 or even 1 percent'),
 ('fijar_cuatro_notas', 12, 115, 'get an overall not ok rating'),
 ('elegir_palabras', 8, 123, 'two to three sentences'),
 ('aplicar_consecuencias', 6, 131, 'except teamwork'),
 ('aplicar_consecuencias', 12, 137, 'documenting performance issues'),
 ('repartir_notas', 4, 147, 'at least 5 percent'),
 ('repartir_notas', 5, 147, 'roughly (very roughly) 15 percent'),
 ('repartir_notas', 6, 147, '1 to 5 percent'),
 ('repartir_notas', 7, 147, '40 percent'),
 ('presionar_curva', 6, 165, 'nonregretted attrition'),
 ('presionar_curva', 8, 169, 'written explanation'),
 ('calibrar_notas', 12, 181, 'slice the ratings by level'),
 ('calibrar_notas', 14, 183, 'two-year program'),
 ('calibrar_notas', 15, 185, 'make a conscious decision'),
 ('evaluar_dos_veces', 4, 191, 'do it twice a year'),
 ('evaluar_dos_veces', 8, 193, 'take two minutes'),
 ('montar_360', 8, 201, 'no more than seventy-five words'),
 ('montar_360', 9, 201, 'expected distribution should be shown'),
 ('hacer_critica_transparente', 6, 213, 'every employee at the company'),
 ('hacer_critica_transparente', 8, 215, 'show, don\'t tell'),
 ('mantener_ligero', 9, 231, 'under thirty minutes'),
 ('mantener_ligero', 13, 239, 'more than thirty people'),
]
print('%-28s %5s %6s  %-9s %s' % ('candidato', 'paso', 'linea', 'veredicto', 'frase buscada en esa linea'))
caidas = 0
for cid, paso, linea, frase in CASOS:
    hay = limpia(frase) in limpia(L[linea-1])
    if not hay:
        caidas += 1
    print('%-28s %5d %6d  %-9s %s' % (cid, paso, linea, 'SOSTIENE' if hay else 'NO ESTA', frase))
print()
print('comprobaciones: %d | sostenidas: %d | sin sostener: %d' % (len(CASOS), len(CASOS)-caidas, caidas))
