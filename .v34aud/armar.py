# -*- coding: utf-8 -*-
"""ARMA docs/loop/APERTURA_CIEGA.md INSERTANDO LAS SALIDAS DE LOS INSTRUMENTOS
TAL CUAL, leidas de su fichero. Ninguna tabla de instrumento se teclea: se lee.

  <<<INSERTA ruta>>>          la mete tal cual (para las tablas markdown, que
                              D.41 tiene que poder ver y tallar)
  <<<CODIGO ruta>>>           la mete sangrada cuatro espacios, que es como esta
                              casa escribe la salida de un comando

LA SANGRIA NO CAMBIA NI UN CARACTER DE LA SALIDA: solo antepone cuatro espacios.
"""
import io, re, sys
plantilla = io.open(sys.argv[1], encoding='utf-8').read()

def leer(ruta):
    return io.open(ruta.strip(), encoding='utf-8').read().rstrip('\n')

def tal_cual(m):
    return leer(m.group(1))

def sangrada(m):
    return '\n'.join(('    ' + l).rstrip() for l in leer(m.group(1)).split('\n'))

salida = re.sub(r'<<<CODIGO ([^>]+)>>>', sangrada, plantilla)
salida = re.sub(r'<<<INSERTA ([^>]+)>>>', tal_cual, salida)
io.open(sys.argv[2], 'w', encoding='utf-8', newline='\n').write(salida)
print('escrito %s, %d lineas' % (sys.argv[2], salida.count('\n') + 1))
