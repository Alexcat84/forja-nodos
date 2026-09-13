# -*- coding: utf-8 -*-
"""CORRECCION 7 DE LA COLA DEL AUDITOR (ACTA 22 seccion 4.4).

El resumen listaba `cinco personas` entre las cifras QUE SUS PASOS LLEVAN, y
ningun paso la llevaba. De las dos salidas que el auditor deja, tomo la que no
pierde material del libro: el paso 10 RECOGE EL LIMITE DE L53, que estaba fuera
del nodo, y entonces la afirmacion del resumen pasa a ser verdadera.
"""
import io
import json

RUTA = 'cuarentena/scott_radical_candor/montar_reuniones_solas_mentalidad_frecuencia.json'
d = json.load(io.open(RUTA, encoding='utf-8'))
viejo = d['pasos_accionables'][9]

NUEVO = (viejo[:-1] +
         u"; y por esa misma razon el texto dice que se limita a cinco personas a su cargo.")
d['pasos_accionables'][9] = NUEVO

AÑADIDO = (
    u" CORRECCION 7 DE LA COLA DE LA VUELTA 23, declarada y sin borrar el texto viejo (ACTA 22 "
    u"seccion 4.4): ESTE RESUMEN LISTABA cinco personas ENTRE LAS CIFRAS QUE SUS PASOS LLEVAN Y "
    u"NINGUN PASO LA LLEVABA. Grepeados los 22, el cinco aparecia en el paso 9 (las cinco de la "
    u"maniana, el gimnasio) y en el paso 10 (cincuenta minutos, cinco horas). La cifra no era falsa "
    u"contra el libro (la linea 53 escribe So I like to limit myself to five direct reports); la "
    u"AFIRMACION era falsa contra sus propios pasos, y de paso el nodo perdia el limite. DE LAS DOS "
    u"SALIDAS QUE EL AUDITOR DEJA (que el resumen deje de afirmarlo, o que el nodo recoja el limite) "
    u"TOMO LA SEGUNDA, y digo por que: la primera arregla la frase y pierde una linea del libro; la "
    u"segunda arregla la frase Y devuelve al nodo el limite que la linea 53 escribe. El paso 10 "
    u"gana la coletilla y por esa misma razon el texto dice que se limita a cinco personas a su "
    u"cargo. LA CUENTA DE PASOS NO SE MUEVE: 22 antes y 22 despues, porque la correccion alarga un "
    u"paso existente en vez de anadir uno nuevo, y asi cap_11 sigue en 187 pasos. RELECTURA DE "
    u"FIDELIDAD D.30 SOBRE LA COLETILLA: TRANSCRIPCION de la linea 53, misma linea de la que ya "
    u"salia el paso 10.")
if u'CORRECCION 7 DE LA COLA DE LA VUELTA 23' not in d['resumen_teorico']:
    d['resumen_teorico'] = d['resumen_teorico'] + AÑADIDO

with io.open(RUTA, 'w', encoding='utf-8', newline='\n') as f:
    f.write(json.dumps(d, ensure_ascii=False, indent=2, sort_keys=True))
    f.write(u'\n')

falta = [i + 1 for i, p in enumerate(d['pasos_accionables']) if u'cinco personas' in p]
print('| | |')
print('|---|---|')
print(u'| **fichero** | `%s` |' % RUTA)
print(u'| **el paso 10 acababa en** | `%s` |' % viejo[-80:])
print(u'| **el paso 10 acaba en** | `%s` |' % NUEVO[-80:])
print(u'| **pasos en los que ya aparece `cinco personas`** | **%s** |' % falta)
print(u'| **pasos, contados del fichero antes y despues** | **22** y **%d** |' % len(d['pasos_accionables']))
