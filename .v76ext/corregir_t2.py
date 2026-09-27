# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 76 de .v73ext/corregir_t2.py, con la marca, la tabla de correcciones, la bandeja (cuarentena/gerber_emyth/) y
la ruta de la relectura cambiadas a la 76, y UNA COSA MAS, dicha: las fichas de Gerber no se serializan con json.dumps(indent=1)
(llevan sus listas cortas en una linea), asi que la copia NO reescribe el fichero entero: sustituye en el texto crudo cada cadena
vieja, codificada como JSON, por la nueva, y comprueba despues que el fichero se lee y que lo leido es exactamente la ficha de antes
con los cambios de la tabla y nada mas. Asi el diff de cada ficha es el de sus lineas cambiadas. Lo que decia la de la 73:
la tabla admite 'campos' (condiciones_activacion, entregable_esperado) ademas de 'pasos'. Lo que decia la de la 71:
TAREA 2.2 de la vuelta 71: los PUENTE de .v71ext/fidelidad.tsv, corregidos en la ficha de la bandeja por correccion
declarada, con el texto viejo dentro, ANTES del barrido (d031). Es la forma de las correcciones de paso de la vuelta 64
(construir_grafico_escalonado_pronosticos): el paso se reescribe y el resumen_teorico gana al final un parrafo
CORRECCION DECLARADA con el texto viejo, el nuevo y la linea del libro que no lo dice. No borra nada mas.
Se corre por ficha: python .v76ext/corregir_t2.py <id>. Si la ficha ya lleva la marca de la vuelta 76, no toca."""
import copy, io, json, sys

MARCA = 'CORRECCION DECLARADA DE LA VUELTA 76'
PIE = (' de la linea serial, en la relectura de fidelidad entera que D.30 y D.58 mandan antes de la insercion (TAREA 2.3 del '
       'encargo de la 76), sin insertar nada.')
C = {
 'aplicar_ocho_reglas_juego_personas': {
  'pasos': {
   8: ('Regla 7: haz que el juego sea divertido de vez en cuando, no todo el tiempo; planea la diversion dejando que tu gente la defina, y no la repitas mas de una vez cada seis meses para que siga siendo algo que esperar.',
       'Regla 7: haz que el juego sea divertido de vez en cuando, no todo el tiempo; planea la diversion dejando que tu gente la defina, y no demasiado a menudo, quiza una vez cada seis meses, para que sea algo que esperar.'),
   9: ('Regla 8: si no se te ocurre un buen juego, robalo, pero aprendetelo de memoria antes de jugarlo con tu gente.',
       'Regla 8: si no se te ocurre un buen juego, robalo, pero una vez robado aprendetelo de memoria, porque no hay nada peor que fingir que juegas un juego.'),
  },
  'nota': (MARCA + PIE + ' LOS PASOS 8 Y 9 TRAIAN UNA CLAUSULA PUENTE CADA UNO Y SE REESCRIBEN SIN BORRAR EL RASTRO. El paso 8 '
           'decia: Regla 7: haz que el juego sea divertido de vez en cuando, no todo el tiempo; planea la diversion dejando que tu '
           'gente la defina, y no la repitas mas de una vez cada seis meses para que siga siendo algo que esperar. Hoy dice lo mismo '
           'hasta la defina, y despues: y no demasiado a menudo, quiza una vez cada seis meses, para que sea algo que esperar. LO QUE '
           'SE CORRIGE es el tope: L163 dice But not too often, maybe once every six months. Something to look forward to, y el '
           'paso viejo volvia tope firme lo que el libro da con un maybe. El paso 9 decia: Regla 8: si no se te ocurre un buen juego, '
           'robalo, pero aprendetelo de memoria antes de jugarlo con tu gente. Hoy dice: Regla 8: si no se te ocurre un buen juego, '
           'robalo, pero una vez robado aprendetelo de memoria, porque no hay nada peor que fingir que juegas un juego. LA CLAUSULA '
           'QUE SE RETIRA, antes de jugarlo con tu gente, no la pone el libro: L165 dice But once you steal somebody else’s game, '
           'learn it by heart. There’s nothing worse than pretending to play a game, que da la razon y no el momento. DONDE '
           'ARRIBA DICE RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 9 pasos, 9 TRANSCRIPCION, 0 PUENTE, y DONDE DICE que el periodo de la '
           'regla 7 es el que el propio libro fija, la cifra de la relectura de la vuelta 76 es 9 pasos, 7 TRANSCRIPCION y 2 PUENTE '
           'sobre el texto viejo, y 9 TRANSCRIPCION y 0 PUENTE despues de esta correccion (.v76ext/fidelidad.tsv). La cifra vieja no '
           'se borra, manual principio 6.'),
 },
 'dictar_ritmo_crecimiento_preguntas_escritas': {
  'pasos': {
   8: ('No te pares por no tener un plan bueno, que el texto lo zanja en una linea: cualquier plan es mejor que ningun plan.',
       'Recuerda que cualquier plan es mejor que ningun plan.'),
  },
  'campos': {
   'entregable_esperado': ('El plan escrito con claridad suficiente para que otros lo entiendan, con las preguntas del libro contestadas para cada marca y con sus planes de contingencia de mejor y de peor caso puestos.',
                           'El plan escrito con claridad suficiente para que otros lo entiendan, con las preguntas del libro contestadas y con sus planes de contingencia de mejor y de peor caso puestos.'),
  },
  'nota': (MARCA + PIE + ' EL PASO 8 TRAIA UNA CLAUSULA PUENTE, Y EL ENTREGABLE OTRA; SE REESCRIBEN SIN BORRAR EL RASTRO. El paso '
           '8 decia: No te pares por no tener un plan bueno, que el texto lo zanja en una linea: cualquier plan es mejor que ningun '
           'plan. Hoy dice: Recuerda que cualquier plan es mejor que ningun plan. LA CLAUSULA QUE SE RETIRA, No te pares por no tener '
           'un plan bueno, no la pone el libro: L287 dice Remember, Sarah, any plan is better than no plan. El entregable decia con '
           'las preguntas del libro contestadas para cada marca, y hoy dice con las preguntas del libro contestadas: L281 pone las '
           'tres marcas (at Benchmark One, at Benchmark Two, at Benchmark Three) solo en la pregunta del espacio, que el paso 4 ya '
           'transcribe asi. DONDE ARRIBA DICE RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 8 pasos, 8 TRANSCRIPCION, 0 PUENTE, la cifra de '
           'la relectura de la vuelta 76 es 8 pasos, 7 TRANSCRIPCION y 1 PUENTE sobre el texto viejo, y 8 TRANSCRIPCION y 0 PUENTE '
           'despues de esta correccion (.v76ext/fidelidad.tsv). La cifra vieja no se borra, manual principio 6.'),
 },
 'operar_modelo_gente_destreza_minima': {
  'pasos': {
   4: ('No contrates a los brillantes: crea el mejor sistema posible para que buenos abogados y buenos medicos queden apalancados y produzcan resultados exquisitos.',
       'No necesitas contratar abogados brillantes ni medicos brillantes: necesitas crear el mejor sistema posible para que buenos abogados y buenos medicos queden apalancados y produzcan resultados exquisitos.'),
  },
  'nota': (MARCA + PIE + ' EL PASO 4 TRAIA UNA CLAUSULA PUENTE Y SE REESCRIBE SIN BORRAR EL RASTRO. El paso 4 decia: No contrates '
           'a los brillantes: crea el mejor sistema posible para que buenos abogados y buenos medicos queden apalancados y produzcan '
           'resultados exquisitos. Hoy dice: No necesitas contratar abogados brillantes ni medicos brillantes: necesitas crear el '
           'mejor sistema posible para que buenos abogados y buenos medicos queden apalancados y produzcan resultados exquisitos. LO '
           'QUE SE CORRIGE es la prohibicion: L89 dice But you don’t need to hire brilliant attorneys or brilliant physicians. '
           'You need to create the very best system through which good attorneys and good physicians can be leveraged to produce '
           'exquisite results; el libro dice que no hace falta, y el paso viejo lo volvia prohibicion. DONDE ARRIBA DICE RELECTURA DE '
           'FIDELIDAD D.30 EN EL ACTO: 10 pasos, 10 TRANSCRIPCION, 0 PUENTE, la cifra de la relectura de la vuelta 76 es 10 pasos, 9 '
           'TRANSCRIPCION y 1 PUENTE sobre el texto viejo, y 10 TRANSCRIPCION y 0 PUENTE despues de esta correccion '
           '(.v76ext/fidelidad.tsv). La cifra vieja no se borra, manual principio 6.'),
 },
 'cambiar_saludo_cliente_dos_ramas': {
  'pasos': {
   1: ('En vez de preguntar Hi, may I help you?, pregunta exactamente Hi, have you been in here before?',
       'En vez de preguntar Hi, may I help you?, prueba a preguntar Hi, have you been in here before?'),
   2: ("Si el cliente responde que si, dile exactamente: Great. We've created a special new program for people who have shopped here before. Let me take just a minute to tell you about it.",
       "Si el cliente responde que si, puedes decirle: Great. We've created a special new program for people who have shopped here before. Let me take just a minute to tell you about it."),
   3: ("Si el cliente responde que no, dile exactamente: Great, we've created a special new program for people who haven't shopped here before. Let me take just a minute to tell you about it.",
       "Si el cliente responde que no, puedes decirle: Great, we've created a special new program for people who haven't shopped here before. Let me take just a minute to tell you about it."),
  },
  'campos': {
   'entregable_esperado': ('El guion exacto del saludo nuevo, con sus dos ramas de respuesta ya escritas segun el cliente diga que si o que no, y el programa especial que las dos ramas necesitan tener listo de antemano.',
                           'El guion del saludo nuevo, con sus dos ramas de respuesta ya escritas segun el cliente diga que si o que no, y el programa especial que las dos ramas necesitan tener listo de antemano.'),
  },
  'nota': (MARCA + PIE + ' LOS PASOS 1, 2 Y 3 TRAIAN UNA CLAUSULA PUENTE CADA UNO, Y EL ENTREGABLE LA MISMA; SE REESCRIBEN SIN '
           'BORRAR EL RASTRO. El paso 1 decia: En vez de preguntar Hi, may I help you?, pregunta exactamente Hi, have you been in '
           'here before? Hoy dice prueba a preguntar donde decia pregunta exactamente: L51 dice Instead of asking, Hi, may I help '
           'you? try Hi, have you been in here before?, y L49 lo presenta como una Innovacion que se prueba (Here’s a perfect '
           'opportunity to try a simple and inexpensive Innovation). Los pasos 2 y 3 decian dile exactamente, y hoy dicen puedes '
           'decirle: L53 y L55 dicen If the answer is yes, you can say y If the answer is no, you can say, que es una posibilidad y '
           'no una orden. El entregable decia El guion exacto del saludo nuevo, y hoy dice El guion del saludo nuevo, por la misma '
           'razon. DONDE ARRIBA DICE RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 4 pasos, 4 TRANSCRIPCION, 0 PUENTE, la cifra de la '
           'relectura de la vuelta 76 es 4 pasos, 1 TRANSCRIPCION y 3 PUENTE sobre el texto viejo, y 4 TRANSCRIPCION y 0 PUENTE '
           'despues de esta correccion (.v76ext/fidelidad.tsv). La cifra vieja no se borra, manual principio 6.'),
 },
 'cuantificar_impacto_innovacion_6_pasos': {
  'pasos': {
   6: ('Determina cual fue la mejora que produjo tu innovacion, comparando los numeros de antes con los de despues.',
       'Determina cual fue la mejora que produjo tu innovacion.'),
  },
  'campos': {
   'condiciones_activacion': ('Cuando pruebas una innovacion en tu negocio, por ejemplo cambiar las palabras con que saludas a un cliente que entra, y quieres saber si de verdad funciono en vez de suponerlo.',
                              'Cuando pruebas una innovacion en tu negocio, por ejemplo cambiar las palabras con que saludas a un cliente que entra, y quieres saber si de verdad funciono.'),
   'entregable_esperado': ('El valor preciso, en numeros, de tu innovacion: la mejora que produjo, comparando los conteos de antes del cambio con los conteos de despues.',
                           'El valor preciso, en numeros, de tu innovacion: la mejora que produjo.'),
  },
  'nota': (MARCA + PIE + ' EL PASO 6 TRAIA UNA CLAUSULA PUENTE, Y LA CONDICION Y EL ENTREGABLE OTRA CADA UNO; SE RETIRAN SIN '
           'BORRAR EL RASTRO. El paso 6 decia: Determina cual fue la mejora que produjo tu innovacion, comparando los numeros de '
           'antes con los de despues. Hoy dice lo mismo sin la clausula comparando. LA CLAUSULA QUE SE RETIRA compara, y el libro no '
           'la pone: L95 dice (6) determining what the improvement was as a result of your Innovation, y These numbers enable you '
           'to determine the precise value of your Innovation, sin decir como. El entregable decia la mejora que produjo, comparando '
           'los conteos de antes del cambio con los conteos de despues, y hoy dice la mejora que produjo; la condicion decia si de '
           'verdad funciono en vez de suponerlo, y hoy dice si de verdad funciono: L87 dice Without Quantification, how would you '
           'know whether the Innovation worked?, sin el contraste. DONDE ARRIBA DICE RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 6 pasos, '
           '6 TRANSCRIPCION, 0 PUENTE, la cifra de la relectura de la vuelta 76 es 6 pasos, 5 TRANSCRIPCION y 1 PUENTE sobre el '
           'texto viejo, y 6 TRANSCRIPCION y 0 PUENTE despues de esta correccion (.v76ext/fidelidad.tsv). La cifra vieja no se '
           'borra, manual principio 6.'),
 },
 'interrogar_negocio_cinco_preguntas': {
  'pasos': {},
  'campos': {
   'entregable_esperado': ('Las cinco preguntas del libro hechas sobre tu propio negocio, y la constatacion escrita de cuales de ellas no sabes contestar.',
                           'Las cinco preguntas del libro hechas sobre tu propio negocio, y la constatacion de que no sabes las respuestas.'),
  },
  'nota': (MARCA + PIE + ' EL ENTREGABLE TRAIA UNA CLAUSULA PUENTE Y SE REESCRIBE SIN BORRAR EL RASTRO; NINGUN PASO CAMBIA. El '
           'entregable decia: Las cinco preguntas del libro hechas sobre tu propio negocio, y la constatacion escrita de cuales de '
           'ellas no sabes contestar. Hoy dice: Las cinco preguntas del libro hechas sobre tu propio negocio, y la constatacion de '
           'que no sabes las respuestas. LO QUE SE CORRIGE es el escrita y el cuales: L265 dice If you ask yourself these '
           'questions, you’ll eventually come face-to-face with the real problem: that you don’t know the answers!, y no '
           'pide escribir nada ni separar las preguntas. La cifra de fidelidad de arriba, 10 pasos, 10 TRANSCRIPCION, 0 PUENTE, es '
           'tambien la de la relectura de la vuelta 76 (.v76ext/fidelidad.tsv): la correccion es del entregable, que no se cuenta '
           'en pasos.'),
 },
}


def enc(s):
    return json.dumps(s, ensure_ascii=False)


i = sys.argv[1]
p = 'cuarentena/gerber_emyth/%s.json' % i
raw = io.open(p, encoding='utf-8', newline='').read()
d = json.loads(raw)
if MARCA in d['resumen_teorico']:
    print('%s: ya corregida' % i); sys.exit(0)
c = C[i]
esperado = copy.deepcopy(d)
for n, (viejo, nuevo) in sorted(c['pasos'].items()):
    assert d['pasos_accionables'][n - 1] == viejo, (i, n, d['pasos_accionables'][n - 1])
    assert raw.count(enc(viejo)) == 1, (i, n, 'la cadena vieja no esta una sola vez en el texto crudo')
    raw = raw.replace(enc(viejo), enc(nuevo))
    esperado['pasos_accionables'][n - 1] = nuevo
for k, (viejo, nuevo) in sorted(c.get('campos', {}).items()):
    assert d[k] == viejo, (i, k, d[k])
    assert raw.count(enc(viejo)) == 1, (i, k, 'la cadena vieja no esta una sola vez en el texto crudo')
    raw = raw.replace(enc(viejo), enc(nuevo))
    esperado[k] = nuevo
viejo_r = d['resumen_teorico']
nuevo_r = viejo_r.rstrip() + ' ' + c['nota']
assert raw.count(enc(viejo_r)) == 1, (i, 'resumen_teorico no esta una sola vez en el texto crudo')
raw = raw.replace(enc(viejo_r), enc(nuevo_r))
esperado['resumen_teorico'] = nuevo_r
assert json.loads(raw) == esperado, (i, 'lo escrito no es la ficha de antes con los cambios de la tabla')
io.open(p, 'w', encoding='utf-8', newline='').write(raw)
print('%s: pasos %s reescritos%s, nota anexada al resumen_teorico' % (i, ', '.join(str(n) for n in sorted(c['pasos'])) or 'ninguno',
      ''.join(', ' + k for k in sorted(c.get('campos', {})))))
