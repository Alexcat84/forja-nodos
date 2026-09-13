# -*- coding: utf-8 -*-
"""CORRECCION 8 DE LA COLA DEL AUDITOR (ACTA 22 seccion 3.3).

Los pasos 3, 4 y 5 empezaban `No pruebes`, y el libro NO prohibe: cuenta que no
cuajaron. Convertir un informe de fracaso en un imperativo negativo mueve el modo
del libro. Los tres llevan ahora la evidencia del libro dentro.
"""
import io
import json

RUTA = 'cuarentena/scott_radical_candor/pelear_proliferacion_reuniones_bloquear_ejecucion.json'
d = json.load(io.open(RUTA, encoding='utf-8'))
viejos = list(d['pasos_accionables'])

P3 = (u"Ten delante el primer remedio que el texto cuenta que no cuaja, quitar las sillas de las "
      u"salas de reunion: el texto reconoce que en teoria acorta las reuniones porque casi nadie "
      u"aguanta de pie mas de una hora, que hay investigacion que dice que la gente es mas creativa "
      u"de pie que sentada, que hay quien dice que estar sentado es el nuevo fumar, y que ademas te "
      u"ahorras el mobiliario, y aun asi cuenta que nunca funciona de verdad y que no conoce "
      u"ninguna empresa que se haya mantenido en ello.")
P4 = (u"Ten delante el segundo, declarar un dia de la semana sin reuniones: el texto cuenta que "
      u"distintos equipos lo intentaron y que ninguno fue capaz de sostenerlo.")
P5 = (u"Y ten delante el tercero, ponerse el objetivo de terminar antes de tiempo una cuarta parte "
      u"de tus reuniones: el texto cuenta que le encanto la idea y que no cree que quien se la puso "
      u"llegara nunca a cumplirla.")
d['pasos_accionables'][2] = P3
d['pasos_accionables'][3] = P4
d['pasos_accionables'][4] = P5

AÑADIDO = (
    u" CORRECCION 8 DE LA COLA DE LA VUELTA 23, declarada y sin borrar el texto viejo (ACTA 22 "
    u"seccion 3.3): LOS PASOS 3, 4 Y 5 EMPEZABAN POR No pruebes Y EL LIBRO NO PROHIBE, CUENTA QUE "
    u"NO CUAJARON. Las tres evidencias, con su linea: it never really works en la linea 229, None "
    u"was ever able to stick to it en la 231, y I don't think he ever hit the goal en la 231. "
    u"CONVERTIR UN INFORME DE FRACASO EN UN IMPERATIVO NEGATIVO MUEVE EL MODO DEL LIBRO. Los tres "
    u"pasos empiezan hoy por Ten delante y llevan la evidencia del libro dentro (el texto cuenta "
    u"que) en vez de la prohibicion seca. EL AUDITOR ADJUDICO QUE ESTO NO ES PUENTE y que el "
    u"numerador de PASOS INVENTADOS no se mueve: no se anade ni un medio, ni una etapa ni un objeto. "
    u"Lo que se corrige es el MODO. La linea 233 sigue ordenando entre ellos (the most effective "
    u"solution) y por eso el paso 6 conserva su imperativo, y manual seccion 2 sigue satisfecha "
    u"porque Ten delante es imperativo. LA CUENTA DE PASOS NO SE MUEVE: 8 antes y 8 despues.")
if u'CORRECCION 8 DE LA COLA DE LA VUELTA 23' not in d['resumen_teorico']:
    d['resumen_teorico'] = d['resumen_teorico'] + AÑADIDO

with io.open(RUTA, 'w', encoding='utf-8', newline='\n') as f:
    f.write(json.dumps(d, ensure_ascii=False, indent=2, sort_keys=True))
    f.write(u'\n')

print('| paso | como empezaba | como empieza | la evidencia del libro, y su linea |')
print('|---:|---|---|---|')
for i, ev in ((2, u'`it never really works`, `L229`'),
              (3, u'`None was ever able to stick to it`, `L231`'),
              (4, u"`I don't think he ever hit the goal`, `L231`")):
    print(u'| %d | `%s` | `%s` | %s |'
          % (i + 1, viejos[i][:22], d['pasos_accionables'][i][:22], ev))
print(u'| | **8 pasos** | **%d pasos** | **la cuenta no se mueve** |' % len(d['pasos_accionables']))
