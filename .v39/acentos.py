# -*- coding: utf-8 -*-
"""LOS CARACTERES ACENTUADOS VIVOS DE dataset/nodos.jsonl, contados hoy.

`enie` NO es acento: es una letra del castellano. Lo que la vuelta 38 llamo
"caracter acentuado" son las vocales con tilde aguda y con dieresis, y esta
cuenta las separa para que la cifra se pueda recontar.
"""
import collections
import io
import json
import unicodedata

MARCAS_DE_ACENTO = (u"́", u"̈")

cuenta = collections.Counter()
acentuados = []
n = 0
for linea in io.open("dataset/nodos.jsonl", encoding="utf-8"):
    if not linea.strip():
        continue
    n += 1
    d = json.loads(linea)
    crudo = json.dumps(d, ensure_ascii=False)
    for i, ch in enumerate(crudo):
        if ord(ch) < 128:
            continue
        cuenta[ch] += 1
        descompuesto = unicodedata.normalize("NFD", ch)
        if len(descompuesto) > 1 and descompuesto[1] in MARCAS_DE_ACENTO:
            acentuados.append((d["id"], ch,
                               crudo[max(0, i - 26):i + 12].replace("\n", " ")))

print("nodos en dataset/nodos.jsonl                     : %d" % n)
print("caracteres NO ASCII, todos                       : %d" % sum(cuenta.values()))
for ch, c in sorted(cuenta.items()):
    print("  U+%04X %-36s x%d" % (ord(ch), unicodedata.name(ch, "?"), c))
print("caracteres ACENTUADOS (tilde aguda o dieresis)   : %d" % len(acentuados))
for ident, ch, ctx in acentuados:
    print("  %-46s %s   ...%s..." % (ident[:46], ch, ctx))
