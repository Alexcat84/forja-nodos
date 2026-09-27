# -*- coding: utf-8 -*-
"""La banda de una tasa de 0 rojas sobre n corridas: cota superior exacta de
Clopper-Pearson al 95 por ciento, que para 0 exitos es 1 - alfa**(1/n).
Una tasa sin banda es media cifra (AUDITOR_FORJA.md 7)."""
for n in (6, 20, 26):
    print("0 rojas de %2d corridas : tasa 0,0 por ciento ; cota superior al 95 por ciento = %.1f por ciento"
          % (n, 100*(1-0.05**(1.0/n))))
