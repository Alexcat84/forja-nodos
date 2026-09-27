# -*- coding: utf-8 -*-
"""Toda cifra que aparezca en los 95 pasos de los cinco candidatos de hoy,
buscada en el tramo del libro del que sale ese candidato. Es la muestra que
mas duele si hay puente: una cifra inventada no se disimula.

Las cifras escritas con letra van tambien, traducidas a su digito, porque
esta casa escribe cinco minutos y no 5 minutos."""
import json, re

F = 'fuentes/scott_radical_candor/cap_09.md'
L = open(F, encoding='utf-8').read().split('\n')

CINCO = [
    ("P22", 301, 313, "revisar_critica_mujer_agresiva_cuatro_tacticas"),
    ("P23", 315, 329, "responder_critica_abrasiva_cuatro_reglas"),
    ("P24", 331, 361, "entregar_evaluacion_formal_desempenio_nueve_consejos"),
    ("P27", 383, 413, "conducir_reuniones_salto_nivel_diez_reglas"),
    ("P28", 415, 425, "resolver_dudas_frecuentes_reuniones_salto_nivel"),
]

# palabra en castellano -> como puede aparecer en el tramo ingles
LETRAS = {
    'una': ['one', 'a year', 'once'], 'dos': ['two', 'twice'], 'tres': ['three'],
    'cuatro': ['four'], 'cinco': ['five'], 'seis': ['six'], 'siete': ['seven'],
    'ocho': ['eight'], 'nueve': ['nine'], 'diez': ['ten', '10'],
    'cincuenta': ['fifty', '50'], 'cien': ['hundred'],
}

total = 0
fallos = []
for n, a, b, i in CINCO:
    tramo = ' '.join(L[k - 1] for k in range(a, b + 1)).lower()
    d = json.load(open('cuarentena/scott_radical_candor/%s.json' % i, encoding='utf-8'))
    for j, paso in enumerate(d['pasos_accionables'], 1):
        p = paso.lower()
        # digitos
        for dig in re.findall(r'\d+', p):
            total += 1
            if dig not in tramo:
                fallos.append((n, j, 'digito ' + dig))
        # numerales escritos con letra
        for pal, formas in LETRAS.items():
            if re.search(r'\b' + pal + r'\b', p):
                total += 1
                if not any(f in tramo for f in formas):
                    fallos.append((n, j, 'numeral ' + pal))
print("cifras y numerales comprobados en los 95 pasos: %d" % total)
print("los que NO estan en su tramo del libro          : %d  %s"
      % (len(fallos), fallos if fallos else '[]'))
