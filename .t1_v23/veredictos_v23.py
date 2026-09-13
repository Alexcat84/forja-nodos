# -*- coding: utf-8 -*-
"""LOS PARES QUE MI ADUANA LEVANTO, CON SU VEREDICTO Y SU RAZON.

Las tres cifras de senial y el paso que las levanto se LEEN de los informes, no
se teclean. El veredicto y la razon son mios y viven en este fichero, que es lo
unico que un guion no puede sacar de otro sitio: las seniales ordenan, nunca
deciden (manual principio 4).

SI UN PAR LEVANTADO NO TIENE VEREDICTO AQUI, ESTE GUION SALE EN ROJO. Es a
proposito: un BLOQUEARIA sin razon escrita es un nodo que entraria por cansancio.
"""
import glob
import io
import os
import re
import sys

CARPETA = '.aduana_v23'
CAB = re.compile(r'^\[(ENTRARIA|BLOQUEARIA|CAERIA)\] (\S+)', re.M)
VEC = re.compile(r'^    vecino (\S+)\s+\[levantada por: (\S+)\]\n'
                 r'\s+similitud_texto ([\d.]+) \| familia_id ([\d.]+) \| paso_contra_nodo ([\d.]+)\n'
                 r'\s+paso (\d+) del candidato contra paso (\d+) de', re.M)

# EL VEREDICTO Y SU RAZON. Clave: (candidato, vecino).
V = {
    ('desplegar_tres_conversaciones_carrera', 'conversar_historia_vida_descubrir_motivadores'): (
        'CONTINUA con arista',
        'par YA adjudicado y ya declarado: es la D.37 numero 1 de la vuelta 22, madre y parte de la '
        'serie de las tres conversaciones de carrera, con --paso 11 citado. La senial lo vuelve a '
        'levantar porque la correccion 3 reescribio la madre, y el veredicto no cambia'),
    ('preguntar_seguimiento_hallar_huecos', 'calibrar_normalidad_preguntas_jefe'): (
        'SANO',
        'cruza de libro (Zhuo contra Scott) y la senial los junta por un molde: el paso 5 pregunta a '
        'quien te reporta que le desvela por la noche y el paso 6 del vecino le pregunta a TU JEFE '
        'que le quita el sueno. Misma frase hecha, direccion contraria. Aquel entrega tus '
        'expectativas calibradas en tus primeros meses; este entrega los huecos de quien te reporta '
        'identificados dentro de una reunion a solas'),
    ('desplegar_plan_orden_operaciones_franqueza_radical', 'armar_plan_anual_crecimiento_equipo'): (
        'CONTINUA con arista',
        'cabeza y parte: el paso 32 de la cabeza nombra el plan de gestion del crecimiento en una '
        'linea y no lo despliega; el vecino lo despliega en 29 pasos, desde poner los nombres en las '
        'casillas hasta comprobar la equidad entre niveles. Arista 41'),
    ('desplegar_plan_orden_operaciones_franqueza_radical', 'bloquear_tiempo_pensar_calendario'): (
        'CONTINUA con arista',
        'cabeza y parte: el paso 30 de la cabeza es una linea entera (pon algo de tiempo para pensar '
        'en tu calendario) y el vecino la despliega en 6 pasos con su aviso al equipo y su defensa '
        'del hueco. Arista 40'),
    ('desplegar_plan_orden_operaciones_franqueza_radical', 'desplegar_tres_conversaciones_carrera'): (
        'CONTINUA con arista',
        'cabeza y parte: el paso 12 de la cabeza nombra las conversaciones de carrera y dice por '
        'donde empezar; el vecino es la cabeza de esa serie y trae sus 12 pasos. Arista 39'),
    ('desplegar_plan_orden_operaciones_franqueza_radical', 'desplegar_marco_franqueza_radical'): (
        'SANO, y con una tension del LIBRO declarada',
        'son hermanos y ninguno despliega al otro: aquel entrega copias del marco puestas a la vista '
        'y el marco en uso como brujula; este entrega el plan recorrido. La senial los junta por '
        'familia de id (0,429), que es el apellido franqueza_radical compartido. Y DECLARO LA '
        'TENSION QUE ENCONTRE AL LEERLOS, porque es del libro y no mia: mi paso 8 transcribe de L21 '
        'de cap_12 que copies el marco y lleves ahi la cuenta de quien te dice que, y el paso 8 del '
        'vecino transcribe de su capitulo que NO escribas nombres en las casillas. No son el mismo '
        'acto (uno apunta quien te critica a ti, el otro etiqueta a otros en un cuadrante) pero se '
        'tocan, y quien los lea juntos merece verlo escrito'),
    ('contar_historias_propias_explicar_franqueza_radical',
     'contar_cuatro_historias_propias_ver_hueco_intencion'): (
        'CONTINUA con arista',
        'lo declara el propio libro: L43 de cap_13 dice que hay un parrafo breve sobre esto en la '
        'seccion final de Getting Started y que les han pedido mas detalle. La madre trae los seis '
        'medios de explicar la idea; la hija trae CUATRO historias con su pregunta de arranque, y '
        'ninguna de las cuatro esta en la madre. Arista 42, y va marcado como discutible 3'),
    ('contar_cuatro_historias_propias_ver_hueco_intencion',
     'contar_historias_propias_explicar_franqueza_radical'): (
        'CONTINUA con arista',
        'es el MISMO par que la fila de arriba, levantado ahora desde el otro extremo, y lo digo en '
        'vez de contarlo dos veces como si fueran dos: la aduana lo levanta en los dos informes '
        'porque la poblacion es grafo mas bandejas (D.38.5) y los dos extremos viven en cuarentena. '
        'Mismo veredicto, misma razon, UNA sola arista: la 42'),
    ('mejorar_consciencia_propia_relacional_dos_practicas',
     'desplegar_plan_orden_operaciones_franqueza_radical'): (
        'SANO',
        'son dos CABEZAS que nombran una misma tercera cosa y ninguna despliega a la otra: mi paso '
        '11 nombra la practica de contar historias y el paso 4 del vecino nombra la etapa comparte '
        'tus historias. Es el caso literal de EXTRACTOR.md 15.6: una cabeza y un vecino que no es '
        'ninguna de sus partes son hermanos, y su veredicto es SANO. La hija comun si lleva arista '
        'de las dos, y son la 42 y la 43'),
    ('contar_cuatro_historias_propias_ver_hueco_intencion', 'evitar_presion_social_actos_equipo'): (
        'SANO',
        'ruido de la banda media aplicado a paso contra nodo: mi paso 16 dice que la consciencia es '
        'el primer paso hacia el cambio y el paso 6 del vecino dice que a veces el mayor regalo es '
        'dejar al equipo irse a casa. Comparten vocabulario de equipo y ni un objeto: aquel entrega '
        'un acto al que va quien quiere ir, este entrega cuatro historias desenterradas'),
    ('practicar_triangulo_critica_tres_papeles', 'abrazar_incomodidad_silencio_contar_seis'): (
        'SANO',
        'la senial que los junta es similitud de texto 0,375, dentro de la banda que EXTRACTOR.md 11 '
        'llama de lectura prioritaria, y por eso los lei enteros. Comparten el molde de un ejercicio '
        'de taller (haz esto con un companiero) y ni un objeto: aquel entrega un silencio aguantado '
        'hasta seis despues de una pregunta, este entrega una conversacion ensayada en grupo de tres '
        'con su recorrido dibujado en el marco. Son hermanos de capitulo'),
    ('practicar_triangulo_critica_tres_papeles', 'escuchar_entender_critica_dominar_defensa'): (
        'SANO',
        'misma especie que el par anterior: similitud 0,352 por el molde del ejercicio de taller. '
        'Aquel entrega tu defensa dominada mientras te critican, con el ejercicio de escuchar tres '
        'minutos sin interrumpir; este entrega el impacto de tus palabras devuelto por un observador. '
        'Uno practica RECIBIR y el otro practica DAR, y ninguno despliega al otro'),
    ('abrazar_incomodidad_silencio_contar_seis', 'escuchar_entender_critica_dominar_defensa'): (
        'SANO, Y ES EL PAR QUE MAS CARO COSTARIA FALLAR DE TODA LA VUELTA',
        'similitud de texto 0,449, o sea POR ENCIMA DE 0,40, y EXTRACTOR.md 11 es tajante con esa '
        'banda: en el catalogo de calibracion hay 325 gemelos y CERO ajenos por encima de 0,40, y si '
        'una senial 1 pasa de 0,40 ese par se lee antes que ningun otro. Lo lei entero, los 12 pasos '
        'contra los 13, y lo sostengo SANO con el argumento del propio libro delante: la linea 237 '
        'de cap_13 ENUMERA los cuatro elementos de pedir critica y nombra estos dos POR SEPARADO '
        '(embracing the discomfort, listening with the intent to understand). Son dos de cuatro, no '
        'uno partido en dos. Y los actos son distintos en el tiempo: aquel aguanta el silencio ANTES '
        'de que llegue la respuesta y entrega la respuesta salida de el; este domina tu defensa '
        'MIENTRAS la respuesta llega y entrega la critica escuchada entera. Cada uno trae ademas su '
        'propio ejercicio con su propia cuenta (contar hasta seis; hablar tres minutos sin '
        'interrumpir) y ninguno de los dos ejercicios sirve para lo del otro. LO QUE LA SENIAL VE, y '
        'lo digo porque es la explicacion honesta del 0,449: los dos textos son cortos, de la misma '
        'seccion, con el mismo vocabulario (critica, incomodidad, practica, companiero) y el mismo '
        'molde de taller. VA MARCADO COMO DISCUTIBLE 12'),
    ('abrazar_incomodidad_silencio_contar_seis', 'practicar_triangulo_critica_tres_papeles'): (
        'SANO',
        'es el espejo de un par ya adjudicado mas arriba desde el otro extremo (similitud 0,373 alli '
        'y 0,373 aqui), y el veredicto y la razon no cambian: molde de ejercicio de taller '
        'compartido, objetos distintos'),
    ('abrazar_incomodidad_silencio_contar_seis', 'premiar_franqueza_hacer_escucha_tangible'): (
        'SANO',
        'similitud 0,360, tercero de los cuatro elementos contra el cuarto, y el libro los enumera '
        'por separado en la linea 237 igual que a los dos anteriores. Aquel entrega el problema '
        'criticado arreglado y contado en publico; este entrega un silencio aguantado. Mi paso 7 '
        '(hazle tu pregunta y cuenta hasta seis) contra su paso 8 (haz una lista de las tres o '
        'cuatro criticas recientes) no comparten ni objeto ni momento'),
    ('abrazar_incomodidad_silencio_contar_seis', 'contar_historias_propias_explicar_franqueza_radical'): (
        'SANO',
        'similitud 0,376 y cruza de capitulo (cap_13 contra cap_12). Mi paso 1 dice que al pedir '
        'critica metes al otro en una situacion incomoda; su paso 3 dice que expliques la idea con '
        'tus propias palabras. Comparten el vocabulario de la franqueza radical y ni un acto: aquel '
        'entrega tus historias contadas, este un silencio aguantado'),
    ('escuchar_entender_critica_dominar_defensa', 'abrazar_incomodidad_silencio_contar_seis'): (
        'SANO',
        'es el espejo del par de 0,449 leido desde el otro extremo (aqui 0,446, y la diferencia son '
        'los dos decimales de una medida no simetrica). Mismo veredicto, misma razon, y va al mismo '
        'discutible 12'),
    ('escuchar_entender_critica_dominar_defensa', 'contar_historias_propias_explicar_franqueza_radical'): (
        'SANO',
        'similitud 0,393, justo por debajo de la banda de gemelo, y cruza de capitulo. Mi paso 4 dice '
        'que practiques con otros y su paso 3 dice que expliques la idea con tus propias palabras. '
        'Aquel entrega tus historias contadas al equipo; este tu defensa dominada mientras te '
        'critican. Ni un objeto compartido'),
    ('escuchar_entender_critica_dominar_defensa', 'premiar_franqueza_hacer_escucha_tangible'): (
        'SANO',
        'similitud 0,370, tercer elemento contra cuarto, y el libro los enumera por separado en la '
        'linea 237. Aquel entrega el problema criticado arreglado y contado en publico; este la '
        'critica escuchada entera sin defensa. La palabra escuchar esta en los dos titulos y ese es '
        'todo el parecido: uno escucha para no defenderse, el otro ENSENIA que escucho'),
    ('escuchar_entender_critica_dominar_defensa', 'practicar_triangulo_critica_tres_papeles'): (
        'SANO',
        'es el espejo de un par ya adjudicado mas arriba desde el otro extremo (0,352 alli y 0,350 '
        'aqui). Mismo veredicto y misma razon: molde de ejercicio de taller compartido, objetos '
        'distintos'),
    ('premiar_franqueza_hacer_escucha_tangible', 'abrazar_incomodidad_silencio_contar_seis'): (
        'SANO',
        'espejo de un par ya adjudicado desde el otro extremo (0,360 alli, 0,353 aqui). Cuarto '
        'elemento contra segundo, enumerados por separado en la linea 237. Mismo veredicto'),
    ('premiar_franqueza_hacer_escucha_tangible', 'escuchar_entender_critica_dominar_defensa'): (
        'SANO',
        'espejo de un par ya adjudicado desde el otro extremo (0,370 alli, 0,382 aqui). Cuarto '
        'elemento contra tercero, enumerados por separado en la linea 237. Mismo veredicto'),
    ('resolver_dudas_frecuentes_pedir_critica', 'despedir_persona_franqueza_radical'): (
        'SANO',
        'ruido puro: mi paso 5 dice que si ninguno de los dos tiene solucion a mano te retes a ti '
        'mismo preguntando si de verdad es algo que no puedes arreglar, y el paso 8 del vecino esta '
        'dentro de una conversacion de despido. Comparten el molde de resolver un problema y ni un '
        'objeto: aquel entrega una conversacion de despido tenida sin distanciarte, este entrega una '
        'duda de pedir critica resuelta'),
    ('resolver_dudas_frecuentes_pedir_critica', 'resolver_dudas_frecuentes_reuniones_salto_nivel'): (
        'SANO, y lo levanta la familia de id porque comparten el APELLIDO resolver_dudas_frecuentes',
        'familia de id 0,375, y la senial hace justo lo que se espera de ella: los dos ids empiezan '
        'igual porque los dos nodos son bloques de preguntas frecuentes. Y ahi acaba el parecido: '
        'aquel contesta las cuatro dudas de una reunion de salto de nivel (el equipo que ya no cree '
        'en su jefe, los que no hablan, los que no callan y el equilibrio) y este contesta las cuatro '
        'de pedir critica (la pregunta rancia, la critica que no puedes arreglar, el jefe joven con '
        'gente mayor y el miedo a empezar). Ni una duda se repite. ES ADEMAS EL PRECEDENTE QUE USE '
        'PARA CORTAR ESTE NODO, y por eso lo leo entero en vez de firmarlo: si aquel es nodo, este '
        'tambien'),
    ('pedir_critica_primero_crear_seguridad_psicologica', 'integrar_peticion_critica_rutina_existente'): (
        'SANO, y es el par que mas cerca esta de caer',
        'paso contra nodo 0,733, la senial mas alta de la vuelta, y la razon es exacta: mi paso 17 y '
        'su paso 6 transcriben LA MISMA ENUMERACION de los cuatro elementos, uno de L113 y otro de '
        'L237, porque el libro la escribe dos veces. Los entregables si son distintos: aquel entrega '
        'el orden de operaciones recorrido desde su primer paso, este entrega la peticion metida al '
        'final de tus reuniones a solas y anunciada al equipo. Va marcado como discutible 5, y si el '
        'auditor lee que dos pasos identicos en dos nodos son un duplicado, la salida es quitar la '
        'enumeracion de uno de los dos'),
}


def informes():
    for ruta in sorted(glob.glob(os.path.join(CARPETA, '*.txt'))):
        yield io.open(ruta, encoding='utf-8').read()


filas = []
for texto in informes():
    cab = CAB.search(texto)
    if not cab:
        continue
    cand = cab.group(2)
    for vecino, senial, s1, s2, s3, pa, pb in VEC.findall(texto):
        filas.append((cand, vecino, senial, s1, s2, s3, pa, pb))

print('=' * 78)
print('1. LOS PARES LEVANTADOS, CON SU VEREDICTO Y SU RAZON')
print('=' * 78)
print('| # | candidato | vecino | senial que lo levanto | `sim` | `fam` | `paso` | veredicto |')
print('|---:|---|---|---|---:|---:|---:|---|')
sin_veredicto = []
for i, (cand, vecino, senial, s1, s2, s3, _pa, _pb) in enumerate(filas, 1):
    v = V.get((cand, vecino))
    if not v:
        sin_veredicto.append((cand, vecino))
        print('| %d | `%s` | `%s` | `%s` | %s | %s | %s | # **SIN VEREDICTO** |'
              % (i, cand, vecino, senial, s1, s2, s3))
        continue
    print('| %d | `%s` | `%s` | `%s` | %s | %s | %s | **%s** |'
          % (i, cand, vecino, senial, s1, s2, s3, v[0]))
print('| | | **%d pares** | | | | | |' % len(filas))

print('')
print('=' * 78)
print('2. LAS RAZONES, UNA POR PAR, PORQUE UN SANO SIN RAZON LO RECHAZA LA ADUANA')
print('=' * 78)
for i, (cand, vecino, _s, _a, _b, _c, pa, pb) in enumerate(filas, 1):
    v = V.get((cand, vecino))
    if not v:
        continue
    print('')
    print('%d. %s  CONTRA  %s' % (i, cand, vecino))
    print('   paso %s del candidato contra paso %s del vecino' % (pa, pb))
    print('   VEREDICTO: %s' % v[0])
    print('   RAZON: %s' % v[1])

print('')
print('=' * 78)
print('3. LA COMPROBACION: NINGUN PAR SIN RAZON ESCRITA')
print('=' * 78)
distintos = set(frozenset(f[:2]) for f in filas)
print('filas levantadas     : %d' % len(filas))
print('PARES DISTINTOS      : %d  (una fila y su espejo son UN par)' % len(distintos))
print('pares con veredicto  : %d' % (len(filas) - len(sin_veredicto)))
print('pares SIN veredicto  : %d   %s' % (len(sin_veredicto), sin_veredicto))
if sin_veredicto:
    sys.exit(1)
