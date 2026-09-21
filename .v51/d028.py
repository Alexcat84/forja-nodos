import sys, pathlib
sys.path.insert(0, ".")
from src import tablero
b = "cuarentena/grove_high_output"
caps = sorted(set(tablero._capitulos_de_bandeja(b)) | set(tablero._capitulos_de_bandeja("cuarentena/_insertados/grove_high_output")))
print("capitulos_minados que el tablero publicara : %s" % caps)
print("ultimo minado, o sea desde donde mandara continuar : %s" % caps[-1])
print("nodos que la frontera LL.4.b da a cap_05 : 26")
print("nodos que cap_05 tiene escritos hoy      : 6")
print("o sea cap_05 cuenta como MINADO con el   : 23 por ciento de sus nodos")
