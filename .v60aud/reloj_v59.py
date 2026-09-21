# -*- coding: utf-8 -*-
"""El reloj de la vuelta 59, medido sobre las fechas de sus propios ficheros
y sobre docs/loop/loop.log. Dos anclas para el techo de 70 minutos que el
encargo de la ACTA 57 escribio: el arranque del turno y el cierre del
primer informe."""
import datetime, os, re

def t(p):
    return datetime.datetime.fromtimestamp(os.path.getmtime(p))

fich = sorted(f for f in os.listdir('.v59ext') if f.startswith('informe59_'))
marcas = [t('.v59ext/' + f) for f in fich]

log = open('docs/loop/loop.log', encoding='utf-8', errors='replace').read()
arr = re.findall(r'\[(2026-09-21 \d\d:\d\d:\d\d)\] VUELTA 4 : EXTRACTOR', log)
fin = re.findall(r'\[(2026-09-21 \d\d:\d\d:\d\d)\] extractor listo \(USD ([\d.]+)\), (\d+)s', log)
t0 = datetime.datetime.strptime(arr[-1], '%Y-%m-%d %H:%M:%S')
t1 = datetime.datetime.strptime(fin[-1][0], '%Y-%m-%d %H:%M:%S')
print('arranque del turno (loop.log) : %s' % t0.time())
print('cierre del turno   (loop.log) : %s   USD %s en %s s'
      % (t1.time(), fin[-1][1], fin[-1][2]))
print()
print('hueco entre informe y informe, en segundos:')
for i in range(1, 7):
    print('   %d a %d : %6.1f s' % (i, i + 1,
          (marcas[i] - marcas[i - 1]).total_seconds()))
huecos = [(marcas[i] - marcas[i - 1]).total_seconds() for i in range(1, 7)]
print('   media de los seis huecos : %.1f s' % (sum(huecos) / len(huecos)))
print('   primero a septimo        : %.0f s  (%.0f min)'
      % ((marcas[-1] - marcas[0]).total_seconds(),
         (marcas[-1] - marcas[0]).total_seconds() / 60))
print()
for nombre, ancla in (('arranque del turno', t0), ('cierre del informe 1', marcas[0])):
    corte = ancla + datetime.timedelta(minutes=70)
    cerrados = sum(1 for m in marcas if m <= corte)
    print('minuto 70 contado desde %-22s -> %s  :  %d de 7 cerrados'
          % (nombre, corte.time(), cerrados))
