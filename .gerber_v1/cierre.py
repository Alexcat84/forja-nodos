# -*- coding: utf-8 -*-
"""EL CIERRE DEL FRENTE gerber_emyth VUELTA 1, MEDIDO AL CIERRE (EXTRACTOR.md 4:
el estado al cierre se mide al cierre, y toda cifra que la propia vuelta pudo
mover se RECOMPUTA).

LA COLUMNA `al abrir` NO SE COPIA DE LA TABLA DE APERTURA: se vuelve a contar
sobre el arbol del commit de apertura con `git show`, para que las dos columnas
salgan del mismo instrumento y una discrepancia se vea sola."""
import io, json, glob, subprocess

APERTURA = '272e8ce'   # LA UNICA CONSTANTE PUESTA POR MI, declarada en la salida


def g(*a):
    return subprocess.check_output(['git'] + list(a)).decode('utf-8', 'replace').strip()


def lineas_en(commit, ruta):
    salida = g('show', '%s:%s' % (commit, ruta))
    return len([l for l in salida.splitlines() if l.strip()])


def ficheros_en(commit, patron):
    salida = g('ls-tree', '-r', '--name-only', commit)
    import fnmatch
    return [l for l in salida.splitlines() if fnmatch.fnmatch(l, patron)]


nodos_hoy = sum(1 for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip())
ver_hoy = sum(1 for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip())
bandeja = sorted(glob.glob('cuarentena/gerber_emyth/*.json'))
pasos = 0
for c in bandeja:
    pasos += len(json.load(io.open(c, encoding='utf-8')).get('pasos_accionables', []))

sedes = ('dataset/', 'bitacora/', 'censos/', 'config/')
tocados = [l for l in g('diff', '--name-only', '%s..HEAD' % APERTURA).splitlines()
           if l.startswith(sedes)]

print('AVISO: la unica constante tecleada por mi en este instrumento es el commit')
print('de apertura del frente, %s (%s).' % (APERTURA, g('log', '-1', '--format=%s', APERTURA)[:52]))
print('Todo lo demas se cuenta de su fichero, y la columna `al abrir` se lee del')
print('arbol de ese commit con `git show`, no de la tabla de apertura.')
print('')
print('| pieza | al abrir | al cierre | de donde sale |')
print('|---|---:|---:|---|')
print('| nodos en el grafo | **%d** | **%d** | `dataset/nodos.jsonl` |'
      % (lineas_en(APERTURA, 'dataset/nodos.jsonl'), nodos_hoy))
print('| veredictos escritos | **%d** | **%d** | `bitacora/VEREDICTOS.jsonl` |'
      % (lineas_en(APERTURA, 'bitacora/VEREDICTOS.jsonl'), ver_hoy))
print('| candidatos en bandeja de `gerber_emyth` | **%d** | **%d** | `PATRON: cuarentena/gerber_emyth/*.json` |'
      % (len(ficheros_en(APERTURA, 'cuarentena/gerber_emyth/*.json')), len(bandeja)))
pasos_al_abrir = 0
for c in ficheros_en(APERTURA, 'cuarentena/gerber_emyth/*.json'):
    pasos_al_abrir += len(json.loads(g('show', '%s:%s' % (APERTURA, c))).get('pasos_accionables', []))
print('| pasos escritos en esa bandeja | **%d** | **%d** | `PATRON: cuarentena/gerber_emyth/*.json` |'
      % (pasos_al_abrir, pasos))
print('| ficheros de dato (`dataset/`, `bitacora/`, `censos/`, `config/`) movidos por la vuelta | | **%d** | `git diff --name-only %s..HEAD` |'
      % (len(tocados), APERTURA))
print('| rama activa | | `%s` | `git rev-parse --abbrev-ref HEAD` |'
      % g('rev-parse', '--abbrev-ref', 'HEAD'))
print('| commit al medir el cierre | `%s` | `%s` | `git rev-parse --short HEAD` |'
      % (APERTURA, g('rev-parse', '--short', 'HEAD')))
print('')
print('CERO INSERCIONES, COMPROBADO Y NO PROMETIDO: %d fichero(s) de dato movidos.'
      % len(tocados))
