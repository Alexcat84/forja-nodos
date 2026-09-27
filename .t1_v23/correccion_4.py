# -*- coding: utf-8 -*-
"""CORRECCION 4 DE LA COLA DEL AUDITOR (ACTA 22 seccion 4.1).

El paso 2 escribia `candelabro de las siete velas` y el libro escribe `A menorah?`
y nada mas. Las siete velas las puso el extractor: es PUENTE por D.30, especie el
objeto. Se retira la cuenta inventada y el resumen deja de declarar 0 PUENTE.
"""
import io
import json

RUTA = 'cuarentena/scott_radical_candor/debatir_decidir_asuntos_cultura_evitar_delegar.json'
d = json.load(io.open(RUTA, encoding='utf-8'))

VIEJO = u'si va a haber candelabro de las siete velas'
NUEVO = u'si va a haber candelabro'
antes = d['pasos_accionables'][1]
d['pasos_accionables'][1] = antes.replace(VIEJO, NUEVO)

V_RES = (u'LAS DOS REFERENCIAS CULTURALES DE LAS LINEAS 303 Y 305 (el candelabro de las siete velas '
         u'y la novela de la isla) SE TRANSCRIBEN POR LO QUE SON, un objeto de una fiesta y el '
         u'nombre de un libro, y no se convierten en otra cosa.')
N_RES = (u'LAS DOS REFERENCIAS CULTURALES DE LAS LINEAS 303 Y 305 (el candelabro y la novela de la '
         u'isla) SE TRANSCRIBEN POR LO QUE SON, un objeto de una fiesta y el nombre de un libro, y '
         u'no se convierten en otra cosa.')
d['resumen_teorico'] = d['resumen_teorico'].replace(V_RES, N_RES)

V_FID = u'RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 6 pasos, 6 TRANSCRIPCION, 0 PUENTE.'
N_FID = (u'RELECTURA DE FIDELIDAD D.30, CORREGIDA EN LA VUELTA 23 Y SIN BORRAR LA VIEJA: esta ficha '
         u'declaraba 6 pasos, 6 TRANSCRIPCION, 0 PUENTE, Y ERA FALSO. Hoy declara 6 pasos, 5 '
         u'TRANSCRIPCION y 1 PUENTE CAZADO Y RETIRADO.')
d['resumen_teorico'] = d['resumen_teorico'].replace(V_FID, N_FID)

AÑADIDO = (
    u" CORRECCION 4 DE LA COLA DE LA VUELTA 23, declarada y sin borrar el texto viejo (ACTA 22 "
    u"seccion 4.1): EL PASO 2 DECIA si va a haber candelabro de las siete velas Y EL LIBRO ESCRIBE "
    u"A menorah? Y NADA MAS. La palabra candle no aparece en el capitulo, y las tres apariciones de "
    u"seven estan en las lineas 57, 61 y 153, ninguna en el tramo 301 a 305. LAS SIETE VELAS LAS "
    u"PUSO EL EXTRACTOR: es PUENTE por D.30, especie el objeto. Hoy el paso 2 escribe si va a haber "
    u"candelabro, sin cuenta. Y LA INVENCION ADEMAS SENIALABA AL OBJETO EQUIVOCADO, que es justo el "
    u"riesgo que D.30 describe: el candelabro de la fiesta de diciembre tiene nueve brazos y el de "
    u"siete es el del templo; el libro no dio el dato porque no hacia falta, y rellenarlo salio mal. "
    u"LA FRASE DE ESTE MISMO RESUMEN QUE DECLARABA 0 PUENTE ERA LA QUE MAS LO ESCONDIA, porque "
    u"afirmaba que las dos referencias culturales se transcriben por lo que son en la misma frase en "
    u"que una de ellas estaba inventada. cap_11 pasa de 0 de 187 a 1 de 187, o sea 0,53.")
if u'CORRECCION 4 DE LA COLA DE LA VUELTA 23' not in d['resumen_teorico']:
    d['resumen_teorico'] = d['resumen_teorico'] + AÑADIDO

with io.open(RUTA, 'w', encoding='utf-8', newline='\n') as f:
    f.write(json.dumps(d, ensure_ascii=False, indent=2, sort_keys=True))
    f.write(u'\n')

print('| | |')
print('|---|---|')
print(u'| **fichero** | `%s` |' % RUTA)
print(u'| **el paso 2 decia** | `%s` |' % VIEJO)
print(u'| **el paso 2 dice** | `%s` |' % NUEVO)
print(u'| **pasos, contados del fichero antes y despues** | **6** y **%d** |' % len(d['pasos_accionables']))
print(u'| **la relectura de fidelidad de la ficha** | de `6 TRANSCRIPCION, 0 PUENTE` a `5 TRANSCRIPCION, 1 PUENTE cazado y retirado` |')
