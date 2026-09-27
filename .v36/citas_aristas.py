# -*- coding: utf-8 -*-
"""Las lineas del libro que sostienen cada arista declarada por lectura, con la
salida literal pegada al lado (D.35). Los fragmentos se recortan y se dice."""

CASOS = [
 ("cap_10", 43,  "a succession of three forty-five-minute conversations",
  "D.37 serie 1: la cuenta y las partes"),
 ("cap_10", 173, "if you do three things",
  "D.37 serie 2: la cuenta de las tres del despido"),
 ("cap_10", 111, "initiate the process of firing these people",
  "D.29: el plan anual NOMBRA el despido sin desplegarlo"),
 ("cap_08", 95,  "career conversations",
  "D.29: la remision de cap_08 al capitulo siete"),
]

print("| que sostiene | fichero | linea | la salida, pegada |")
print("|---|---|---:|---|")
for cap, n, frag, que in CASOS:
    ruta = "fuentes/scott_radical_candor/%s.md" % cap
    texto = open(ruta, encoding="utf-8").read().split("\n")[n - 1]
    i = texto.find(frag)
    trozo = texto[max(0, i - 50):i + len(frag) + 50] if i >= 0 else "NO ENCONTRADO"
    for codigo, llano in ((8212, ", "), (8220, chr(34)), (8221, chr(34)),
                          (8217, chr(39)), (8211, ", ")):
        trozo = trozo.replace(chr(codigo), llano)
    print("| %s | `%s.md` | L%d | `%d: ...%s...` |" % (que, cap, n, n, trozo))
