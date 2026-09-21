# -*- coding: utf-8 -*-
"""LA SENIAL DE LA CASA NO ES SIMETRICA, y lo compruebo antes de publicar cualquier
'el mas proximo'. src.aduana.senal_similitud_texto llama a difflib.SequenceMatcher, que
indexa la SEGUNDA secuencia: cambiar el orden de los dos nodos cambia el digito.
Se mide sobre los pares de esta tanda que salen por encima del umbral en mi barrido."""
import json, io, sys
sys.path.insert(0, '.')
from src import aduana, comun
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def t(i):
    return comun.texto_comparable(json.load(open('cuarentena/grove_high_output/%s.json' % i, encoding='utf-8')))
PARES = [('buscar_regularidad_bloques_iguales_trabajo_mando', 'llevar_inventario_proyectos_discrecionales'),
         ('decir_no_trabajo_excede_capacidad', 'usar_calendario_herramienta_planificacion_produccion'),
         ('decir_no_trabajo_excede_capacidad', 'llevar_inventario_proyectos_discrecionales'),
         ('decir_no_trabajo_excede_capacidad', 'identificar_paso_limitante_jornada_desfases'),
         ('decir_no_trabajo_excede_capacidad', 'agrupar_tareas_semejantes_aprovechar_preparacion'),
         ('llevar_inventario_proyectos_discrecionales', 'identificar_paso_limitante_jornada_desfases'),
         ('llevar_inventario_proyectos_discrecionales', 'agrupar_tareas_semejantes_aprovechar_preparacion')]
print('los 7 pares distintos que mi barrido deja por encima del umbral 0.35, medidos en los DOS sentidos:')
dif = 0
for a, b in PARES:
    ab = aduana.senal_similitud_texto(t(a), t(b)); ba = aduana.senal_similitud_texto(t(b), t(a))
    if abs(ab - ba) > 1e-9: dif += 1
    print('   %.4f  contra  %.4f   (%+.4f)   %s  <->  %s' % (ab, ba, ab - ba, a[:34], b[:34]))
print()
print('pares en los que el digito cambia al invertir el orden: %d de %d' % (dif, len(PARES)))
