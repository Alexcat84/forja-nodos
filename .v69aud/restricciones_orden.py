# Fase ciega de la 69 (copia de .v68aud/restricciones_orden.py, con R7: el reparto de las restricciones por clase lleva su suma): las restricciones de orden que MI lectura pone a la insercion de cap_05 y cap_06, escritas antes de
# ver el orden del extractor. (a) madre antes que hijo (D.29, D.36) por mis CONTINUA de .v68aud/mis_clases.tsv y
# mis SOSTENGO de .v68aud/aristas_lectura.tsv con los dos extremos en la bandeja; (b) D.36: par de la tanda que el
# barrido levanta desde un solo lado; se publica aparte y NO obliga, porque la aduana de insertar mide grafo mas
# bandejas (D.38.5) y el par se lee entre en el orden que entre. Y cuantas viola el orden del
# libro (.v66aud/cola_grove.txt filas 23 a 42, que es .v68aud/los20.txt, que es orden de pieza y no un orden de insercion). Solo lee.
import io, re, sys
sys.stdout.reconfigure(encoding="utf-8")
tanda = [l.strip() for l in io.open('.v68aud/los20.txt', encoding='utf-8') if l.strip()]
dentro = set(tanda); antes = []
for f in [l.rstrip('\n').split('\t') for l in io.open('.v68aud/mis_clases.tsv', encoding='utf-8')][1:]:
    if f[2] == 'CONTINUA' and f[0] in dentro and f[1] in dentro:
        hijo = f[1] if f[3] == f[0] else f[0]
        antes.append((f[3], hijo, 'CONTINUA'))
for f in [l.rstrip('\n').split('\t') for l in io.open('.v68aud/aristas_lectura.tsv', encoding='utf-8')][1:]:
    if f[2].startswith('SOSTENGO') and f[0] in dentro and f[1] in dentro:
        antes.append((f[0], f[1], 'arista por lectura'))
for l in io.open('.v68aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +~ (\S+) +tanda-tanda solo (\S+)', l)
    if m:
        a, b, lado = m.groups(); otro = b if lado == a else a
        antes.append((otro, lado, 'D.36, solo lo levanta %s' % lado))
pos = dict((i, n) for n, i in enumerate(tanda))
print('restricciones: %d' % len(antes))
for a, b, por in antes:
    print('  %-52s antes que %-56s %-22s %s' % (a, b, por, 'el orden del libro la cumple' if pos[a] < pos[b] else 'EL ORDEN DEL LIBRO LA VIOLA'))
oblig = [r for r in antes if not r[2].startswith('D.36')]
print('restricciones: %d | por clase: %s | suma: %d' % (len(antes), {'obligan (madre antes que hijo)': len(oblig), 'D.36 de un solo lado, informativas': len(antes) - len(oblig)}, len(antes)))
print('de las que obligan, violadas por el orden del libro: %d' % sum(pos[a] > pos[b] for a, b, _ in oblig))
print('con madre usar_tres_clases_reunion_proceso: %d' % sum(a == 'usar_tres_clases_reunion_proceso' for a, b, _ in antes))
print('ultimas dos del orden del libro: %s' % tanda[-2:])
