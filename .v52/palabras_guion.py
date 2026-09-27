ln = open('fuentes/grove_high_output/cap_05.md', encoding='utf-8').read().split('\n')[54]
w = ln.split()
g = [x for x in w if '-' in x]
print("$ python .v52/palabras_guion.py   sobre sed -n '55p' de cap_05.md")
print("  palabras tal como las cuenta wc -w      : %d" % len(w))
print("  piezas unidas por guion corto           : %d  %s" % (len(g), " ".join(g)))
print("  palabras si cada guion corto partiera   : %d" % (len(w) + sum(x.count('-') for x in g)))
