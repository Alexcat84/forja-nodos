# -*- coding: utf-8 -*-
"""Vuelta 75, TAREA 2.3: lo que las tres operaciones movieron, medido. Compara dataset/nodos.jsonl de HEAD (antes de la TAREA 2,
que no se ha commiteado todavia) contra el de trabajo: que nodos cambian y en que campos; los pasos de dar_elogio hoy; lo que su
resumen gana; y la linea que corregir dejo en la bitacora. Solo lee."""
import io, json, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')
N = 'dar_elogio_disciplina_igual_critica'
antes = dict((d['id'], d) for d in (json.loads(l) for l in subprocess.run(['git', 'show', 'HEAD:dataset/nodos.jsonl'],
         capture_output=True, text=True, encoding='utf-8').stdout.splitlines() if l.strip()))
hoy = dict((d['id'], d) for d in (json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()))
cambian = [(i, sorted(k for k in set(antes[i]) | set(hoy.get(i, {})) if antes[i].get(k) != hoy.get(i, {}).get(k))) for i in antes]
cambian = [c for c in cambian if c[1]]
print('nodos antes: %d | hoy: %d | nuevos: %d | que desaparecen: %d | que cambian: %d %s' % (len(antes), len(hoy),
      len(set(hoy) - set(antes)), len(set(antes) - set(hoy)), len(cambian), cambian))
a, b = antes[N], hoy[N]
print('pasos de %s: antes %d | hoy %d' % (N, len(a['pasos_accionables']), len(b['pasos_accionables'])))
viejos = a['pasos_accionables']; nuevos = b['pasos_accionables']
mapa = [(k + 1, nuevos.index(p) + 1 if p in nuevos else None) for k, p in enumerate(viejos)]
print('numeracion vieja > nueva: ' + ', '.join('%d>%s' % (v, n if n else 'SALE') for v, n in mapa))
print('el resumen viejo sigue entero al principio del nuevo: %s | caracteres %d > %d' % (b['resumen_teorico'].startswith(a['resumen_teorico']),
      len(a['resumen_teorico']), len(b['resumen_teorico'])))
print('lo que gana el resumen, por sus frases de apertura:')
for m in ['CORRECCION DECLARADA (26 sep 2026', 'CORRECCION DECLARADA (17 sep 2026, D.54): EL PASO 17', 'CORRECCION DECLARADA (17 sep 2026, D.54): EL PASO 8']:
    print('  %-60s %d vez' % (m, b['resumen_teorico'][len(a['resumen_teorico']):].count(m)))
for n, p in enumerate(nuevos, 1):
    print('%2d %s' % (n, p))
L = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()]
d = L[-1]
print('bitacora: %d lineas; la ultima: candidato %s | veredicto %s | levantada_por %s | huella_vecino (antes) %s | huella_candidato (despues de corregir) %s' % (
      len(L), d['candidato'], d['veredicto'], d['levantada_por'], d['huella_vecino'], d['huella_candidato']))
