# -*- coding: utf-8 -*-
# COBERTURA DE LA FRONTERA: que lineas de cuerpo de un capitulo quedan SIN que
# ningun candidato de la bandeja las reclame. Los tramos NO se teclean: se leen
# de los rangos L<n> a L<m> que cada resumen_teorico declara para ESE capitulo.
import io, json, glob, os, re, sys

libro = 'grove_high_output'
cap = sys.argv[1]
ruta = 'fuentes/%s/%s.md' % (libro, cap)
lineas = io.open(ruta, encoding='utf-8').read().split('\n')

# el cuerpo empieza tras el segundo separador --- del frontmatter
cierres = [n for n, l in enumerate(lineas, 1) if l.strip() == '---']
primera = cierres[1] + 1
ultima = len(lineas)
while ultima > primera and not lineas[ultima - 1].strip():
    ultima -= 1

RANGO = re.compile(r'L(\d+)\s+a\s+L(\d+)')
SUELTA = re.compile(r'\bL(\d+)\b')
reclamadas = {}
for p in sorted(glob.glob('cuarentena/%s/*.json' % libro)):
    d = json.load(io.open(p, encoding='utf-8'))
    texto = d.get('resumen_teorico', '')
    if ('fuentes/%s/%s.md' % (libro, cap)) not in texto:
        continue
    for m in RANGO.finditer(texto):
        for n in range(int(m.group(1)), int(m.group(2)) + 1):
            reclamadas.setdefault(n, set()).add(d['id'])
    for m in SUELTA.finditer(texto):
        reclamadas.setdefault(int(m.group(1)), set()).add(d['id'])

print('%s  cuerpo L%d a L%d' % (ruta, primera, ultima))
print('lineas de cuerpo                       : %d' % (ultima - primera + 1))
con_texto = [n for n in range(primera, ultima + 1) if lineas[n - 1].strip()]
print('lineas de cuerpo CON texto             : %d' % len(con_texto))
sin_reclamar = [n for n in con_texto if n not in reclamadas]
print('lineas con texto que NINGUN candidato cita: %d' % len(sin_reclamar))
for n in sin_reclamar:
    t = lineas[n - 1].strip()
    print('  L%-4d %d palabras | %s' % (n, len(t.split()), t[:110]))
