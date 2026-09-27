import io, re
CAP07 = ['.v30e/ins_%s_%s.txt' % p for p in [
    ('01', 'parar_debate'), ('02', 'fijar_fecha'), ('03', 'repartir'),
    ('04', 'pedir_hechos'), ('05', 'persuadir'), ('06', 'credibilidad'),
    ('07', 'compartir'), ('08', 'minimizar'), ('09', 'proteger'),
    ('10', 'mantener'), ('11', 'reservar'), ('12', 'cuidarse')]]
suma = []
for ruta in CAP07:
    t = io.open(ruta, encoding='utf-8').read()
    suma.append(int(re.search(r'VECINOS POR ENCIMA DE UMBRAL: (\d+)', t).group(1)))
print('LOS 12 DE cap_07, VECINOS LEVANTADOS EN LA INSERCION DE VERDAD')
print('  por candidato, en el orden del libro: %s' % ', '.join(str(n) for n in suma))
print('  candidatos: %d' % len(suma))
print('  SUMA: %d' % sum(suma))
print('  lo que el barrido ciego del auditor publico (APERTURA_CIEGA.md 77): 77')
print('  DIFERENCIA: %d' % (sum(suma) - 77))
