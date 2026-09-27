# -*- coding: utf-8 -*-
"""CASO POSITIVO DEL CERROJO, RE CORRIDO TRAS LA MUDANZA (D.52).

Dos procesos de verdad sobre el mismo dataset: el primero lo toma y lo retiene tres
segundos; el segundo arranca medio segundo despues y **tiene que esperar**, no fallar.
"""
import os
import subprocess
import sys
import tempfile
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
from src import cerrojo, comun  # noqa: E402

TALLER = tempfile.mkdtemp(prefix="cerrojo_d52_")
DATASET = os.path.join(TALLER, "nodos.jsonl")
comun.escribir_texto(DATASET, "")

HIJO = os.path.join(TALLER, "hijo.py")
comun.escribir_texto(HIJO, chr(10).join([
    "import os, sys, time",
    "sys.path.insert(0, %r)" % RAIZ,
    "from src import cerrojo",
    "arranque = time.time()",
    "with cerrojo.tomar(%r) as c:" % DATASET,
    "    print('TOMADO por pid %d tras esperar %.2f s' % (os.getpid(),"
    " time.time() - arranque))",
    "    time.sleep(float(sys.argv[1]))",
    ""]))

print("sede del cerrojo : %s" % comun.relativa(cerrojo.ruta_de(DATASET)))
print("dentro de dataset/ : %s"
      % ("SI" if os.sep + "dataset" + os.sep in cerrojo.ruta_de(DATASET) else "NO"))
print("")

primero = subprocess.Popen([sys.executable, HIJO, "3"], stdout=subprocess.PIPE)
time.sleep(0.5)
arranque = time.time()
segundo = subprocess.Popen([sys.executable, HIJO, "0"], stdout=subprocess.PIPE)
salida_1 = primero.communicate()[0].decode("utf-8", "replace").strip()
salida_2 = segundo.communicate()[0].decode("utf-8", "replace").strip()
espero = time.time() - arranque

print("proceso 1: %s" % salida_1)
print("proceso 2: %s" % salida_2)
print("")
print("el segundo tardo %.2f s en entrar, y el primero retuvo 3 s" % espero)
print("VEREDICTO: %s" % ("ESPERO, no fallo" if espero > 2.0 else "NO ESPERO: la guarda no muerde"))
print("cerrojo suelto al final: %s" % (not os.path.exists(cerrojo.ruta_de(DATASET))))
