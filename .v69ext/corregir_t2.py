# -*- coding: utf-8 -*-
"""TAREA 2 de la vuelta 69: la relectura conjunta de la ACTA 67 67.4.d (D68.7 y D68.15), escrita por correccion declarada.
Es la forma de .v67ext/corregir_t2.py, con los pares cambiados: cada linea que cambia en .v68ext/veredictos_listos.txt o
.v68ext/aristas_lectura.txt queda ENCIMA de la nueva como comentario '# vuelta 69, <motivo>: <linea vieja>'. No borra nada.
Las copias de antes estan en .v69ext/veredictos_listos_antes.txt y .v69ext/aristas_lectura_antes.txt.
Se corre una vez; si ya corrio, no toca."""
import io, sys
C = 'usar_tres_clases_reunion_proceso'
FR, DU, GU, CU = ('fijar_frecuencia_reunion_individual_madurez_tarea', 'fijar_duracion_lugar_reunion_individual',
                  'preparar_guion_reunion_individual_subordinado', 'cubrir_indicadores_problemas_reunion_individual')
IN = 'infundir_regularidad_reunion_proceso'
# lo que parte de cada hijo, con su linea del libro
HIJO = {
 FR: ('decidir cada cuanto te reunes a solas con cada profesional que te reporta', 'L33 a L35, How often should you have one-on-ones', 'diez'),
 DU: ('poner en el calendario cuanto dura la reunion individual y en que sitio se tiene', 'L37 y L39, How long should a one-on-one meeting last y Where should a one-on-one take place', 'diez'),
 GU: ('la reunion individual ya programada y decidir de quien es y quien la prepara', 'L41, A key point about a one-on-one', 'siete'),
 CU: ('decidir que asuntos se tratan dentro de la reunion individual', 'L43, What should be covered in a one-on-one', 'diez'),
}
def desde_cabeza(h):
    cond, lin, n = HIJO[h]
    return (h + '|SANO|Relectura conjunta de la vuelta 69 (ACTA 67 67.4.d, D68.7): esta cabeza solo produce saber que las reuniones '
            'de proceso son de tres clases y como se llaman (pasos 1 a 4, L23). La condicion del vecino, ' + cond + ', parte de su '
            'propia situacion con el uno a uno ya en marcha y contesta su propia pregunta del libro (' + lin + '); ninguno de sus ' + n +
            ' pasos usa el producto de aqui. El unico hilo es el rotulo del paso 2, y nombrar no es procedimentar. El encabezado '
            'ONE-ON-ONES (L25) dice donde esta el vecino en el libro, no que continue el trabajo de la cabeza (P.17). Es la figura de '
            'D67.3 y no la de C1: en C1 la condicion del hijo era el producto de pasos de la madre que mandan algo. SANO. Correccion '
            'declarada: la linea vieja decia CONTINUA madre=' + C + ' (DISCUTIBLE D69.1).')
def desde_hijo(h):
    cond, lin, n = HIJO[h]
    return (C + '|SANO|El mismo par que la cabeza lee desde su lado (relectura conjunta de la vuelta 69, D68.7): este candidato '
            'parte de su propia situacion con el uno a uno en marcha y contesta su propia pregunta del libro (' + lin + '); no usa '
            'el saber de cuantas clases de reunion de proceso hay y como se llaman, que es todo lo que la cabeza produce (L23). '
            'SANO. Correccion declarada: la linea vieja decia CONTINUA madre=' + C + ' (DISCUTIBLE D69.1).')
MOT = 'D68.7, CONTINUA a SANO'
V = {(C, h): (MOT, desde_cabeza(h)) for h in HIJO}
V.update({(h, C): (MOT, desde_hijo(h)) for h in HIJO})
# las razones tio y sobrino de D68.8: la clase SANO se sostiene, la razon deja de decir tio
T1, T2 = 'Tio y sobrino (DISCUTIBLE D68.8)', 'tio y sobrino (DISCUTIBLE D68.8)'
N1 = ('Del mismo tramo de reuniones de proceso y sin jerarquia entre ellos (DISCUTIBLE D68.8; razon corregida en la vuelta 69, '
      'D69.2: decia tio y sobrino porque leia a ' + C + ' como madre del vecino, y la relectura conjunta de D68.7 la deja sin hijos)')
N2 = 'del mismo tramo y sin jerarquia (DISCUTIBLE D68.8; razon corregida en la vuelta 69, D69.2)'
f = '.v68ext/veredictos_listos.txt'
t = io.open(f, encoding='utf-8').read()
if '# vuelta 69' in t:
    print('ya corregido'); sys.exit(0)
out, act, hechos, tios = [], None, 0, 0
for l in t.split('\n'):
    if l.startswith('## '):
        act = l[3:].strip()
    elif l.strip() and not l.startswith('#'):
        k = (act, l.split('|')[0])
        if k in V:
            motivo, nueva = V[k]
            out.append('# vuelta 69, %s: %s' % (motivo, l)); out.append(nueva); hechos += 1; continue
        if T1 in l or T2 in l:
            assert (act == IN) or (k[1] == IN), k
            out.append('# vuelta 69, razon corregida, la clase SANO se sostiene: ' + l)
            out.append(l.replace(T1, N1).replace(T2, N2)); tios += 1; continue
    out.append(l)
assert hechos == 8, hechos
assert tios == 8, tios
io.open(f, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
print('veredictos_listos: %d lineas CONTINUA a SANO y %d razones tio y sobrino corregidas, la vieja encima como comentario' % (hechos, tios))

g = '.v68ext/aristas_lectura.txt'
t = io.open(g, encoding='utf-8').read().rstrip('\n').split('\n')
ARI = {
 'facilitar_expresion_subordinado_pregunta_mas': ('madre paso 2, hijo paso 1', 'cap_05 L45', 'estar dentro de la reunion individual como supervisor y decidir que papel juegas', 'L45, What is the role of the supervisor in a one-on-one', 'seis'),
 'acumular_asuntos_importantes_fichero_espera': ('madre paso 2, hijo paso 2', 'cap_05 L51', 'los asuntos que aparecen entre una reunion individual y la siguiente', 'L51, A real time-saver is using a hold file', 'cuatro'),
 'alentar_asuntos_corazon_vigilar_final_reunion': ('madre paso 2, hijo paso 1', 'cap_05 L53', 'la reunion individual en marcha y decidir si se abre la puerta a los problemas de fondo', 'L53, The supervisor should also encourage the discussion of heart-to-heart issues', 'ocho'),
 'programar_reunion_individual_cadena': ('madre paso 2, hijo paso 1', 'cap_05 L57', 'poner en el calendario la reunion individual siguiente', 'L57, One-on-ones should be scheduled on a rolling basis', 'cinco'),
}
out, hechos, razon = [], 0, 0
for l in t:
    p = [c.strip() for c in l.split('|')]
    if l.startswith('SOSTENGO | ' + C + ' | ') and p[2] in ARI:
        pasos, linea, cond, lib, n = ARI[p[2]]
        out.append('# vuelta 69, D68.7, SOSTENGO a NO SOSTENGO: ' + l)
        out.append('NO SOSTENGO | ' + C + ' | ' + p[2] + ' | ' + pasos + ' | ' + linea + ' | Relectura conjunta de la vuelta 69 (ACTA 67 '
                   '67.4.d, D68.7): la cabeza solo produce saber que las reuniones de proceso son de tres clases y como se llaman (L23). '
                   'La condicion del hijo, ' + cond + ', parte de su propia situacion con el uno a uno en marcha y contesta su propia '
                   'pregunta del libro (' + lib + '); ninguno de sus ' + n + ' pasos usa el producto de la cabeza. El unico hilo es el '
                   'rotulo del paso 2, y el encabezado ONE-ON-ONES (L25) es formato (P.17). Figura de D67.3, no de C1. SANO. Correccion '
                   'declarada: la fila vieja decia SOSTENGO (DISCUTIBLE D69.1).')
        hechos += 1; continue
    if l.startswith('NO SOSTENGO | ' + C + ' | tomar_notas_copia_guion_reunion_individual'):
        out.append('# vuelta 69, razon corregida, NO SOSTENGO se sostiene: ' + l)
        out.append('NO SOSTENGO | ' + C + ' | tomar_notas_copia_guion_reunion_individual, conducir_reunion_individual_telefono_distancia | '
                   'madre paso 2 | cap_05 L49, L55 | Tambien despliegan un aspecto del uno a uno, y por la misma razon que las ocho de la '
                   'relectura conjunta de la vuelta 69 (D68.7): la cabeza solo produce saber cuantas clases hay y como se llaman (L23), y '
                   'ninguna condicion de estos dos parte de eso. La de tomar_notas es el guion ya preparado, producto de '
                   'preparar_guion_reunion_individual_subordinado (L49), y la de conducir_telefono sigue a tomar_notas (L55); las dos '
                   'CONTINUA en .v68ext/veredictos_listos.txt. SANO. Correccion declarada: la razon vieja los llamaba nieta y bisnieta de '
                   'la cabeza por preparar_guion, y la conjunta deja a preparar_guion sin madre en la cabeza (DISCUTIBLE D69.2).')
        razon += 1; continue
    out.append(l)
assert hechos == 4, hechos
assert razon == 1, razon
out.append('# vuelta 69, D.37 corregido por la relectura conjunta de D68.7 (DISCUTIBLE D69.2): el comentario D.37 de arriba dice que el uno')
out.append('# a uno lo despliegan sus preguntas, que van arriba por D.29 y en los veredictos, figura de C1. Desde la vuelta 69 ninguna de')
out.append('# esas preguntas cuelga de la cabeza: todas quedan SANO o NO SOSTENGO con ella, porque la cabeza solo nombra las tres clases.')
out.append('# Lo que D.37 decidia no cambia: ninguna de las tres clases es un nodo, y no hay arista cabeza a parte que declarar.')
out.append('# vuelta 69, relectura conjunta de D68.15 (ACTA 67 67.4.d), con las dos lecturas para d170 (DISCUTIBLE D69.3). SIGUE EN ESPERA y')
out.append('# no toca a la 70. LA DE LA 68: SOSTENGO aplazada, porque L33 deriva la frecuencia del principio del estilo (As we will see later,')
out.append('# Accordingly) y el paso 5 del hijo lo nombra. LA DEL AUDITOR: NO, porque el paso 5 del hijo es un Cuenta con que nombra el')
out.append('# principio, el producto de la madre es un estilo elegido para un subordinado y ningun paso del hijo lo usa. MI LECTURA DE LA 69: NO.')
out.append('# El hijo no parte del estilo elegido: mide la madurez el mismo (paso 3, L33, how much experience does a given subordinate have with')
out.append('# the specific task at hand) y saca la frecuencia de esa madurez (pasos 6 y 7) y del ritmo del area (pasos 8 a 10, L35). Lo que')
out.append('# comparte con la madre es la madurez de tarea y el principio que la madre despliega (pasos 4 a 6), no su producto; As we will')
out.append('# see later es una remision del libro, y una remision es metadato (P.17). Si la aduana de la vuelta que inserte la madre levanta')
out.append('# el par, es linea de veredicto SANO; si no lo levanta, no hay arista que declarar. d170 no se paga aqui.')
io.open(g, 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
print('aristas_lectura: %d filas SOSTENGO a NO SOSTENGO, %d razon corregida, y los comentarios de D.37 y de la EN ESPERA anadidos' % (hechos, razon))
