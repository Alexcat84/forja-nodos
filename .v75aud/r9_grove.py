# -*- coding: utf-8 -*-
"""Fase ciega de la 75: el mismo grep R9 de .v75aud/cap13_despues.py (el patron se importa de alli, no se copia) sobre los
42 pasos de las 7 de Grove que entraron, leidos del grafo, cada coincidencia con la linea del libro que le da MI fila
sellada de la 73 (.v73aud/fidelidad_fuente.txt) y su capitulo (.v72aud/normal/siete.txt), y el tramo LITERAL del libro que sostiene la clausula, buscado con un patron que
escribo yo leyendo la linea (TRAMO; 'NADA' si no lo encuentra, y la fila seria P por R9; apostrofo curvo a recto). Reparte con su suma (R7). NO
imprime ninguna clave de relacion (R6). Solo lee."""
import io, re, json, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
src = io.open('.v75aud/cap13_despues.py', encoding='utf-8').read()
PAT = re.compile(eval(re.search(r'PAT = re\.compile\((r".*?"), re\.I\)', src).group(1)), re.I)
los7 = [l.strip() for l in io.open('.v73aud/los7.txt', encoding='utf-8') if l.strip()]
cap = dict((l.split()[1], l.split()[0]) for l in io.open('.v72aud/normal/siete.txt', encoding='utf-8') if l.startswith('cap_'))
M = dict(((f[0], int(f[1])), f[3]) for f in (l.rstrip('\n').split('|', 4) for l in io.open('.v73aud/fidelidad_fuente.txt', encoding='utf-8') if l.strip()))
G = dict((d['id'], d) for d in map(json.loads, io.open('dataset/nodos.jsonl', encoding='utf-8')) if d['id'] in los7)
TRAMO = {('gestionar_retencion_subordinado_valioso_renuncia', 6): r"commitments he has made to the people he has been working with daily are far stronger than one made to a casual new acquaintance",
         ('reciclar_empleado_ascendido_mas_alla_capacidad', 2): r"take forthright and deliberate steps",
         ('responder_primer_aviso_renuncia_subordinado', 6): r"Don't try to change his mind at this point, but buy time"}
c = collections.Counter(); t = collections.Counter(); n = 0
for i in los7:
    for k, p in enumerate(G[i]['pasos_accionables'], 1):
        n += 1
        for m in PAT.finditer(p):
            c[cap[i]] += 1; a = max(0, m.start() - 60)
            print('  %s %s paso %d %s: ...%s...' % (cap[i], i[:26], k, M[(i, k)], p[a:m.end() + 50]))
            linea = io.open('fuentes/grove_high_output/%s.md' % cap[i], encoding='utf-8').read().split(chr(10))[int(M[(i, k)][1:]) - 1].replace(chr(0x2019), "'")
            h = re.search(TRAMO.get((i, k), '(?!x)x'), linea); t['tramo hallado' if h else 'NADA'] += 1
            print('      el libro: %s' % (h.group(0) if h else 'NADA'))
print('pasos leidos: %d | coincidencias por capitulo: %s | suma: %d' % (n, dict(c), sum(c.values())))
print('coincidencias con su tramo literal: %s | suma: %d' % (dict(t), sum(t.values())))
