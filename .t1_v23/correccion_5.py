# -*- coding: utf-8 -*-
"""CORRECCION 5 DE LA COLA DEL AUDITOR (ACTA 22 seccion 4.2).

Dos encargos del libro perdidos (L123 y L127), un tercer motivo de L127 mutado, y
un resumen_teorico que afirma que el libro solo encarga en dos seniales cuando
encarga en cuatro. No es puente: es lo contrario, no escribir lo que el libro dice.
"""
import io
import json

RUTA = 'cuarentena/scott_radical_candor/leer_seniales_fallo_jefe_reunion_solas.json'
d = json.load(io.open(RUTA, encoding='utf-8'))
viejos = list(d['pasos_accionables'])

P4_NUEVO = (u"Mira si solo oyes buenas noticias: si es asi, es senial de que la gente no se siente "
            u"comoda trayendote sus problemas, o de que cree que no vas a hacer nada con ellos. En "
            u"esos casos, pide explicitamente las malas noticias, y no dejes caer el asunto hasta "
            u"que oigas alguna.")
P6_NUEVO = (u"Mira si llegan sin agenda: si vienen sistematicamente sin temas que tratar, puede "
            u"significar que estan desbordados, que no entienden para que es esta reunion, o que no "
            u"la consideran util. Se directo pero educado, con la frase que el texto escribe: este "
            u"es tu tiempo, pero no pareces venir con mucho de que hablar. Puedes decirme por que?")
d['pasos_accionables'][3] = P4_NUEVO
d['pasos_accionables'][5] = P6_NUEVO

V_RES = (u'LA UNICA ACCION ENCARGADA QUE EL TEXTO DA ES LA DE LA SEGUNDA SENIAL (encourage them to '
         u'use the time more constructively) y la del recordatorio de la cuarta (Remember that '
         u'phrase). Las otras tres solo traen su lectura, y por eso sus pasos solo traen su lectura: '
         u'completar las tres que faltan seria exactamente el puente que D.30 llama el destinatario.')
N_RES = (u'EL TEXTO ENCARGA EN CUATRO DE LAS CINCO SENIALES, contadas una a una contra su linea: la '
         u'segunda (linea 121, encourage them to use the time more constructively), la tercera '
         u'(linea 123, you need to ask explicitly for the bad news, Don\'t let the issue drop till '
         u'you hear some), la cuarta (linea 125, Remember that phrase) y la quinta (linea 127, Be '
         u'direct but polite, con la frase literal que hay que decir). LA UNICA QUE SOLO TRAE '
         u'LECTURA ES LA PRIMERA, la de las cancelaciones de la linea 119.')
d['resumen_teorico'] = d['resumen_teorico'].replace(V_RES, N_RES)

V_FID = (u'RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 6 pasos, 6 TRANSCRIPCION, 0 PUENTE.')
N_FID = (u'RELECTURA DE FIDELIDAD D.30: 6 pasos, 6 TRANSCRIPCION, 0 PUENTE, y sigue siendo cierta '
         u'porque la caida de esta ficha NO fue un puente sino lo contrario, callar lo que el libro '
         u'si dice, que es una especie que D.30 no cubre.')
d['resumen_teorico'] = d['resumen_teorico'].replace(V_FID, N_FID)

AÑADIDO = (
    u" CORRECCION 5 DE LA COLA DE LA VUELTA 23, declarada y sin borrar el texto viejo (ACTA 22 "
    u"seccion 4.2): ESTA FICHA PERDIA DOS ENCARGOS DEL LIBRO Y SU RESUMEN AFIRMABA QUE NO EXISTEN. "
    u"La frase vieja decia que LA UNICA ACCION ENCARGADA QUE EL TEXTO DA ES LA DE LA SEGUNDA SENIAL "
    u"y la del recordatorio de la cuarta, y que las otras tres solo traen su lectura, y NO ES "
    u"CIERTO. Recuperados: el paso 4 gana el encargo de la linea 123 (pedir explicitamente las malas "
    u"noticias y no dejar caer el asunto hasta oir alguna) y el paso 6 gana el de la linea 127 (ser "
    u"directo pero educado, con su frase literal). Y CORREGIDO ADEMAS EL TERCER MOTIVO DE LA LINEA "
    u"127: el paso 6 escribia que no la estan tomando en serio donde el libro escribe they don't "
    u"consider it useful, que no son lo mismo y que ninguna regla de traduccion pedia cambiar; hoy "
    u"escribe que no la consideran util. LA ESPECIE NO ES PUENTE: es lo contrario, no escribir lo "
    u"que el libro si dice, y D.30 no la cubre. El entregable_esperado ya prometia la accion que el "
    u"texto encarga para las que la llevan y entregaba dos de cuatro; hoy entrega las cuatro.")
if u'CORRECCION 5 DE LA COLA DE LA VUELTA 23' not in d['resumen_teorico']:
    d['resumen_teorico'] = d['resumen_teorico'] + AÑADIDO

with io.open(RUTA, 'w', encoding='utf-8', newline='\n') as f:
    f.write(json.dumps(d, ensure_ascii=False, indent=2, sort_keys=True))
    f.write(u'\n')

print('| senial | lo que el paso traia | lo que el paso trae |')
print('|---|---|---|')
print(u'| `L123`, solo buenas noticias | `%s` | `%s` |' % (viejos[3][-90:], d['pasos_accionables'][3][-90:]))
print(u'| `L127`, sin agenda | `%s` | `%s` |' % (viejos[5][-90:], d['pasos_accionables'][5][-90:]))
print(u'| **pasos, contados del fichero** | **%d** | **%d** |' % (len(viejos), len(d['pasos_accionables'])))
