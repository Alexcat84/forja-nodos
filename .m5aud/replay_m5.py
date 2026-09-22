# -*- coding: utf-8 -*-
"""EL REPLAY DEL REGISTRO DE CREDITO EN LOS DOS ESTADOS QUE TUVO EN LA VUELTA 4.

El registro es append only: en esta vuelta solo existio con 14 lineas (al abrir)
y con 18 (al cerrar). Se replica cada estado en un fichero aparte y se corre el
mismo `revisar` del instrumento sobre los dos. No se toca el registro de verdad.
"""

import io
import os
import sys
import tempfile

sys.path.insert(0, '.')

from src import credito

REGISTRO = 'docs/loop/CREDITO_marquet_turn_the_ship.jsonl'


def main():
    todas = [l for l in io.open(REGISTRO, encoding='utf-8').read().splitlines() if l.strip()]
    print('lineas del registro hoy: %d' % len(todas))
    for corte in (14, len(todas)):
        ruta = os.path.join(tempfile.gettempdir(), 'cred_m5_%d.jsonl' % corte)
        io.open(ruta, 'w', encoding='utf-8').write(u"\n".join(todas[:corte]) + u"\n")
        sucesos = credito.leer(ruta_registro=ruta)
        vigilables = [s for s in sucesos
                      if s.get('tipo') == 'tanda' and not s.get('migrado') and 'cae' in s]
        discrepancias = credito.revisar(sucesos=sucesos)
        estado = credito.estado(sucesos=sucesos)
        print('--- con las primeras %d lineas' % corte)
        print('    tandas vigilables (con cae escrito): %d' % len(vigilables))
        print('    discrepancias del replay           : %d' % len(discrepancias))
        for caso in discrepancias:
            print('      linea %d, %s en %s: declara %d, el replay da %d'
                  % (caso['linea_del_fichero'], caso['especie'], caso['tanda'],
                     caso['declarada'], caso['replay']))
        dato = estado.get('CIFRA PUBLICADA', {})
        print('    CIFRA PUBLICADA declarada          : %s  (de: %s)'
              % (dato.get('racha'), dato.get('de')))


main()
