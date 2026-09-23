# DECISION DEL FUNDADOR, 24 SEP 2026: **UNA CARPETA, UN ACTOR DE GIT**

*Sobre las muertes de las dos lineas del 23 sep. **La decision va arriba, literal.** Debajo, el
dictamen que la sesion de chat escribio con la linea parada, que es lo que la decision pide.*

---

## LA DECISION, LITERAL

> SESION DE CHAT en forja-nodos. NO commitees nada si alguna linea esta
> a mitad de turno: primero comprueba su estado. DECISION DEL FUNDADOR
> (24 sep 2026) sobre las muertes de anoche:
>
> 1. DIAGNOSTICO primero, sin tocar git: lee la cola de los dos logs y
>    el visor de eventos de Windows (suspension, reinicio, actualizacion)
>    de anoche, y dictamina de que murio cada linea: sesion, suspension,
>    reinicio, la tarea programada, o otro actor con git en la carpeta.
>    Si fue la tarea programada, revisa sus condiciones (que no se
>    detenga con bateria ni por inactividad, sin limite de duracion).
> 2. UNA CARPETA, UN ACTOR DE GIT: mientras una linea corre, su carpeta
>    es solo del arnes. Tu, como supervisor, VIGILAS SOLO LEYENDO (ps,
>    tail, cat); nunca pull, checkout ni commit en una carpeta con una
>    linea a mitad de turno. Tus arreglos de ARNES se commitean con la
>    linea parada, que para eso ya se detuvo. Escribelo en PARALELO.md.
> 3. NADIE MAS USA ESTA CARPETA: cualquier otra sesion que necesite leer
>    la forja hace su propio git clone en una carpeta aparte. Escribelo
>    tambien.
> 4. PARALELO.md y el dictamen citan el metodo de lanzamiento VIGENTE
>    (tarea programada con ventana oculta), no el WMI, con su prueba de
>    vida y el aviso de que ningun lanzador sobrevive a una suspension.
> 5. Si las lineas estan vivas, sigue vigilando; si murieron otra vez,
>    relanzalas por el metodo vigente cuando tengas el dictamen. Tu
>    reporte abre con la causa de anoche en una linea.

El fundador lo acompanio de su hallazgo: *la otra sesion estaba trabajando en el mismo git, y
por eso murieron, estaban muriendo, habia choque real.* Y despues: *ya he pausado las
actualizaciones, ya no son un problema.*

---

## EL DICTAMEN, MEDIDO SIN TOCAR GIT

### Primera muerte: lanzadas el 23 a las `00:03`, con `nohup` desde la sesion

**UN REINICIO DE WINDOWS UPDATE.** Visor de eventos, registro de sistema:

    00:29:59  1074  MoUsoCoreWorker.exe ha iniciado el reinicio del equipo   (KB5124010)
    00:31:35    13  el sistema operativo se apaga
    00:32:00    12  el sistema operativo arranca
    00:32:52  1074  TrustedInstaller.exe ha iniciado OTRO reinicio
    00:33:15    12  arranca

Los dos logs se cortan antes y no dicen nada mas. **La sesion de chat murio de lo mismo**, y el
dictamen del 23 que culpaba al cierre de la sesion **se corrige** (su propia seccion 1 lo
declara).

### Segunda muerte: relanzadas a las `06:25` por WMI, muertas hacia las `06:27`

En esa franja **no hay reinicio ni suspension**. Hay dos hechos, y ninguno lo prueba solo:

- **las consolas de WMI eran visibles**, y el fundador las vio *vacias, sin proceso alguno*;
- **OTRO ACTOR DE GIT EN LA CARPETA**: `.git/FETCH_HEAD` se escribio a las `06:30:38` con
  **las CINCO ramas del remoto, incluida `main`**. Eso es un `git fetch` o un `pull` sin
  argumentos. **El arnes no fue** (solo pide la suya: `git pull --rebase origin
  extraccion-mundo-11`) **y la sesion tampoco**. Coincide con lo que encontro el fundador.

El reflog de las dos carpetas no tiene mas actores que el arnes y la sesion: el otro no movio
`HEAD`, pero si leyo del remoto dentro de la carpeta.

### La tarea programada NO es un riesgo, medido

    forja_linea_serial / forja_linea_marquet
      no arranca con bateria : False   se para al pasar a bateria: False
      limite de duracion     : PT0S    solo si inactivo: False

Su accion (`wscript`) termina al instante y **deja el Git Bash corriendo suelto**; probado con
un trabajo de `150` segundos que sobrevivio a su tarea.

### Y una falta de la sesion, declarada

A las `06:37`, antes de conocer esta decision, **la sesion commiteo dos ficheros en la carpeta
de la serial con su linea a mitad de la fase ciega**. Salio limpio (hook verde, sin lock, sin
push), **y es exactamente lo que esta decision prohibe.** No se repite: desde entonces solo se
lee.

---

## DONDE QUEDA ESCRITO

`PARALELO.md` seccion `7`: una carpeta un actor, nadie mas usa estas carpetas, el lanzador
vigente con su prueba de vida, y el aviso de que **ningun lanzador sobrevive a un reinicio ni a
una suspension**.
