# ENCARGO DE LA VUELTA 46: **MINAR `grove_high_output` DESDE `cap_04`**

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor en la `ACTA 44`,
**ratificando la decision del fundador del 19 sep 2026** (`ae49086`), que corrigio el
encargo de la vuelta 45. Modo austero (`D.47`).*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO PRIMERO: **LA VUELTA 45 TENIA RAZON, Y SE LO VERIFIQUE**

**Mediste la puerta de `D.39`, la encontraste cerrada y te negaste a insertar, con las citas
pegadas.** La `ACTA 44` `44.3` la reproduce fila a fila **y la muerde por mutacion**: `0`
insertables con el arbol como esta, `22` al meter `grove_high_output` en
`cerrados_en_extraccion`. **La puerta esta viva y tu `0` es un `0` medido.**

**Y EL TABLERO DICE LO MISMO POR SU LADO**, que es donde `D.49` manda mirar:

    $ python forja.py tablero --puedo grove_high_output
    LINEA 'serial', LIBRO 'grove_high_output': SI
      'grove_high_output' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi
      que se continua desde el capitulo siguiente al ultimo minado (cap_03), citando su
      frontera. D.50.

> **`D.50` dice MINAR, no insertar.** Los `22` de la bandeja **esperan hasta que el libro
> este minado entero**, y eso son `15` capitulos mas. `3` de `18` no cierra nada.

## Y LO SEGUNDO: **LO QUE LA `ACTA 44` TE CARGA, PARA QUE NO TE LLEGUE DE OIDAS**

| | |
|---|---|
| **`REPORTE` sube a `1 de 3`** | el reporte **no cerro**: `3` de las `4` filas de tu esqueleto vacias, sin guardas al cierre, sin tabla `D.52`, sin `PASOS INVENTADOS` y **sin la linea del tramo**. Y tu `16` utiles es `22` menos una deuda: el unico instrumento que midio los `22` juntos dice **`9` entran y `13` bloquean** |
| **la causa esta medida, no supuesta** | `.v45/informe_d021.reloj` dice que lanzaste la aduana a las `23:29:34` y tu turno acabo `655` s despues con el fichero en `0` bytes. **El encargo de la 45 ya traia el remedio escrito**: *si tu arnes no puede esperar tanto en una sola llamada, dilo con la medida al lado.* **La medida estaba. La frase no** |
| **`CLASE`, `CIFRA PUBLICADA` y `DATO MOVIDO` salen LIMPIAS** | y `CIFRA PUBLICADA` **baja de `1 de 2` a `0`** por `D.38.1`, no por indulto |
| **la caida que mas pesa es MIA** | mi apertura sellada publico *ninguno de los `22` dice de que capitulo sale* y **los `22` lo dicen** en `resumen_teorico`. `AUDITOR` sube a `1 de 3` |

---

## TAREA 1. **LOS REGISTROS DE LA `ACTA 44`**

**Cerrada cuando las cuatro filas esten hechas y dichas.**

### 1.a. `d021` **NO ESTA PAGADA**, y ahora cubre tres cosas

**Reescribiste el paso `4` en el arbol a las `23:29` y no lo registraste**, asi que la deuda
sigue viva y correcta. **Y el mismo puente sigue en pie un paso mas abajo.** Lo adjudico en
`ACTA 44` `44.4` y lo dejo anotado como **`d023`**:

    $ python scripts/deuda.py        (la fila d023, vuelta 45)

1. **El paso `5`** de `clasificar_trabajo_proceso_montaje_prueba` casa `L45` (la pieza que
   falla su prueba **unitaria**, donde no hay publico) con `L41` (*rehacer contra las
   preocupaciones y las objeciones del publico que la probo*). **El libro no lo dice en
   ningun renglon**, y lo condena el argumento que escribio tu propia correccion del paso
   `4`: en `L41` lo que se prueba es la presentacion **YA MONTADA**, o sea del lado de la
   prueba de sistema.
2. **La linea `FRONTERA DENTRO DEL NODO`** del `resumen_teorico` sigue diciendo *la mitad de
   los pasos `4` y `5` de `L41`*. **Despues de tu correccion eso solo es cierto del `5`.**
3. **La cifra de la ficha**: dice `7 TRANSCRIPCION, 0 PUENTE despues de esta correccion`, y
   son **`6` y `1`**.

**LAS TRES SE REPARAN POR CORRECCION DECLARADA, SIN BORRAR EL TEXTO VIEJO**, y las tres
**antes de que ese candidato pase la aduana**, que es la letra de `d021`. **Hoy no pasa
ninguna aduana, asi que esto NO te bloquea: lo cierras y sigues.**

### 1.b. Los `7` de `cap_02` no tienen informe de aduana, y eso esta anotado como `d024`

**Los `15` informes por candidato de `.v2g/` son los `15` de `cap_03`. De `cap_02` hay
cero**, contado por mi contra `UNIDAD DE ORIGEN`. **No lo pagues hoy**: esta agendado para
la vuelta que abra la insercion del lote 7, porque su tramo no se puede dimensionar sin el.

### 1.c. La pregunta de doctrina que registro y **dejo ahi** (`D.55`)

*Una cifra de fidelidad falsa en la ficha de un candidato en cuarentena no es ninguna de las
cuatro especies de `5.2`, y sin embargo viaja al dataset intacta el dia que el candidato
entra.* **Esta en `ACTA 44` `44.5.b` con su medida. No abre parada, no entra en la cola de
`11` y no va al banco.**

---

## TAREA 2. **LA FRONTERA DE `cap_04`, ANTES DE CORTAR NADA**

**Publicala y cierrala contra el cuerpo**: la suma de las filas tiene que dar el `wc -w` del
cuerpo, con **cero lineas sin cubrir y cero solapes**. **Si no cierra, no se publica ninguna
cuenta de nodos.**

**Y CITA LA FRONTERA HEREDADA** (`D.50`), que es la de `cap_03` y la cerro el frente al
digito. **No la recomputes: citala con su sede**, que la tienes en el arbol:

    $ grep -n "5828" docs/loop/archivo/grove_high_output/REPORTE.md
    ...  | **5828** | **15** | el cuerpo entero de cap_03, cero lineas sin cubrir y cero solapes |

    cuerpo de cap_03                       : 5828 palabras
    fichero entero, para cruzar con wc -w  : 5855 palabras      (5828 mas 27 de cabecera)
    nodos que el frente le saco            : 15

**LA TABLA VA PEGADA DE SU INSTRUMENTO** (`D.41`), y el tallado la compara celda a celda.

---

## TAREA 3. **MINAR `cap_04`, CON EL TECHO POR DELANTE**

- **Entre cinco y quince candidatos** (`EXTRACTOR.md` 12.4). Si `cap_04` solo da tres,
  cierras en tres y **lo declaras con su cifra**; si pasa de quince, **la vuelta cierra en
  esa unidad y lo dice**.
- **Un candidato por vez y en el orden del libro.**
- **Cada uno pasa por `python forja.py informe <candidato>` en el acto de escribirlo**, y el
  que caeria se corrige y se reintenta.
- **CERO INSERCIONES.** El lote 7 esta **ABIERTO**: `D.39` no deja entrar nada hasta que
  cierre. Los candidatos van a `cuarentena/grove_high_output/` y **ahi se quedan**.
- **Las aristas que la senial no levanta se declaran por lectura** (`D.29`) con su razon
  escrita, **y se cablean el dia de la insercion**, no hoy.

> ### **Y UNA COSA QUE TE PUSO EN `1 de 3`, ASI QUE VA CON SU MEDIDA**
>
> **Una aduana en seco sobre esta poblacion tarda del orden de `385` s por candidato**, y lo
> mido de dos sitios distintos: `.v45/informe_d021.reloj` (`655` s sin salida) y mi propio
> barrido de la fase ciega (`384` s en un candidato).
>
> **NINGUNA CORRIDA SOBREVIVE A TU TURNO.** Esperala bloqueado hasta leer su codigo de
> salida. **Y si no cabe, escribes que no cabe, con el reloj al lado, y cierras igual.**
> Un turno que se queda sin cierre por una corrida que no cabia **pierde las dos cosas**: la
> corrida y el reporte.

---

## TAREA 4. **LA FIDELIDAD `D.30` DE `cap_04`, ANTES DE CERRAR**

**`PASOS INVENTADOS` de `cap_04`**, releyendo los pasos contra su parrafo, **con la fila del
capitulo y el total**. Tope `10`. **La escalada se decide sobre el peor capitulo.**

**Y ESCRIBE EL DENOMINADOR AUNQUE SEA CERO.** La vuelta 45 no publico esta metrica y yo tuve
que publicarla con `sin denominador` en las tres filas (`ACTA 44` `44.8`). **Una cifra
agregada no se desglosa despues.**

---

## TAREA 5. **EL CIERRE, QUE ES LA FILA QUE LA VUELTA 45 NO ENTREGO**

    python forja.py gate
    python forja.py guiones
    python tests/test_aceptacion.py
    python scripts/cerrar_reporte.py
    python scripts/tabla_de_cierre.py --escribir      y se pega su salida
    python forja.py tablero --escribir
    python forja.py credito                           lo lees; NO anotes tu propia vuelta

**Y ESCRIBE LA LINEA DEL TRAMO, sea cual sea el numero, incluido `0`:**

> *la vuelta cierra en el candidato `N` de `M`; los que quedaban pasan a la vuelta
> siguiente.*

**LAS CUATRO FILAS DE TU ESQUELETO SE CIERRAN TODAS, O LAS QUE NO SE CIERREN LLEVAN SU
MOTIVO ESCRITO EN SU CELDA.** Una fila vacia no dice nada; una fila que dice *no cupo, y
aqui esta el reloj* dice todo lo que hace falta.

**Si un turno tuyo pasa de `10` USD y la vuelta no es de saneamiento, el reporte lo declara
con el desglose de en que se fue** (`D.55`).

---

## LO QUE NO ES TAREA TUYA ESTA VUELTA

| | |
|---|---|
| **la deuda** | **`11`** pendientes en `docs/loop/DEUDA.jsonl` tras anotar `d023` y `d024`. **No la pagues hoy**: se paga junta en una vuelta de saneamiento (`D.55`). La ultima fue la `44` |
| **los `6` de `d005`** | son de `cap_03` y se reparan antes de insertar, **no antes de minar `cap_04`** |
| **la doctrina** | congelada en `11`. Si encuentras una pregunta nueva, **registrala con su medida y dejala ahi** |
| **tareas bloqueantes** | **CERO.** Ninguna guarda de DATO esta en rojo (`ACTA 44` `44.11`), asi que `D.55` no me deja dejarte ninguna |

> **LO UNICO QUE TE BLOQUEA ES UNA GUARDA DE DATO EN ROJO**: `gate`, el cerrojo, el censo no
> decreciente, o la fidelidad `D.30` con puente. **Eso no es deuda: es averia.**

## LO QUE NO SE TOCA

- **El banco no gana reglas nuevas** salvo que una guarda de DATO lo exija con su cita.
- **`config/frentes.json` y `config/umbrales.json`** se leen, no se editan.
- **`src/`, el banco, el arnes y los protocolos** no se tocan mientras corran frentes en
  paralelo (`D.45`).
- **El bucle no funde ramas y el bucle no crea remotos.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una
regla vigente, paras y lo traes. No adivines.**
