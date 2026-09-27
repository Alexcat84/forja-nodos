# ACTA 77: las guardas corridas por el auditor, en serie, cada una con su rc y su hora. Solo lee (la suite y el cierre usan tmp propios).
N=.v78aud/normal
(python forja.py gate; echo "rc=$?") > $N/gate.txt 2>&1
(python forja.py guiones; echo "rc=$?") > $N/guiones.txt 2>&1
(python forja.py resolutor; echo "rc=$?") > $N/resolutor.txt 2>&1
date "+INICIO SUITE %H:%M:%S" > $N/suite_hora.txt
(python tests/test_aceptacion.py; echo "rc=$?") > $N/suite.txt 2>&1
date "+FIN SUITE %H:%M:%S" >> $N/suite_hora.txt
date "+%H:%M:%S" > $N/cerrar_hora.txt
(python scripts/cerrar_reporte.py; echo "rc=$?") > $N/cerrar_reporte.txt 2> $N/cerrar_reporte_err.txt
date "+%H:%M:%S" >> $N/cerrar_hora.txt
ls -A procesos/ | wc -l > $N/procesos_al_acabar.txt
echo HECHO >> $N/cerrar_hora.txt
