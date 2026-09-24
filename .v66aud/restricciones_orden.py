# Fase ciega de la 66: las restricciones de orden que MI lectura pone a la insercion de cap_04, escritas antes de
# ver el orden del extractor. (a) madre antes que hijo (D.29, D.36) por mis CONTINUA de .v66aud/mis_clases.tsv y
# mis SOSTENGO de .v66aud/aristas_lectura.tsv con los dos extremos en la bandeja; (b) D.36: par de cap_04 que el
# barrido levanta desde un solo lado; se publica aparte y NO obliga, porque la aduana de insertar mide grafo mas
# bandejas (D.38.5) y el par se lee entre en el orden que entre. Y cuantas viola el orden del
# libro (.v66aud/cola_grove.txt, que es orden de pieza y no un orden de insercion). Solo lee.
import io, re, sys
sys.stdout.reconfigure(encoding="utf-8")
cap04 = [l.strip() for l in io.open('.v66aud/los22_cap04.txt', encoding='utf-8') if l.strip()]
dentro = set(cap04); antes = []
for f in [l.rstrip('\n').split('\t') for l in io.open('.v66aud/mis_clases.tsv', encoding='utf-8')][1:]:
    if f[2] == 'CONTINUA' and f[0] in dentro and f[1] in dentro:
        hijo = f[1] if f[3] == f[0] else f[0]
        antes.append((f[3], hijo, 'CONTINUA'))
for f in [l.rstrip('\n').split('\t') for l in io.open('.v66aud/aristas_lectura.tsv', encoding='utf-8')][1:]:
    if f[2].startswith('SOSTENGO') and f[0] in dentro and f[1] in dentro:
        antes.append((f[0], f[1], 'arista por lectura'))
for l in io.open('.v66aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +~ (\S+) +cap04-cap04 solo (\S+)', l)
    if m:
        a, b, lado = m.groups(); otro = b if lado == a else a
        antes.append((otro, lado, 'D.36, solo lo levanta %s' % lado))
pos = dict((i, n) for n, i in enumerate(cap04))
print('restricciones: %d' % len(antes))
for a, b, por in antes:
    print('  %-52s antes que %-56s %-22s %s' % (a, b, por, 'el orden del libro la cumple' if pos[a] < pos[b] else 'EL ORDEN DEL LIBRO LA VIOLA'))
oblig = [r for r in antes if not r[2].startswith('D.36')]
print('que obligan (madre antes que hijo): %d | violadas por el orden del libro: %d' % (len(oblig), sum(pos[a] > pos[b] for a, b, _ in oblig)))
print('D.36 de un solo lado, informativas: %d' % (len(antes) - len(oblig)))
print('ultimas dos del orden del libro: %s' % cap04[-2:])
