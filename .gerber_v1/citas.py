# -*- coding: utf-8 -*-
"""LA CITA DE LINEA CON SU SALIDA PEGADA AL LADO (D.35, EXTRACTOR.md 15.5).

    python .gerber_v1/citas.py <fichero> <salida> <n> [<n> ...]

Imprime, linea a linea, lo que `sed -n '<n>p'` imprime de ese fichero. Cero
celdas tecleadas: el texto sale del fichero y no de mi memoria.

LA UNICA TRANSFORMACION, Y SE DECLARA EN LA PRIMERA LINEA DE SALIDA: el libro
trae guiones largos (U+2014) y medios (U+2013) de su editor, y el barrido de
estilo de esta casa los tumba en todo lo que ESTA casa escribe. El guion largo
se sustituye por coma mas espacio y el medio por guion corto, se cuenta cuantos
fueron, y la cuenta va en la cabecera. Es el mismo remedio que la vuelta 26
declaro en su cita de `L117`.
"""
import io, sys

LARGO, MEDIO = chr(0x2014), chr(0x2013)   # escritos por su punto de codigo: el barrido
                                          # de esta casa tumba el caracter literal, y con razon

RUTA, SALIDA, NUMEROS = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3:]]
lineas = io.open(RUTA, encoding='utf-8').read().splitlines()

out, largos, medios = [], 0, 0
for n in NUMEROS:
    t = lineas[n - 1]
    largos += t.count(LARGO)
    medios += t.count(MEDIO)
    t = t.replace(LARGO, u', ').replace(MEDIO, u'-')
    out.append(u'%d: %s' % (n, t))

cab = [u'AVISO: cero celdas tecleadas. Cada linea es la que sed -n imprime de %s.' % RUTA,
       u'UNICA TRANSFORMACION DECLARADA: %d guion(es) largo(s) U+2014 sustituido(s) por coma mas'
       % largos,
       u'espacio y %d guion(es) medio(s) U+2013 por guion corto, porque el barrido de estilo de' % medios,
       u'esta casa tumba los dos. El resto es byte a byte el del libro.',
       u'']
io.open(SALIDA, 'w', encoding='utf-8', newline='\n').write(u'\n'.join(cab + out) + u'\n')
print(u'escrito %s: %d linea(s), %d guion(es) largo(s) y %d medio(s) sustituidos'
      % (SALIDA, len(NUMEROS), largos, medios))
