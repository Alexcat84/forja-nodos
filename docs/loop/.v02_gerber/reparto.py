# reparto.py: reparte los vecinos que levanto la aduana en DENTRO de la bandeja de este
# frente y FUERA de ella. Sin listas tecleadas: la bandeja se lee del disco y las lineas
# de vecino se leen del informe que la aduana acaba de escribir.
import io, re, sys, pathlib
informe = io.open(sys.argv[1], encoding="utf-8").read().splitlines()
bandeja = set(p.stem for p in pathlib.Path(sys.argv[2]).glob("*.json"))
dentro = fuera = 0
ajenos = []
sin_vecino = []
actual = None
tiene = set()
for l in informe:
    m = re.match(r"\[(\w+)\] (\S+)", l.strip())
    if m:
        actual = m.group(2)
        if m.group(1) == "ENTRARIA":
            sin_vecino.append(actual)
        continue
    m = re.match(r"vecino (\S+)", l.strip())
    if m:
        v = m.group(1)
        tiene.add(actual)
        if v in bandeja:
            dentro += 1
        else:
            fuera += 1
            ajenos.append(v)
print("vecinos DENTRO de la bandeja de este frente : %d" % dentro)
print("vecinos FUERA de la bandeja de este frente  : %d" % fuera)
print("vecinos en total                            : %d" % (dentro + fuera))
print("candidatos SIN NI UN VECINO                 : %d" % len(sin_vecino))
for c in sin_vecino:
    print("    %s" % c)
print("ids ajenos distintos                        : %d" % len(set(ajenos)))
for a in sorted(set(ajenos)):
    print("    %s" % a)
