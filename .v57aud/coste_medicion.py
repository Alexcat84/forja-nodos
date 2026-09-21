# -*- coding: utf-8 -*-
"""LA CIFRA QUE EL ENCARGO DE LA VUELTA 56 DEJO PENDIENTE Y ES MIA DE MEDIR:
el coste del turno de extractor de Sonnet contra los dos de Opus.
Se lee de docs/loop/loop.log y de ningun otro sitio (D.38.3).
D.59: la razon la imprime el instrumento con numerador y denominador nombrados."""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
L = open('docs/loop/loop.log', encoding='utf-8').read().split('\n')

arranques = [n for n, l in enumerate(L) if 'arranque: rama' in l]
pat_turno = re.compile(r'^\[(\S+ \S+)\]\s+(extractor|auditor ciego|auditor) listo \(USD ([0-9.]+)\), (\d+)s')
pat_rol   = re.compile(r'^\[\S+ \S+\] VUELTA (\d+) : (EXTRACTOR|AUDITOR|APERTURA CIEGA) \((\S+)\)')

filas, vuelta, modelo = [], None, None
for n, l in enumerate(L):
    m = pat_rol.match(l)
    if m:
        vuelta, modelo = m.group(1), m.group(3).rstrip(')')
    m = pat_turno.match(l)
    if m:
        corrida = max([i for i in arranques if i < n] or [0])
        filas.append((corrida, vuelta, m.group(2), modelo, float(m.group(3)), int(m.group(4)), m.group(1)))

ext = [f for f in filas if f[2] == 'extractor']
print('TODOS LOS TURNOS DE EXTRACTOR QUE EL LOG REGISTRA, EN ORDEN:')
print('  %-22s %-7s %-18s %10s %8s  %s' % ('arranque de su corrida', 'vuelta', 'modelo', 'USD', 'seg', 'cerrado'))
for c, v, t, mo, usd, seg, cu in ext:
    print('  %-22s %-7s %-18s %10.4f %8d  %s'
          % (L[c][1:20], v, mo, usd, seg, cu))

print()
print('LOS TRES QUE LA MEDICION COMPARA, nombrados por su vuelta de la linea serial:')
tres = ext[-3:]
etiqueta = ['VUELTA 54', 'VUELTA 55', 'VUELTA 56']
for (c, v, t, mo, usd, seg, cu), e in zip(tres, etiqueta):
    print('  %-10s  modelo %-18s  %8.4f USD   %5d s' % (e, mo, usd, seg))

opus = [f[4] for f in tres[:2]]
son  = tres[2][4]
print()
print('EL UMBRAL ESCRITO ANTES DE MEDIR: la mitad o menos de los dos de Opus')
for usd in opus:
    print('  numerador (coste de Sonnet, vuelta 56)  : %.4f USD' % son)
    print('  denominador (coste de Opus)             : %.4f USD' % usd)
    print('  la mitad de ese denominador             : %.4f USD' % (usd / 2))
    print('  razon Sonnet / Opus                     : %.4f' % (son / usd))
    print('  CUMPLE (razon <= 0.5)                   : %s' % ('SI' if son <= usd / 2 else 'NO'))
    print()
print('CONTRA EL PEOR CASO PARA SONNET (el Opus MAS BARATO, %.4f):' % min(opus))
print('  CUMPLE                                  : %s' % ('SI' if son <= min(opus) / 2 else 'NO'))
print()
print('Y LA CIFRA DEL AUSTERO D.56, el tope de 10 USD por turno:')
print('  el turno de extractor de la vuelta 56    : %.4f USD   %s de 10'
      % (son, 'PASA' if son > 10 else 'NO pasa'))
