#!/bin/bash
# ACTA 72: las guardas corridas por el auditor, en serie, cada una con su rc.
cd "$(dirname "$0")/../.."
D=.v73aud/normal
echo "INICIO $(date '+%F %T')" > $D/verificar.log
python forja.py gate > $D/gate.txt 2>&1; echo "rc=$?" >> $D/gate.txt
python forja.py guiones > $D/guiones.txt 2>&1; echo "rc=$?" >> $D/guiones.txt
python forja.py resolutor > $D/resolutor.txt 2>&1; echo "rc=$?" >> $D/resolutor.txt
python tests/test_aceptacion.py > $D/suite.txt 2>&1; echo "rc=$?" >> $D/suite.txt
python scripts/cerrar_reporte.py > $D/cerrar_reporte.txt 2>$D/cerrar_reporte_err.txt; echo "rc=$?" >> $D/cerrar_reporte.txt
echo "TODOS TERMINADOS $(date '+%F %T')" >> $D/verificar.log
