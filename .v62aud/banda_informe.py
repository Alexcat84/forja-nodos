# -*- coding: utf-8 -*-
"""LA BANDA DEL RELOJ DE UN `forja.py informe`, CON TODAS SUS MEDIDAS DIRECTAS.

Se publica como BANDA y MEDIANA, nunca como punto: publicarla como punto es la
caida que la `ACTA 58` `58.10` y la `ACTA 59` `59.13` cargaron en la racha del
auditor, dos actas seguidas.
"""
MEDIDAS = [
    (388.6, 437, 'ACTA 57 57.10'),
    (477.8, 437, 'ACTA 57 57.10'),
    (1002.0, 437, 'ACTA 58 58.10, cronometro del auditor'),
    (1062.0, 437, 'ACTA 58 58.10, cronometro del auditor'),
    (510.0, 439, 'ACTA 59 59.10, el auditor'),
    (507.0, 440, 'VUELTA 61 61.2.a, el extractor'),
    (668.0, 440, 'VUELTA 61 61.2.b, el extractor (su texto dice 667)'),
    (490.0, 440, 'ACTA 60 60.4, el auditor, HOY'),
]

v = sorted(x[0] for x in MEDIDAS)
n = len(v)
mediana = v[n // 2] if n % 2 else (v[n // 2 - 1] + v[n // 2]) / 2.0

print('MEDIDAS DIRECTAS DEL RELOJ DE UN python forja.py informe')
for s, p, d in sorted(MEDIDAS):
    print('  %7.1f s   poblacion %d   %s' % (s, p, d))
print('  ' + '-' * 66)
print('  medidas   : %d' % n)
print('  BANDA     : %.1f a %.1f s   (factor %.2f entre extremos)'
      % (v[0], v[-1], v[-1] / v[0]))
print('  MEDIANA   : %.1f s' % mediana)
print('  media     : %.1f s   (se publica junto a la banda, nunca sola)'
      % (sum(v) / n))
print()
print('  NO SE PUBLICA COMO PUNTO. La ACTA 58 58.10 y la ACTA 59 59.13 cargaron')
print('  en la racha del auditor exactamente eso, dos actas seguidas.')
