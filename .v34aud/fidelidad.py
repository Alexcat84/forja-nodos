# -*- coding: utf-8 -*-
"""MI RELECTURA DE FIDELIDAD (D.30), PASO A PASO CONTRA SU LINEA DEL LIBRO.

IMPRIME LA TABLA EN MARKDOWN para pegarla sin tocarla (D.41: una tabla que dice
venir de un instrumento tiene que poder ensenarlo).

CERO IDS TECLEADOS: la tanda sale de .v34aud/tanda.txt, que la escribio
cifras.py desde `git diff --name-only`. Los pasos se cuentan del dataset. LO
UNICO TECLEADO es MI veredicto por nodo, que es lo que esta relectura produce, y
va con el paso nombrado cuando no es cero.
"""
import io, json, re

# nodo -> (pasos que LEO como PUENTE, con su numero). Vacio = los 0 PUENTE.
MIS_PUENTES = {
    'practicar_franqueza_radical_jefe_propio': [13],
}

rutas = [l.strip() for l in io.open('.v34aud/tanda.txt', encoding='utf-8') if l.strip()]
nodos = {json.loads(l)['id']: json.loads(l)
         for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()}
filas = []
for r in rutas:
    i = json.load(io.open(r, encoding='utf-8'))['id']
    rt = nodos[i]['resumen_teorico']
    a = int(re.search(r'l[ií]neas? (\d+)', rt).group(1))
    b = int(re.search(r'l[ií]neas? \d+\s*(?:a|-|hasta)\s*(\d+)', rt).group(1))
    filas.append((a, b, i, len(nodos[i]['pasos_accionables'])))

print('| # | nodo | lineas del libro | pasos | **TRANSCRIPCION (yo)** | **PUENTE (yo)** | paso |')
print('|---:|---|---|---:|---:|---:|---|')
tp = tt = tb = 0
for k, (a, b, i, p) in enumerate(sorted(filas), 1):
    pu = MIS_PUENTES.get(i, [])
    tp += p; tb += len(pu); tt += p - len(pu)
    print('| %d | `%s` | L%d a L%d | %d | %d | **%d** | %s |'
          % (k, i, a, b, p, p - len(pu), len(pu),
             ', '.join('P%d' % x for x in pu) if pu else '.'))
print('| | **cap_09, total** | **L%d a L%d** | **%d** | **%d** | **%d** | |'
      % (min(f[0] for f in filas), max(f[1] for f in filas), tp, tt, tb))
print()
print('PASOS INVENTADOS POR CAPITULO (AUDITOR_FORJA.md 8), leido por mi:')
print('  cap_09 : %d de %d = %.2f por ciento' % (tb, tp, 100.0 * tb / tp))
print('  tope de la regla 8.1: 10 por ciento')
