# -*- coding: utf-8 -*-
"""Fase ciega de la 80 (copia libre de .v77aud/deudas_encargo.py): las dos deudas que mi encargo de la 80 manda pagar
(d104, TAREA 1; d183, TAREA 4), leidas de docs/loop/DEUDA.jsonl POR CAMPO y no por su prosa: si hay linea de tipo 'pago'
con ese id, y con que vuelta. NO imprime el campo 'como' (es prosa del extractor, y lo leo en mi turno normal). Y la
cuenta de lineas con vuelta 80 por tipo, con su suma (R7), para ver que no pago ninguna otra. Solo lee."""
import io, json, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
F = [json.loads(l) for l in io.open('docs/loop/DEUDA.jsonl', encoding='utf-8') if l.strip()]
for i in ('d104', 'd183'):
    d = [f for f in F if f.get('id') == i and f.get('tipo') == 'deuda']
    p = [f.get('vuelta') for f in F if f.get('id') == i and f.get('tipo') == 'pago']
    print('%s | anotada: %s | lineas de pago: %d, en la vuelta %s | mi encargo la quiere pagada en la 80' % (i, 'SI' if d else 'NO', len(p), p))
c = collections.Counter('%s %s' % (f.get('tipo'), f.get('id')) for f in F if str(f.get('vuelta')) == '80')
print('lineas de DEUDA.jsonl con vuelta 80 (el campo es texto), por tipo e id: %s | suma: %d' % (dict(c), sum(c.values())))
