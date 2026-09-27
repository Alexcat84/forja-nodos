# -*- coding: utf-8 -*-
"""Vuelta 64, TAREA 2.a: las correcciones de fidelidad (D.30) de los seis de d005, en la
bandeja y ANTES de ninguna insercion. Cada cambio comprueba que el texto viejo esta, lo
cambia y anexa al resumen_teorico su CORRECCION DECLARADA con el texto viejo dentro, como
hizo la vuelta 63. Idempotente: si la correccion ya esta anexada, no hace nada."""
import io, json
B = 'cuarentena/grove_high_output/%s.json'
CAB = ('CORRECCION DECLARADA de la vuelta 64 de la linea serial, la de saneamiento, en la relectura '
       'de fidelidad entera que el encargo de la 64 y D.30 mandan sobre los seis de d005, ANTES de su '
       'insercion y sin insertar nada. ')
C = {
 'construir_grafico_escalonado_pronosticos': [
  ('paso', 5,
   'Hazlo con la tasa de pedidos entrantes: pon el pronostico de esa tasa, y debajo el mismo pronostico preparado el mes siguiente, y el del mes de despues, y asi sucesivamente.',
   'Hazlo con la tasa de pedidos entrantes: pon el pronostico de esa tasa, y con el el mismo pronostico preparado el mes siguiente, y el del mes de despues, y asi sucesivamente.'),
  ('titulo', 0,
   'Construir el grafico escalonado que pone cada pronostico nuevo encima de los anteriores',
   'Construir el grafico escalonado que pone cada pronostico nuevo junto a los anteriores'),
  ('entregable_esperado', 0,
   'El grafico con una fila por mes de pronostico, los meses pronosticados en columnas, el numero real marcado con asterisco, y leida la variacion de un pronostico al siguiente.',
   'El grafico con cada pronostico mensual junto a los anteriores, el numero real marcado con asterisco, y leida la variacion de un pronostico al siguiente.'),
  'EL PASO 5 TRAIA UNA CLAUSULA PUENTE DE DISPOSICION, Y EL TITULO Y EL ENTREGABLE LA MISMA ESPECIE; SE REESCRIBEN SIN BORRAR EL RASTRO. El paso 5 decia y debajo el mismo pronostico preparado el mes siguiente y hoy dice y con el el mismo pronostico preparado el mes siguiente. El titulo decia que pone cada pronostico nuevo encima de los anteriores y hoy dice junto a los anteriores. El entregable decia El grafico con una fila por mes de pronostico, los meses pronosticados en columnas, y hoy dice El grafico con cada pronostico mensual junto a los anteriores. L91 y L93 dicen as compared to several prior forecasts y The stagger chart then provides the same forecast prepared in the following month, in the month after that, and so on, y la disposicion vive en una figura que este recorte no trae: ni debajo, ni encima, ni filas ni columnas estan en el texto, y la propia ficha decia debajo en un sitio y encima en otro. CIFRA DE FIDELIDAD DE ESTA RELECTURA: 8 pasos, 7 TRANSCRIPCION y 1 PUENTE de clausula reescrito, el paso 5, que CUENTA como puente (ACTA 62 62.5). La cifra vieja de arriba no se borra.'],
 'construir_indicador_tendencia_patron': [
  ('entregable_esperado', 0,
   'La serie de la salida contra el tiempo con el patron dibujado encima, la extrapolacion hecha, y escrito el porque de la diferencia entre el resultado y el patron.',
   'La salida medida contra el tiempo y contra el patron, la extrapolacion hecha, y pensado el porque de la diferencia entre el resultado y el patron.'),
  'EL ENTREGABLE TRAIA UN PUENTE DE SOPORTE Y UNO DE DISPOSICION, Y SE REESCRIBE SIN BORRAR EL RASTRO: decia La serie de la salida contra el tiempo con el patron dibujado encima y escrito el porque de la diferencia, y hoy dice La salida medida contra el tiempo y contra el patron y pensado el porque de la diferencia. L89 dice makes you think through why the results were what they were, que es pensar, y esta misma ficha declara arriba que no escribe que la explicacion se anote; y L89 dice measured against some standard or expected level, sin dibujo. Los 6 pasos, releidos uno a uno contra L89: 6 TRANSCRIPCION, 0 PUENTE.'],
 'elegir_fabricar_pedido_pronostico': [
  ('paso', 8,
   'Mezcla las dos vias donde te convenga, como hace la fabrica de desayunos: fabrica tu producto contra el pedido del cliente y compra a tus proveedores contra la demanda pronosticada.',
   'Cuenta con que las dos vias pueden convivir en la misma operacion, como en la fabrica de desayunos: fabrica su producto contra el pedido del cliente, pero compra a sus proveedores, como al huevero, contra la demanda pronosticada.'),
  ('entregable_esperado', 0,
   'Escrito cual de las dos vias usas para cada cosa que produces o compras, y, si es contra pronostico, el riesgo de inventario reconocido y el plazo dentro del cual esperas que se materialicen los pedidos.',
   'Decidido cual de las dos vias usas para cada cosa que produces o compras, y, si es contra pronostico, el riesgo de inventario reconocido y el plazo dentro del cual esperas que se materialicen los pedidos.'),
  'EL PASO 8 TRAIA UN CRITERIO PUENTE Y EL ENTREGABLE UN PUENTE DE SOPORTE; SE REESCRIBEN SIN BORRAR EL RASTRO. El paso 8 decia Mezcla las dos vias donde te convenga, como hace la fabrica de desayunos: fabrica tu producto contra el pedido del cliente y compra a tus proveedores contra la demanda pronosticada, y hoy dice Cuenta con que las dos vias pueden convivir en la misma operacion, como en la fabrica de desayunos. L109 dice Our breakfast factory makes its product to customer order, but buys from its suppliers, like the egg man, on the basis of forecasted demand, y lo dice para ensenar que fabricar contra pronostico es comun (So building to forecast is a very common business practice); no manda mezclar, y el donde te convenga es un criterio de adecuacion que el libro no pone. El entregable decia Escrito cual de las dos vias usas y hoy dice Decidido: ningun renglon de L103 a L109 manda escribirlo, y esta misma ficha declara arriba que no escribe que el pronostico se escriba en ningun sitio. CIFRA DE FIDELIDAD DE ESTA RELECTURA: 9 pasos, 8 TRANSCRIPCION y 1 PUENTE reescrito, el paso 8, que CUENTA como puente (ACTA 62 62.5). La cifra vieja de arriba no se borra.'],
 'elegir_indicador_salida_trabajo_administrativo': [
  ('entregable_esperado', 0,
   'Un indicador de salida por unidad administrativa, fisico y contable, con su pareja de calidad escrita al lado y el responsable de la calificacion nombrado cuando esa calificacion sea en parte subjetiva.',
   'Un indicador de salida por unidad administrativa, fisico y contable, con su pareja de calidad al lado.'),
  'EL ENTREGABLE TRAIA UN PUENTE DE SOPORTE Y UNO DE RESPONSABLE, Y SE REESCRIBE SIN BORRAR EL RASTRO: decia con su pareja de calidad escrita al lado y el responsable de la calificacion nombrado cuando esa calificacion sea en parte subjetiva, y hoy dice con su pareja de calidad al lado. L37 no manda escribir la pareja, y el mando con despacho en el edificio es el evaluador del ejemplo de la limpieza, que el paso 7 transcribe; convertirlo en un responsable que se nombra para toda calificacion en parte subjetiva es la especie responsable de D.30, la misma que esta ficha declara arriba que no escribe. Los 7 pasos, releidos uno a uno contra L35 a L67: 7 TRANSCRIPCION, 0 PUENTE.'],
 'emparejar_indicadores_efecto_contraefecto': [
  ('entregable_esperado', 0,
   'Cada indicador con su pareja escrita al lado, el efecto y el contraefecto nombrados, y los dos vigilados a la vez en el mismo sitio.',
   'Cada indicador con su pareja, el efecto y el contraefecto nombrados, y los dos vigilados a la vez.'),
  'EL ENTREGABLE TRAIA DOS PUENTES DE SOPORTE Y SE REESCRIBE SIN BORRAR EL RASTRO: decia Cada indicador con su pareja escrita al lado y los dos vigilados a la vez en el mismo sitio, y hoy dice Cada indicador con su pareja y los dos vigilados a la vez. L31 dice you need to monitor both inventory levels and the incidence of shortages, sin soporte ni sitio, y esta misma ficha declara arriba que no escribe que el par se publique ni donde. Los 7 pasos, releidos uno a uno contra L31 a L33: 7 TRANSCRIPCION, 0 PUENTE.'],
}
for i, cambios in C.items():
    p = B % i
    d = json.loads(io.open(p, encoding='utf-8').read())
    if 'CORRECCION DECLARADA de la vuelta 64' in d['resumen_teorico']:
        print('YA CORREGIDA  %s' % i)
        continue
    nota = cambios[-1]
    for campo, n, viejo, nuevo in cambios[:-1]:
        if campo == 'paso':
            assert d['pasos_accionables'][n - 1] == viejo, (i, n)
            d['pasos_accionables'][n - 1] = nuevo
        else:
            assert d[campo] == viejo, (i, campo)
            d[campo] = nuevo
        print('CAMBIA  %-48s %s %s' % (i, campo, n or ''))
    d['resumen_teorico'] = d['resumen_teorico'] + ' ' + CAB + nota
    io.open(p, 'w', encoding='utf-8', newline='').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
