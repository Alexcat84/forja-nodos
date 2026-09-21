#!/bin/sh
# Que ficheros de cuarentena NACEN en los commits de esta vuelta (desde la apertura
# del arnes, 327d969). Solo nombres: no abro REPORTE.md.
git log --diff-filter=A --name-only --format='' 327d969..HEAD -- cuarentena/ | sort -u
