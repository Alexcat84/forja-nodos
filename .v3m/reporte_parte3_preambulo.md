# TAREA 3. CIERRA LA ADUANA QUE LA VUELTA 2 DEJO ABIERTA, Y GUARDA SU SALIDA (`ACTA M2` remedio 3,
`ACTA M3` `M3.10`, `M3.18.3`)

**LA VUELTA 2 AFIRMO `PASADOS POR LA ADUANA EN SECO EN EL MISMO ACTO` SOBRE DOS CANDIDATOS QUE NO LA
TUVIERON.** El unico fichero que esa corrida abrio, `.m2/informe_aplicar_ejercicio.txt`, tenia `0`
bytes (`ACTA M3` `M3.10`), y `ls .m2/ | grep -c asignar` daba `0`.

**LAS DOS SE CORREN AQUI, DE UNA EN UNA, REDIRIGIDAS A FICHERO ANTES DE SEGUIR**, y la de
`aplicar_ejercicio` se corre DESPUES de pagar su puente (`TAREA 2`), porque la ficha cambio:

    python forja.py informe cuarentena/marquet_turn_the_ship/aplicar_ejercicio_codigo_genetico_control.json > .v3m/aduana/c1.txt
    python forja.py informe cuarentena/marquet_turn_the_ship/asignar_responsable_unico_evolucion_planificada.json > .v3m/aduana/c2.txt

**LANZADAS AL EMPEZAR LA VUELTA, EN SEGUNDO PLANO, MIENTRAS SE ESCRIBIA EL RESTO DEL REPORTE**, con la
cifra del propio encargo delante: `9` minutos por informe medidos por el auditor con la poblacion en
`449`, asi que las dos son cerca de veinte minutos de reloj. **No se pega ni una linea de esta seccion
hasta que los ficheros tuvieran bytes de verdad.**
