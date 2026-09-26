# -*- coding: utf-8 -*-
"""El reloj de los 20 insertar de la vuelta 72 (COPIA DE LA VUELTA 72 de .v70ext/relojes.py, ruta cambiada; la de la 70 era copia de .v67ext/relojes.py), leido de la ultima linea de cada .v72ext/insertar_*.txt."""
import glob, io, re
s = []
for f in sorted(glob.glob('.v72ext/insertar_*.txt')):
    m = re.search(r'fin (\S+ \S+) \| codigo de salida (\d+) \| ([\d.]+) s', io.open(f, encoding='utf-8').read())
    s.append(float(m.group(3)))
    print('%-72s codigo %s  %7.1f s  fin %s' % (f, m.group(2), float(m.group(3)), m.group(1)))
s.sort()
print('insertar: %d | minimo %.1f s | mediana %.1f s | maximo %.1f s | suma %.1f s (%.2f h)' % (
    len(s), s[0], (s[9] + s[10]) / 2, s[-1], sum(s), sum(s) / 3600))
