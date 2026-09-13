# -*- coding: utf-8 -*-
"""TODA CIFRA Y TODO NUMERAL DE LOS 194 PASOS DE HOY, BUSCADO EN SU TRAMO DEL LIBRO.

Es la muestra que mas duele si hay puente, y por eso la corro: una cifra inventada
no se disimula. Mismo metodo que `.t1_v20/cifras.py` de la vuelta pasada, con el
tramo de cada candidato en vez del capitulo entero, que es lo que la hace estrecha
de verdad: si un plazo del nodo de despedir apareciera solo en el tramo de
contratar, esto lo caza.

Las cifras escritas con letra van tambien traducidas a sus formas inglesas, porque
esta casa escribe cinco minutos y no 5 minutos.
"""
import json
import re

F = 'fuentes/scott_radical_candor/cap_10.md'
L = open(F, encoding='utf-8').read().split('\n')

# (pieza, desde, hasta, id).  El tramo es el del candidato, NO el capitulo.
TRECE = [
    ("P7",         47,  59, "conversar_historia_vida_descubrir_motivadores"),
    ("P8",         61,  75, "conversar_suenios_cruzar_habilidades"),
    ("P9",         77,  87, "trazar_plan_dieciocho_meses_aprendizaje"),
    ("P13 a P17",  97, 125, "armar_plan_anual_crecimiento_equipo"),
    ("P19 y P21", 129, 163, "montar_proceso_contratacion_reducir_sesgo"),
    ("P24",       169, 173, "facilitar_despido_tres_cosas"),
    ("P25",       175, 179, "admitir_pronto_mal_desempenio_cuatro_razones"),
    ("P26",       181, 187, "calibrar_decision_despido_documentarla"),
    ("P27",       189, 195, "sopesar_consejo_legal_despedir_humildad"),
    ("P28",       197, 201, "contactar_despedido_mes_despues"),
    ("P30",       205, 223, "calibrar_ascensos_evitar_politica"),
    ("P33",       229, 237, "evitar_obsesion_ascenso_estatus"),
    ("P34 a P36", 239, 251, "reconocer_excelencia_trayectoria_gradual"),
]

# El caso de Russ (L23 a L45) es ejemplo nombrado dentro de P7, P8 y P9
# (manual 3.5), asi que su texto cuenta como tramo legitimo para esos tres.
CASO = (23, 45)

LETRAS = {
    'una': ['one', 'a year', 'once', 'a month', 'an hour', 'a couple'],
    'un': ['one', 'a year', 'a month', 'an hour', 'a day', 'a couple'],
    'dos': ['two', 'twice', 'couple'],
    'tres': ['three'], 'cuatro': ['four', 'forty'], 'cinco': ['five'],
    'seis': ['six'], 'siete': ['seven'], 'ocho': ['eight'], 'nueve': ['nine'],
    'diez': ['ten', '10'], 'quince': ['fifteen', '15'],
    'veinte': ['twenty', '20'], 'treinta': ['thirty', '30'],
    'cuarenta': ['forty', '40'], 'cincuenta': ['fifty', '50'],
    'cien': ['hundred'], 'mil': ['thousand'],
    'dieciocho': ['eighteen'], 'decada': ['decade'],
    'trimestre': ['quarter'], 'anio': ['year'], 'anios': ['years'],
    'mes': ['month'], 'meses': ['months'],
}

total = 0
fallos = []
for n, a, b, i in TRECE:
    tramo = ' '.join(L[k - 1] for k in range(a, b + 1)).lower()
    if n in ("P7", "P8", "P9"):
        tramo += ' ' + ' '.join(L[k - 1] for k in range(CASO[0], CASO[1] + 1)).lower()
    d = json.load(open('cuarentena/scott_radical_candor/%s.json' % i, encoding='utf-8'))
    for j, paso in enumerate(d['pasos_accionables'], 1):
        p = paso.lower()
        for dig in re.findall(r'\d+', p):
            total += 1
            if dig not in tramo:
                fallos.append((n, i, j, 'digito ' + dig))
        for pal, formas in LETRAS.items():
            if re.search(r'\b' + pal + r'\b', p):
                total += 1
                if not any(f in tramo for f in formas):
                    fallos.append((n, i, j, 'numeral ' + pal))

print("cifras y numerales comprobados en los 194 pasos : %d" % total)
print("los que NO estan en su tramo del libro           : %d" % len(fallos))
for f in fallos:
    print("   %s  %s  paso %d  ->  %s" % f)
if not fallos:
    print("   []")
