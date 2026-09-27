# -*- coding: utf-8 -*-
"""d032: las dos frases del resumen_teorico de la ficha de P38, corregidas SIN BORRAR."""
import json, pathlib, collections
p = pathlib.Path('cuarentena/grove_high_output/dimensionar_numero_subordinados_medio_dia_semanal.json')
raw = p.read_bytes().decode('utf-8')
d = json.loads(raw, object_pairs_hook=collections.OrderedDict)
viejo = d['resumen_teorico']
assert 'Es el tramo mas rico de esta tanda' in viejo
assert 'ese cinco sale del dibujo que el libro pone debajo' in viejo
correccion = (
 " CORRECCION DECLARADA EN LA VUELTA 49, SIN BORRAR NADA DE LO DE ARRIBA"
 " (deuda d032, anotada por el auditor en la ACTA 47 secciones 47.6.a y 47.6.b y encargada en la"
 " TAREA 2.b de la vuelta 49; manual principio 6: el texto viejo queda en pie, tachado por la"
 " correccion). SON DOS FRASES Y VAN UNA A UNA."
 " (1) DONDE ARRIBA DICE 'Es el tramo mas rico de esta tanda': NO LO ES. P38 tiene 396 palabras y"
 " P34 tiene 469, y P34 es de ESTA MISMA TANDA y es madre de dos de los cinco candidatos de la"
 " vuelta 48 (decir_no_trabajo_excede_capacidad y usar_calendario_herramienta_planificacion_produccion,"
 " comprobado hoy con grep -l 'PIEZA P34' sobre la bandeja). La lista ordenada de"
 " .v47aud/44_tramos.py, corrida por mi en esta vuelta 49, da P34 469 palabras y P38 396, o sea P34"
 " por delante. LA OTRA MITAD DE LA MISMA FRASE, 'el quinto del capitulo entero', SI ES CIERTA y la"
 " vuelvo a comprobar hoy contra la misma salida: P38 es el puesto 5 de 44 (P5 674, P2 530, P34 469,"
 " P3 411, P38 396). ASI QUE LA FRASE CORREGIDA ES: P38 es el QUINTO tramo del capitulo entero y el"
 " SEGUNDO de esta tanda, por detras de P34."
 " (2) DONDE ARRIBA DICE 'pero ese cinco sale del dibujo que el libro pone debajo (the arrangement,"
 " shown below) y el dibujo NO esta en el fichero de texto': ESO EL LIBRO LO DESMIENTE EN LA MISMA"
 " LINEA. sed -n '299p' fuentes/grove_high_output/cap_04.md escribe en su propia prosa 'So the plant"
 " manager will actually have six direct reports: five engineers and the manufacturing manager', y la"
 " frase SIGUIENTE, 'The arrangement, shown below', se refiere al ESQUEMA y no a los numeros."
 " LA DECISION DE NO ESCRIBIR EL CINCO SE SOSTIENE Y NO LA CAMBIO: la ACTA 47 47.6.b la firma y el"
 " encargo de la vuelta 49 me manda expresamente no tocarla. LO QUE SE CORRIGE ES EL MOTIVO, y el"
 " motivo bueno es otro y mas estrecho: el cinco y el seis son del CASO de la planta con dos secciones"
 " que este mismo tramo monta, no de la regla del nodo, y el manual seccion 3.5 dice que el caso no es"
 " la casa y que la senial barata de que se hizo mal es que el entregable del caso lleve un dato del"
 " caso. POR ESO NO CAMBIA NI UN PASO NI UNA ATRIBUCION: el paso 10 sigue escribiendo la RELACION y no"
 " el total, y las atribuciones siguen llevando las cifras de la REGLA (six to eight, three or four too"
 " few, ten too many, half a day a week, two days a week, an hour a week) y ninguna del caso."
)
d['resumen_teorico'] = viejo + correccion
final = json.dumps(d, ensure_ascii=False, indent=2) + ('\n' if raw.endswith('\n') else '')
p.write_bytes(final.encode('utf-8'))
print('d032 corregida, resumen_teorico pasa de %d a %d caracteres' % (len(viejo), len(d['resumen_teorico'])))
