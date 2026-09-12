# ENCARGO DE LA VUELTA 15: LOS CINCO PASOS, EL LOTE 3 DENTRO, Y EL LOTE 4

*Escrito por **Alexis** el 11 sep 2026, al levantar la parada de la vuelta 14
(`docs/loop/paradas/2026-09-11-la-apertura-ciega-no-cuenta-a-mano.md`).*

---

## LO QUE HA CAMBIADO, Y ES LO MAS GRANDE DE LA CAMPAÑA

> ### `D.39`: LA INSERCION DE UN LOTE CERRADO YA NO SE PIDE. SE HACE.
>
> **Cuando un lote queda cerrado en extraccion y el acta del auditor certifica su
> informe, LO INSERTAS EN TU VUELTA SIGUIENTE, sin firma nueva del fundador.**
>
> **Los candidatos de un lote ABIERTO se quedan en cuarentena hasta que su lote
> cierre.**

**`MODO_INSERCION` llega en `insertar` por defecto.** **NO es barra libre:** la
letra de arriba manda, y **meter candidatos de un lote abierto es una caida de
dato**, no un adelanto. Esta en `EXTRACTOR.md` **15.7** con su motivo.

**Y DOS REGLAS NUEVAS PARA EL AUDITOR**, que te afectan porque vais a comparar
lecturas: **`D.38.3`**, su apertura ciega **publica clases y lecturas, no cifras
contadas a mano**; y **`D.38.4`**, su barrido de vecinos se hace sobre **grafo mas
bandejas**, que es la poblacion que tu barriste y el no.

**Su racha propia arranca en CERO.**

---

## TAREA 0, BLOQUEANTE: LOS CINCO PASOS QUE FALTAN

*Decision 4 del fundador. **Va antes de insertar nada.***

    firmado por las actas 9 a 13 : 1.112 pasos
    medido hoy en los ficheros   : 1.107 pasos
    faltan                       :     5
    y el hueco vive entero en la mitad ARCHIVADA (558 firmados, 553 medidos)

**LA VIA LA DEJO ESCRITA EL EXTRACTOR Y NADIE LA HA CORRIDO.** El auditor lo dice
asi de claro: *"no afirmo lo que daria, porque no la he corrido"*.

    git log -p -- cuarentena/zhuo_manager/ | ...      anterior al commit 3ad8998

**QUE HACER CON LO QUE ENCUENTRES, y son dos caminos y no uno:**

| lo que salga | que se hace |
|---|---|
| **pasos podados con motivo** (un puente retirado, una correccion de fidelidad) | **se cita el commit y el motivo**, y la cifra firmada se corrige por **correccion declarada**: el texto viejo no se borra |
| **pasos perdidos sin motivo** | **se restauran del libro**, con su linea citada y su `sed` pegado, y el candidato vuelve a pasar por la aduana |

**PUBLICA LA CIFRA ANTES Y DESPUES**, y **con su instrumento al lado**: el recuento
de pasos sale de un comando corrido en esta vuelta, no de las actas.

> **Y SI RESULTA QUE LAS DOS CIFRAS ERAN CIERTAS BAJO DOS CONVENCIONES DISTINTAS,
> eso tambien es un resultado y se escribe con las dos convenciones nombradas.** No
> fuerces un hueco que no exista.

---

## TAREA 1: INSERTAR EL LOTE 3, `zhuo_manager`

**El lote 3 esta CERRADO en extraccion** (`cap_01` a `cap_12` minados) **y su
informe esta certificado**: 68 candidatos, los 68 `[ENTRARIA]`, cero caidas. **Esa
es exactamente la condicion de `D.39`.**

**NO EMPIECES ESTA TAREA SI LA TAREA 0 NO HA CERRADO.** Un lote con cinco pasos sin
reconciliar no entra: **insertar es la unica accion de esta casa que no se deshace
leyendo.**

**COMO, y es lo de siempre:**

1. **Publica el censo esperado ANTES**: el censo de partida **mas** los que vayan
   a entrar.

> **CORRECCION DECLARADA, 11 sep 2026: ESTA TAREA QUEDO A MEDIAS Y SE REANUDA.**
> La vuelta 15 se corto por un congelamiento de la maquina del fundador, **en un
> bloqueo de la aduana y no a mitad de una escritura**. Lo hecho quedo asegurado en
> el commit que trae esta correccion, y el estado **medido** al reanudar es:
>
>     dataset/nodos.jsonl                        186 nodos   (eran 135)
>     bitacora/VEREDICTOS.jsonl                  132         (eran 100)
>     cuarentena/zhuo_manager/                    17 pendientes
>     cuarentena/_insertados/zhuo_manager/       119 archivados  (68 + 51)
>
> **LA CIFRA DE PARTIDA YA NO ES 135: ES 186.** El texto viejo se tacha y no se
> borra. **REMIDELO TU** con su instrumento al lado antes de publicar nada: que esta
> cifra este aqui escrita no te exime de comprobarla (`D.38.3` es del auditor, pero
> la vara es de la casa).
>
> **LA TAREA 0 YA ESTA CERRADA** en el commit `3c6fd7f`: los cinco pasos eran **dos
> podas con motivo escrito** (`6ee153f` menos 4 y `5efd637` menos 1) y **nada que
> restaurar**. No la repitas.
>
> **DONDE SE PARO, exacto:** el ultimo candidato pidio veredicto con
> `repartir_equipo_cartera_horizontes` por vecino, y el turno se corto antes de
> escribirlo. **Ese veredicto no existe y hay que leerlo**, no darlo por hecho.
> El log de la corrida esta en `.insercion_lote3_vuelta15.log`.
>
> **Y LOS 51 QUE YA ENTRARON NO SE REINSERTAN:** la aduana los rechazaria por `el id
> ya vive en el grafo` y haria bien. Se comprobo al reanudar que **cero archivados
> estan fuera del grafo y cero de la bandeja estan dentro**, asi que la frontera
> entre lo hecho y lo pendiente es limpia.
2. **`D.36`, el orden que lee**: mide la asimetria de los pares que bloqueen **en
   los dos sentidos** y ordena para que el par se lea. Y **di si hizo falta
   reordenar o no**, porque comprobarlo y que no haga falta **no es lo mismo que no
   mirarlo**.
3. **Uno por vez, por la aduana**, con su veredicto razonado por vecino.
4. **`D.37` despues**: las cabezas que dicen cuantas partes tienen y las nombran,
   con `python forja.py arista --madre ... --hijo ... --paso ... --razon ...`.
   **Publica las esperadas antes y cuentalas despues.**
5. **Los insertados a `cuarentena/_insertados/zhuo_manager/` EN EL MISMO ACTO**
   (`D.31`), con su `LEEME` de archivo.
6. **Gate, resolutor, vigencia y suite al cerrar**, y el censo contado.

---

## TAREA 2: LA BITACORA AL DIA

**Hoy hay 26 veredictos razonados que viven SOLO en `REPORTE.md`**, que no es su
sede (`D.26` los pone en `bitacora/VEREDICTOS.jsonl`). No se han perdido, porque el
reporte se apende, **pero no estan donde la regla los pone.**

**LA TAREA 1 ESCRIBE LA MAYORIA SOLA**, porque son veredictos de pares que la
aduana levanta al insertar. **Los que no, se declaran a mano:**

| especie | donde va |
|---|---|
| **`CONTINUA` que ninguna señal levanta** | `python forja.py arista`, con su paso citado (`D.29`, `D.37`) |
| **`SANO` que ninguna señal levanta** | **NO TIENE SEDE, y no te la inventes** |

> **ESE HUECO ES REAL Y LO DIGO YO, no lo descubras tu a mitad de vuelta:** la
> aduana escribe veredictos de los vecinos que levanta, y `forja.py arista` solo
> escribe `CONTINUA`. **Una lectura que concluye `SANO` sobre un par que ninguna
> señal junta no tiene donde escribirse hoy.**
>
> **QUE HACER CON ELLA: dejarla en el reporte, DECIRLO, y contar cuantas son.**
> **No inventes una sede y no fuerces un `CONTINUA` que tu lectura no sostiene.**
> Si al cerrar la vuelta son muchas, **eso es un dato que traes**, y yo decido si
> la casa necesita una sede para esa especie.

**Al cerrar, publica el cuadre:** veredictos en la bitacora antes, escritos en esta
vuelta, y **cuantos siguen viviendo solo en el reporte, con su razon**.

---

## TAREA 3: EL LOTE 4, `scott_radical_candor`, CUATRO CAPITULOS

**Cuatro por vuelta** (`D.38` y la decision 5.8), y son **`cap_04` a `cap_07`**,
que son los **capitulos 1 a 4** del libro.

| fichero | unidad | titulo textual | palabras |
|---|---|---|---:|
| `cap_04.md` | Cap. 1 | Build Radically Candid Relationships | 6.263 |
| `cap_05.md` | Cap. 2 | Get, Give, and Encourage Guidance | 8.756 |
| `cap_06.md` | Cap. 3 | Understand What Motivates Each Person on Your Team | 11.587 |
| `cap_07.md` | Cap. 4 | Drive Results Collaboratively | 13.678 |
| | | **total** | **40.284** |

> **AVISO QUE TE DOY YO Y QUE NADIE HA MEDIDO TODAVIA: CUATRO CAPITULOS DE ESTE
> LIBRO SON 40.284 PALABRAS, casi el libro entero de `smart_who` (44.133).** Los
> capitulos de `zhuo_manager` promediaban 6.000; estos promedian **10.000**, y el
> `cap_07` solo **pesa mas que dos de los otros**.
>
> **El volumen de cuatro se firmo sobre capitulos de otro tamaño.** Si no caben,
> **cierras los que quepan enteros y lo dices con su cifra**: un capitulo cerrado
> vale mas que dos a medias, y **la unidad atomica sigue siendo el capitulo**.
>
> **Y ESO NO ES UN FALLO TUYO NI UNA EXCUSA: ES LA MEDIDA QUE FALTA.** Publicala y
> el volumen del lote 5 se decidira con ella delante.

**El resto, como siempre:** frontera antes de cortar con su `sed` pegado, la
relectura de fidelidad **dentro** del acto de escribir (`D.30`), un commit por
capitulo, y las cuatro medidas **por capitulo**.

**Y LOS DOS CANDIDATOS QUE YA ESPERAN** en `cuarentena/scott_radical_candor/`
**siguen esperando**: el lote 4 esta ABIERTO, y `D.39` solo abre la insercion de un
lote **cerrado**.

---

## LAS PARADAS

**Paras, lo declaras en TU REPORTE y te detienes si:**

- una regla de la casa te obliga a algo que rompe otra regla de la casa;
- necesitas mover un umbral, el esquema, `D.27`, `D.37` o la vara de continua
  contra repite;
- **la TAREA 0 encuentra algo que no sabes reconciliar**;
- el informe del lote 3 no sale como el acta lo certifico.

**TU NO ESCRIBES `docs/loop/PARA_ALEXIS.md`** (`D.28`).

**NO paras por:** que la aduana levante muchos vecinos con 135 nodos y una bandeja
llena (**eso es la aduana funcionando**), que los cuatro capitulos no quepan (se
dice con su cifra), ni porque haya lecturas `SANO` sin sede (se cuentan y se
traen).

**Y NO FABRICAS MAQUINARIA** (seccion 13). **En particular: no inventes una sede
para los `SANO` sin vecino.** Esa decision es mia y la tomare con tu cifra delante.

---

**Cero guiones largos y cero guiones medios. Si algo contradice una regla vigente,
paras y lo traes. No adivines.**
