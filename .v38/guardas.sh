#!/bin/sh
# Las tres guardas del cierre de la vuelta 38, con su salida pegada (EXTRACTOR.md 6).
cd /c/Users/AlexDesk/Documents/forja-nodos
{
  echo '$ python forja.py gate'
  python forja.py gate
  echo
  echo '$ python forja.py guiones'
  python forja.py guiones
  echo
  echo '$ python tests/test_aceptacion.py'
  python tests/test_aceptacion.py
} > .v38/guardas_cierre.txt 2>&1 < /dev/null
tail -4 .v38/guardas_cierre.txt
