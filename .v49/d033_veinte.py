# -*- coding: utf-8 -*-
"""d033: la tasa de la corrida intermitente. Corre el caso AISLADO 20 veces y publica
su codigo de salida. NO TOCA tests/: solo corre lo que ya esta escrito (D.45).
Si alguna sale ROJA, la traza entera se guarda en .v49/d033_traza_<n>.txt."""
import subprocess, sys, time, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
CASO = "tests.test_aceptacion.PruebaE.test_e_guion_largo_rompe_el_hook"
N = 20
rojas = []
relojes = []
print("$ python -m unittest %s      (x%d, una detras de otra, arbol quieto)" % (CASO, N))
print()
print("  #   codigo   segundos   veredicto")
print("  " + "-" * 44)
entorno = dict(os.environ)
entorno["PYTHONIOENCODING"] = "utf-8"
t_total = time.time()
for i in range(1, N + 1):
    t0 = time.time()
    p = subprocess.Popen([sys.executable, "-m", "unittest", CASO],
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=entorno)
    crudo = p.communicate()[0].decode("utf-8", "replace")
    dt = time.time() - t0
    relojes.append(dt)
    if p.returncode != 0:
        rojas.append(i)
        open(".v49/d033_traza_%02d.txt" % i, "w", encoding="utf-8").write(crudo)
    print("  %2d   %d        %6.1f     %s%s"
          % (i, p.returncode, dt, "OK" if p.returncode == 0 else "ROJA",
             "" if p.returncode == 0 else "  (traza en .v49/d033_traza_%02d.txt)" % i))
total = time.time() - t_total
print()
print("corridas            : %d" % N)
print("rojas               : %d   %s" % (len(rojas), rojas if rojas else "(ninguna)"))
print("tasa de roja        : %.4f  (%d de %d)" % (len(rojas) / float(N), len(rojas), N))
# Banda de Wilson al 95 por ciento: una tasa sin banda es media cifra (manual principio 5).
z = 1.96
ph = len(rojas) / float(N)
den = 1 + z * z / N
centro = (ph + z * z / (2 * N)) / den
medio = z * ((ph * (1 - ph) / N + z * z / (4.0 * N * N)) ** 0.5) / den
print("banda al 95 por ciento (Wilson) : de %.4f a %.4f" % (max(0.0, centro - medio),
                                                            min(1.0, centro + medio)))
print()
print("reloj por corrida   : menor %.1f s, media %.1f s, mayor %.1f s"
      % (min(relojes), sum(relojes) / len(relojes), max(relojes)))
print("reloj de las %d      : %.1f s" % (N, total))
