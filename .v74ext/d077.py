# -*- coding: utf-8 -*-
"""Vuelta 74, TAREA 2.2 (d077): cuales son las fichas de la tanda 58 y, por cada una, su barrido sobre grafo mas bandejas
antes de entrar o de quedar lista. Instrumento de lectura: no escribe nada fuera de su salida.
La tanda sale de tres vias, y las tres tienen que dar la misma lista: los .v58ext/informe_N_<id>.txt que d077 cita, el commit
de la vuelta 58 (db70fe94, lo que anadio en cuarentena/grove_high_output/) y lo que cada ficha dice de si misma (la
fecha de su fuente, la del dia en que se mino). Por ficha: su sede hoy; el barrido que la midio (el .v71ext o .v73ext/barrido_<id>.txt,
con su poblacion y sus vecinos, y la hora de INICIO de su barrido.log); los commits que tocaron la ficha, con su hora y si
cambiaron su contenido (git log --numstat: 0 0 es mover sin cambiar); y si el blob de hoy es el del cierre de su vuelta de barrido.
Y las lineas de la bitacora que la tienen de candidato."""
import io, json, glob, re, subprocess, os
git = lambda *a: subprocess.run(['git'] + list(a), capture_output=True, text=True, encoding='utf-8').stdout
por_informe = [re.match(r'\.v58ext/informe_(\d)_(.+)\.txt$', p.replace(os.sep, '/')) for p in glob.glob('.v58ext/informe_*.txt')]
por_informe = [m.group(2) for m in sorted(por_informe, key=lambda m: int(m.group(1)))]
por_commit = sorted(os.path.basename(l)[:-5] for l in git('show', '--name-only', '--diff-filter=A', '--format=', 'db70fe94').split()
                    if l.startswith('cuarentena/grove_high_output/') and l.endswith('.json'))
print('tanda 58 por .v58ext/informe_*.txt (%d): %s' % (len(por_informe), ' '.join(por_informe)))
print('tanda 58 por el commit db70fe94 (%d): misma lista: %s' % (len(por_commit), sorted(por_informe) == por_commit))
CIERRE = {'.v71ext': '6b2f721', '.v73ext': '70916d6'}
bit = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8')]
for k, i in enumerate(por_informe, 1):
    ruta = 'cuarentena/grove_high_output/%s.json' % i
    ins = 'cuarentena/_insertados/grove_high_output/%s.json' % i
    hoy = ruta if os.path.exists(ruta) else ins
    d = json.load(io.open(hoy, encoding='utf-8'))
    print()
    print('%d %s | sede hoy: %s | su fuente dice de si: %s' % (k, i, 'bandeja' if hoy == ruta else '_insertados',
          ', '.join('%s %s' % (f['clave'], f['fecha']) for f in d['fuentes'])))
    b = [p for p in ('.v71ext', '.v73ext') if os.path.exists('%s/barrido_%s.txt' % (p, i))]
    for p in b:
        ini = io.open('%s/barrido.log' % p, encoding='utf-8').readline().strip()
        print('  barrido %s: %s | %s' % (p, io.open('%s/barrido_%s.txt' % (p, i), encoding='utf-8').read().strip(), ini))
        v = json.load(io.open('%s/vecinos_%s.json' % (p, i), encoding='utf-8'))
        print('    vecinos: %s' % (', '.join('%s (%s)' % (x['id'], x['sede']) for x in v['vecinos']) or 'ninguno'))
        base = git('rev-parse', '%s:%s' % (CIERRE[p], ruta)).strip()
        print('    blob en %s (cierre de su vuelta de barrido): %s | blob hoy en HEAD: %s | igual: %s' % (
            CIERRE[p], base[:10], git('rev-parse', 'HEAD:' + hoy).strip()[:10], base == git('rev-parse', 'HEAD:' + hoy).strip()))
    if not b:
        print('  SIN BARRIDO en .v71ext ni .v73ext')
    for l in git('log', '--format=@%h %cI %s', '--numstat', '-M', '--', ruta, ins).splitlines():
        if l.startswith('@'):
            c = l[1:].split(' ', 2); print('  commit %s %s %s' % (c[0], c[1], c[2][:70]), end='')
        elif l.strip():
            a, r, _ = l.split('\t', 2); print(' | +%s -%s' % (a, r))
    n = [str(j) for j, x in enumerate(bit, 1) if x.get('candidato') == i]
    print('  lineas de la bitacora con ella de candidato: %d %s' % (len(n), ' '.join(n)))
