import json, re, os, glob
BAN = 'cuarentena/scott_radical_candor'
filas = []
for p in sorted(glob.glob(BAN + '/*.json')):
    d = json.load(open(p, encoding='utf-8'))
    rt = d.get('resumen_teorico', '')
    m = re.search(r'cap_07\.md, lineas (\d+) a (\d+)', rt)
    if not m:
        continue
    filas.append((int(m.group(1)), int(m.group(2)), d['id'], len(d['pasos_accionables'])))
filas.sort()
print('ORDEN DEL LIBRO, cap_07, LO QUE QUEDA EN BANDEJA')
print('poblacion: ' + BAN + ', filtrada por resumen_teorico que cita cap_07.md')
print()
print('| # | id | lineas | pasos |')
print('|---:|---|---|---:|')
tot = 0
for i, (a, b, i_, n) in enumerate(filas, 1):
    print('| %d | `%s` | `L%d` a `L%d` | %d |' % (i, i_, a, b, n))
    tot += n
print()
print('candidatos: %d   pasos: %d' % (len(filas), tot))
