# DECISION DEL FUNDADOR, 25 SEP 2026: **PRESUPUESTO UNICO DE PROCESOS Y LA LINEA EN PRIORIDAD BAJA**

*La decision va arriba, literal. Debajo, lo que la sesion de chat midio y como se aplico, con la
linea parada en la frontera entre vueltas.*

---

## LA DECISION, LITERAL

> 1. PARTE A: visto a las 41 etiquetas corregidas.
> 2. PARTE B, OPCION 1: aplica el presupuesto unico de 13 plazas y el
>    lanzador en prioridad baja en la proxima pausa natural entre vueltas,
>    con commit propio. Es estrictamente mejor que el reparto actual y la
>    equivalencia es identica.
> 3. SE PROHIBEN las pruebas de carga en esta maquina mientras la serial
>    corra. Desde ahora solo se mide OBSERVANDO: tras aplicar, muestrea
>    cada hora el arranque de PowerShell y la cola de procesos sin lanzar
>    carga propia, y reportalo. Si la mediana pasa de 2 segundos mientras
>    el fundador usa la maquina, en la pausa siguiente baja a 6 plazas.
> 4. El fundador va a poner el modo de energia en Maximo rendimiento;
>    anota la hora y compara la respuesta antes y despues con la misma
>    observacion pasiva.

## POR QUE (lo medido antes de decidir)

- El reparto de la señal 1 que corria en la linea desde la vuelta 71 tomaba, en CADA aduana, un
  proceso por hilo menos uno (19). Con el barrido de cinco candidatos a la vez eran hasta 95
  procesos de calculo: el barrido del auditor de la vuelta 71 llego a 107 procesos python vivos.
- El equipo de la serial es un i9-12900HK: 14 nucleos (6 de rendimiento con dos hilos y 8 de
  eficiencia), 20 hilos. Con el plan de energia Equilibrado, Windows lleva el trabajo en segundo
  plano y de prioridad baja a los 8 nucleos de eficiencia: se miden al 100% mientras los de
  rendimiento estan casi ociosos.
- Equivalencia: cinco barridos a la vez, cada uno con su aduana entera (filas 07 a 11 de la
  muestra fija), IDENTICOS byte a byte a los resultados del codigo previo al reparto.
- Respuesta (arranque de un PowerShell oculto): reposo 0,2 s; con 13 plazas, los primeros cinco
  minutos mediana 0,37 s y maximo 0,4 s; despues mediana 1,3 s con picos de hasta 33 s; junto al
  barrido de la propia serial con el reparto sin presupuesto, picos de hasta 115 s.

## QUE SE APLICO

- `src/presupuesto.py` y `src/aduana.py`: el presupuesto unico (nucleos fisicos menos uno, 13
  plazas en este equipo), tambien para el calculo en serie de la aduana. Misma formula, mismos
  pares: solo cambia quien calcula y cuando.
- `scripts/lanzar_linea.ps1` y `scripts/prioridad_baja.ps1`: la linea arranca en BelowNormal y
  todo lo que cuelga de ella lo hereda.
- Pruebas: `tests/test_presupuesto_procesos.py` y `tests/test_reparto_similitud.py`.

## DESDE AHORA

- **Prohibidas las pruebas de carga en esta maquina mientras la serial corra.** Solo se mide
  observando: cada hora, el arranque de PowerShell y la cola del procesador, sin carga propia.
- **Umbral:** si la mediana del arranque pasa de 2 s mientras el fundador usa la maquina, en la
  pausa siguiente el presupuesto baja a 6 plazas.
- **Modo de energia:** el fundador lo pasa a Maximo rendimiento; se anota la hora y se compara la
  respuesta antes y despues con la misma observacion pasiva.
