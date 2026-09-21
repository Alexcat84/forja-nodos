# -*- coding: utf-8 -*-
"""Cosecha 7.C: toda guarda que el reporte declare mordiendo se re corre POR
MUTACION. La vuelta 59 dice en SS.5.c que D.59 le tumbo la celda `P2` de
`resolver_dudas` porque la palabra 'variacion' caia a menos de 40 caracteres
de la cita `L171`, y que la reescribio sin la palabra. Le devuelvo la palabra
y compruebo que la guarda CAE en esa misma linea."""
import io, sys
sys.path.insert(0, 'scripts')
import tallar_reporte as t

texto = io.open('docs/loop/REPORTE.md', encoding='utf-8').read()
print('TAL CUAL (debe ser verde) :', t.cifras_derivadas_sueltas(texto=texto))

ACTUAL = next(l for l in texto.split(chr(10))
              if l.startswith('| `P2` | cambia la pregunta si no esta sacando'))
print('celda viva  :', ACTUAL[:120])
MUTADA = ACTUAL.replace('cambia la pregunta si no esta sacando respuestas',
                        'introduce alguna variacion si no saca respuestas')
print('celda mutada:', MUTADA[:120])

hall = t.cifras_derivadas_sueltas(texto=texto.replace(ACTUAL, MUTADA))
print('MUTADO (debe MORDER)      :', len(hall), 'hallazgo(s)')
for h in hall:
    print('   linea', h['linea'], '|', h['frase'][:130])
