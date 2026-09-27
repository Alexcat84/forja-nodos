# -*- coding: utf-8 -*-
"""EL LIBRO MAYOR DE `cap_13` DE scott_radical_candor: que acta firmo que nodo.

Lo levanto porque la vuelta 59 pago `d006` sobre un `154` que ya estaba rancio
cuando se escribio. Los denominadores salen de los ficheros, no de ninguna acta:
los pasos se cuentan sobre dataset/nodos.jsonl y cuarentena/.

Las firmas se citan por su LINEA de docs/loop/ACTA_AUDITOR.md, para que cada
una se pueda abrir."""
import json, os, glob

CAP = 'scott_radical_candor/cap_13.md'

pasos = {}
for l in open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l)
    if any(CAP in str(f.get('ruta', '')) or CAP in str(f)
           for f in d.get('fuentes', [])) or CAP in json.dumps(d, ensure_ascii=False):
        pasos[d['id']] = (len(d.get('pasos_accionables', [])), 'GRAFO')
for p in glob.glob('cuarentena/**/*.json', recursive=True):
    if '_insertados' in p or '_derivadas' in p:
        continue
    d = json.load(open(p, encoding='utf-8'))
    if CAP in json.dumps(d, ensure_ascii=False) and d['id'] not in pasos:
        pasos[d['id']] = (len(d.get('pasos_accionables', [])), 'BANDEJA')

# QUIEN FIRMO QUE, con la linea del acta que lo dice
FIRMAS = {
    'pedir_critica_primero_crear_seguridad_psicologica':
        'ACTA 38 (linea 31630 y 31634): los 56 de su tramo, 0 PUENTE, LA FIRMO',
    'elegir_pregunta_recurrente_pedir_critica':
        'ACTA 38 (linea 31630 y 31634): los 56 de su tramo, 0 PUENTE, LA FIRMO',
    'resolver_dudas_frecuentes_pedir_critica':
        'ACTA 38 (linea 31630 y 31634) Y OTRA VEZ la vuelta 59 (SS.3.b)',
    'abrazar_incomodidad_silencio_contar_seis':
        'ACTA 39 (linea 31987) y ACTA 40 (7.2): los 58 y los 12, 0 PUENTE',
    'escuchar_entender_critica_dominar_defensa':
        'ACTA 39 (linea 31987): los 58 de su tramo, 0 PUENTE, LA FIRMO',
    'premiar_franqueza_hacer_escucha_tangible':
        'ACTA 39 (linea 31987): los 58 de su tramo, 0 PUENTE, LA FIRMO',
    'integrar_peticion_critica_rutina_existente':
        'ACTA 39 (linea 31987): los 58 de su tramo, 0 PUENTE, LA FIRMO',
    'mejorar_consciencia_propia_relacional_dos_practicas':
        'VUELTA 59 (SS.3.b), y la ACTA 58 la firma tras releer sus 13 citas',
    'practicar_triangulo_critica_tres_papeles':
        'VUELTA 59 (SS.3.b), y la ACTA 58 la firma tras releer sus 15 citas',
}
EL_154 = ['mejorar_consciencia_propia_relacional_dos_practicas',
          'contar_cuatro_historias_propias_ver_hueco_intencion',
          'practicar_triangulo_critica_tres_papeles',
          'pedir_critica_primero_crear_seguridad_psicologica',
          'elegir_pregunta_recurrente_pedir_critica',
          'resolver_dudas_frecuentes_pedir_critica',
          'dar_elogio_disciplina_igual_critica',
          'medir_critica_respuesta_oyente_brujula']

print('nodos de cap_13 que encuentro: %d   pasos: %d'
      % (len(pasos), sum(v[0] for v in pasos.values())))
print()
print('%-52s %5s %-8s %s' % ('nodo', 'pasos', 'sede', 'quien lo firmo'))
print('-' * 132)
for k in sorted(pasos, key=lambda x: -pasos[x][0]):
    n, sede = pasos[k]
    marca = '* ' if k in EL_154 else '  '
    print('%s%-50s %5d %-8s %s' % (marca, k[:50], n, sede,
                                   FIRMAS.get(k, 'NADIE')))
print()
print('(*) los ocho candidatos que componen el 154 de `d006`'
      ' (ACTA 39, linea 31857: NO releidos: 8 candidatos, 154 pasos)')
print()
el154 = sum(pasos[k][0] for k in EL_154)
firmados = sum(pasos[k][0] for k in EL_154 if k in FIRMAS)
print('el 154, recontado por mi sobre los ficheros : %d' % el154)
print('  de esos, ya firmados por alguna acta      : %d  (%s)'
      % (firmados, ', '.join(k[:26] for k in EL_154 if k in FIRMAS)))
print('  de esos, firmados HOY por la vuelta 59    : %d'
      % sum(pasos[k][0] for k in
            ('mejorar_consciencia_propia_relacional_dos_practicas',
             'practicar_triangulo_critica_tres_papeles',
             'resolver_dudas_frecuentes_pedir_critica')))
print('  SIN FIRMA DE NADIE, hoy incluido          : %d  (%s)'
      % (el154 - firmados, ', '.join(k[:34] for k in EL_154 if k not in FIRMAS)))
print()
sin = sum(n for k, (n, s) in pasos.items() if k not in FIRMAS)
print('cap_13 ENTERO sin firma de nadie            : %d de %d pasos'
      % (sin, sum(v[0] for v in pasos.values())))
