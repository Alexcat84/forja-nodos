import sys, io
a, b = int(sys.argv[1]), int(sys.argv[2])
L = io.open('fuentes/scott_radical_candor/cap_07.md', encoding='utf-8').read().split('\n')
for n in range(a, b + 1):
    t = L[n - 1]
    if t.strip():
        print('L%d: %s' % (n, t))
