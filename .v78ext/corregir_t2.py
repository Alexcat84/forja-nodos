# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 78 de .v76ext/corregir_t2.py, con la marca, la tabla de correcciones, la bandeja
(cuarentena/marquet_turn_the_ship/) y la ruta de la relectura cambiadas a la 78; nada mas cambiado. Las fichas de Marquet si se
serializan con sangria, pero la sustitucion en el texto crudo de la 76 vale igual y deja el diff de cada ficha en sus lineas
cambiadas. Se corre por ficha: python .v78ext/corregir_t2.py <id>. Lo que decia la de la 76: COPIA DE LA VUELTA 76 de .v73ext/corregir_t2.py, con la marca, la tabla de correcciones, la bandeja (cuarentena/gerber_emyth/) y
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

MARCA = 'CORRECCION DECLARADA DE LA VUELTA 78'
PIE = (' de la linea serial, en la relectura de fidelidad entera que D.30 y D.58 mandan antes de la insercion (TAREA 2.3 del '
       'encargo de la 78), sin insertar nada.')
C = {
 'seguir_frustrado_preguntar_implantacion_ideas': {
  'pasos': {
   2: ('Nombrale lo que viste, sin pregunta y sin acusacion. La frase del texto es que parecias un poco frustrado.',
       'Nombrale lo que viste. La frase del texto es que parecias un poco frustrado.'),
  },
  'nota': (MARCA + PIE + ' EL PASO 2 TRAIA UNA CLAUSULA PUENTE Y SE REESCRIBE SIN BORRAR EL RASTRO. El paso 2 decia: Nombrale lo '
           'que viste, sin pregunta y sin acusacion. La frase del texto es que parecias un poco frustrado. Hoy dice: Nombrale lo que '
           'viste. La frase del texto es que parecias un poco frustrado. LA CLAUSULA QUE SE RETIRA, sin pregunta y sin acusacion, no '
           'la pone el libro: L25 da solo la frase, Weps, you seemed a bit frustrated, y ninguna linea del capitulo dice como no hay '
           'que nombrarlo. DONDE ARRIBA DICE RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 8 pasos, 8 TRANSCRIPCION, 0 PUENTE, la cifra de '
           'la relectura de la vuelta 78 es 8 pasos, 7 TRANSCRIPCION y 1 PUENTE sobre el texto viejo, y 8 TRANSCRIPCION y 0 PUENTE '
           'despues de esta correccion (.v78ext/fidelidad.tsv). La cifra vieja no se borra, manual principio 6.'),
 },
 'informar_cierre_jornada_conservar_propiedad_trabajo': {
  'pasos': {
   2: ("Reporta primero el estado de un trabajo en curso con signo positivo, nombrando el propio trabajo. El texto pone el ejemplo: the charts for next week's underway are coming along fine.",
       "Reporta primero el estado de un trabajo en curso, nombrando el propio trabajo. El texto pone el ejemplo: the charts for next week's underway are coming along fine."),
   4: ("Si algo quedo sin hacer, dilo sin disculpa vacia y da el plan de cuando se hara. El texto cierra el ejemplo asi: I wasn't able to see Petty Officer Smith for his qualification interview but will be able to make that up tomorrow.",
       "Si algo quedo sin hacer, dilo y da el plan de cuando se hara. El texto cierra el ejemplo asi: I wasn't able to see Petty Officer Smith for his qualification interview but will be able to make that up tomorrow."),
  },
  'nota': (MARCA + PIE + ' LOS PASOS 2 Y 4 TRAIAN UNA CLAUSULA PUENTE CADA UNO Y SE REESCRIBEN SIN BORRAR EL RASTRO. El paso 2 '
           'decia: Reporta primero el estado de un trabajo en curso con signo positivo, nombrando el propio trabajo. Hoy dice lo mismo '
           'sin con signo positivo. LA CLAUSULA QUE SE RETIRA la pone el extractor y no el libro: el coming along fine de L35 es el '
           'ejemplo del guion, y L35 no pide que el estado que se reporta sea bueno. El paso 4 decia: Si algo quedo sin hacer, dilo '
           'sin disculpa vacia y da el plan de cuando se hara. Hoy dice: Si algo quedo sin hacer, dilo y da el plan de cuando se '
           'hara. LA CLAUSULA QUE SE RETIRA, sin disculpa vacia, tampoco la pone el libro: L35 da lo pendiente y su plan de '
           'reponerlo, y ninguna linea del capitulo habla de disculpas. DONDE ARRIBA DICE RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 5 '
           'pasos, 5 TRANSCRIPCION, 0 PUENTE, la cifra de la relectura de la vuelta 78 es 5 pasos, 3 TRANSCRIPCION y 2 PUENTE sobre '
           'el texto viejo, y 5 TRANSCRIPCION y 0 PUENTE despues de esta correccion (.v78ext/fidelidad.tsv). La cifra vieja no se '
           'borra, manual principio 6.'),
 },
}


def enc(s):
    return json.dumps(s, ensure_ascii=False)


i = sys.argv[1]
p = 'cuarentena/marquet_turn_the_ship/%s.json' % i
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
