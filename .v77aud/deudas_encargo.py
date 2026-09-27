# -*- coding: utf-8 -*-
"""Fase ciega de la 77: las cuatro deudas que nombra mi encargo de la 77 (TAREA 4.5: d111 y d108 se pagan aqui; d098 y
d104 siguen vivas), leidas de docs/loop/DEUDA.jsonl POR CAMPO y no por su prosa: si hay linea de tipo 'pago' con ese id,
y con que vuelta. NO imprime el campo 'como' (es prosa del extractor, y lo leo en mi turno normal). Y la cuenta de lineas
de 'pago' por vuelta de la 77, con su suma (R7). Solo lee."""
import io, json, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
F = [json.loads(l) for l in io.open('docs/loop/DEUDA.jsonl', encoding='utf-8') if l.strip()]
for i, quiere in (('d111', 'pagada en la 77'), ('d108', 'pagada en la 77'), ('d098', 'viva'), ('d104', 'viva')):
    d = [f for f in F if f.get('id') == i and f.get('tipo') == 'deuda']
    p = [f.get('vuelta') for f in F if f.get('id') == i and f.get('tipo') == 'pago']
    print('%s | anotada: %s | lineas de pago: %d, en la vuelta %s | mi encargo la quiere %s' % (i, 'SI' if d else 'NO', len(p), p, quiere))
c = collections.Counter(f.get('tipo') for f in F if str(f.get('vuelta')) == '77')
print('lineas de DEUDA.jsonl con vuelta 77 (el campo es texto), por tipo: %s | suma: %d' % (dict(c), sum(c.values())))
