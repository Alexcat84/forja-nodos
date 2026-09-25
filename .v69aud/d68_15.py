# -*- coding: utf-8 -*-
"""Fase ciega de la 69, D68.15: en que pasos de fijar_frecuencia_reunion_individual_madurez_tarea aparece la palabra
'estilo' (el producto de elegir_estilo_direccion_madurez_relevante_tarea es un estilo elegido) y 'madurez', y con que
forma empieza cada uno ('Cuenta con' u otro imperativo), con su suma. Fichas de la bandeja de hoy. Solo lee."""
import io, json, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
p = json.load(io.open('cuarentena/grove_high_output/fijar_frecuencia_reunion_individual_madurez_tarea.json', encoding='utf-8'))['pasos_accionables']
for pal in ('estilo', 'madurez'):
    n = [i for i, x in enumerate(p, 1) if pal in x]
    c = collections.Counter('Cuenta con' if p[i - 1].startswith('Cuenta con') else 'otro imperativo' for i in n)
    print('pasos con %-8s: %s | por forma: %s | suma: %d' % (pal, n, dict(c), sum(c.values())))
