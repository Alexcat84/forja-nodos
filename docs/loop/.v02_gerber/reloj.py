# reloj.py: la duracion de una corrida, de los dos ficheros de marca que la envuelven.
# Sin constantes tecleadas: las dos horas se leen del disco.
import datetime, io, sys
F = "%Y-%m-%d %H:%M:%S"
a = datetime.datetime.strptime(io.open(sys.argv[1]).read().strip(), F)
b = datetime.datetime.strptime(io.open(sys.argv[2]).read().strip(), F)
d = b - a
print("arranco  : %s" % a.strftime(F))
print("termino  : %s" % b.strftime(F))
print("duracion : %d min %d s" % (d.seconds // 60, d.seconds % 60))
