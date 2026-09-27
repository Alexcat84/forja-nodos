# -*- coding: utf-8 -*-
"""TAREA 2 de la vuelta 67: la relectura conjunta de la ACTA 65 65.4.b, escrita por correccion declarada.
Cada linea que cambia en .v66ext/veredictos_listos.txt o .v66ext/aristas_lectura.txt queda ENCIMA de la nueva
como comentario '# vuelta 67, <motivo>: <linea vieja>'. No borra nada. Se corre una vez; si ya corrio, no toca."""
import io, sys
S, B, E, D = ('subir_productividad_gerencial_tres_vias', 'buscar_actividad_alta_palanca_tres_vias',
              'elegir_momento_actividad_palanca_maxima', 'detectar_palanca_negativa_actividad_mando')
V = {
 (S, B): ('C1, SANO a CONTINUA madre subir', B + '|CONTINUA|madre=' + S + '|Relectura conjunta de la vuelta 67 (ACTA 65 65.4.b, C1): las tres vias de este candidato son medios y no metas, el ritmo, la palanca de las actividades y la mezcla son objetos de trabajo nombrados uno a uno (L195 a L201), asi que pasa 9.1. El vecino despliega la segunda y la tercera: L203 abre su tramo con Let us consider first the leverage of various types of managerial work, y su condicion escrita, Cuando ya sabes que quieres subir la palanca de lo que haces y te falta saber donde esta la palanca alta, es el producto de los pasos 3 y 4 de aqui, que mandan subir la palanca y correr la mezcla hacia las de mayor palanca sin decir cuales son. El vecino lo dice por sus tres vias (L207 a L213). Fuera del solape queda procedimiento en los dos lados, el ritmo y la mezcla aqui y las tres vias alli: continua, no repite. La razon vieja usaba EXTRACTOR 9.1 restriccion 1 para decidir la arista, y la restriccion 3 dice que 9.1 no mueve la vara de continua contra repite.'),
 (B, S): ('C1, SANO a CONTINUA madre subir', S + '|CONTINUA|madre=' + S + '|El mismo par que subir lee desde su lado y con la misma direccion (relectura conjunta de la vuelta 67, C1): este candidato usa el producto de los pasos 3 y 4 de la madre, subir la palanca y correr la mezcla hacia las de mayor palanca, y anade lo que la madre no tiene, las tres vias por las que se reconoce una actividad de alta palanca (L203 a L213). La razon vieja usaba EXTRACTOR 9.1 restriccion 1, que no decide aristas (restriccion 3).'),
 (B, E): ('C2, SANO a CONTINUA madre buscar', E + '|CONTINUA|madre=' + B + '|Relectura conjunta de la vuelta 67 (ACTA 65 65.4.b, C2): la condicion escrita del vecino, Cuando la actividad que tienes delante es de las de alta palanca, es el producto de este candidato, y L215 lo ata al texto: el ejemplo de Robin es el de la primera via (The first is the most obvious example) y de el dice el libro leverage that depends, however, on when it is performed. El vecino toma la actividad de alta palanca que las vias reconocieron y anade el momento, por delante o inmediato (L215 a L217), que ninguna de las tres vias de aqui nombra; fuera del solape queda procedimiento en los dos lados. La razon vieja contestaba si el vecino despliega una via, y lo que decide es si usa el producto de este candidato: lo usa.'),
 (E, B): ('C2, SANO a CONTINUA madre buscar', B + '|CONTINUA|madre=' + B + '|El mismo par que buscar lee desde su lado y con la misma direccion (relectura conjunta de la vuelta 67, C2): este candidato parte de una actividad ya reconocida como de alta palanca, que es el producto de la madre, y le anade el momento (L215 a L217).'),
 (S, E): ('razon corregida, la clase SANO se sostiene', E + '|SANO|La condicion del vecino, Cuando la actividad que tienes delante es de las de alta palanca, no es producto de este candidato sino de buscar_actividad_alta_palanca_tres_vias, que es hijo de este (C1) y madre del vecino (C2). El paso 3 de aqui manda subir la palanca y el vecino no la sube: elige el momento de una actividad que buscar ya reconocio (L215 a L217). La relacion pasa por buscar y no pide arista propia: SANO. Correccion declarada de la vuelta 67: la razon vieja usaba EXTRACTOR 9.1 restriccion 1, que no decide aristas (restriccion 3); cae el argumento y la clase se sostiene por 6.1 (DISCUTIBLE D67.4).'),
 (E, S): ('razon corregida, la clase SANO se sostiene', S + '|SANO|El mismo par que subir lee desde su lado: este candidato parte de una actividad de alta palanca ya reconocida, producto de buscar_actividad_alta_palanca_tres_vias y no de este vecino; la relacion con subir pasa por buscar (C1 y C2) y no pide arista propia. Correccion declarada de la vuelta 67: la razon vieja usaba EXTRACTOR 9.1 restriccion 1, que no decide aristas (restriccion 3) (DISCUTIBLE D67.4).'),
}
f = '.v66ext/veredictos_listos.txt'
t = io.open(f, encoding='utf-8').read()
if '# vuelta 67' in t:
    print('ya corregido'); sys.exit(0)
out, act, hechos = [], None, 0
for l in t.split('\n'):
    if l.startswith('## '):
        act = l[3:].strip()
    elif l.strip() and not l.startswith('#'):
        k = (act, l.split('|')[0])
        if k in V:
            motivo, nueva = V[k]
            out.append('# vuelta 67, %s: %s' % (motivo, l)); out.append(nueva); hechos += 1; continue
    out.append(l)
assert hechos == 6, hechos
io.open(f, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
print('veredictos_listos: %d lineas corregidas, la vieja encima como comentario' % hechos)
g = '.v66ext/aristas_lectura.txt'
t = io.open(g, encoding='utf-8').read().rstrip('\n').split('\n')
out, hechos = [], 0
for l in t:
    if l.startswith('NO SOSTENGO | ' + S + ' | identificar_paso_limitante'):
        out.append('# vuelta 67, razon corregida, NO SOSTENGO se sostiene: ' + l)
        out.append('NO SOSTENGO | ' + S + ' | identificar_paso_limitante_jornada_desfases, agrupar_tareas_semejantes_aprovechar_preparacion, usar_calendario_herramienta_planificacion_produccion, decir_no_trabajo_excede_capacidad, llevar_inventario_proyectos_discrecionales | madre paso 2 | cap_04 L259 a L261 | El tramo de L259 a L291 cuelga del paso 2 de la madre (L259, Increasing Managerial Activity Rate: Speeding Up the Line), pero ninguno de los cinco usa el producto de ese paso: sus condiciones escritas parten de su propia situacion (ordenar la jornada, varias actividades del mismo tipo, el calendario lleno por otros, trabajo por encima de la capacidad, tiempo libre sin nada preparado) y no de querer acelerar, y cada uno aplica su propio principio de produccion (L267 First, L269 A second production principle, L277 y L289 Another production principle), que es lo que usa (d072 para el paso limitante). Es la diferencia con buscar_actividad_alta_palanca_tres_vias, cuya condicion escrita si es el producto de los pasos 3 y 4 de la madre (C1). Correccion declarada de la vuelta 67: la razon vieja decia que el paso 2 era una meta (EXTRACTOR 9.1, restriccion 1), y esa vara no decide aristas (restriccion 3); cae el argumento y la clase se sostiene por 6.1 (DISCUTIBLE D67.3).')
        hechos += 1; continue
    out.append(l)
assert hechos == 1
out.append('# vuelta 67, relectura conjunta de la ACTA 65 65.4.b, C3: un par que la lectura de la 66 no miro.')
out.append('NO SOSTENGO | ' + B + ' | ' + D + ' | madre paso 1, hijo condicion | cap_04 L193, L219 | La condicion del hijo, Cuando repasas tus propias actividades de mando buscando su palanca, coincide con el paso 1 de la madre, pero ese repaso no es producto de la madre: es el mandato de L193 (being sensitive to the leverage of what you do during the day), que el paso 1 de la madre transcribe (D66.3, sostenido T por L193) y del que cuelgan los dos. El producto de la madre son las actividades de alta palanca reconocidas por sus tres vias (L207 a L213), y ninguno de los nueve pasos del hijo las usa ni nombra una via: el hijo busca en el mismo repaso las de signo contrario (L219, Leverage can also be negative) y trae su procedimiento entero. Dos busquedas hermanas sobre el mismo repaso. SANO (DISCUTIBLE D67.2).')
io.open(g, 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
print('aristas_lectura: 1 razon corregida y la fila de C3 anadida')
