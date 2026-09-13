# -*- coding: utf-8 -*-
"""Instrumento del AUDITOR, vuelta 23, fase ciega.
Cierra la frontera declarada de cap_12 y cap_13 contra su cuerpo, al digito.
No lee el reporte del extractor: los tramos salen del campo resumen_teorico
de los propios candidatos de cuarentena/, que es material del lote y no informe.
"""
import json, glob, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

TRAMOS = {
 'cap_12': [
  ('P1 desplegar_plan_orden_operaciones_franqueza_radical', [(13,13),(15,15),(19,49)]),
  ('P2 contar_historias_propias_explicar_franqueza_radical', [(17,17)]),
 ],
 'cap_13': [
  ('P1  mejorar_consciencia_propia_relacional_dos_practicas', [(17,22),(35,40)]),
  ('P2  contar_cuatro_historias_propias_ver_hueco_intencion', [(41,58)]),
  ('P3  practicar_triangulo_critica_tres_papeles',            [(59,72)]),
  ('P4  pedir_critica_primero_crear_seguridad_psicologica',   [(73,86),(105,110),(113,114)]),
  ('P5  elegir_pregunta_recurrente_pedir_critica',            [(115,120),(129,166)]),
  ('P6  resolver_dudas_frecuentes_pedir_critica',             [(167,186)]),
  ('P7  abrazar_incomodidad_silencio_contar_seis',            [(187,198)]),
  ('P8  escuchar_entender_critica_dominar_defensa',           [(199,214)]),
  ('P9  premiar_franqueza_hacer_escucha_tangible',            [(215,234)]),
  ('P10 integrar_peticion_critica_rutina_existente',          [(111,112),(235,246)]),
  ('P11 dar_elogio_disciplina_igual_critica',                 [(247,252),(267,288)]),
  ('P12 medir_critica_respuesta_oyente_brujula',              [(289,322)]),
 ],
}
# el cuerpo empieza tras el cierre del front-matter (segundo '---')
def cuerpo(cap):
    lin = open('fuentes/scott_radical_candor/%s.md'%cap, encoding='utf-8').read().split('\n')
    ini = [i for i,l in enumerate(lin,1) if l.strip()=='---'][1] + 1
    return lin, ini, len(lin)

def pal(s): return len([w for w in re.split(r'\s+', s) if w])

for cap in ('cap_12','cap_13'):
    lin, ini, fin = cuerpo(cap)
    # linea 'fin' puede ser una ultima vacia por el salto final
    while fin>ini and not lin[fin-1].strip(): fin -= 1
    total = sum(pal(lin[i-1]) for i in range(ini, fin+1))
    print('='*78)
    print('%s  cuerpo = lineas %d a %d   palabras del cuerpo = %d' % (cap, ini, fin, total))
    print('-'*78)
    dueno = {}
    suma = 0
    solapes = []
    for nom, rangos in TRAMOS[cap]:
        p = 0
        for a,b in rangos:
            for i in range(a,b+1):
                if i < ini or i > fin: continue
                if i in dueno: solapes.append((i, dueno[i], nom))
                dueno[i] = nom
                p += pal(lin[i-1])
        suma += p
        print('  %-56s %s  %5d palabras' % (nom, ','.join('L%d-L%d'%r for r in rangos), p))
    residuo = [i for i in range(ini, fin+1) if i not in dueno]
    pres = sum(pal(lin[i-1]) for i in residuo)
    print('-'*78)
    print('  SUMA DE LOS TRAMOS         = %d palabras en %d piezas' % (suma, len(TRAMOS[cap])))
    print('  RESIDUO (lineas no cubiertas) = %d palabras en %d lineas' % (pres, len(residuo)))
    print('  SUMA + RESIDUO = %d   CUERPO = %d   %s' % (suma+pres, total,
          'CIERRA AL DIGITO' if suma+pres==total else '*** NO CIERRA ***'))
    print('  SOLAPES = %d %s' % (len(solapes), solapes if solapes else ''))
    print('  LINEAS DEL RESIDUO, NOMBRADAS UNA A UNA (orden 7.4 A del ACTA 19):')
    # agrupa el residuo en tramos contiguos
    tr=[]
    for i in residuo:
        if tr and i==tr[-1][1]+1: tr[-1][1]=i
        else: tr.append([i,i])
    for a,b in tr:
        pw = sum(pal(lin[i-1]) for i in range(a,b+1))
        txt = ' | '.join(lin[i-1][:70] for i in range(a,b+1) if lin[i-1].strip())[:150]
        print('    L%-3d a L%-3d  %4d pal   %s' % (a,b,pw,txt))
