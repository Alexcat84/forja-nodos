# -*- coding: utf-8 -*-
"""TODA RUTA QUE EL ACTA PUBLICA COMO PRUEBA EXISTE Y NO ESTA EN CERO BYTES.

Cosecha `7.B`: *una ruta publicada como evidencia de una corrida cuenta como
CIFRA PUBLICADA en su sede; si apunta a un fichero inexistente o de cero bytes,
es caida de cifra.* Se corre sobre el borrador ANTES de apendar el acta.

LA EXCEPCION SE DECLARA Y NO SE ESCONDE: hay rutas que el acta cita PRECISAMENTE
porque estan en cero bytes, que es el hallazgo. Van en `CERO_DECLARADO` y se
comprueba al reves: si alguna dejase de estar en cero, el acta estaria mintiendo.
"""
import io
import os
import re
import sys

CERO_DECLARADO = ('.v61ext/informe_3_pedir_critica.txt',
                  '.v60ext/informe_2_desarrollar_primer_curso_entrenamiento.txt')
# La salida de este mismo script no se mide a si misma: se esta escribiendo.
SE_EXCLUYE = ('.v62aud/rutas.txt', '.v62aud/acta_60.md')

ACTA = sys.argv[1] if len(sys.argv) > 1 else '.v62aud/acta_60.md'
texto = io.open(ACTA, encoding='utf-8').read()
rutas = sorted(set(re.findall(r'\.v6\d(?:aud|ext)/[A-Za-z0-9_.]+\.[a-z]+', texto)))

malas = 0
for r in rutas:
    if r in SE_EXCLUYE:
        continue
    if r in CERO_DECLARADO:
        ok = os.path.exists(r) and os.path.getsize(r) == 0
        print('  CERO DECLARADO : %s   %s' % (r, 'sigue en cero, correcto' if ok
                                              else 'YA NO ESTA EN CERO: el acta miente'))
        if not ok:
            malas += 1
    elif not os.path.exists(r):
        print('  NO EXISTE      : %s' % r)
        malas += 1
    elif os.path.getsize(r) == 0:
        print('  CERO BYTES     : %s' % r)
        malas += 1
    else:
        print('  %8d bytes : %s' % (os.path.getsize(r), r))
print('  ' + '-' * 58)
print('  rutas citadas en el acta                   : %d' % len(rutas))
print('  rutas que NO existen o estan en CERO sin declarar : %d' % malas)
