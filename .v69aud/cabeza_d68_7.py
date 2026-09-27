# -*- coding: utf-8 -*-
"""Fase ciega de la 69, D68.7: la cabeza usar_tres_clases_reunion_proceso contra los ocho hijos que el extractor
le colgo en la 68 (los ocho los nombra el encargo de la 69, TAREA 2, y mi ACTA 67 67.4.d). Mide, sobre las fichas
de la bandeja de hoy: (a) cada paso de la cabeza por su forma: 'Cuenta con', rotulo 'Primera/Segunda/Tercera clase:' u otro imperativo, con su suma; (b) en que
pasos de la cabeza aparece 'uno a uno'; (c) por cada hijo, si su condicion de activacion contiene alguna de las
palabras del producto de la cabeza ('clase', 'clases', 'tres', 'proceso') y si la contiene 'reunion individual'.
No imprime claves de relacion (R6). Solo lee."""
import io, json, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
B = 'cuarentena/grove_high_output/%s.json'
cab = json.load(io.open(B % 'usar_tres_clases_reunion_proceso', encoding='utf-8'))
p = cab['pasos_accionables']
def forma(x):
    if x.startswith('Cuenta con'): return 'Cuenta con'
    if re.match(r'^(Primera|Segunda|Tercera) clase: ', x): return 'rotulo de clase'
    return 'otro imperativo'
c = collections.Counter(forma(x) for x in p)
print('cabeza: pasos %d | por forma: %s | suma: %d' % (len(p), dict(c), sum(c.values())))
print('pasos de la cabeza que dicen uno a uno: %s' % [n for n, x in enumerate(p, 1) if 'uno a uno' in x])
HIJOS = ['fijar_frecuencia_reunion_individual_madurez_tarea', 'fijar_duracion_lugar_reunion_individual',
         'preparar_guion_reunion_individual_subordinado', 'cubrir_indicadores_problemas_reunion_individual',
         'facilitar_expresion_subordinado_pregunta_mas', 'acumular_asuntos_importantes_fichero_espera',
         'alentar_asuntos_corazon_vigilar_final_reunion', 'programar_reunion_individual_cadena']
PAL = re.compile(r'\b(clase|clases|tres|proceso)\b', re.I)
r = collections.Counter()
for h in HIJOS:
    cond = json.load(io.open(B % h, encoding='utf-8'))['condiciones_activacion']
    cond = cond if isinstance(cond, str) else ' '.join(cond)
    pal = sorted(set(m.lower() for m in PAL.findall(cond)))
    r['con palabra del producto de la cabeza' if pal else 'sin palabra del producto de la cabeza'] += 1
    print('  %-52s | palabras de la cabeza: %-10s | dice reunion individual: %s' % (h, pal or '-', 'reunion individual' in cond))
print('hijos: %d | por condicion: %s | suma: %d' % (len(HIJOS), dict(r), sum(r.values())))
