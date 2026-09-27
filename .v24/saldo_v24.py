# -*- coding: utf-8 -*-
"""EL SALDO DE LA ADUANA DE ESTA VUELTA, CONTADO DE LOS INFORMES CRUDOS.

Un informe por candidato, corrido en el acto de escribirlo (EXTRACTOR.md 16).
La tabla se imprime de estos ficheros y no se teclea (D.41).
"""
import glob
import io
import os
import re

ORDEN = [
    'repartir_semana_cuarenta_horas_jefe',
    'montar_equipo_gestion_desempenio_revisar_sistema',
    'recorrer_trece_elementos_proceso_evaluacion_formal',
    'decidir_poner_nota_comunicar_proposito_limites',
    'elegir_categorias_nota_palabras_propias_empresa',
    'escribir_escaleras_puesto_evitar_dos_extremos',
    'fijar_cuatro_notas_calcular_nota_global',
    'elegir_palabras_nota_definirlas_empresa_entera',
    'aplicar_consecuencias_nota_apoyar_fuerzas_persona',
    'repartir_notas_publicar_reparto_esperado',
    'presionar_curva_notas_sin_forzarla',
    'presionar_curva_notas_evitar_forzarla',
    'calibrar_notas_reunion_jefes_pares',
    'evaluar_desempenio_dos_veces_anio',
    'montar_evaluacion_360_grados_ligera_pares',
    'hacer_critica_pares_transparente_ensenar_escribirla',
    'mantener_proceso_evaluacion_ligero_vigilar_crecimiento',
]

SALDO = re.compile(r'^\[(ENTRARIA|BLOQUEARIA|CAERIA)\]', re.M)
POBLACION = re.compile(r'poblacion del barrido\s*:\s*(\d+)')

filas = []
for nombre in ORDEN:
    ruta = os.path.join('.aduana_v24', nombre + '.txt')
    if not os.path.exists(ruta):
        continue
    texto = io.open(ruta, encoding='utf-8').read()
    saldo = SALDO.findall(texto) or ['(sin saldo)']
    pob = POBLACION.search(texto)
    vecinos = len(re.findall(r'^    vecino ', texto, re.M))
    filas.append((nombre, saldo[0], pob.group(1) if pob else '?', vecinos))

print('| # | candidato | saldo | poblacion del barrido | vecinos levantados |')
print('|---:|---|---|---:|---:|')
for indice, (nombre, saldo, pob, vecinos) in enumerate(filas, 1):
    print('| %d | `%s` | **%s** | %s | **%d** |' % (indice, nombre, saldo, pob, vecinos))

cuenta = {}
for _n, s, _p, _v in filas:
    cuenta[s] = cuenta.get(s, 0) + 1

print('')
print('| el saldo de la tanda | cuantos |')
print('|---|---:|')
print('| corridas del informe de un candidato | **%d** |' % len(filas))
print('| `ENTRARIA` | **%d** |' % cuenta.get('ENTRARIA', 0))
print('| `BLOQUEARIA` (cola de lectura, no rechazo) | **%d** |' % cuenta.get('BLOQUEARIA', 0))
print('| `CAERIA` | **%d** |' % cuenta.get('CAERIA', 0))
print('| filas vecino levantadas en total | **%d** |'
      % sum(v for _n, _s, _p, v in filas))
print('| pares distintos y sus veredictos | **ver la tabla de `R.5.e`** |')
