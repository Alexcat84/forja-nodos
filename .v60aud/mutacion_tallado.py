# -*- coding: utf-8 -*-
"""Cosecha 7.C, la otra guarda que la vuelta 59 declara mordiendo (SS.5.c):
el tallado --estricto le marco en rojo las tablas de SS.3.b y SS.3.c por
llevar `salida=` a secas cuando la tabla resume su fichero en vez de
reproducirlo celda a celda. Les quito el `parcial` y compruebo que CAEN."""
import io, sys
sys.path.insert(0, 'scripts')
import tallar_reporte as t

VIVO, COPIA = 'docs/loop/REPORTE.md', '.v60aud/REPORTE_mutado.md'
texto = io.open(VIVO, encoding='utf-8').read()
MARCAS = ['<!-- TALLADO: parcial salida=.v59ext/d006_fuente_tres_nodos.txt -->',
          '<!-- TALLADO: parcial salida=.v59ext/d006_pasos_releidos.txt -->']
for m in MARCAS:
    assert m in texto, m

def mirar(ruta, etiqueta):
    d = t.revisar(ruta_reporte=ruta)
    mias = [x for x in d
            if 'd006_fuente' in str(x['tabla'].get('salida'))
            or 'd006_pasos' in str(x['tabla'].get('salida'))]
    rojas = [x for x in d if x['estado'] not in ('VERDE', 'SIN COMPROBAR')]
    print('%-9s  tablas=%d  rojas en todo el fichero=%d' % (etiqueta, len(d), len(rojas)))
    for x in mias:
        print('           %-34s -> %s  (parcial=%s)'
              % (str(x['tabla'].get('salida'))[-34:], x['estado'],
                 x['tabla'].get('parcial')))
    return [x['estado'] for x in mias]

a = mirar(VIVO, 'TAL CUAL')
mut = texto
for m in MARCAS:
    mut = mut.replace(m, m.replace('parcial ', ''))
io.open(COPIA, 'w', encoding='utf-8').write(mut)
b = mirar(COPIA, 'MUTADO')
print()
print('las dos tablas pasan de %s a %s' % (a, b))

print()
print('=== y ahora el dictamen en --estricto, que es el que el reporte dice que le mordio ===')
for ruta, etq in ((VIVO, 'TAL CUAL'), (COPIA, 'MUTADO')):
    d = t.revisar(ruta_reporte=ruta)
    inf = t.texto_informe(d, estricto=True)
    ultimas = [l for l in inf.split(chr(10)) if 'd006' in l]
    print('%-9s  %s' % (etq, inf.strip().split(chr(10))[-1][:100]))
    for l in ultimas:
        print('           ', l.strip()[:120])
