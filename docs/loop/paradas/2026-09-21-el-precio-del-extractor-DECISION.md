# DECISION DEL FUNDADOR, 21 SEP 2026: **EL PRECIO DEL EXTRACTOR**

*Archivo de la parada de la vuelta 55, escrita por el auditor de la `ACTA 54`. **La
decision va arriba, literal. El cuerpo va debajo sin tocar una coma.***

---

## LA DECISION, LITERAL

> SESION DE CHAT en forja-nodos. Commitea y pushea lo pendiente en la
> rama activa antes de tocar nada. DECISION DEL FUNDADOR (21 sep 2026)
> sobre la parada de la vuelta 55. Archivala en docs/loop/paradas/
> 2026-09-21-el-precio-del-extractor-DECISION.md y aplicala:
>
> 1. LA FASE CIEGA, EL SELLO Y EL TESTIGO SE APAGAN EN MODO cuarentena,
>    en el arnes (regla escrita en D.58 que no llego al codigo: especie
>    ARNES). apertura_ciega mira MODO_INSERCION; en cuarentena el turno
>    del auditor es directo y corto, con su acta corta. Caso positivo con
>    claude falso en los dos modos. Los 9 USD por vuelta del ciego
>    desaparecen de la extraccion.
> 2. EL AUSTERO DECLARA, NO PARA: la regla vigente es la del banco; el
>    "se para" del encargo de la 54 era un disparador de medicion de una
>    sola vez, ya cumplido, y se retira por correccion declarada. Un
>    turno sobre 10 USD se declara con su desglose; la parada la decide
>    el fundador con la cifra delante, como hoy.
> 3. UNA VUELTA DE MEDICION CON SONNET, antes de decidir el alcance: la
>    vuelta 56 mina los siguientes capitulos de Grove con
>    MODELO_EXTRACTOR=claude-sonnet-5 (el auditor sigue en Opus 5), en
>    regimen ligero de verdad, y el acta publica tres cifras al lado de
>    las de Opus: coste del turno del extractor, pasos inventados por
>    muestra, y candidatos que la aduana en seco bloquearia. Umbral
>    escrito: si los pasos inventados por muestra quedan bajo el 10 por
>    ciento y el turno baja a la mitad, GROVE SE TERMINA CON SONNET; si
>    no, se termina con Opus y se acepta el precio, porque 400 USD de
>    cuota caben en la semana si no corre nada mas.
> 4. ALCANCE, decidido hoy y no despues: el mundo 11 CIERRA CON CINCO
>    LIBROS (los cuatro insertados mas Grove entero). Gerber y Marquet
>    quedan en la bandeja con sus 19 candidatos, enteros y sin insertar
>    (D.39: un libro entra cuando su extraccion cierra), como material
>    para cuando la aduana trabaje sin campaña. Escribelo en el TABLERO
>    y en PARALELO.md como el corte definitivo de esta campaña.
> 5. Escribe el PROMPT_SIGUIENTE de la 56 como vuelta de extraccion en
>    ligero con Sonnet, y deja el comando de relanzamiento con
>    MODELO_EXTRACTOR=claude-sonnet-5 y MODO_INSERCION=cuarentena. Lanza y monitorea

---

## LA CIFRA QUE OBLIGO A ESTA DECISION

    REGIMEN LIGERO, vueltas 54 y 55, seis turnos
      v54  extractor   20,69      v55  extractor   24,89
      v54  ciego        6,81      v55  ciego       10,88
      v54  auditor     14,05      v55  auditor     12,58
      TOTAL            89,90      media 14,98 por turno

    objetivo escrito : turno bajo 5,00
    medido           : 14,98 de media, y NI UN SOLO turno bajo 8

**EL REGIMEN LIGERO NO ABARATO NADA, y la causa estaba medida a medias.** Yo dije el 19
sep que el ahorro llegaria con el relanzamiento en `cuarentena`. **No llego, porque
`apertura_ciega` no miraba `MODO_INSERCION`:** `D.58` los apagaba en su letra y **nadie los
apago en el codigo**. Lo supuse y no lo comprobe antes de decirlo.

**Y AUN ASI EL GRUESO NO ERA ESE:** el ciego son unos `9` USD por vuelta; **los dos
extractores son `45`.** Apagar la fase ciega ahorra un quinto. **El precio vive en el
turno que mina**, y por eso el punto 3 mide otro modelo en vez de recortar mas auditoria.

---

## LO QUE SE APLICO

| punto | donde quedo |
|---|---|
| **1. la fase ciega en cuarentena** | `orquestador_forja.sh`: `apertura_ciega` y `verificar_sello` miran `MODO_INSERCION`. **Escenarios `18` y `18b`** del banco, uno por modo |
| **2. el austero declara** | **correccion declarada** en el banco, junto a la regla del austero. **La leccion es mia:** un encargo no puede escribir una regla que contradiga al banco |
| **3. la medicion con Sonnet** | encargo de la `56`, con sus tres cifras y su umbral escrito |
| **4. el corte definitivo** | `config/frentes.json` y `PARALELO.md` seccion `4.d` |

### LO QUE EL AUDITOR HIZO BIEN Y CONVIENE QUE QUEDE ESCRITO

**No eligio entre las dos reglas que se contradecian: paro y las subio**, con sus dos
textos y sus dos fechas, diciendo que `D.13` no lo resolvia **porque una es del banco y la
otra de un encargo**. Esa distincion no estaba escrita en ningun sitio y la hizo bien.

---

# EL CUERPO DE LA PARADA, SIN TOCAR

# PARA ALEXIS: **EL BUCLE SE PARA, Y NO PORQUE ALGO ESTE ROTO**

*Escrito por el auditor al cerrar la `ACTA 54`, que audito la vuelta `55` de la linea serial
(`extraccion-mundo-11`). `AUDITOR_FORJA.md` seccion `3`.*

> ## **LA VUELTA `55` ES BUENA Y SE LA FIRMO ENTERA. LO QUE PARA EL BUCLE ES LO QUE CUESTA, Y LA DECISION NO ES MIA.**

---

## 1. EL MOTIVO, EN UNA TABLA

| condicion de la seccion `3` | se cumple |
|---|---|
| **contradiccion con una regla vigente** que no resuelven las reglas de correccion existentes | **SI** |
| **decision de Alexis**: lo que la casa reserva | **SI**, y es la misma |

**LAS OTRAS CUATRO NO SE CUMPLEN Y LAS MEDI UNA A UNA** (`ACTA 54` `54.7`): doctrina nueva NO,
fallo tecnico repetido NO, credito roto NO, campania consumada NO.

### 1.a. La contradiccion, con sus dos textos delante

| lo que dice | quien lo escribe | cuando |
|---|---|---|
| *si tras DOS vueltas el turno sigue por encima de `8` USD... **el bucle se para** para revisarlo* | el **auditor**, en el encargo de la vuelta `54` | 20 sep 2026 |
| *si un turno pasa de `10` USD... tu acta **lo declara** con el desglose. **No prohibe gastar**: obliga a decir en que* | **tu**, `D.56` | 18 sep 2026 |

**LAS DOS NO PUEDEN GOBERNAR ESTE TURNO: una manda parar y la otra manda seguir declarando.**
`D.13` (entre dos reglas fechadas gana la mas reciente) **no lo resuelve**, porque una es
doctrina tuya y la otra es un encargo de un auditor, **y no estan en el mismo plano.**

**Y NINGUNA DE LAS DOS SALIDAS ES MIA SIN ABSOLVERME:** ignorar el encargo de mi predecesor es
vaciar de valor la unica sede que el protocolo me da (`5.6`), **y ensanchar por mi cuenta la
lista de paradas de la seccion `3` es doctrina nueva**, que es justamente lo que `D.56`
congela.

### 1.b. El disparador, medido y no supuesto

**Estaba anunciado con una vuelta de antelacion.** La `ACTA 53` `53.13` lo escribio asi: *el
disparador de coste del encargo de la `54` va por `1` de `2`. Si el turno de la `55` vuelve a
pasar de `8`, la condicion escrita se cumple y el bucle se para.* El encargo se lo repitio al
extractor, que lo leyo y lo recogio en su `VV.7.e`.

    $ python .v56aud/coste.py
    vuelta  turno                 USD      seg  cerrado
    1       extractor         20.6911     3503  2026-09-20 13:06:30
    1       auditor ciego      6.8138     1029  2026-09-20 13:23:40
    1       auditor           14.0510     1844  2026-09-20 13:54:37
    2       extractor         24.8943     6724  2026-09-20 15:46:42
    2       auditor ciego     10.8811     2616  2026-09-20 16:30:18

    TURNOS CERRADOS EN ESTA CORRIDA                 : 5
    TURNOS POR ENCIMA DE 8 USD                      : 4
    TURNOS POR ENCIMA DE 10 USD (D.56)              : 4
    GASTO SUMADO DE LA CORRIDA, SIN MI TURNO         : 77.3314 USD
      VUELTA 1 (serial 54): 20.6911 USD   PASA de 8
      VUELTA 2 (serial 55): 24.8943 USD   PASA de 8
      VUELTAS SEGUIDAS DE EXTRACTOR POR ENCIMA DE 8 USD: 2

**Se cumple bajo cualquiera de sus dos lecturas:** por turnos de extractor van `2` seguidos por
encima de `8`; por turnos cerrados van `4` de `5`, **y esos mismos `4` pasan tambien tu umbral
de `10`.**

> ### **Y LA CIFRA QUE DE VERDAD PIDE TU DECISION NO ES NINGUNA DE ESAS**
>
> **`77,3314` USD gastados en esta corrida con el grafo exactamente donde lo encontro:** `346`
> nodos al abrir y `346` al cerrar, `740` veredictos y `740`.
>
> **NO ES QUE EL TRABAJO ESTE MAL HECHO. Esta bien hecho y lo he verificado entero.** Es que
> `MODO_INSERCION=cuarentena` y `D.39` hacen que el producto de una vuelta sean candidatos en
> bandeja, no nodos en el grafo. **La bandeja de `grove_high_output` esta en `74` candidatos y
> el grafo lleva sin moverse desde antes de esta corrida.**

---

## 2. EL ESTADO EXACTO

    $ git rev-parse --abbrev-ref HEAD
    extraccion-mundo-11
    $ git rev-parse HEAD
    4f9e3ab   (mas el commit de esta acta, que va detras de esta linea)
    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python forja.py resolutor
    nodos vivos: 346   nodos deprecados (archivo): 0   alias registrados: 0
    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346   740   1
    $ ls cuarentena/grove_high_output/*.json | wc -l
    74
    $ python tests/test_aceptacion.py
      total: 339 pruebas, 2 fallos, 0 errores
    $ python scripts/deuda.py
      pendientes: 19    pagadas: 25       ultima vuelta de saneamiento: 54
    $ python forja.py tablero
      1    7    grove_high_output    COSECHADO    NINGUNO    74  cap_10
      MUNDO 11: faltan 3 de 3 libros del corte (grove_high_output, gerber_emyth, marquet_turn_the_ship)
      COLA DE DOCTRINA (D.56): 11 pregunta(s), 0 bloquea(n)

| | |
|---|---|
| **fase** | la vuelta `55` esta CERRADA y AUDITADA. **No hay ninguna vuelta sin acta**: la `ACTA 54` cubre la `55` y la `53` cubria la `54` |
| **credito de la linea** | `REPORTE 0 de 3`, `CIFRA PUBLICADA 0 de 2`, `CLASE 0 de 2`, `DATO MOVIDO 0 de 2`, `AUDITOR 2 de 3`. **Ninguna especie en su tope** |
| **guardas de DATO** | las cuatro de `D.55` en VERDE: `gate`, el cerrojo, el censo no decreciente y la fidelidad `D.30` (`0` PUENTE de `23` pasos releidos por mi) |
| **lo que produjo la vuelta** | `9` candidatos en `cuarentena/grove_high_output/`, `0 CAERIAN`, `0` inserciones, y las fronteras de `cap_09` y `cap_10` publicadas |

---

## 3. LO QUE NECESITO DE TI

**UNA SOLA DECISION, Y TIENE TRES SALIDAS. Ninguna es mia.**

| salida | que significa | que habria que escribir |
|---|---|---|
| **A. el coste esta bien y el disparador sobra** | `D.56` manda sola: se declara y no se para | **retirar el disparador del `8`** por correccion declarada, y decir si un auditor puede o no escribir condiciones de parada en su encargo |
| **B. el coste no esta bien** | hay que bajarlo antes de seguir | decir por donde. **Lo que domina no es lo que el turno escribe**: la `ACTA 53` `53.10` lo midio en los turnos internos y los tokens de lectura de cache que el reporte de `53.788` lineas arrastra |
| **C. el reparto esta mal** | el bucle gasta en extraer y no inserta | **autorizar la insercion del lote 7**, que es lo unico que convierte `74` candidatos en nodos. Hoy `MODO_INSERCION=cuarentena` y `D.39` lo impiden, **y eso es autorizacion tuya, no default** |

> **MI RECOMENDACION, Y LA DOY PORQUE ME LA PIDE `3` Y NO PORQUE DECIDA YO:** la **C**, y
> despues la **A**. El disparador del `8` no esta midiendo un derroche: esta midiendo que un
> turno de esta casa cuesta lo que cuesta y que **lo que falta no es gastar menos, es cerrar el
> lote**. La bandeja esta en `74` candidatos con `0 CAERIAN` y una cola de lectura medida; **lo
> que no hay es una vuelta que los haga entrar.**

### 3.a. **Y DOS AVERIAS QUE NO PARAN PERO QUE SOLO PUEDES ARREGLAR TU**, porque `D.45` veda su sede

| id | que es | por que sube |
|---|---|---|
| **`d067`** | dos pruebas de aceptacion clavan el registro VIVO (`tests/test_aceptacion.py` lineas `3703` y `3733`): afirman `ultima_saneamiento() == 49` y el registro ya dice `54`. **Segunda vuelta seguida en rojo por la misma causa** | **no se destasca solo**: va a fallar todas las vueltas hasta que alguien toque `tests/`, y `D.45` lo veda |
| **`d071`** | `D.58` dice que en regimen ligero **no hay fase ciega, ni sello, ni testigo**, y el arnes hizo las tres **en las dos vueltas de esta corrida** | el arnes es sede vedada por `D.45`. **La fase ciega de la `55` costo `10,8811` USD**, asi que no es solo una discrepancia de letra |

---

## 4. COMO RETOMAR

1. **Escribe tu decision en `docs/loop/paradas/`**, con su fecha. Si la decision toca el
   credito, dilo ahi: **la racha no la reinicia nadie mas que tu** (`5.4`), y hoy `AUDITOR` va
   por `2 de 3`.
2. **`docs/loop/PROMPT_SIGUIENTE.md` esta VACIO a proposito.** El arnes no abre vuelta sin la
   linea `LIBRO DE ESTA VUELTA` (`D.49`), asi que mientras siga vacio el bucle no arranca.
3. **Para reanudar sin mas**, escribe el encargo de la vuelta `56` con su linea de libro y
   relanza el orquestador. El estado esta limpio y verde: **no hay nada que reparar antes.**
4. **Si la decision es la salida C**, la vuelta `56` es de INSERCION y no de extraccion, y
   entonces vuelven a correr enteras la relectura de fidelidad del lote y la vara de continua
   contra repite sobre las `43` vecindades que la `55` dejo medidas (`REPORTE.md` `VV.9.a`).

**EL BUCLE NO FUNDE RAMAS Y EL BUCLE NO CREA REMOTOS.** Esta rama sigue siendo
`extraccion-mundo-11` y no he pedido ningun merge: el mundo `11` sigue en `3` de `3` libros
pendientes, asi que **esto no es la parada feliz.**
