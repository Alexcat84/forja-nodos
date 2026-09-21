# -*- coding: utf-8 -*-
"""PASOS INVENTADOS POR CAPITULO (AUDITOR_FORJA.md 8) para la vuelta 59.
Cuento yo los pasos que la vuelta ESCRIBIO (su numerador y su denominador),
y aparte los que RELEYO, que no son lo mismo y por eso van en filas distintas."""
import json, os, subprocess

def sal(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True,
                          text=True).stdout.strip()

ANTES, AHORA = '77b506b', 'c559d78'
nuevos = sal('git diff --name-status %s %s -- cuarentena/ dataset/' % (ANTES, AHORA))
print('$ git diff --name-status %s %s -- cuarentena/ dataset/' % (ANTES, AHORA))
print(nuevos if nuevos else '(vacio: ni una ficha nueva, ni una linea de dataset)')
print()

TRES = ['mejorar_consciencia_propia_relacional_dos_practicas',
        'practicar_triangulo_critica_tres_papeles',
        'resolver_dudas_frecuentes_pedir_critica']
cuenta = {}
for l in open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l)
    if d['id'] in TRES:
        cuenta[d['id']] = len(d['pasos_accionables'])
print('pasos de los tres nodos que la vuelta 59 releyo, contados por mi')
print('sobre dataset/nodos.jsonl y no sobre su tabla:')
for k in TRES:
    print('   %-52s %2d' % (k, cuenta[k]))
print('   %-52s %2d' % ('TOTAL RELEIDO', sum(cuenta.values())))
