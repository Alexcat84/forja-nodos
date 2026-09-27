# -*- coding: utf-8 -*-
"""TAREA 2.2 de la vuelta 71: los PUENTE de .v71ext/fidelidad.tsv, corregidos en la ficha de la bandeja por correccion
declarada, con el texto viejo dentro, ANTES del barrido (d031). Es la forma de las correcciones de paso de la vuelta 64
(construir_grafico_escalonado_pronosticos): el paso se reescribe y el resumen_teorico gana al final un parrafo
CORRECCION DECLARADA con el texto viejo, el nuevo y la linea del libro que no lo dice. No borra nada mas.
Se corre por ficha: python .v71ext/corregir_t2.py <id>. Si la ficha ya lleva la marca de la vuelta 71, no toca."""
import io, json, sys

MARCA = 'CORRECCION DECLARADA DE LA VUELTA 71'
C = {
 'planificar_tres_pasos_demanda_estado_brecha': {
  'pasos': {
   1: ('Monta tu proceso general de planificacion sobre un razonamiento analogo al de la fabrica, y no sobre otra cosa.',
       'Monta tu proceso general de planificacion sobre un razonamiento analogo al de la fabrica.'),
   4: ('Formula ese paso 2 tambien de la otra manera, que es la que obliga a contestarlo: donde va a estar tu negocio si no haces nada distinto de lo que estas haciendo.',
       'Formula ese paso 2 tambien de la otra manera: donde va a estar tu negocio si no haces nada distinto de lo que estas haciendo.'),
  },
  'nota': (MARCA + ' de la linea serial, en la relectura de fidelidad entera que D.30 y D.58 mandan antes de la insercion '
           '(TAREA 2.2 del encargo de la 71), sin insertar nada. LOS PASOS 1 Y 4 TRAIAN UNA CLAUSULA PUENTE CADA UNO Y SE '
           'REESCRIBEN SIN BORRAR EL RASTRO. El paso 1 decia: Monta tu proceso general de planificacion sobre un razonamiento '
           'analogo al de la fabrica, y no sobre otra cosa. Hoy dice: Monta tu proceso general de planificacion sobre un '
           'razonamiento analogo al de la fabrica. LA CLAUSULA QUE SE RETIRA, y no sobre otra cosa, no la pone el libro: L19 dice '
           'solamente Your general planning process should consist of analogous thinking. El paso 4 decia: Formula ese paso 2 '
           'tambien de la otra manera, que es la que obliga a contestarlo: donde va a estar tu negocio si no haces nada distinto '
           'de lo que estas haciendo. Hoy dice: Formula ese paso 2 tambien de la otra manera: donde va a estar tu negocio si no '
           'haces nada distinto de lo que estas haciendo. LA CLAUSULA QUE SE RETIRA, que es la que obliga a contestarlo, tampoco '
           'la pone el libro: L19 dice solamente Put another way, where will your business be if you do nothing different from '
           'what you are now doing? DONDE ARRIBA DICE RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 6 pasos, 6 TRANSCRIPCION, 0 PUENTE, '
           'la cifra de la relectura de la vuelta 71 es 6 pasos, 4 TRANSCRIPCION y 2 PUENTE sobre el texto viejo, y 6 '
           'TRANSCRIPCION y 0 PUENTE despues de esta correccion (.v71ext/fidelidad.tsv). La cifra vieja no se borra, manual '
           'principio 6.'),
 },
 'repartir_supervision_puesto_funcional_mision': {
  'pasos': {
   8: ('Encarga al jefe funcional que cuide su carrera dentro de la funcion, promocionandolo si lo hace bien.',
       'Encarga al jefe funcional que cuide su carrera dentro de la funcion, quiza promocionandolo si lo hace bien.'),
  },
  'nota': (MARCA + ' de la linea serial, en la relectura de fidelidad entera que D.30 y D.58 mandan antes de la insercion '
           '(TAREA 2.2 del encargo de la 71), sin insertar nada. EL PASO 8 TRAIA UNA CLAUSULA PUENTE Y SE REESCRIBE SIN BORRAR '
           'EL RASTRO. El paso 8 decia: Encarga al jefe funcional que cuide su carrera dentro de la funcion, promocionandolo si '
           'lo hace bien. Hoy dice: Encarga al jefe funcional que cuide su carrera dentro de la funcion, quiza promocionandolo si '
           'lo hace bien. LO QUE SE CORRIGE es que el paso viejo se comia el perhaps del libro y mandaba lo que el libro solo da '
           'como posibilidad: L43 dice and looks after his career inside finance, promoting him, perhaps, to the position of '
           'controller of a bigger, more complex division if he performs well. El destino del ascenso sigue fuera, porque es dato '
           'del caso (manual 3.5). DONDE ARRIBA DICE RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 8 pasos, 8 TRANSCRIPCION, 0 PUENTE, '
           'la cifra de la relectura de la vuelta 71 es 8 pasos, 7 TRANSCRIPCION y 1 PUENTE sobre el texto viejo, y 8 '
           'TRANSCRIPCION y 0 PUENTE despues de esta correccion (.v71ext/fidelidad.tsv). La cifra vieja no se borra, manual '
           'principio 6.'),
 },
 'entregar_evaluacion_desempeno_tres_claves': {
  'pasos': {
   2: ('Recuerda que el objetivo de la comunicacion es hacer llegar el pensamiento completo de tu cabeza a la del subordinado, y que las palabras son solo el medio para transmitirlo.',
       'Recuerda que el objetivo de la comunicacion es hacer llegar tus pensamientos de tu cabeza a la del subordinado, y que las palabras son solo el medio: el fin es que se comunique el pensamiento correcto.'),
  },
  'nota': (MARCA + ' de la linea serial, en la relectura de fidelidad entera que D.30 y D.58 mandan antes de la insercion '
           '(TAREA 2.2 del encargo de la 71), sin insertar nada. EL PASO 2 TRAIA UNA CLAUSULA PUENTE Y SE REESCRIBE SIN BORRAR '
           'EL RASTRO. El paso 2 decia: Recuerda que el objetivo de la comunicacion es hacer llegar el pensamiento completo de tu '
           'cabeza a la del subordinado, y que las palabras son solo el medio para transmitirlo. Hoy dice: Recuerda que el '
           'objetivo de la comunicacion es hacer llegar tus pensamientos de tu cabeza a la del subordinado, y que las palabras son '
           'solo el medio: el fin es que se comunique el pensamiento correcto. LO QUE SE CORRIGE es el completo, que no lo pone el '
           'libro: L111 dice The aim of communication is to transmit thoughts from the brain of person A to the brain of person B, '
           'y mas abajo Words themselves are nothing but a means; getting the right thought communicated is the end. El fin del '
           'libro es el pensamiento correcto, no el completo. DONDE ARRIBA DICE RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 6 pasos, 6 '
           'TRANSCRIPCION, 0 PUENTE, la cifra de la relectura de la vuelta 71 es 6 pasos, 5 TRANSCRIPCION y 1 PUENTE sobre el '
           'texto viejo, y 6 TRANSCRIPCION y 0 PUENTE despues de esta correccion (.v71ext/fidelidad.tsv). La cifra vieja no se '
           'borra, manual principio 6.'),
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
d['resumen_teorico'] = d['resumen_teorico'].rstrip() + ' ' + c['nota']
io.open(p, 'w', encoding='utf-8', newline='').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
print('%s: pasos %s reescritos, nota anexada al resumen_teorico' % (i, ', '.join(str(n) for n in sorted(c['pasos']))))
