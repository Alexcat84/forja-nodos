# -*- coding: utf-8 -*-
"""ANEXA LAS SECCIONES DE LA TAREA 2 Y DE LA TAREA 3, CON TODA TABLA PEGADA DE SU FICHERO.

Se corre cuando los informes de candidato ya estan escritos. Ninguna celda se teclea:
las tablas se leen del .txt de su instrumento y los huecos @@X@@ se rellenan de ahi.

    python .vm01/finalizar.py
"""
import io, os, re, subprocess, sys

REPORTE = 'docs/loop/REPORTE.md'


def correr(orden, salida):
    with io.open(salida, 'w', encoding='utf-8', newline='\n') as destino:
        codigo = subprocess.call(orden, stdout=destino, stderr=subprocess.STDOUT)
    if codigo:
        sys.exit('EN ROJO: %s devolvio %d, ver %s' % (' '.join(orden), codigo, salida))
    return io.open(salida, encoding='utf-8').read()


def tabla(texto, cabecera):
    lineas = texto.split('\n')
    i = next(n for n, l in enumerate(lineas) if l.startswith(cabecera))
    fin = i
    while fin < len(lineas) and lineas[fin].startswith('|'):
        fin += 1
    return '\n'.join(lineas[i:fin])


def veredicto(fichero):
    texto = io.open(os.path.join('.vm01', 'aduana', fichero), encoding='utf-8').read()
    return re.search(r"\[(ENTRARIA|BLOQUEARIA|CAERIA)\]", texto).group(1)


tanda = correr([sys.executable, '.vm01/tanda.py'], '.vm01/tanda_cap03.txt')
vered = correr([sys.executable, '.vm01/veredictos.py'], '.vm01/veredictos_cap03.txt')

huecos = {
    'TABLA_TANDA': tabla(tanda, '| # | pieza |'),
    'TABLA_VEREDICTOS': tabla(vered, '| candidato | vecino levantado |'),
    'VER_C0': veredicto('c0_encargar_meta_especifica_dejar_libre_metodo.txt'),
    'VER_C00': veredicto('c00_cambiar_forma_trabajar_conservar_plantilla.txt'),
    'PARES': re.search(r'\*\*(\d+)\*\* \| \| \| \| \| \| \|', vered).group(1),
}

fide = io.open('.vm01/fidelidad_lote.txt', encoding='utf-8').read()
huecos['TABLA_UNIDADES'] = tabla(fide, '| unidad | nodos |')
huecos['TABLA_FRENO'] = tabla(fide, '| | |')
huecos['TABLA_RETIRADOS'] = tabla(fide, '| nodo | paso | especie |')

if os.path.exists('.vm01/informe_lote.txt') and os.path.getsize('.vm01/informe_lote.txt') > 200:
    lote = io.open('.vm01/informe_lote.txt', encoding='utf-8').read()
    trozo = lote[lote.index('candidatos revisados'):lote.index('LA LISTA COMPLETA')]
    huecos['SALDO_LOTE'] = '\n'.join('    ' + l for l in trozo.strip().split('\n'))
    choca = re.search(r'CHOCAN entre si dentro del lote\s*:\s*(\d+)', lote).group(1)
    huecos['NOTA_LOTE'] = (
        '**`CHOCAN entre si dentro del lote`: `%s`.** Es la cifra por la que este informe existe, y '
        'es la unica que los nueve informes de uno en uno no podian dar.' % choca)
else:
    huecos['SALDO_LOTE'] = (
        '    (SIN SALDO: el informe del lote entero se lanzo y NO cerro dentro del turno)')
    huecos['NOTA_LOTE'] = (
        '> **DECLARADO Y NO MAQUILLADO: EL INFORME DEL LOTE ENTERO SE LANZO Y NO CERRO DENTRO DE MI '
        'TURNO.** `.vm01/informe_lote.txt` queda en su tamanio real y `VACIA A PROPOSITO: el '
        'instrumento se lanzo y no cerro en el turno` va escrito al lado de la unica cifra que le '
        'faltaba a esta vuelta.\n>\n'
        '> **ES EXACTAMENTE LA MEDIDA DE `D.43`, REPETIDA EN ESTE FRENTE:** *una cifra que no cabe en '
        'un turno no se firma en un turno.* Con `9` candidatos a `4` minutos medidos por candidato '
        '(`1.c`), el lote entero no cabe, y por eso el serial se lo quito al extractor hace cuatro '
        'dias. **Va como propuesta `2` en `C.8` y no como cifra inventada.**\n>\n'
        '> **LO QUE SI TENGO, Y LO DIGO CON SU LIMITE:** los `9` informes de candidato de esta vuelta '
        'dan `0 CAERIA` y `0 CHOCAN` **cada uno contra los demas de a uno**. Lo que no tengo es el '
        'cruce simultaneo de los nueve, **y no lo firmo.**')

destino = io.open(REPORTE, 'a', encoding='utf-8', newline='\n')
for ruta in ('.vm01/t2_a.md', '.vm01/t2_b_tanda.md', '.vm01/t2_b.md', '.vm01/t2_c.md',
             '.vm01/t2_d_plantilla.md', '.vm01/t2_f_plantilla.md', '.vm01/t3_plantilla.md'):
    texto = io.open(ruta, encoding='utf-8').read()
    for nombre, valor in huecos.items():
        texto = texto.replace('@@%s@@' % nombre, valor)
    sobra = sorted(set(re.findall(r'@@[A-Z_]+@@', texto)))
    if sobra:
        sys.exit('HUECO SIN RELLENAR en %s: %s' % (ruta, sobra))
    destino.write(texto)
destino.close()
print('ANEXADAS las secciones de la TAREA 2 y de la TAREA 3')
print('pares con veredicto: %s' % huecos['PARES'])
