# -*- coding: utf-8 -*-
"""d031: comprobar que la correccion de d027 NO toco el texto que alimenta las senales.
Senal 1 (src/aduana.py 278): titulo mas resumen mas pasos. Senal 3 (linea 304): pasos,
y titulo mas resumen como cuerpo. El entregable_esperado no entra en ninguna de las dos."""
import json, subprocess, io, sys, hashlib
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
RUTA = 'cuarentena/grove_high_output/reunir_informacion_gerencial_vias_variadas.json'
viejo = json.loads(subprocess.check_output(['git', 'show', 'HEAD:' + RUTA]).decode('utf-8'))
nuevo = json.load(open(RUTA, encoding='utf-8'))
def pienso(d):
    return '%s. %s || %s' % (d.get('titulo') or '', d.get('resumen_teorico') or '',
                             ' | '.join(d.get('pasos_accionables') or []))
for nombre, d in (('HEAD (antes de la correccion)', viejo), ('arbol (despues)', nuevo)):
    t = pienso(d)
    print('%-32s  %d caracteres  sha1 %s' % (nombre, len(t), hashlib.sha1(t.encode('utf-8')).hexdigest()))
print()
print('texto que alimenta senal 1 y senal 3 IDENTICO :', pienso(viejo) == pienso(nuevo))
print('entregable_esperado cambiado                  :', viejo['entregable_esperado'] != nuevo['entregable_esperado'])
print('campos con diferencia                         :',
      sorted(k for k in nuevo if viejo.get(k) != nuevo.get(k)))
