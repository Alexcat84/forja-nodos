#!/bin/sh
# LAS TRES GUARDAS DEL CIERRE, con su salida pegada (EXTRACTOR.md 6).
cd /c/Users/AlexDesk/Documents/forja-nodos
{
  echo '    $ python forja.py gate'
  python forja.py gate 2>&1
  echo ''
  echo '    $ python forja.py guiones'
  python forja.py guiones 2>&1
  echo ''
  echo '    $ python tests/test_aceptacion.py'
  python tests/test_aceptacion.py 2>&1 | tail -6
} > .v40/guardas_cierre.txt 2>&1
cat .v40/guardas_cierre.txt
