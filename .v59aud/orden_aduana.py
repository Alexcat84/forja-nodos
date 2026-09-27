# Auditor de la vuelta 59. LA PRUEBA DE QUE LA ADUANA MIDIO EN ORDEN,
# independiente de la linea 'poblacion del barrido' que el reporte pega.
#
# REGLA: si el candidato N se midio contra una poblacion que solo contenia
# a los candidatos 1..N-1, entonces NINGUN vecino levantado por el candidato N
# puede ser un candidato de indice mayor que N. Si lo fuera, la aduana habria
# corrido con la tanda entera dentro.
import re, io

ORDEN = ['entregar_evaluacion_desempeno_tres_claves',
         'preparar_resena_mixta_hoja_trabajo',
         'guiar_subordinado_etapas_resistencia_desempeno',
         'usar_banco_nueve_preguntas_entrevista',
         'responder_primer_aviso_renuncia_subordinado',
         'gestionar_retencion_subordinado_valioso_renuncia',
         'reciclar_empleado_ascendido_mas_alla_capacidad']

print('cand  poblacion  vecinos levantados que son candidatos de esta tanda   veredicto')
print('-' * 92)
roto = 0
for i, nombre in enumerate(ORDEN, 1):
    txt = io.open('.v58ext/informe_%d_%s.txt' % (i, nombre), encoding='utf-8').read()
    pob = re.search(r'poblacion del barrido\s*:\s*(\d+)', txt).group(1)
    vec = re.findall(r'vecino (\S+)\s+\[levantada por', txt)
    dentro = [(ORDEN.index(v) + 1) for v in vec if v in ORDEN]
    posteriores = [n for n in dentro if n > i]
    if posteriores:
        roto += 1
    print('%4d  %9s  %-52s  %s' % (
        i, pob,
        (', '.join('cand %d' % n for n in sorted(dentro)) or 'ninguno'),
        'ROTO: ve a ' + str(posteriores) if posteriores else 'EN ORDEN'))
print()
print('CANDIDATOS QUE VEN A UN HERMANO POSTERIOR: %d' % roto)
print('LA ADUANA MIDIO EN EL ORDEN DEL LIBRO      : %s' % ('NO' if roto else 'SI'))
