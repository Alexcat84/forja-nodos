#!/bin/bash
# ACTA 75: las guardas del turno normal, en serie, cada salida a su fichero con su rc
cd "$(dirname "$0")/../.."
N=.v76aud/normal
python forja.py gate > $N/gate.txt 2>&1; echo "rc=$?" >> $N/gate.txt
python forja.py guiones > $N/guiones.txt 2>&1; echo "rc=$?" >> $N/guiones.txt
python forja.py resolutor > $N/resolutor.txt 2>&1; echo "rc=$?" >> $N/resolutor.txt
date "+INICIO SUITE %H:%M:%S" > $N/suite_hora.txt
python tests/test_aceptacion.py > $N/suite.txt 2>&1; echo "rc=$?" >> $N/suite.txt
date "+FIN SUITE %H:%M:%S" >> $N/suite_hora.txt
python scripts/cerrar_reporte.py > $N/cerrar_reporte.txt 2> $N/cerrar_reporte_err.txt; echo "rc=$?" >> $N/cerrar_reporte.txt
echo "TODAS TERMINADAS $(date +%H:%M:%S)" > $N/guardas.fin
