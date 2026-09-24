# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 66 de .v64aud/normal/pasos_y_huellas.py con UNA ruta cambiada: en HEAD la ficha se busca
en cuarentena/grove_high_output/ y, si ya no esta, en cuarentena/_insertados/grove_high_output/ (las 20 filas de la 65).
(1) Cuenta los pasos de los seis de d005 en 067c9df (como los escribio el extractor) y hoy.
(2) Para los 22 de cap_02 y cap_03 (.v64ext/los22.txt): el blob de su ficha en el commit donde se
leyo su fidelidad entera (b63405c para los 16 de la 63, 997054d para los seis de d005) contra HEAD."""
import json, subprocess
D005 = ['archivar_indicadores_resolver_problemas', 'construir_grafico_escalonado_pronosticos',
        'construir_indicador_tendencia_patron', 'elegir_fabricar_pedido_pronostico',
        'elegir_indicador_salida_trabajo_administrativo', 'emparejar_indicadores_efecto_contraefecto']
git = lambda *a: subprocess.run(['git'] + list(a), capture_output=True, text=True, encoding='utf-8').stdout
ruta = lambda i: 'cuarentena/grove_high_output/%s.json' % i
hoy = lambda i: ruta(i) if subprocess.run(['git', 'cat-file', '-e', 'HEAD:' + ruta(i)], stderr=subprocess.DEVNULL).returncode == 0 else 'cuarentena/_insertados/grove_high_output/%s.json' % i
t0 = t1 = 0
for i in D005:
    a = len(json.loads(git('show', '067c9df:' + ruta(i)))['pasos_accionables'])
    b = len(json.loads(git('show', 'HEAD:' + hoy(i)))['pasos_accionables'])
    t0 += a; t1 += b
    print('%-48s pasos en 067c9df %d | hoy %d' % (i, a, b))
print('total pasos: 067c9df %d | hoy %d' % (t0, t1))
los22 = [l.split()[0] for l in open('.v64ext/los22.txt', encoding='utf-8') if l.strip() and not l.startswith('#')]
iguales = distintos = 0
for i in los22:
    base = '997054d' if i in D005 else 'b63405c'
    x = git('rev-parse', '%s:%s' % (base, ruta(i))).strip(); y = git('rev-parse', 'HEAD:' + hoy(i)).strip()
    if x == y: iguales += 1
    else: distintos += 1; print('DISTINTA desde su lectura: %s (%s)' % (i, base))
    print('  %-48s %s %s' % (i, 'bandeja   ' if hoy(i) == ruta(i) else '_insertados', 'igual' if x == y else 'DISTINTA'))
print('fichas de los 22: %d | iguales al commit de su lectura entera: %d | distintas: %d' % (len(los22), iguales, distintos))
