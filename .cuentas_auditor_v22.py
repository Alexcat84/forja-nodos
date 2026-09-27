# -*- coding: utf-8 -*-
"""Las dos fronteras de la vuelta 22 contadas: cap_10 con su pieza 14 dentro,
y cap_11 entero. La aritmetica de PASOS INVENTADOS la hace el guion, no yo."""
import io, json
CAP10 = """admitir_pronto_mal_desempenio_cuatro_razones armar_plan_anual_crecimiento_equipo
calibrar_ascensos_evitar_politica calibrar_decision_despido_documentarla
contactar_despedido_mes_despues conversar_historia_vida_descubrir_motivadores
conversar_suenios_cruzar_habilidades evitar_obsesion_ascenso_estatus
facilitar_despido_tres_cosas montar_proceso_contratacion_reducir_sesgo
reconocer_excelencia_trayectoria_gradual sopesar_consejo_legal_despedir_humildad
trazar_plan_dieciocho_meses_aprendizaje desplegar_tres_conversaciones_carrera""".split()
CAP11 = [l.strip() for l in io.open('.lote_v22_auditor.txt',encoding='utf-8')
         if l.strip() and l.strip()!='desplegar_tres_conversaciones_carrera']
# PUENTES que MI relectura ciega caza EN ESTA FASE, con su cita
PUENTES = {('debatir_decidir_asuntos_cultura_evitar_delegar',2):
           'candelabro de las SIETE velas: L303 escribe solo A menorah?'}
# PUENTES YA CAZADOS EN VUELTAS ANTERIORES, que siguen contando en el numerador
# (ACTA 21 seccion 4.8: el numerador cuenta los puentes escritos y cazados, se
# hayan corregido o no). Sin esta linea la fila de cap_10 saldria 0 y seria falsa.
HEREDADOS = {'cap_10': 17, 'cap_11': 0}
def pasos(n):
    d=json.load(io.open('cuarentena/scott_radical_candor/%s.json'%n,encoding='utf-8'))
    return len(d['pasos_accionables'])
for rot, lote in (('cap_10', CAP10), ('cap_11', CAP11)):
    tot=0
    print('=== %s : %d piezas ===' % (rot, len(lote)))
    for n in sorted(lote):
        p=pasos(n); tot+=p
        print('  %4d  %s' % (p, n))
    nuevos=sum(1 for (nid,_) in PUENTES if nid in lote)
    here=HEREDADOS[rot]
    pue=nuevos+here
    print('  PASOS ESCRITOS EN %s : %d' % (rot, tot))
    print('  puentes ya cazados en vueltas anteriores : %d (ACTA 21 4.8)' % here)
    print('  puentes que MI relectura caza HOY        : %d' % nuevos)
    print('  PASOS INVENTADOS %s : (%d + %d) / %d = %.2f por ciento'
          % (rot, here, nuevos, tot, 100.0*pue/tot))
    print('  tope del freno: 10 por ciento -> %s' % ('SE DISPARA' if 100.0*pue/tot>10 else 'NO se dispara'))
    print('')
print('PUENTES CAZADOS, uno a uno con su cita:')
for (nid,i),q in PUENTES.items():
    print('  %s paso %d : %s' % (nid,i,q))
