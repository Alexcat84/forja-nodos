# -*- coding: utf-8 -*-
"""CORRECCION 3 DE LA COLA DEL AUDITOR (ACTA 22 seccion 3.7).

La pieza 14 de cap_10 gana su paso 12 con la primera mitad de L91, y su
resumen_teorico dice de donde sale y que el borde viejo era corto. El texto
viejo NO se borra: queda escrito dentro del propio resumen.
"""
import io
import json

RUTA = 'cuarentena/scott_radical_candor/desplegar_tres_conversaciones_carrera.json'
d = json.load(io.open(RUTA, encoding='utf-8'))

PASO_12 = (u"Y ten presente lo que el texto dice que se juega tu capacidad de hacerlas bien: "
           u"construir confianza con la gente que te reporta, y averiguar para que papel encaja "
           u"mejor cada persona, para que tu equipo pueda conseguir resultados.")

antes = len(d['pasos_accionables'])
if PASO_12 not in d['pasos_accionables']:
    d['pasos_accionables'].append(PASO_12)
despues = len(d['pasos_accionables'])

AÑADIDO = (
    u" CORRECCION 3 DE LA COLA DE LA VUELTA 23, declarada y sin borrar nada (ACTA 22 seccion 3.7): "
    u"ESTE NODO GANA UN PASO 12 QUE SALE DE LA PRIMERA MITAD DE LA LINEA 91, y con el la unidad de "
    u"origen deja de ser solo las lineas 19, 21 y 43. La frase vieja de este resumen decia que la "
    u"linea 91 NO aporta pasos a este nodo y se queda en el resto de la frontera, y esa frase es "
    u"FALSA desde hoy: el auditor adjudico que los dos fines que la linea 91 escribe (construir "
    u"confianza con quien te reporta, y averiguar para que papel encaja mejor cada persona para que "
    u"el equipo consiga resultados) no estan entre los tres que el paso 4 recoge de la linea 19, y "
    u"que esta casa no puede aceptar tres fines de la linea 19 como pasos y rechazar dos de la 91 "
    u"por ser fines. LA SEGUNDA MITAD DE LA LINEA 91 NO VIAJA Y SE DICE POR QUE: la direccion web y "
    u"el libro que Russ esta escribiendo son promocion, no doctrina. LO QUE ESTO MUEVE Y LO QUE NO: "
    u"la frontera de cap_10 SIGUE EN 14 PIEZAS, este nodo pasa de 11 a 12 pasos, y el resto de "
    u"cap_10 baja de 1.686 a 1.585 palabras porque el tramo L88 a L92 deja de ser resto. "
    u"RELECTURA DE FIDELIDAD D.30 SOBRE EL PASO NUEVO: 12 pasos, 12 TRANSCRIPCION, 0 PUENTE. P12 de "
    u"la primera mitad de la linea 91.")

if u'CORRECCION 3 DE LA COLA DE LA VUELTA 23' not in d['resumen_teorico']:
    d['resumen_teorico'] = d['resumen_teorico'] + AÑADIDO

with io.open(RUTA, 'w', encoding='utf-8', newline='\n') as f:
    f.write(json.dumps(d, ensure_ascii=False, indent=2, sort_keys=True))
    f.write(u'\n')

print('| | |')
print('|---|---|')
print(u'| **fichero** | `%s` |' % RUTA)
print(u'| **pasos antes** | **%d** |' % antes)
print(u'| **pasos despues** | **%d** |' % despues)
print(u'| **paso 12, impreso del fichero** | `%s` |' % d['pasos_accionables'][11])
