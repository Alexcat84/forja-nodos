# -*- coding: utf-8 -*-
import json, io
IDS="""escuchar_entender_critica_dominar_defensa 13
premiar_franqueza_hacer_escucha_tangible 20
integrar_peticion_critica_rutina_existente 13
dar_elogio_disciplina_igual_critica 20
medir_critica_respuesta_oyente_brujula 33
montar_equipo_gestion_desempenio_revisar_sistema 12
recorrer_trece_elementos_proceso_evaluacion_formal 14
decidir_poner_nota_comunicar_proposito_limites 8
elegir_categorias_nota_palabras_propias_empresa 15
escribir_escaleras_puesto_evitar_dos_extremos 7
fijar_cuatro_notas_calcular_nota_global 12
elegir_palabras_nota_definirlas_empresa_entera 10
aplicar_consecuencias_nota_apoyar_fuerzas_persona 16
repartir_notas_publicar_reparto_esperado 9
presionar_curva_notas_evitar_forzarla 11
calibrar_notas_reunion_jefes_pares 15
evaluar_desempenio_dos_veces_anio 11
montar_evaluacion_360_grados_ligera_pares 10
hacer_critica_pares_transparente_ensenar_escribirla 11
mantener_proceso_evaluacion_ligero_vigilar_crecimiento 13"""
esp=[(l.split()[0],int(l.split()[1])) for l in IDS.strip().splitlines()]
N={}
for l in io.open('dataset/nodos.jsonl',encoding='utf-8'):
    if l.strip():
        d=json.loads(l); N[d['id']]=d
tot=0; mal=0
print('%-56s %5s %5s %s'%('id','dice','mido','ok'))
for i,(k,v) in enumerate(esp,1):
    if k not in N:
        print('%-56s %5d   NO ESTA EN EL GRAFO'%(k,v)); mal+=1; continue
    m=len(N[k].get('pasos_accionables') or [])
    tot+=m
    ok='OK' if m==v else '<<< DIFIERE'
    if m!=v: mal+=1
    print('%-56s %5d %5d %s'%(k,v,m,ok))
print('TOTAL pasos que mido:',tot,' (el reporte dice 273)   filas que difieren:',mal)
