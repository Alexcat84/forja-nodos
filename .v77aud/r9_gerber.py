# -*- coding: utf-8 -*-
"""Fase ciega de la 77 (copia libre de .v75aud/r9_grove.py con la tanda de la 76): el mismo grep R9 de
.v75aud/cap13_despues.py (el patron se importa de alli, no se copia) sobre los 176 pasos de las 22 de Gerber que
entraron, leidos del grafo, cada coincidencia con el capitulo y la linea del libro que le da MI fila sellada de la 76
(.v76aud/fidelidad.tsv), y el tramo LITERAL del libro que sostiene la clausula, buscado con un patron que escribo yo
leyendo la linea (TRAMO; 'NADA' si no lo encuentra, y la fila seria P por R9; apostrofo curvo a recto). Reparte con su
suma (R7). NO imprime ninguna clave de relacion (R6). Solo lee."""
import io, re, json, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
src = io.open('.v75aud/cap13_despues.py', encoding='utf-8').read()
PAT = re.compile(eval(re.search(r'PAT = re\.compile\((r".*?"), re\.I\)', src).group(1)), re.I)
M = dict(((f[0], int(f[1])), (f[3], f[4])) for f in (l.rstrip('\n').split('\t') for l in list(io.open('.v76aud/fidelidad.tsv', encoding='utf-8'))[1:] if l.strip()))
las22 = io.open('.v76aud/las22.txt', encoding='utf-8').read().split()
G = dict((d['id'], d) for d in map(json.loads, io.open('dataset/nodos.jsonl', encoding='utf-8')) if d['id'] in las22)
TRAMO = {('aplicar_ocho_reglas_juego_personas', 9, 'peor que'): r"There's nothing worse than pretending to play a game",
         ('cambiar_saludo_cliente_dos_ramas', 1, 'prueba'): r"Instead of asking, .Hi, may I help you\?. try",
         ('dar_valor_constante_cuatro_publicos', 2, 'no solo'): r"would not only provide consistent value",
         ('dar_valor_constante_cuatro_publicos', 2, 'sino'): r"but would provide it beyond their wildest expectations",
         ('dictar_ritmo_crecimiento_preguntas_escritas', 8, 'mejor que'): r"any plan is better than no plan",
         ('fingir_prototipo_cinco_mil_replicas', 2, 'sino'): r"Not almost like it, but just like it",
         ('medir_sistema_venta_trece_indicadores_benchmark', 14, 'datos'): r"as a database on your computer",
         ('trazar_modelo_negocio_cliente_primero', 8, 'sino'): r"does not start with a picture of the business to be created but of the customer",
         ('trazar_modelo_negocio_cliente_primero', 8, 'a diferencia de'): r"Thus, the Entrepreneurial Model does not start with",
         ('unificar_color_forma_vestuario_modelo', 1, 'estudios'): r"Marketing studies tell us"}
c = collections.Counter(); t = collections.Counter(); n = 0
for i in las22:
    for k, p in enumerate(G[i]['pasos_accionables'], 1):
        n += 1
        for m in PAT.finditer(p):
            cap, L = M[(i, k)]; c[cap] += 1
            linea = io.open('fuentes/gerber_emyth/%s.md' % cap, encoding='utf-8').read().split('\n')[int(L[1:]) - 1].replace(chr(0x2019), "'")
            h = re.search(TRAMO.get((i, k, m.group(0).lower()), '(?!x)x'), linea); t['tramo hallado' if h else 'NADA'] += 1
            print('  %s %s %s paso %d [%s] | el libro: %s' % (cap, L, i[:30], k, m.group(0), h.group(0) if h else 'NADA'))
print('pasos leidos: %d | coincidencias por capitulo: %s | suma: %d' % (n, dict(c), sum(c.values())))
print('coincidencias con su tramo literal: %s | suma: %d' % (dict(t), sum(t.values())))
