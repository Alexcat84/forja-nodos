#!/bin/sh
# Las fichas de cuarentena NACIDAS en el commit de cabeza (la vuelta que audito).
# No leo REPORTE.md: la lista sale de git, que no es ninguno de los cuatro retirados.
git show --name-status --diff-filter=A HEAD | awk '$2 ~ /^cuarentena\// {print $2}'
