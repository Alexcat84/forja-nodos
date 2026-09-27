# -*- coding: utf-8 -*-
"""Fase ciega de la 69, d053: la ficha fijar_duracion_lugar_reunion_individual de la bandeja de hoy, partida por
el corte que la deuda escribe (entre el paso 4 y el paso 5), y cada mitad contra su linea de
fuentes/grove_high_output/cap_05.md (L37 y L39). Mide por mitad: pasos por forma ('Cuenta con', 'Mira ...', otro
imperativo) con su suma, y en su linea del libro cuantos signos de interrogacion trae. No decide nada. Solo lee."""
import io, json, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
d = json.load(io.open('cuarentena/grove_high_output/fijar_duracion_lugar_reunion_individual.json', encoding='utf-8'))
p = d['pasos_accionables']
lin = io.open('fuentes/grove_high_output/cap_05.md', encoding='utf-8').read().split('\n')
print('pasos en la ficha: %d' % len(p))
def forma(x):
    if x.startswith('Cuenta con'): return 'Cuenta con'
    if x.startswith('Mira '): return 'Mira'
    return 'otro imperativo'
for nombre, rango, L in (('mitad duracion', range(0, 4), 37), ('mitad lugar', range(4, len(p)), 39)):
    c = collections.Counter(forma(p[i]) for i in rango)
    t = lin[L - 1]
    print('%s: pasos %s | por forma: %s | suma: %d' % (nombre, [i + 1 for i in rango], dict(c), sum(c.values())))
    print('  L%d: %d caracteres | signos de interrogacion: %d | empieza: %s' % (L, len(t), len(re.findall(r'\?', t)), t[:60]))
    for i in rango:
        if forma(p[i]) == 'otro imperativo': print('  P%d. %s' % (i + 1, p[i]))
