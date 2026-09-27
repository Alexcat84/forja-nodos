# -*- coding: utf-8 -*-
"""LA TABLA DE RUTAS DE LA VUELTA 22, CONSTRUIDA PARA SOBREVIVIR A SU PROPIA PUBLICACION.

TAREA 5 y ACTA 21 seccion 4.7. El diagnostico del auditor no fue que la vuelta 21
incumpliera su remedio: fue que DOS de sus nueve filas contaban el fichero que el
propio acto de publicar la tabla estaba creando, y esas no se arreglan midiendo
mejor.

LA REGLA QUE APLICA ESTE GUION, literal del encargo: las filas que cuentan
artefactos que el acto de publicar crea O SE CUENTAN CON EL FICHERO EXCLUIDO Y SE
DICE CUAL, O NO SE PUBLICAN. Las dos salidas valen; lo que no vale es una cifra
que caduca en un minuto.

COMO LO HACE, y es lo unico interesante de este fichero: cada fila declara su
ALCANCE (que comando la cuenta) y su ESPECIE (cerrada o auto referencial). En las
auto referenciales el guion EXCLUYE POR NOMBRE los ficheros que van a nacer
despues de contarse, y los IMPRIME, para que quien audite pueda sumarlos.
"""
import fnmatch
import glob
import os

# LOS QUE NACEN DESPUES DE QUE ESTA TABLA SE CUENTE, excluidos POR NOMBRE.
# No es una estimacion: son los ficheros que el cierre escribe a continuacion.
NACEN_DESPUES = [
    '.t1_v22/salida_rutas_cierre.txt',      # la salida de ESTE guion
    '.t1_v22/salida_gate_cierre.txt',
    '.t1_v22/salida_guiones_cierre.txt',
    '.t1_v22/salida_aceptacion_cierre.txt',
    '.v22/frag_t5.md',                      # el fragmento que CONTIENE esta tabla
    '.v22/frag_cierre.md',
]

FILAS = [
    ('.aduana_v22/*.txt', 'ls .aduana_v22/*.txt | wc -l',
     'cerrada', 'los informes de un candidato de esta vuelta'),
    ('.aduana_v22/[ABCD]_*.txt', 'ls .aduana_v22/[ABCD]_*.txt | wc -l',
     'cerrada', 'los de cap_11, escritos cuatro por lote'),
    ('.t1_v22/*.py', 'ls .t1_v22/*.py | wc -l',
     'cerrada', 'los guiones de la vuelta'),
    ('.t1_v22/*.txt', 'ls .t1_v22/*.txt | wc -l',
     'AUTO REFERENCIAL', 'las salidas guardadas'),
    ('.v22/*.md', 'ls .v22/*.md | wc -l',
     'AUTO REFERENCIAL', 'los fragmentos del reporte'),
    ('cuarentena/scott_radical_candor/*.json',
     'ls cuarentena/scott_radical_candor/*.json | wc -l',
     'cerrada', 'la bandeja del lote 4 entera'),
]


def norm(p):
    return os.path.normpath(p).replace('\\', '/')


print('| ruta | comando, QUE ES SU ALCANCE | especie | **cuenta** | que es, y que excluye |')
print('|---|---|---|---:|---|')
pendientes = []
for patron, comando, especie, que in FILAS:
    hay = sorted(norm(x) for x in glob.glob(patron))
    if especie == 'AUTO REFERENCIAL':
        futuros = [norm(f) for f in NACEN_DESPUES if fnmatch.fnmatch(norm(f), norm(patron))]
        hay = [x for x in hay if x not in futuros]
        pendientes.append((patron, futuros))
        nota = '**excluidos por nombre: %s**' % ', '.join(
            '`%s`' % os.path.basename(f) for f in futuros)
        print('| `%s` | `%s` | **AUTO REFERENCIAL** | **%d** | %s. %s |'
              % (patron, comando.replace('|', chr(92) + '|'), len(hay), que, nota))
    else:
        print('| `%s` | `%s` | cerrada | **%d** | %s |'
              % (patron, comando.replace('|', chr(92) + '|'), len(hay), que))

print('')
print('LAS DOS FILAS AUTO REFERENCIALES, CON SUS EXCLUIDOS NOMBRADOS UNO A UNO:')
for patron, futuros in pendientes:
    print('  %-16s excluye %d: %s' % (patron, len(futuros), ', '.join(futuros)))
print('')
print('POR QUE SE EXCLUYEN Y NO SE ESTIMAN: son los ficheros que el cierre escribe')
print('DESPUES de que esta tabla se cuente. Sumarlos seria publicar una cifra que')
print('todavia no es cierta; contarlos sin decirlo es lo que hizo falsas las dos')
print('filas de la vuelta 21. Quien audite suma estos nombres y vuelve a contar.')
print('')
print('=' * 74)
print('LA FILA DE ALCANCE DE cuarentena/_insertados/, RECONCILIADA (TAREA 5)')
print('=' * 74)
plano = sorted(glob.glob('cuarentena/_insertados/*.json'))
recursivo = [os.path.join(r, f) for r, _d, fs in os.walk('cuarentena/_insertados')
             for f in fs if f.endswith('.json')]
subcarpetas = sorted(d for d in os.listdir('cuarentena/_insertados')
                     if os.path.isdir(os.path.join('cuarentena/_insertados', d)))
print('| comando | alcance | cuenta |')
print('|---|---|---:|')
print('| `ls cuarentena/_insertados/*.json \\| wc -l` | **glob PLANO**: solo la raiz de la carpeta | **%d** |' % len(plano))
print('| `find cuarentena/_insertados -name "*.json" \\| wc -l` | **RECURSIVO**: raiz mas subcarpetas | **%d** |' % len(recursivo))
print('')
print('LAS DOS SON CIERTAS Y MIDEN COSAS DISTINTAS. La reconciliacion es que en la')
print('raiz NO hay ni un JSON suelto: los %d viven en %d subcarpetas por libro.'
      % (len(recursivo), len(subcarpetas)))
for d in subcarpetas:
    n = len([f for f in os.listdir(os.path.join('cuarentena/_insertados', d))
             if f.endswith('.json')])
    print('   cuarentena/_insertados/%-24s %4d' % (d + '/', n))
print('   %-47s %4d' % ('SUMA DE LAS SUBCARPETAS', len(recursivo)))
print('   %-47s %4d' % ('SUELTOS EN LA RAIZ', len(plano)))
