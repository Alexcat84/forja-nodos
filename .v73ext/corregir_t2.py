# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 73 de .v71ext/corregir_t2.py, con la marca, la tabla de correcciones y la ruta de la relectura cambiadas a
la 73, y UNA COSA MAS, dicha: la tabla admite 'campos' (condiciones_activacion, entregable_esperado) ademas de 'pasos', para las
dos clausulas puente que la relectura encontro fuera de los pasos (D73.7). Lo que decia la de la 71:
TAREA 2.2 de la vuelta 71: los PUENTE de .v71ext/fidelidad.tsv, corregidos en la ficha de la bandeja por correccion
declarada, con el texto viejo dentro, ANTES del barrido (d031). Es la forma de las correcciones de paso de la vuelta 64
(construir_grafico_escalonado_pronosticos): el paso se reescribe y el resumen_teorico gana al final un parrafo
CORRECCION DECLARADA con el texto viejo, el nuevo y la linea del libro que no lo dice. No borra nada mas.
Se corre por ficha: python .v73ext/corregir_t2.py <id>. Si la ficha ya lleva la marca de la vuelta 73, no toca."""
import io, json, sys

MARCA = 'CORRECCION DECLARADA DE LA VUELTA 73'
PIE = (' de la linea serial, en la relectura de fidelidad entera que D.30 y D.58 mandan antes de la insercion (TAREA 2.2 del '
       'encargo de la 73), sin insertar nada.')
C = {
 'usar_banco_nueve_preguntas_entrevista': {
  'pasos': {
   3: ('Preguntale que te convenceria de que tu empresa deberia contratarlo.',
       'Pidele que te convenza de por que tu empresa deberia contratarlo.'),
   8: ('Si el puesto lo justifica, preguntale por que cree que deberia elegirse a un ingeniero para un puesto de marketing, o la variante equivalente segun la situacion.',
       'Preguntale por que cree que deberia elegirse a un ingeniero para un puesto de marketing, variando esta pregunta segun la situacion.'),
  },
  'campos': {
   'condiciones_activacion': ('Cuando el mando va a entrevistar a un candidato a un puesto y necesita preguntas concretas para llenar la hora u hora y media de que dispone.',
                              'Cuando el mando va a entrevistar a un candidato a un puesto y necesita preguntas concretas para la hora o dos de entrevista de que dispone.'),
  },
  'nota': (MARCA + PIE + ' LOS PASOS 3 Y 8 TRAIAN UNA CLAUSULA PUENTE CADA UNO, Y LA CONDICION UNA CIFRA QUE EL LIBRO NO DA; SE '
           'REESCRIBEN SIN BORRAR EL RASTRO. El paso 3 decia: Preguntale que te convenceria de que tu empresa deberia contratarlo. '
           'Hoy dice: Pidele que te convenza de por que tu empresa deberia contratarlo. LO QUE SE CORRIGE es la pregunta: L43 dice '
           'Convince me why my company should hire you, que le pide al candidato que convenza, y el paso viejo le preguntaba que '
           'convenceria al mando, que es otra pregunta. El paso 8 decia: Si el puesto lo justifica, preguntale por que cree que '
           'deberia elegirse a un ingeniero para un puesto de marketing, o la variante equivalente segun la situacion. Hoy dice: '
           'Preguntale por que cree que deberia elegirse a un ingeniero para un puesto de marketing, variando esta pregunta segun '
           'la situacion. LA CLAUSULA QUE SE RETIRA, Si el puesto lo justifica, no la pone el libro: L53 dice (Vary this one '
           'according to the situation.), que manda variar la pregunta y no condicionarla. La condicion de activacion decia la '
           'hora u hora y media de que dispone, y hoy dice la hora o dos de entrevista de que dispone: L27 dice an hour or two of '
           'interview time. DONDE ARRIBA DICE RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 9 pasos, 9 TRANSCRIPCION, 0 PUENTE, la cifra '
           'de la relectura de la vuelta 73 es 9 pasos, 7 TRANSCRIPCION y 2 PUENTE sobre el texto viejo, y 9 TRANSCRIPCION y 0 '
           'PUENTE despues de esta correccion (.v73ext/fidelidad.tsv). La cifra vieja no se borra, manual principio 6.'),
 },
 'responder_primer_aviso_renuncia_subordinado': {
  'pasos': {
   6: ('Pide el tiempo que necesites para prepararte antes del siguiente encuentro, en vez de intentar resolverlo todo en el momento.',
       'No intentes cambiarle la idea en este momento, sino compra tiempo: cuando haya dicho todo lo que tiene que decir, pide el tiempo que necesites para prepararte para el siguiente encuentro.'),
  },
  'nota': (MARCA + PIE + ' EL PASO 6 TRAIA UNA CLAUSULA PUENTE Y SE REESCRIBE SIN BORRAR EL RASTRO. El paso 6 decia: Pide el '
           'tiempo que necesites para prepararte antes del siguiente encuentro, en vez de intentar resolverlo todo en el momento. '
           'Hoy dice: No intentes cambiarle la idea en este momento, sino compra tiempo: cuando haya dicho todo lo que tiene que '
           'decir, pide el tiempo que necesites para prepararte para el siguiente encuentro. LO QUE SE CORRIGE es la clausula en '
           'vez de intentar resolverlo todo en el momento, que reescribe la del libro: L111 dice Don\'t try to change his mind at '
           'this point, but buy time. After he\'s said all he has to say, ask for whatever time you feel is necessary to prepare '
           'yourself for the next round. Lo que el libro prohibe es cambiarle la idea, no resolverlo todo. DONDE ARRIBA DICE '
           'RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 7 pasos, 7 TRANSCRIPCION, 0 PUENTE, la cifra de la relectura de la vuelta 73 '
           'es 7 pasos, 6 TRANSCRIPCION y 1 PUENTE sobre el texto viejo, y 7 TRANSCRIPCION y 0 PUENTE despues de esta correccion '
           '(.v73ext/fidelidad.tsv). La cifra vieja no se borra, manual principio 6.'),
 },
 'gestionar_retencion_subordinado_valioso_renuncia': {
  'pasos': {
   1: ('Lleva el problema a tu propio jefe y hazlo participar de la solucion, en vez de cargar con todo tu solo.',
       'Lleva el problema a tu propio jefe en busca de ayuda y consejo y, aunque el tambien intente posponerlo, haz que sea problema suyo y que participe de la solucion.'),
   5: ('Ayudalo a sentirse comodo con el nuevo arreglo, dejando claro que no se trata de una concesion arrancada por chantaje, sino de corregir algo que ya se deberia haber hecho.',
       'Haz que se sienta comodo con el nuevo arreglo; puedes decirle algo como que no les arranco por chantaje nada que no debieran haber hecho igual, que al estar a punto de irse les hizo ver su error, y que solo hacen lo que debieron hacer sin que pasara nada de esto.'),
  },
  'nota': (MARCA + PIE + ' LOS PASOS 1 Y 5 TRAIAN UNA CLAUSULA PUENTE CADA UNO Y SE REESCRIBEN SIN BORRAR EL RASTRO. El paso 1 '
           'decia: Lleva el problema a tu propio jefe y hazlo participar de la solucion, en vez de cargar con todo tu solo. Hoy '
           'dice: Lleva el problema a tu propio jefe en busca de ayuda y consejo y, aunque el tambien intente posponerlo, haz que '
           'sea problema suyo y que participe de la solucion. LA CLAUSULA QUE SE RETIRA, en vez de cargar con todo tu solo, no la '
           'pone el libro: L113 dice you go to your supervisor for help and advice, que el jefe He, like you, will try to put '
           'things off, y It is up to you to make it your supervisor\'s problem and make him participate in the solution to your '
           'problem. El paso 5 decia: Ayudalo a sentirse comodo con el nuevo arreglo, dejando claro que no se trata de una '
           'concesion arrancada por chantaje, sino de corregir algo que ya se deberia haber hecho. Hoy dice: Haz que se sienta '
           'comodo con el nuevo arreglo; puedes decirle algo como que no les arranco por chantaje nada que no debieran haber hecho '
           'igual, que al estar a punto de irse les hizo ver su error, y que solo hacen lo que debieron hacer sin que pasara nada '
           'de esto. LO QUE SE CORRIGE es que el paso viejo mandaba lo que el libro solo ofrece como ejemplo de lo que se puede '
           'decir: L119 dice You now have to make him feel comfortable with the new arrangement. You might say something like, '
           'You did not blackmail us into doing anything we shouldn\'t have done anyway. When you almost quit, you shook us up and '
           'made us aware of the error of our ways. We are just doing what we should have done without any of this happening. El '
           'mandato del libro es hacerlo sentir comodo; lo demas es un might. DONDE ARRIBA DICE RELECTURA DE FIDELIDAD D.30 EN EL '
           'ACTO: 6 pasos, 6 TRANSCRIPCION, 0 PUENTE, la cifra de la relectura de la vuelta 73 es 6 pasos, 4 TRANSCRIPCION y 2 '
           'PUENTE sobre el texto viejo, y 6 TRANSCRIPCION y 0 PUENTE despues de esta correccion (.v73ext/fidelidad.tsv). La cifra '
           'vieja no se borra, manual principio 6.'),
 },
 'pedir_critica_anonima_curso_entrenamiento_dictado': {
  'pasos': {
   3: ('Estudia y considera las respuestas, entendiendo que nunca podras complacer a todos los miembros de tu clase por igual.',
       'Estudia y considera las respuestas, entendiendo que nunca podras complacer a todos los miembros de tu clase.'),
  },
  'campos': {
   'entregable_esperado': ('Un conjunto de criticas anonimas recogidas y estudiadas, con el propio mando satisfecho de estar logrando lo que se propuso, sin esperar complacer a todos los alumnos por igual.',
                           'Un conjunto de criticas anonimas recogidas y estudiadas, con el propio mando satisfecho de estar logrando lo que se propuso, sin esperar complacer a todos los alumnos.'),
  },
  'nota': (MARCA + PIE + ' EL PASO 3 TRAIA UNA CLAUSULA PUENTE, Y EL ENTREGABLE LA MISMA; SE RETIRAN SIN BORRAR EL RASTRO. El '
           'paso 3 decia: Estudia y considera las respuestas, entendiendo que nunca podras complacer a todos los miembros de tu '
           'clase por igual. Hoy dice lo mismo sin por igual. El entregable decia sin esperar complacer a todos los alumnos por '
           'igual, y hoy lo dice sin por igual. LA CLAUSULA QUE SE RETIRA, por igual, no la pone el libro: L61 dice Study and '
           'consider the responses, but understand that you will never be able to please all members of your class. DONDE ARRIBA '
           'DICE RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 4 pasos, 4 TRANSCRIPCION, 0 PUENTE, la cifra de la relectura de la vuelta '
           '73 es 4 pasos, 3 TRANSCRIPCION y 1 PUENTE sobre el texto viejo, y 4 TRANSCRIPCION y 0 PUENTE despues de esta '
           'correccion (.v73ext/fidelidad.tsv). La cifra vieja no se borra, manual principio 6.'),
 },
}

i = sys.argv[1]
p = 'cuarentena/grove_high_output/%s.json' % i
raw = io.open(p, encoding='utf-8', newline='').read()
d = json.loads(raw)
assert json.dumps(d, ensure_ascii=False, indent=1) + '\n' == raw, 'la ficha no se serializa como se leyo'
if MARCA in d['resumen_teorico']:
    print('%s: ya corregida' % i); sys.exit(0)
c = C[i]
for n, (viejo, nuevo) in sorted(c['pasos'].items()):
    assert d['pasos_accionables'][n - 1] == viejo, (i, n, d['pasos_accionables'][n - 1])
    d['pasos_accionables'][n - 1] = nuevo
for k, (viejo, nuevo) in sorted(c.get('campos', {}).items()):
    assert d[k] == viejo, (i, k, d[k])
    d[k] = nuevo
d['resumen_teorico'] = d['resumen_teorico'].rstrip() + ' ' + c['nota']
io.open(p, 'w', encoding='utf-8', newline='').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
print('%s: pasos %s reescritos%s, nota anexada al resumen_teorico' % (i, ', '.join(str(n) for n in sorted(c['pasos'])),
      ''.join(', ' + k for k in sorted(c.get('campos', {})))))
