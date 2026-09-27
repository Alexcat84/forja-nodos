import json, glob, os
fr = json.load(open('config/frentes.json', encoding='utf-8'))
cer = set(fr['cerrados_en_extraccion'].keys())
libros = sorted(d.name for d in os.scandir('cuarentena') if d.is_dir()
                and d.name not in ('_insertados', '_derivadas', 'ensayo_referencia_163'))

def cruce(cerrados):
    tot = 0; filas = []
    for libro in libros:
        n = len(glob.glob('cuarentena/%s/*.json' % libro))
        ins = n if libro in cerrados else 0
        tot += ins
        filas.append((libro, n, 'SI' if libro in cerrados else 'NO', ins))
    return filas, tot

f, t = cruce(cer)
print('=== EL ARBOL TAL COMO ESTA (valor esperado del reporte: 0) ===')
for r in f: print('   %-30s %3d  %-3s %3d' % r)
print('   INSERTABLES POR D.39:', t)
f2, t2 = cruce(cer | {'grove_high_output'})
print()
print('=== MUTACION: grove_high_output DENTRO de cerrados_en_extraccion ===')
for r in f2: print('   %-30s %3d  %-3s %3d' % r)
print('   INSERTABLES POR D.39:', t2)
print()
print('LA PUERTA MUERDE:', t == 0 and t2 > 0,
      '   (%d -> %d al mutar la unica celda que la decide)' % (t, t2))
