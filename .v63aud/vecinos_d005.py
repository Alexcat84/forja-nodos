# -*- coding: utf-8 -*-
"""Los 6 candidatos de d005 (cap_03 de grove que su aduana en seco dejo en BLOQUEARIA):
su veredicto de aduana y sus vecinos, leidos de los informes que la fase ciega ANULADA
de la vuelta 63 dejo archivados (poblacion 462). Y el control de determinismo: los
informes de los 16 de la tanda, archivados alli y re corridos en la fase ciega sellada,
se comparan linea a linea quitando solo la linea INICIO."""
import io, os, re
A = 'docs/loop/archivo/interrumpidas/2026-09-23-v63-fase-ciega-2/v63ciega'
D005 = ['archivar_indicadores_resolver_problemas', 'construir_grafico_escalonado_pronosticos',
        'construir_indicador_tendencia_patron', 'elegir_fabricar_pedido_pronostico',
        'elegir_indicador_salida_trabajo_administrativo', 'emparejar_indicadores_efecto_contraefecto']
def leer(r):
    return io.open(r, encoding='utf-8').read()
for i in D005:
    t = leer('%s/informe_%s.txt' % (A, i))
    pob = re.search(r'poblacion del barrido\s*:\s*(\d+)', t).group(1)
    ver = re.search(r'^\[(\w+)\] %s' % re.escape(i), t, re.M)
    print('%s  %s  poblacion %s' % (ver.group(1) if ver else 'SIN VEREDICTO', i, pob))
    for m in re.finditer(r'vecino (\S+)\s+\[levantada por: ([^\]]+)\]\n\s+similitud_texto ([\d.]+) \| familia_id ([\d.]+) \| paso_contra_nodo ([\d.]+)\n\s+(paso \d+ del candidato contra paso \d+) de', t):
        print('    %-50s %-26s texto %s familia %s paso %s  %s' % m.groups()[:6])
print()
print('CONTROL DE DETERMINISMO, los 16 de la tanda: archivo de la fase 2 contra .v63aud/')
iguales = distintos = vacios = 0
for i in io.open('.v63aud/tanda.txt', encoding='utf-8').read().split():
    a = '%s/informe_%s.txt' % (A, i)
    if os.path.getsize(a) == 0:
        vacios += 1; print('   VACIO en el archivo: %s' % i); continue
    la = [l for l in leer(a).split('\n') if not l.startswith('INICIO')]
    lb = [l for l in leer('.v63aud/informe_%s.txt' % i).split('\n') if not l.startswith('INICIO')]
    if la == lb: iguales += 1
    else:
        distintos += 1; print('   DISTINTO: %s' % i)
print('   identicos linea a linea: %d | distintos: %d | vacios en el archivo: %d' % (iguales, distintos, vacios))
