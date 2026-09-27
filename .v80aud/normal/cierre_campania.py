"""ACTA 79: las tres cosas medidas que PARALELO.md 4.c pide al PARA_ALEXIS de MUNDO 11 COMPLETO, y lo que queda esperando al
fundador. (1) el censo por libro, por la clave de la primera fuente de cada nodo de dataset/nodos.jsonl, con su suma; (2) las
aristas entre libros, contadas y nombradas, y cuantas viven por los dos lados; (3) los tres libros del corte, con su ficha de
fuentes/FUENTES_CANONICAS.json, sus capitulos en fuentes/<clave>/ y su motivo de config/frentes.json. Y la cola de doctrina y las
deudas esperando, contadas. Solo lee."""
import json, glob, os, collections, subprocess

N = [json.loads(l) for l in open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
libro = {n['id']: n['fuentes'][0] if isinstance(n['fuentes'][0], str) else n['fuentes'][0].get('clave') for n in N}
c = collections.Counter(libro.values())
print('(1) CENSO POR LIBRO (clave de la primera fuente de cada nodo de dataset/nodos.jsonl)')
for k, v in c.most_common():
    print('      %-32s %4d' % (k, v))
print('      %-32s %4d  (filas del fichero: %d) | nodos con mas de una fuente: %d' % (
    'SUMA', sum(c.values()), len(N), sum(1 for n in N if len(n['fuentes']) > 1)))

sig = {(n['id'], h) for n in N for h in n.get('nodos_siguientes', [])}
pre = {(m, n['id']) for n in N for m in n.get('nodos_previos', [])}
todas = sig | pre
entre = sorted((a, b) for a, b in todas if libro.get(a) != libro.get(b))
print('(2) ARISTAS: %d | escritas en la madre y en el hijo: %d | solo en un lado: %d | entre libros distintos: %d | dentro de un libro: %d | suma: %d' % (
    len(todas), len(sig & pre), len(todas - (sig & pre)), len(entre), len(todas) - len(entre), len(entre) + len(todas) - len(entre)))
for a, b in entre:
    print('      %s (%s) > %s (%s)' % (a, libro[a], b, libro[b]))

F = json.load(open('fuentes/FUENTES_CANONICAS.json', encoding='utf-8'))
C = json.load(open('config/frentes.json', encoding='utf-8'))
orden = None
for v in C.values():
    if isinstance(v, dict):
        for kk, vv in v.items():
            if isinstance(vv, dict) and 'bernerslee_bananas' in vv:
                orden = vv
print('(3) LOS TRES DEL CORTE, EN BANDEJA SIN EXTRAER')
for k in ('bernerslee_bananas', 'openstax_business_ethics', 'openstax_org_behavior'):
    f = F[k]
    caps = len(glob.glob(os.path.join('fuentes', k, 'cap_*')))
    en_grafo = c.get(k, 0)
    cuar = len(glob.glob(os.path.join('cuarentena', k, '*.json')))
    print('      %s | %s, %s, %s | capitulos en fuentes/%s/: %d | nodos en el grafo: %d | fichas en cuarentena: %d' % (
        k, f['titulo_completo'], f['autor'], f['anio'], k, caps, en_grafo, cuar))
    print('        prioridad %s, fuera de campania: %s | motivo: %s' % (orden[k]['prioridad'], orden[k]['fuera_de_campania'], orden[k]['motivo']))

cola = C.get('cola_de_doctrina', {}).get('preguntas', [])
print('COLA DE DOCTRINA (config/frentes.json): %d preguntas | %s | suma: %d' % (
    len(cola), dict(collections.Counter('bloquea' if p.get('bloquea') else 'no bloquea' for p in cola)), len(cola)))
d = subprocess.run(['python', 'scripts/deuda.py'], capture_output=True, text=True, encoding='utf-8').stdout
print('DEUDAS (scripts/deuda.py): %s' % [l.strip() for l in d.split('\n') if 'pendientes:' in l][0])
