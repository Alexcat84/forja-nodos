LIBRO DE ESTA VUELTA: marquet_turn_the_ship

# ENCARGO DE LA VUELTA 8 DEL FRENTE `marquet_turn_the_ship`: **SANEAMIENTO. EL RESTO DE `d104`, CON LA ESPERA ESCRITA PASO A PASO**

*Linea **`marquet_turn_the_ship`** (`extraccion-marquet_turn_the_ship`, worktree
`C:/Users/AlexDesk/Documents/forja-marquet_turn_the_ship`). Lo escribe el auditor al cerrar la **`ACTA M8`**, que
audita tu vuelta `7`. `MODO_INSERCION=cuarentena`, regimen ligero.*

> # **LIBRO DE ESTA VUELTA: `marquet_turn_the_ship`**
> # **CLASE DE ESTA VUELTA: SANEAMIENTO** (`python scripts/deuda.py --clase 8` da `LIBRE`; se declara de saneamiento porque todo su trabajo es pagar `d104` y `d103`)

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **COMO SE ESPERA MAS DE DIEZ MINUTOS. LEELO ANTES QUE NADA**

**Tus vueltas `6` y `7` acabaron el turno con aduanas corriendo de fondo** (*Waiting for the background task...*). **Las dos veces
las recogio tu auditor. No cuentes con eso.** **Cuando tu turno acaba, ya no hay un despues para ti.**

**LA CAUSA MAS PROBABLE ES MECANICA, y a tu auditor le paso lo mismo en su propio turno** (`ACTA M8` `M8.8`): **una llamada de Bash
sin `timeout` explicito se corta a los `120` s y se va sola al fondo**, y ninguna llamada puede durar mas de `600` s. **Una tanda
de cinco tarda unos `26` minutos** (`M8.9`: `826` a `1566` s). **Por eso no se espera con una sola llamada: se espera con varias,
una detras de otra.** Hazlo exactamente asi:

1. **Preparas una vez:**

       mkdir -p .v8m/aduana && sed 's/\.v7m/.v8m/g' .v7m/barrido_tanda.sh > .v8m/barrido_tanda.sh

2. **Lanzas la tanda** con UNA llamada normal, que vuelve enseguida. **NO uses el parametro `run_in_background` de la herramienta:**

       nohup bash .v8m/barrido_tanda.sh <ficha1> <ficha2> <ficha3> <ficha4> <ficha5> > .v8m/tanda_N.log 2>&1 &

3. **Esperas** con una llamada **con el parametro `timeout` puesto a `600000`**:

       timeout 570 bash -c 'until grep -q "TANDA RECOGIDA" .v8m/tanda_N.log; do sleep 20; done'; tail -1 .v8m/tanda_N.log; cat .v8m/aduana_tiempos.txt

4. **Si no imprime `TANDA RECOGIDA`, repites la llamada 3 tal cual.** Una tanda de `26` minutos son tres o cuatro llamadas.
   **Entre una llamada y otra no escribes ningun mensaje final.**
5. **Solo cuando imprime `TANDA RECOGIDA`** lees los ficheros y lanzas la tanda siguiente.

**Y antes de terminar el turno, pegas en el reporte la prueba de que no dejas nada vivo:**

    powershell -NoProfile -Command "(Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match 'forja.py informe cuarentena/marquet' }).Count"

**Tiene que dar `0`.** Los `forja.py informe` de `cuarentena/grove_high_output/` o de `cuarentena/gerber_emyth/` **son de otras
lineas: no los toques.**

**ESCRIBE EL CIERRE PROVISIONAL ANTES DE LA PRIMERA TANDA, y reescribelo cada vez que recojas una.** Si el turno se corta, lo
que quede escrito tiene que ser verdad. **Tu vuelta `7` lo hizo bien, y lo que escribiste era verdad** (`M8.8`).

---

## TAREA 1. **REGISTROS: LA ACTA M8**

**Lee la `ACTA M8`** (`docs/loop/ACTA_AUDITOR.md`, al final). Lo que te toca:

- **`d098` BIEN PAGADA, y la cuenta del libro FIRMADA fila a fila** (`M8.3`, `M8.4`). **`cap_01` queda en `0,00`.**
- **LAS SEIS CAIDAS DE `M8.7` NO ACUMULAN, y todas tus rachas estan en `0`** (`M8.10`). Estas dos arreglalas:
  - **`M8.7.b`:** leiste mal la condicion para reusar. **Los tres informes de `.v6m/` no valen**, porque la `TAREA 2` cambio
    una ficha. **Se vuelven a correr en la `TAREA 2` de esta vuelta.**
  - **`M8.7.c`:** **SI habia una aduana previa de `ceder_control`**, en `.v25/aduana_lote5.txt`. **La culpa es en parte de la
    lista de carpetas de tu encargo, y tu auditor lo declara como error suyo** (`M8.13`).
- **Tu vuelta `7` no declaro el saneamiento; lo declaro tu auditor** (`M8.12`). **Esta vez lo declaras tu al cerrar.**

---

## TAREA 2. **`d104`: LAS `14` FICHAS QUE FALTAN, EN TRES TANDAS, CON LA ESPERA DE LA SECCION `0`**

**Ya estan barridas contra el texto final, y NO se vuelven a correr** (`M8.9`): `ceder_control_reforzar_competencia_claridad`,
`eliminar_seguimiento_descendente_responsabilizar_dueno`, `declarar_intencion_reemplazar_peticion_permiso`,
`contar_firmas_cadena_tramite_parado`, `auditar_formacion_premios_ultima_fila` y `cambiar_forma_trabajar_conservar_plantilla`.
**Sus informes estan en `.v7m/aduana/`.**

**Faltan estas `14`**, en tandas de hasta cinco. Cada tanda se recoge ENTERA antes de lanzar la siguiente:

- **tanda 1:** `asignar_responsable_unico_evolucion_planificada`, `acoger_inspectores_externos_fuente_aprendizaje`,
  `aplicar_ejercicio_codigo_genetico_control`, `encargar_meta_especifica_dejar_libre_metodo`,
  `identificar_temas_formacion_tarjetas_decision`
- **tanda 2:** `informar_cierre_jornada_conservar_propiedad_trabajo`, `inspeccionar_reparto_informacion_notas_jefe`,
  `observar_reunion_rutinaria_senales_plantilla`, `recorrer_organizacion_escuchar_plantilla`,
  `reforzar_principios_guia_lenguaje_prueba_conocimiento`
- **tanda 3:** `repetir_mensaje_invariable_diario_reunion_evento`, `resistir_dar_solucion_clasificar_decision_urgencia`,
  `seguir_frustrado_preguntar_implantacion_ideas`, `tomar_accion_deliberada_pausar_vocalizar_gesticular`

**LO QUE PUBLICAS:** el saldo de las `20` (`ENTRARIAN`, `BLOQUEARIAN`, `CAERIAN`, `CHOCAN`), sumando las `6` de `.v7m/aduana/`.
Y **por cada ficha, la ultima aduana guardada que tenia antes, y que vecindad cambio**. **La ultima aduana anterior la
buscas con `grep -rl "\] <ficha>" --include=*.txt .`, en TODAS las carpetas y no en una lista.** **Si no aparece ninguna,
pegas debajo el `grep` que no encontro nada.** **Bajo `$` va solo lo que imprime el comando.**

**SI NO CABE:** das la lista exacta de las fichas sin barrer, **y `d104` sigue viva**. **Una tanda que no vas a poder
esperar entera, no la lances.**

---

## TAREA 3. **LOS PARES EN BANDA ALTA, LEIDOS POR SUS PASOS** (`EXTRACTOR.md` `11`)

**Cada par con `similitud_texto` de `0,4` en adelante, o levantado por `paso_contra_nodo`, lo lees por sus pasos.** Si
dudas, lo marcas discutible **ANTES de saber si aciertas**. **Ya hay estos, del barrido de la vuelta `7`** (`M8.9`):

- `declarar_intencion_reemplazar_peticion_permiso` contra `resistir_dar_solucion_clasificar_decision_urgencia` (`0.422`) y
  contra `acoger_inspectores_externos_fuente_aprendizaje` (`0.404`)
- `cambiar_forma_trabajar_conservar_plantilla` contra `encargar_meta_especifica_dejar_libre_metodo` (`0.441`) y contra
  `escuchar_entender_critica_dominar_defensa` (**`paso_contra_nodo 0.612`**)

**Y los que salgan de tus tres tandas.** **Los dos pares de `ceder_control` que bajaron de la banda alta ya los leyo tu
auditor** (`M8.5`), y no te tocan.

**Si acabas la `TAREA 2` entera y esta:** `python scripts/deuda.py --pagar d104 --vuelta 8 --como "..."`. Y ademas
`--pagar d103`, si ninguna ficha cambio despues de su aduana.

---

## TAREA 4. **EL CIERRE, CON TODO LO QUE TU VUELTA `7` NO LLEGO A HACER**

- **Declara el saneamiento:** `python scripts/deuda.py --saneamiento --vuelta 8`.
- **Anota tu tanda:** `python forja.py credito --anotar`, **con `--cae` o `--limpia` en cada especie, y que cuadre con tu tabla.**
- **`D.61`:** cada discutible, ejecutado o cerrado con su motivo.
- **`python scripts/cerrar_reporte.py`, SOLO, sin ninguna otra prueba corriendo a la vez** (`M8.13`), con su ultima linea pegada.
- **Mide las condiciones de parada una a una.** **Si `d104` queda pagada, dilo con la cifra delante: tu auditor tiene que poder
  medir la campaña consumada.** **Si esta consumada, NO cosechas, NO fundes y NO insertas** (`D.39`, `D.50`, decision del `22`
  sep punto `4`). **No escribas `PARA_ALEXIS.md`.**
- **Commitea `docs/loop/`, `.v8m/` y, si alguna cambio, `cuarentena/marquet_turn_the_ship/`. Y pega el conteo de procesos vivos
  de la seccion `0`, que tiene que dar `0`.**

---

## LO QUE NO HACES

- **NO INSERTAS.** `MODO_INSERCION=cuarentena`.
- **NO TOCAS LA MAQUINARIA** (`D.45`): `orquestador_forja.sh`, `src/`, `scripts/`, `tests/`, `hooks/`, `esquema/`, **ni `config/`**.
  Tus scripts de la vuelta van en `.v8m/`.
- **NO ESCRIBES DOCTRINA.** Si hace falta una regla nueva, se para.
- **NO TOCAS NINGUNA FICHA.** Esta vuelta solo mide y lee.
- **NO TOCAS `cuarentena/grove_high_output/` NI `cuarentena/gerber_emyth/`**, ni sus procesos.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No adivines.
