# -*- coding: utf-8 -*-
"""Los seis de d005: sus vecinos en el informe de HOY (.v64aud/informe_<id>.txt, fichas tal
como estan en la bandeja en esta fase) contra los del archivo de la fase 2 de la 63
(poblacion 462, fichas de 067c9df). Dice por candidato que pares siguen, cuales
dejan de levantar y cuales aparecen."""
import io, re
A = 'docs/loop/archivo/interrumpidas/2026-09-23-v63-fase-ciega-2/v63ciega'
D005 = ['archivar_indicadores_resolver_problemas', 'construir_grafico_escalonado_pronosticos',
        'construir_indicador_tendencia_patron', 'elegir_fabricar_pedido_pronostico',
        'elegir_indicador_salida_trabajo_administrativo', 'emparejar_indicadores_efecto_contraefecto']
PAT = r'vecino (\S+)\s+\[levantada por: ([^\]]+)\]\n\s+similitud_texto ([\d.]+) \| familia_id ([\d.]+) \| paso_contra_nodo ([\d.]+)\n\s+(paso \d+ del candidato contra paso \d+) de'
def lee(r):
    t = io.open(r, encoding='utf-8').read()
    pob = re.search(r'poblacion del barrido\s*:\s*(\d+)', t)
    ver = None
    for i in D005:
        m = re.search(r'^\[(\w+)\] %s' % re.escape(i), t, re.M)
        if m: ver = m.group(1)
    return (pob.group(1) if pob else '?'), ver, {m.group(1): m.groups()[1:6] for m in re.finditer(PAT, t)}, 'NADA SE INSERTO' in t
sig = dejan = nuevos = 0
for i in D005:
    pa, va, ga, _ = lee('%s/informe_%s.txt' % (A, i))
    ph, vh, gh, cerrado = lee('.v64aud/informe_%s.txt' % i)
    print('%s  %s  hoy poblacion %s%s | archivo: %s poblacion %s' % (vh or 'SIN VEREDICTO', i, ph, '' if cerrado else ' SIN LINEA DE CIERRE', va, pa))
    for v in sorted(set(ga) | set(gh)):
        if v in ga and v in gh: e = 'SIGUE'; sig += 1
        elif v in ga: e = 'DEJA DE LEVANTAR'; dejan += 1
        else: e = 'NUEVO'; nuevos += 1
        g = gh.get(v) or ga.get(v)
        print('    %-17s %-48s %-26s texto %s familia %s paso %s  %s' % ((e, v) + g))
print('pares que siguen: %d | dejan de levantar: %d | nuevos: %d' % (sig, dejan, nuevos))
