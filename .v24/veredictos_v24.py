# -*- coding: utf-8 -*-
"""LOS VEREDICTOS DE LOS PARES QUE LA ADUANA LEVANTO EN ESTA VUELTA.

Los PARES y sus SENIALES salen de los informes crudos de .aduana_v24, uno por
candidato, corridos en el acto de escribir cada uno. El VEREDICTO y su RAZON son
mios y estan escritos abajo: eso es lo unico que un instrumento no puede sacar,
porque las seniales ordenan y nunca deciden (manual principio 4).
"""
import glob
import io
import os
import re

CAND = re.compile(r'^\[(?:BLOQUEARIA|ENTRARIA|CAERIA)\] (\S+)', re.M)
BLOQUE = re.compile(
    r'^    vecino (\S+)\s+\[levantada por: ([^\]]+)\]\n'
    r'\s+similitud_texto ([\d.]+) \| familia_id ([\d.]+) \| paso_contra_nodo ([\d.]+)', re.M)

# (candidato, vecino) -> (veredicto, razon). LA RAZON ES OBLIGATORIA: un SANO sin
# razon es un nodo que entro por cansancio.
VEREDICTOS = {
 ('presionar_curva_notas_evitar_forzarla', 'evaluar_desempenio_dos_veces_anio'):
   ('SANO', 'hermanos de la misma serie, elementos 8 y 10, y es el espejo del par 11 de esta misma tabla, levantado por los dos lados. El veredicto es el mismo por la misma razon: uno decide que se hace con la curva del reparto y el otro cada cuanto se evalua'),
 ('presionar_curva_notas_evitar_forzarla', 'mantener_proceso_evaluacion_ligero_vigilar_crecimiento'):
   ('SANO', 'hermanos de la misma serie, elementos 8 y 13, espejo del par 22 de esta tabla. Los dos exigen explicacion al jefe que se sale del reparto esperado, y esa coincidencia la escribe el libro en dos sitios: en la presion sobre la curva y dentro de la herramienta ligera. Ninguno despliega al otro'),
 ('presionar_curva_notas_evitar_forzarla', 'escribir_escaleras_puesto_evitar_dos_extremos'):
   ('SANO', 'hermanos de la misma serie, elementos 8 y 3, y la familia_id los roza en 0,100 porque los dos ids llevan evitar. Uno evita forzar la curva y el otro evita los dos extremos de una escalera de puesto: el verbo es el mismo y el objeto no se parece en nada'),
 ('presionar_curva_notas_evitar_forzarla', 'manejar_enfado_persona_desafiada'):
   ('SANO', 'el paso 1 de este candidato define que es una curva forzada y el paso 2 del vecino habla de aceptar que la gente se enfade contigo. La senial 1 los junta en 0,367 por el vocabulario de jefe y equipo, que es el vocabulario de todo el libro. No hay ni objeto compartido ni despliegue: el vecino es de cap_04 y trata una conversacion de dos personas'),
 ('recorrer_trece_elementos_proceso_evaluacion_formal', 'aprender_resultados_vencer_dos_presiones'):
   ('SANO', 'el paso 11 de la cabeza dice decide la frecuencia de la evaluacion y el paso 4 del vecino dice aprende de la experiencia: los dos son imperativos cortos de una linea y por eso la senial 3 los empareja en el umbral justo, 0,600, pero uno decide un elemento del sistema de notas y el otro cierra la rueda de gestion de un equipo. Ni uno despliega al otro ni comparten objeto'),
 ('decidir_poner_nota_comunicar_proposito_limites', 'recorrer_trece_elementos_proceso_evaluacion_formal'):
   ('CONTINUA', 'el vecino es la CABEZA de la serie y este candidato es su primera parte: el paso 2 de la cabeza dice uno, decide si pones nota o no, y este nodo despliega esa decision en 8 pasos que la cabeza no tiene. La arista 58 declara este par con su paso citado'),
 ('escribir_escaleras_puesto_evitar_dos_extremos', 'decidir_poner_nota_comunicar_proposito_limites'):
   ('SANO', 'son dos elementos DISTINTOS de la misma serie numerada, el 3 y el 1, hermanos y no madre e hija. La senial 1 los junta porque los dos pesan pegas contra beneficios con el mismo vocabulario de nota y jefe, pero uno decide si hay nota y el otro escribe las descripciones de puesto por nivel. Ninguno de los dos nombra al otro en ningun paso'),
 ('elegir_palabras_nota_definirlas_empresa_entera', 'decidir_momento_despedir_persona'):
   ('SANO', 'el paso 7 de este candidato dice que en otras empresas la nota mas baja puede ser menos grave, y el paso 2 del vecino dice que no hay respuesta absoluta a cuando toca despedir: la senial 3 los empareja en 0,626 por la forma de la frase, no hay respuesta unica, pero uno define el lenguaje de una nota y el otro decide un despido. No hay procedimiento compartido'),
 ('elegir_palabras_nota_definirlas_empresa_entera', 'elegir_categorias_nota_palabras_propias_empresa'):
   ('SANO', 'hermanos de la misma serie, elementos 5 y 2, y la familia_id los junta en 0,500 porque los dos ids empiezan por elegir y hablan de nota y de palabras. Pero uno elige QUE se califica, las categorias, y el otro elige COMO SE LLAMA cada escalon de la nota. La propia serie los separa en dos elementos numerados distintos'),
 ('elegir_palabras_nota_definirlas_empresa_entera', 'escribir_escaleras_puesto_evitar_dos_extremos'):
   ('SANO', 'hermanos de la misma serie, elementos 5 y 3. Los dos avisan de que el lenguaje importa, que es lo que la senial 1 ve, pero uno escribe la escalera de puesto por nivel y el otro escribe la definicion de cada escalon de la nota. Son dos textos distintos con dos destinatarios distintos'),
 ('elegir_palabras_nota_definirlas_empresa_entera', 'recorrer_trece_elementos_proceso_evaluacion_formal'):
   ('CONTINUA', 'el vecino es la CABEZA y este candidato es su quinta parte: el paso 6 de la cabeza dice cinco, cuida el lenguaje, porque el texto dice que las palabras importan, y este nodo lo despliega en 10 pasos. La arista 62 declara este par con su paso citado'),
 ('repartir_notas_publicar_reparto_esperado', 'decidir_poner_nota_comunicar_proposito_limites'):
   ('SANO', 'hermanos de la misma serie, elementos 7 y 1. Los dos hablan de lo que la nota arrastra y por eso la senial 1 los junta, pero uno decide SI hay nota y el otro decide QUE PROPORCION de cada nota espera la empresa. El elemento 7 presupone que ya se decidio que si'),
 ('repartir_notas_publicar_reparto_esperado', 'elegir_palabras_nota_definirlas_empresa_entera'):
   ('SANO', 'hermanos de la misma serie, elementos 7 y 5. Uno reparte porcentajes y el otro elige palabras: comparten el objeto nota y nada mas'),
 ('evaluar_desempenio_dos_veces_anio', 'presionar_curva_notas_sin_forzarla'):
   ('SANO', 'hermanos de la misma serie, elementos 10 y 8. La senial 1 los junta en 0,388 porque los dos usan el verbo recomendar sobre la misma nota, pero uno fija CADA CUANTO se evalua y el otro fija QUE SE HACE con la curva del reparto. AVISO DE IDENTIDAD: este informe se corrio cuando el vecino todavia llevaba su id viejo, presionar_curva_notas_sin_forzarla, que la aduana tumbo despues por la regla 3; el nodo es el mismo y hoy se llama presionar_curva_notas_evitar_forzarla'),
 ('evaluar_desempenio_dos_veces_anio', 'repartir_notas_publicar_reparto_esperado'):
   ('SANO', 'hermanos de la misma serie, elementos 10 y 7. Uno fija cada cuanto se evalua y el otro que porcentaje cae en cada nota: la frecuencia no toca el reparto y el reparto no toca la frecuencia'),
 ('evaluar_desempenio_dos_veces_anio', 'elegir_palabras_nota_definirlas_empresa_entera'):
   ('SANO', 'hermanos de la misma serie, elementos 10 y 5. No comparten ni objeto ni acto: uno pone dos fechas en el calendario y el otro escribe las definiciones de los escalones'),
 ('evaluar_desempenio_dos_veces_anio', 'decidir_poner_nota_comunicar_proposito_limites'):
   ('SANO', 'hermanos de la misma serie, elementos 10 y 1. Los dos hablan de la nota frente al desarrollo, que es lo que la senial 1 ve, pero uno decide SI hay nota y el otro CADA CUANTO se pone'),
 ('montar_evaluacion_360_grados_ligera_pares', 'evaluar_desempenio_dos_veces_anio'):
   ('SANO', 'hermanos de la misma serie, elementos 11 y 10, y con una remision lateral real: el P6 del elemento 10 dice que la evaluacion escrita lleve un componente ligero de trescientos sesenta grados. Es una remision, no un despliegue: ninguno de los dos tiene los pasos del otro, y los dos cuelgan ya de la misma cabeza por las aristas 67 y 68. Una arista lateral sin madre ni hija es justo lo que EXTRACTOR.md 15.6 no autoriza'),
 ('hacer_critica_pares_transparente_ensenar_escribirla', 'montar_evaluacion_360_grados_ligera_pares'):
   ('SANO', 'hermanos de la misma serie, elementos 12 y 11, y el par mas proximo de los trece: el 12 solo tiene sentido si el 11 se decidio que si, y su P1 lo dice, si ya has decidido hacer critica de trescientos sesenta grados. Pero decidir SI la haces y decidir si lo que se escribe es VISIBLE son dos decisiones que el libro numera por separado, y ninguno de los dos despliega un paso del otro'),
 ('hacer_critica_pares_transparente_ensenar_escribirla', 'calibrar_notas_reunion_jefes_pares'):
   ('SANO', 'hermanos de la misma serie, elementos 12 y 9. Los dos hablan de lo que pasa cuando la gente sabe que otros van a ver su juicio, que es lo que la senial 1 ve, pero uno trata la critica escrita entre pares y el otro la reunion en la que los jefes cuadran sus notas'),
 ('hacer_critica_pares_transparente_ensenar_escribirla', 'decidir_poner_nota_comunicar_proposito_limites'):
   ('SANO', 'hermanos de la misma serie, elementos 12 y 1. Comparten la palabra transparencia y nada mas: uno decide si hay nota y el otro si la critica entre pares lleva nombre'),
 ('mantener_proceso_evaluacion_ligero_vigilar_crecimiento', 'elegir_palabras_nota_definirlas_empresa_entera'):
   ('SANO', 'hermanos de la misma serie, elementos 13 y 5, y el unico par de la tanda que levanta la senial 3 por encima de 0,60 dentro de cap_14: el paso 9 del uno comprueba que el impreso se rellena en menos de treinta minutos y el paso 10 del otro comprueba que la definicion es facil de entender y rapida de leer. Son dos varas de comprobacion con la misma forma y objetos distintos, que es exactamente lo que D.19 mide que la senial no puede separar'),
 ('mantener_proceso_evaluacion_ligero_vigilar_crecimiento', 'montar_evaluacion_360_grados_ligera_pares'):
   ('SANO', 'hermanos de la misma serie, elementos 13 y 11, con remision lateral escrita: el P6 del 13 dice monta la herramienta de evaluacion ligera igual que la herramienta de trescientos sesenta grados. LO MARCO COMO DISCUTIBLE porque la remision es la mas fuerte de las trece y podria defenderse una arista por lectura; no la declaro porque ninguno despliega al otro, los dos cuelgan de la misma cabeza (aristas 68 y 70) y una arista lateral sin madre ni hija no esta autorizada'),
 ('mantener_proceso_evaluacion_ligero_vigilar_crecimiento', 'calibrar_notas_reunion_jefes_pares'):
   ('SANO', 'hermanos de la misma serie, elementos 13 y 9. Los dos avisan de procesos que se comen el tiempo y piden una parada, que es lo que la senial 1 ve, pero uno vigila el proceso entero y el otro una reunion concreta'),
 ('mantener_proceso_evaluacion_ligero_vigilar_crecimiento', 'presionar_curva_notas_sin_forzarla'):
   ('SANO', 'hermanos de la misma serie, elementos 13 y 8. Los dos piden explicacion al jefe que se sale del reparto esperado, y esa coincidencia es del libro y no mia: el elemento 13 pone esa comprobacion dentro de la herramienta y el 8 dentro de la presion sobre la curva. Ninguno despliega al otro. AVISO DE IDENTIDAD: el informe se corrio con el id viejo del vecino, hoy presionar_curva_notas_evitar_forzarla'),
 ('mantener_proceso_evaluacion_ligero_vigilar_crecimiento', 'evaluar_desempenio_dos_veces_anio'):
   ('SANO', 'hermanos de la misma serie, elementos 13 y 10, con remision lateral: el P4 del 13 recomienda un proceso ligero que ocurra dos veces al anio, que es la cifra del elemento 10. La cifra viaja, el procedimiento no'),
 ('repartir_notas_publicar_reparto_esperado', 'fijar_cuatro_notas_calcular_nota_global'):
   ('SANO', 'hermanos de la misma serie, elementos 7 y 4, y son el par mas proximo de la tanda porque los dos manejan cifras sobre la misma nota. Pero uno decide CUANTOS escalones hay y como se combinan en la global, y el otro decide QUE PORCENTAJE de la plantilla cae en cada escalon. Un sistema puede tener cuatro notas y cualquier reparto: la cuenta de escalones no fija el reparto'),
}


def pares_de_los_informes():
    filas = []
    for ruta in sorted(glob.glob('.aduana_v24/*.txt')):
        texto = io.open(ruta, encoding='utf-8').read()
        cands = CAND.findall(texto)
        if not cands:
            continue
        candidato = cands[0]
        for vecino, senial, s1, s2, s3 in BLOQUE.findall(texto):
            filas.append((candidato, vecino, senial, s1, s2, s3))
    return filas


filas = pares_de_los_informes()
print('| # | candidato | vecino | levantada por | sim | fam | paso | veredicto | la razon, escrita |')
print('|---:|---|---|---|---:|---:|---:|---|---|')
for indice, (c, v, senial, s1, s2, s3) in enumerate(filas, 1):
    ver, razon = VEREDICTOS.get((c, v), ('SIN VEREDICTO', 'FALTA ESCRIBIRLA'))
    print('| %d | `%s` | `%s` | %s | %s | %s | %s | **%s** | %s |'
          % (indice, c, v, senial, s1, s2, s3, ver, razon))

print('')
print('| el recuento de veredictos | cuantos |')
print('|---|---:|')
print('| filas vecino leidas | **%d** |' % len(filas))
# EL ID VIEJO Y EL NUEVO SON EL MISMO NODO, y contarlos como dos pares distintos
# inflaria la cifra. Se normaliza antes de contar y se dice que se normaliza.
VIEJO_A_NUEVO = {'presionar_curva_notas_sin_forzarla': 'presionar_curva_notas_evitar_forzarla'}


def norma(x):
    return VIEJO_A_NUEVO.get(x, x)


print('| pares DISTINTOS sin orden, con el id corregido normalizado | **%d** |'
      % len(set(tuple(sorted((norma(c), norma(v)))) for c, v, _a, _b, _d, _e in filas)))
print('| de ellos levantados por los DOS lados | **%d** |'
      % (len(filas) - len(set(tuple(sorted((norma(c), norma(v)))) for c, v, _a, _b, _d, _e in filas))))
for nombre in ('CONTINUA', 'SANO', 'REPITE', 'SIN VEREDICTO'):
    n = len([1 for c, v, _a, _b, _d, _e in filas if VEREDICTOS.get((c, v), ('SIN VEREDICTO',))[0] == nombre])
    if n:
        print('| `%s` | **%d** |' % (nombre, n))
