import io, sys
L = io.open('fuentes/scott_radical_candor/cap_07.md', encoding='utf-8').read().split('\n')
MAP = [(chr(0x2014), '-'), (chr(0x2013), '-'), (chr(0x2019), "'"), (chr(0x2018), "'"),
       (chr(0x201c), '"'), (chr(0x201d), '"'), (chr(0x2026), '...'), (chr(0xa0), ' ')]
def limpia(t):
    for k, v in MAP:
        t = t.replace(k, v)
    return t.replace('|', '/')
def cita(n, ancla, largo):
    t = limpia(L[n - 1])
    i = t.find(ancla)
    assert i >= 0, (n, ancla)
    pre = '...' if i > 0 else ''
    frag = t[i:i + largo]
    post = '...' if i + largo < len(t) else ''
    return '%d: %s%s%s' % (n, pre, frag, post)
out = io.open(sys.argv[1], 'w', encoding='utf-8', newline='\n')
def fila(rot, n, ancla, largo, ver):
    out.write('| %s | `%s` | %s |\n' % (rot, cita(n, ancla, largo), ver))
out.write('| paso | la salida de `.v30e/cita.py` sobre el libro, pegada | veredicto |\n')
out.write('|---|---|---|\n')
fila('`proteger_tiempo_equipo_jefe` paso `2`: *escucha, asegurate de haberlo entendido, y desactiva las situaciones*',
     377, 'listen, make sure', 112, '**TRANSCRIPCION**')
fila('`mantener_manos_trabajo_real_equipo` paso `8`: *la rueda entera se para si no entiendes a fondo la cosa que tu equipo esta intentando hacer*',
     383, 'The GSD wheel will grind', 104, '**TRANSCRIPCION**')
fila('`minimizar_impuesto_colaboracion_equipo` paso `4`: las tres cosas del equilibrio',
     373, 'Here are the three', 152, '**TRANSCRIPCION**, y ademas es la cabeza de una serie `D.37`')
fila('`cuidarse_agotamiento_centro_rueda` paso `7`: *bloquea en tu calendario tiempo de pensar todos los dias*',
     417, 'ability to stay centered', 92, '**TRANSCRIPCION**')
fila('`repartir_decision_cercanos_hechos` paso `10`: las tres cosas del diagnostico',
     283, '1) his decisions', 168, '**TRANSCRIPCION**')
out.close()
