# -*- coding: utf-8 -*-
"""CORRECCION 6 DE LA COLA DEL AUDITOR (ACTA 22 seccion 4.3), la mitad de fichero.

El resumen_teorico de preguntar_seguimiento_hallar_huecos escribia que la arista
va declarada en docs/loop/REPORTE.md de la vuelta 22, y el reporte de la vuelta 22
dice expresamente que NO la declara, porque el remite de L97 no se transcribio
como paso y sin paso no hay cita. Una de las dos frases sobra, y sobra la del
fichero: el reporte tiene razon.

LA OTRA MITAD (las dos aristas D.29 que L57 debe) NO es de fichero: se declara en
el reporte y se cablea el dia de la insercion.
"""
import io
import json

RUTA = 'cuarentena/scott_radical_candor/preguntar_seguimiento_hallar_huecos.json'
d = json.load(io.open(RUTA, encoding='utf-8'))

VIEJA = (u'Ese procedimiento ya vive en la bandeja como impedir_punialadas_espalda_equipo, y la '
         u'arista va declarada en docs/loop/REPORTE.md de la vuelta 22.')
NUEVA = (u'Ese procedimiento ya vive en la bandeja como impedir_punialadas_espalda_equipo, y EL PAR '
         u'SE DECLARA COMO LECTURA SIN ARISTA: sin paso en la madre no hay linea que citar, y una '
         u'arista sin su linea es una afirmacion sin cita.')
assert VIEJA in d['resumen_teorico']
d['resumen_teorico'] = d['resumen_teorico'].replace(VIEJA, NUEVA)

AÑADIDO = (
    u" CORRECCION 6 DE LA COLA DE LA VUELTA 23, mitad de fichero, declarada y sin borrar el texto "
    u"viejo (ACTA 22 seccion 4.3): ESTE RESUMEN PROMETIA UNA ARISTA QUE EL REPORTE NO DECLARA. "
    u"Escribia la arista va declarada en docs/loop/REPORTE.md de la vuelta 22, y el reporte de la "
    u"vuelta 22 escribe en su seccion P.8, en la tabla de los pares que NO llevan arista, que el "
    u"remite existe en el LIBRO pero no en mi nodo. Una de las dos frases sobraba y sobraba esta: "
    u"el par queda declarado como LECTURA SIN ARISTA. LA OTRA MITAD DE LA CORRECCION 6 NO ES DE "
    u"ESTE FICHERO: son las dos aristas D.29 que la linea 57 de cap_11 debe, madre "
    u"montar_reuniones_solas_mentalidad_frecuencia con su paso 15, hijos "
    u"desplegar_tres_conversaciones_carrera y entregar_evaluacion_formal_desempenio_nueve_consejos, "
    u"y van declaradas en el reporte de la vuelta 23 para cablearse el dia de la insercion.")
if u'CORRECCION 6 DE LA COLA DE LA VUELTA 23' not in d['resumen_teorico']:
    d['resumen_teorico'] = d['resumen_teorico'] + AÑADIDO

with io.open(RUTA, 'w', encoding='utf-8', newline='\n') as f:
    f.write(json.dumps(d, ensure_ascii=False, indent=2, sort_keys=True))
    f.write(u'\n')

print('| | |')
print('|---|---|')
print(u'| **fichero** | `%s` |' % RUTA)
print(u'| **decia** | `%s` |' % VIEJA)
print(u'| **dice** | `%s` |' % NUEVA)
print(u'| **pasos, contados del fichero antes y despues** | **16** y **%d** |' % len(d['pasos_accionables']))
