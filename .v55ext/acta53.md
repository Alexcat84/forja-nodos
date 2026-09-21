# ACTA 53. VUELTA 54, lote 7 (`grove_high_output`), **VUELTA DE SANEAMIENTO EN REGIMEN LIGERO, LA PRIMERA BAJO `D.58`**: **LA VUELTA PAGA LO QUE SE LE PIDIO Y SUS MEDICIONES ME SALEN AL DIGITO; LO QUE SE CAE ES LA CONCLUSION DE SU TAREA MAS GRANDE**. Le verifico con mis comandos las cuatro guardas, el estado (`346`, `740`, `1`, `65`), la deuda (`17` y `25`) y el credito; **reproduzco sus mediciones de pago una a una**: los `6` commits de `d047` dan los seis `f33c8d9c`, la tasa de `d033` la extiendo de `0` de `12` a **`0` de `17`** con cinco corridas mias, los `15` informes de `cap_03` me dan sus **`6` / `9` / `0`** con los seis nombres y sus poblaciones de `358` a `371`, los `7` de `cap_02` me dan **`7` `BLOQUEARIAN` de `7`** sobre `414` con `1997` s y `17` vecindades, y **la banda de `d058` me sale identica al decimo** (`83,2` por ciento agregado, `372840` sobre `448080`, de `54,8` a `96,2`). **Y LE FIRMO LA MEDICION QUE SOSTIENE TODA SU TAREA 4**: `huella_de_nodo` da `d228fe61d4d02678` **con los dos `U+0008` y sin ellos**, corrido por mi. **De sus DIEZ discutibles marcados se sostienen NUEVE y CAE UNO, el `1`, que es la conclusion de fondo de la vuelta**: su *especie vieja en sede sin casillero* es falsa, porque **`DATO MOVIDO` tiene `dataset/` por sede desde el 16 sep y la `ACTA 38` `6` ya cargo ESTE MISMO EJEMPLAR en ella**, con su tension escrita delante. Vive en CABECERA, en la TABLA de `D.52` y en la CONCLUSION de `PP.5.c`, asi que **`REPORTE` sube de `0 de 3` a `1 de 3`**. Sus otras dos caidas son **de PROSA y NO acumulan**: la misma ruta `.v54/deuda_cierre.txt` pegada dos veces con **`16` / `23` y `17` / `25`**, y un *el barrido cubre toda la cuarentena* que midio `575` de `577`. `CIFRA PUBLICADA` sale **LIMPIA** y baja de `1 de 2` a **`0 de 2`** por `D.38.1`; `CLASE` y `DATO MOVIDO` salen **LIMPIAS** con su motivo medido: `740` contra `740` y `git diff` vacio sobre `dataset/`, `bitacora/`, `censos/`, `config/`, `esquema/`, `src/`, `scripts/`, `tests/`, `hooks/` y el banco. **TRAIGO DE MI FASE CIEGA LA ADJUDICACION QUE FALTABA**: su discutible `7`, el par `construir_flujo_produccion_paso_limitante` contra `rehacer_flujo_paso_limitante_capacidad`, **lo adjudico CONTINUA y no duplicado**, leido por los pasos antes de ver su informe. **Y DESENTIERRO LO QUE MAS VALE Y NO ES CAIDA DE NADIE DEL BUCLE: `D.58` DICE QUE EN LIGERO NO HAY FASE CIEGA, NI SELLO, NI TESTIGO, Y ESTA CORRIDA HIZO LAS TRES**, medidas en el log, **y la fase ciega costo `6,81` USD contra un objetivo escrito de `5`**. **Y LA CAIDA QUE PESA ES MIA Y ES UNA CIFRA DE MI PAGINA SELLADA**: publique `rancios 4` donde **el instrumento, en el fichero que yo mismo guarde, imprime `RANCIO 71`**. **`AUDITOR` sube de `0 de 3` a `1 de 3`**, lo subo yo. Ninguna condicion de parada se cumple y las mido una a una: **no escribo `PARA_ALEXIS.md`**, y el encargo de la vuelta `55` sale de esta sede.

## 53.0. **HUECO DE ACTA Y HERENCIA** (`1.0`, `D.40`)

**NO HAY HUECO.** La `ACTA 52` cubre la vuelta `53` y yo cubro la `54`, la inmediatamente
siguiente. **HEREDADOS: `0`**, declarado en mi apertura sellada seccion `0` y comprobado hoy
contra el mismo instrumento, que devuelve la misma huella que el prompt me entrego.

<!-- TALLADO: parcial salida=.v55aud/herencia.txt -->

    $ python forja.py herencia
      acta anterior : ACTA 52. VUELTA 53, lote 7 (`grove_high_output`), `cap_06` y la cabeza de `cap_07` ...
      su huella     : d5f4eb832cb0ffd11ddaf35a5bf406e4e2b5f231
      heredados     : 0

## 53.1. **LO QUE VERIFICO AL DIGITO, CON MIS PROPIOS COMANDOS**

*Modo austero (`D.47`): lo que el `loop.log` ya registro no se repite. Va lo que **yo** corri.*

<!-- TALLADO: parcial salida=.v55aud/guardas.txt -->

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python forja.py resolutor
    nodos vivos: 346   nodos deprecados (archivo): 0   alias registrados: 0
    $ python tests/test_aceptacion.py
      total: 339 pruebas, 2 fallos, 0 errores
    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346   740   1
    $ ls cuarentena/grove_high_output/*.json | wc -l
    65
    $ python scripts/deuda.py
      pendientes: 17    pagadas: 25       ultima vuelta de saneamiento: 54

**Los pagos, reproducidos uno a uno y no leidos de su reporte.** *Tabla de mi propia corrida;
cada fila lleva la ruta del fichero que la imprime.*

| lo que la vuelta publica | lo que me sale a mi | ruta de mi corrida |
|---|---|---|
| `d047`: los `6` commits dan `f33c8d9c` | **los seis, identicos** | `.v55aud/d047_seis_commits.txt` |
| `d033`: `0` ROJO de `12`, `19,0` s | **`0` ROJO de `17`**, `18,9` s, con `5` corridas mias encima | `.v55aud/d033_tasa_auditor.txt` |
| `d005`: `6` BLOQUEARIAN, `9` ENTRARIAN, `0` CAERIAN de `15` | **`6` / `9` / `0`, y los seis nombres coinciden** | `.v55aud/d005_recuento.txt` |
| `d005`: `14` de `15` fichas intactas | **`14` de `15`**, y la tocada es `variar_frecuencia_inspeccion_nivel_calidad`, un `ENTRARIA` | `.v55aud/d005_recuento.txt` |
| `d024`: `7` BLOQUEARIAN de `7` sobre `414`, `1997` s, `17` vecindades | **`7` / `0` / `0`, poblacion `414` en los siete, `17` vecindades, y los siete relojes suman `1997`** | `.v55aud/d024_recuento.txt` |
| `d058`: `83,2` por ciento agregado, banda `54,8` a `96,2` | **identico al decimo**, numerador `372840` y denominador `448080` | `.v55aud/d058_recuento.txt` |
| `d068`: `--clase 58` da `LIBRE` y `--clase 59` da `SANEAMIENTO` | **las dos, corridas hoy** | `.v55aud/clase_58_59.txt` |

**Y LE FIRMO LA MEDICION QUE SOSTIENE SU TAREA MAS GRANDE**, porque de ella cuelga toda la
segunda mitad de la pregunta `11`:

<!-- TALLADO: parcial script=.v55aud/huella_p11.py salida=.v55aud/huella_p11.txt -->

    $ python .v55aud/huella_p11.py
    U+0008 en crudo                  : 2
    U+0008 en texto_comparable       : 0        largo comparable 12208
    huella con los dos controles     : d228fe61d4d02678
    huella SIN los dos controles     : d228fe61d4d02678
    cambia la huella al quitarlos?   : NO

**Y SU BARRIDO DE `4` COINCIDENCIAS LO REPITO ENTERO CON MI PROPIO CODIGO**:

<!-- TALLADO: parcial script=.v55aud/p11_barrido_propio.py salida=.v55aud/p11_barrido_propio.txt -->

    $ python .v55aud/p11_barrido_propio.py
    nodos del grafo barridos              : 346
    fichas .json bajo cuarentena/ barridas: 577  (SIN excluir _derivadas)
    documentos barridos                   : 923
    caracteres de control ENCONTRADOS     : 4

**Las mismas `4`, en las mismas dos posiciones (`5162` y `5166`) y en las mismas dos sedes.**
Su hallazgo es correcto; lo unico que no reproduce es su denominador, y eso va en `53.7`.

**LO QUE NO REPRODUZCO Y DIGO POR QUE:** no relanzo los `7` informes de `d024` ni los `15` de
`d005`. Los de `d024` costaron **`1997` s de reloj medidos en `.v54/d024_reloj.txt`**, y los
de `d005` son de `.v2g/`, de otra vuelta. **Los verifico leyendo los ficheros que las dos
corridas dejaron**, que es lo que `1.1` me pide cuando el instrumento no cabe en el turno.

## 53.2. **`PASOS INVENTADOS POR CAPITULO`** (seccion `8`): **SIN SUPERFICIE, Y LA FILA SE ESCRIBE IGUAL**

**`8` dice que no es opcional. Tambien dice que el denominador son los pasos que la vuelta
escribio**, y esta vuelta escribio cero. **No lo afirmo: lo corro**, que es lo que `D.40`
pide de un `NO APLICA`.

<!-- TALLADO: parcial script=.v55aud/acta53_cifras.py salida=.v55aud/acta53_cifras.txt -->

    $ python .v55aud/acta53_cifras.py
    3. PASOS INVENTADOS POR CAPITULO (AUDITOR_FORJA.md 8), VUELTA 54
       $ git diff --name-only e63f5af..HEAD -- cuarentena/
       fichas de cuarentena creadas o modificadas por la vuelta 54 : 0
       LA FILA POR CAPITULO, y el denominador es 'pasos ESCRITOS POR LA VUELTA 54':
         cap_02  pasos vivos en bandeja  50  |  pasos escritos por la 54: 0  ->  fila SIN SUPERFICIE
         cap_03  pasos vivos en bandeja 121  |  pasos escritos por la 54: 0  ->  fila SIN SUPERFICIE
         cap_04  pasos vivos en bandeja 156  |  pasos escritos por la 54: 0  ->  fila SIN SUPERFICIE
         cap_05  pasos vivos en bandeja  84  |  pasos escritos por la 54: 0  ->  fila SIN SUPERFICIE
         cap_06  pasos vivos en bandeja  62  |  pasos escritos por la 54: 0  ->  fila SIN SUPERFICIE
         cap_07  pasos vivos en bandeja   6  |  pasos escritos por la 54: 0  ->  fila SIN SUPERFICIE
         TOTAL      pasos vivos en bandeja 479  |  pasos escritos por la 54: 0

**`LECTURA`: LA CIFRA QUE DIMENSIONA EL LOTE SIGUIENTE ES LA DE LA `ACTA 52`**, `0,0` por
ciento en `cap_06`, `cap_07` y `cap_08`, **y no la toco**: una vuelta sin superficie no puede
mover un volumen ni hacia arriba ni hacia abajo. **Ninguna fila pasa del tope de `10`.**

**Y LA FIDELIDAD `D.30`, QUE SI ES UNA DE LAS CUATRO QUE BLOQUEAN, NO SE DECLARA VERDE: SE
DECLARA SIN OBJETO.** El propio reporte lo dijo asi en `PP.0.b` y **le doy la razon**: una
guarda sin superficie que medir no esta verde, esta sin objeto. **`0` pasos escritos, `0`
pasos que cotejar, y la muestra de `D.58` no tiene de que sacar semilla.**

## 53.3. **LA MUESTRA PINEADA DE LOS `SANO`** (seccion `7`): **SIN POBLACION, Y MEDIDO**

<!-- TALLADO: parcial script=.v55aud/acta53_cifras.py salida=.v55aud/acta53_cifras.txt -->

    $ git diff --numstat e63f5af..HEAD -- bitacora/VEREDICTOS.jsonl
    lineas de veredicto anadidas por la vuelta 54 : 0
    veredictos SANO de la tanda                   : 0  ->  no hay poblacion que muestrear

**`7` lo dice con todas sus letras: no se inventa una muestra donde no hay poblacion.** La
vuelta no escribio un veredicto, y el `740` contra `740` de `53.8` es la otra cara de la misma
medida.

## 53.4. **LA RELECTURA CIEGA: SUS DIEZ DISCUTIBLES MARCADOS** (`5.1`)

*Austero (`D.47`): por numero y por su renglon, sin reabrir el argumento que el reporte ya
escribio. Lo que va aqui es **mi** veredicto y **lo que lo sostiene**. Tabla de lectura mia,
sin cifra derivada: las que lleva estan impresas en `53.1` por sus instrumentos.*

| # | que marco | mi veredicto | lo que lo decide |
|---:|---|---|---|
| `1` | la pregunta `11` es **especie vieja en sede sin casillero** y no una cuarta especie | **CAE** | `53.6` entero: **`DATO MOVIDO` tiene `dataset/` por sede** y la `ACTA 38` `6` ya cargo este mismo ejemplar |
| `2` | el sitio es `D.42` y **no una quinta guarda de dato** | **SE SOSTIENE** | las cuatro de `deuda.py` las repaso yo contra el ejemplar: `gate` VERDE con los dos vivos dentro, la huella no se mueve, `texto_comparable` da `0`, y `D.30` cuenta pasos y el defecto esta en `resumen_teorico` |
| `3` | pagar `d007` **por la mitad** | **SE SOSTIENE** | `d007` escribe dos oraciones y solo una es una accion. *La cola queda congelada* es un ESTADO que sostiene `D.56`; *la `11` se clasifica con un ejemplar delante* es la accion, y se hizo |
| `4` | la tasa de `d033`, **que no acota por abajo**, y aun asi cierra la deuda | **SE SOSTIENE** | `d033` pedia la tasa, no el arreglo, y lo escribe con estas palabras: *sin tasa medida no se sabe si es una corrida intermitente o un fallo real*. **La extiendo**, y el dato va en `53.1` |
| `5` | dejar `d011` y `d012` abiertas **pudiendo cerrarlas** | **SE SOSTIENE, y su autoacusacion es mas dura de lo que la medida aguanta** | no hay contradiccion con el `3`: `d007` tenia una accion discreta y se hizo; `d011` es una obligacion permanente y `d012` un ejemplar registrado, **y ninguna de las dos se termina**. Y `53.9` refuerza `d012`: su superficie **no** ha desaparecido |
| `6` | el `6` de `cap_03` es un **SUELO** | **SE SOSTIENE** | mi recuento da `14` de `15` fichas con un solo commit, y la unica tocada es un `ENTRARIA` cuyo `resumen_teorico` **crecio**: empuja hacia `BLOQUEARIA`, no al reves |
| `7` | `construir_flujo` contra `rehacer_flujo` es **la vecindad mas seria de las `17`** | **SE SOSTIENE AL DIGITO, Y LA ADJUDICO YO** | es **el unico par de los `17` levantado por DOS seniales** y el unico mutuo, comprobado sobre los siete informes. Mi clase va en `53.5` |
| `8` | los `2` fallos **NO son la causa de la parada de la `53`** | **SE SOSTIENE** | `test_caso_negativo_el_encargo_que_declara_el_que_toca_pasa` **pasa hoy**; las dos que fallan son otras y por otro mecanismo. El contador de *la misma causa* va por `1`, no por `2` |
| `9` | `26,06` USD como **el contraste bueno** | **SE SOSTIENE** | lo recomputo del log y sale al centavo. Y le anado en `53.10` la celda que su turno no podia citar |
| `10` | no relanzar los `15` de `cap_03` amparandose en `D.43` | **SE SOSTIENE EL RESULTADO, Y DIGO QUE LA CITA NO ES LA QUE LO SOSTIENE** | `D.43` extendida (`EXTRACTOR.md` `2`) **si** cubre la cola por candidato, pero **cubriria igual a los `7` de `cap_02` que la vuelta si lanzo**. Lo que separa a unos de otros es el mandato de `d024` contra el de `d005`, no `D.43` |

> **`9` SE SOSTIENEN Y `1` CAE. LA UNICA QUE CAE ES LA QUE EL EXTRACTOR PUSO LA PRIMERA Y
> DESCRIBIO COMO *la decision de fondo de toda la tarea*.** Eso es exactamente lo que `5.1`
> llama informativo: **sabia donde estaba su duda.** No lo absuelve, y lo digo para que no se
> lea como absolucion: **la caida cuenta igual.**

## 53.5. **LA ADJUDICACION QUE TRAIGO DE MI FASE CIEGA, Y CIERRA SU DISCUTIBLE `7`**

**Mi pagina sellada `5.c` clasifico los `7` candidatos de `cap_02` leyendo sus `50` pasos
contra las `79` lineas de `cap_02.md`, ANTES de ver el reporte y antes de correr ninguna
senial** (`APERTURA_CIEGA.md` `5.b`, donde declaro el orden en que lo hice). **El par que el
reporte marca como el mas serio de las `17` es el mismo que yo adjudique a ciegas.**

> ### **`rehacer_flujo_paso_limitante_capacidad` CONTINUA de `construir_flujo_produccion_paso_limitante`. NO ES DUPLICADO.**
>
> **Con direccion y sin bascula** (`6.1`): la pregunta va del hijo a la madre. El hijo toma de
> la madre **un paso**, el calculo hacia atras; lo que queda fuera **es procedimiento en los
> dos lados**. En el hijo: detectar el supuesto de capacidad infinita, buscar donde hay cola,
> **contar el tiempo de espera dentro del flujo**, dejar iguales los ciclos que la cola no
> toca y no cambiar de componente el que manda la calidad. En la madre: los cuatro requisitos
> basicos, el descarte de la carta blanca, el tiempo total de paso y el escalonado.
> **Condiciones de activacion distintas**: la madre, *todavia no sabes por cual empezar*; el
> hijo, *ya tienes flujo y aparece un turno de espera*.
>
> **Y NO LA ADJUDICO CITANDO UNA SENIAL** (`D.19`). Las dos seniales que levantan el par
> dijeron donde mirar y ahi acabo su trabajo.

**LO QUE ESTO LE AHORRA A LA VUELTA DE LA INSERCION:** el reporte lo dejo *nombrado para que
el dia de la insercion se lea el primero*. **Ya esta leido.** La arista madre a hijo queda
justificada por ese paso, y **eso es una lectura menos de las `17`.**

### 53.5.a. **Y LA OTRA MITAD DE MI PAGINA CIEGA LA CONFIRMA SU PROPIO INSTRUMENTO, POR EL LADO CONTRARIO**

Mi `7.b` publico que **ninguna senial levanta `construir_flujo_produccion_paso_limitante`
contra `identificar_paso_limitante_jornada_desfases`**, medido corriendo el informe del hijo.
**El informe que la vuelta corrio para `d024` es el de la MADRE, y tampoco lo levanta:**

<!-- TALLADO: parcial salida=.v55aud/d024_recuento.txt -->

    $ grep 'vecino' .v54/d024_construir_flujo_produccion_paso_limitante.txt
        vecino retirar_barreras_politicas_metodo  [levantada por: paso_contra_nodo]
        vecino rehacer_flujo_paso_limitante_capacidad  [levantada por: similitud_texto, familia_id]
        vecino preferir_inspeccion_proceso_prueba_destructiva  [levantada por: similitud_texto]

**`LECTURA`: dos corridas independientes, una por cada extremo, y el par no aparece en ninguna
de las dos.** Mi hallazgo ciego queda comprobado **por el instrumento de la vuelta que
audito**, que es la unica forma de comprobarlo que no depende de mi. **Va a `DEUDA`**, porque
se cobra el dia de la insercion y no hoy.

## 53.6. **LA CAIDA DE `REPORTE`, Y SUBE A `1 de 3`: LA PREGUNTA `11` SI TIENE CASILLERO, Y YA SE COBRO UNA VEZ**

**Lo que el reporte publica**, en `PP.4.d` y repetido en `PP.5.c` `2` y en la fila `4` de su
tabla `D.52`:

> *la tabla solo da `dataset/` a **CLASE**, que es un veredicto mal puesto*

**ES FALSO, Y LA FILA QUE LO DESMIENTE ESTA EN `5.2` DE MI PROTOCOLO, EN EL BLOQUE QUE LA
ENCABEZA:**

> **`DATO MOVIDO`: una operacion que cambia `dataset/`, `bitacora/` o `censos/` sin que ningun
> veredicto este mal puesto.**

**Y NO ES UNA ESPECIE TEORICA PARA ESTE EJEMPLAR: ES LA QUE YA LO COBRO.** La `ACTA 38`
seccion `6` cargo **estos dos mismos `U+0008`**, en esta misma sede, con esta misma tension
razonada delante:

> *LA LECTURA QUE ME SALVARIA DE CARGARLA, Y NO LA TOMO: son dos caracteres invisibles y no
> cambian ninguna decision. Es verdad y no basta. El dano es real, su sede es `dataset/`, y
> ningun veredicto esta mal puesto. Ese es el casillero.*

**LA PRUEBA DE QUE EL REPORTE PODIA VERLO ES QUE LO TENIA PEGADO DOS VECES EN SU PROPIA
PAGINA:** su `PP.0.c` y su `PP.5.h` publican la tabla del credito, **y las dos llevan la fila
`DATO MOVIDO 0 de 2`.** No es una regla escondida en el banco: **es una linea de la salida que
el propio reporte pego al abrir y al cerrar.**

### 53.6.a. **LA PARTE DE SU LECTURA QUE SI SOBREVIVE, Y LA SEPARO PARA NO TIRARLA CON EL RESTO**

**Su distincion de fondo es buena y la recojo**: `DATO MOVIDO` cobra **la operacion** que
escribio los dos caracteres, y la cobro una vez, en la vuelta `39`. Lo que el reporte mide es
**el defecto que quedo en pie**, que es otro objeto y que **ninguna guarda encuentra por
construccion**. **Esa medicion es suya, es correcta y no se la quito.**

**LO QUE CAE NO ES LA MEDICION: ES LA FRASE QUE LA CORONA.** Decir *sede sin casillero* cuando
el casillero existe y tiene un cobro escrito es la figura que `D.38.3` ensanchada nombra con
todas sus letras: **la cifra es cierta y lo falso es la frase.** Y aqui pesa mas que de
costumbre, porque **la frase ES el entregable**: la tarea pedia clasificar, y la clase es lo
que se publica.

### 53.6.b. **MI ADJUDICACION DE LA PRIMERA MITAD DE LA PREGUNTA `11`, Y NO ABRE PARADA**

> **NO HACE FALTA ESPECIE NUEVA. EL DEFECTO DE ESTE EJEMPLAR CABE EN `DATO MOVIDO`**, que
> tiene `dataset/` por sede y que ya lo cobro con su cita (`ACTA 38` `6`). **Adjudico citando
> una regla escrita**, que es lo que `3` me manda hacer antes de considerar una parada.

**Y LO QUE NO ADJUDICO, PORQUE NO ES MIO:** meter `dataset/` en la columna de `CIFRA
PUBLICADA`, o ensanchar la clausula de `5.5` de RUTA a COMANDO CITADO. **Las dos cambian la
metrica de credito, y la metrica es de Alexis.** `D.56` congela la cola, la pregunta `11` se
queda dentro **CLASIFICADA y no adjudicada**, y eso **no es una parada**: `D.56` lo dice con
sus palabras, *registrala con su medida y dejala ahi*.

### 53.6.c. **DONDE VIVE, QUE ES LO QUE DECIDE SI ACUMULA** (`5.2`)

*Tabla de localizacion, sin cifras: son tres sedes nombradas por su rotulo.*

| sede | que dice ahi |
|---|---|
| **CABECERA**, fila `PP.4` del esqueleto | *clasificado como especie vieja en sede sin casillero y no como cuarta especie* |
| **TABLA** de `D.52`, fila `4`, en `docs/loop/TABLA_DE_CIERRE.txt` | la misma frase, palabra por palabra |
| **CONCLUSION**, `PP.5.c` punto `2` | *Si hay hueco... Faltan dos lineas* |

**Las tres son de las que acumulan. `REPORTE` sube de `0 de 3` a `1 de 3`.** **Y la subo con
la racha recien reiniciada por el fundador**, lo que la hace la primera de su serie nueva:
**lejos del tope, y lo digo para que no se lea como alarma.**

## 53.7. **LAS DOS CAIDAS DE PROSA, QUE REGISTRO Y NO ACUMULAN** (`5.2`, ultima fila)

<!-- TALLADO: parcial script=.v55aud/dos_caidas_de_reporte.py salida=.v55aud/dos_caidas_de_reporte.txt -->

    $ python .v55aud/dos_caidas_de_reporte.py
    A. LA MISMA RUTA PEGADA DOS VECES CON DOS SALIDAS DISTINTAS
       linea 52559 del fichero: <!-- TALLADO: parcial salida=.v54/deuda_cierre.txt -->
            -> pega: pendientes: 16    pagadas: 23
       linea 52722 del fichero: <!-- TALLADO: parcial salida=.v54/deuda_cierre.txt -->
            -> pega: pendientes: 17    pagadas: 25
       $ grep -n 'pendientes:' .v54/deuda_cierre.txt   (la ruta que las dos citan, hoy)
            4:  pendientes: 17    pagadas: 25

    B. EL DENOMINADOR DEL BARRIDO DE LA PREGUNTA 11
       linea 52151: fichas de cuarentena barridas : 575  (ficheros .json bajo cuarentena/)
       $ find cuarentena -name '*.json' | wc -l
            577
       $ ls cuarentena/_derivadas/*.json | wc -l
            2

**`A`.** El `16` / `23` de `PP.5.a` **fue cierto cuando se corrio** y es un estado intermedio
real, pero **la ruta que lo respalda ya no lo contiene**, y su propia tabla de cinco pagos no
cuadra con el: `23` pagadas son cuatro pagos, y la tabla lista cinco. **El cierre bueno es el
de `PP.5.g`, y me sale identico.** Vive en un pegado de instrumento, no en TABLA ni en
CABECERA ni en CONCLUSION: **registra y NO acumula.**

**`B`.** El numerador es correcto: **mi barrido independiente sobre los `923` documentos
encuentra las mismas `4` coincidencias, en las mismas posiciones.** Lo falso es el rotulo y la
frase que lo corona, *el barrido cubre el grafo entero y toda la cuarentena*: **midio `575` de
`577`**, dejando fuera `cuarentena/_derivadas/`. **Las dos que faltaban las barri yo y estan
limpias, asi que la conclusion no se mueve.** Es prosa de acompanamiento: **registra y NO
acumula.**

> **POR QUE NO LAS SUBO A LA RACHA, DICHO ANTES DE QUE SE LEA COMO INDULTO:** `5.2` reparte
> por **sede**, no por gravedad, *y eso fue lo que evito que el bucle parara por una frase
> mientras los datos estaban intactos*. **Las dos quedan con su nombre escrito**, que es lo
> unico que `5.4` les quita: congelar el contador.

## 53.8. **`CIFRA PUBLICADA`, `CLASE` Y `DATO MOVIDO`: LAS TRES LIMPIAS, CON SU MOTIVO MEDIDO**

<!-- TALLADO: parcial salida=.v55aud/dato_movido.txt -->

    $ git diff --stat e63f5af..HEAD -- dataset/ bitacora/ censos/ config/ esquema/ \
                                       src/ tests/ scripts/ hooks/ docs/BANCO_DE_REGLAS.md
    (sin salida: ni un fichero)

- **`CLASE` LIMPIA:** `740` veredictos contra `740`. **Esta vuelta no escribio ni uno**, y la
  identidad de los cuatro contadores es el entregable de una vuelta de saneamiento, no una
  casualidad. **`0 de 2`.**
- **`DATO MOVIDO` LIMPIA:** el `git diff` de arriba no imprime un solo fichero de `dataset/`,
  `bitacora/` ni `censos/`. **`0 de 2`.**
- **`CIFRA PUBLICADA` LIMPIA, y BAJA de `1 de 2` a `0 de 2`.** Reviso sus escrituras en
  `docs/loop/DEUDA.jsonl`, que es sede de `5.2` **por mi propia adjudicacion de la `ACTA 49`
  `48.9.b`**: los pagos de `d047`, `d033` y `d024` los reproduzco al digito en `53.1`, `d068`
  me sale corriendo sus dos clases hoy, y `d067` **la corrigio la propia vuelta con `d069`
  antes de que yo llegara**, separando lo que midio de lo que infirio. **No encuentro una
  cifra falsa en sede duradera.** Baja **por la tanda limpia de `5.4` y `D.38.1`, no por
  indulto mio.**

## 53.9. **LO QUE DESENTIERRO, Y NO ES CAIDA DE NADIE DEL BUCLE: `D.58` MANDA TRES COSAS QUE ESTA CORRIDA NO CUMPLIO**

**`D.58` es tajante:** en `MODO_INSERCION=cuarentena`, *NO hay fase ciega, NO hay sello y NO
hay testigo.* **Las tres ocurrieron**, y no las deduzco: estan en el registro.

<!-- TALLADO: parcial script=.v55aud/d58_contra_el_arnes.py salida=.v55aud/d58_contra_el_arnes.txt -->

    $ python .v55aud/d58_contra_el_arnes.py
      4173:[2026-09-20 12:08:04] arranque: rama extraccion-mundo-11, MODO_INSERCION=cuarentena
      4190:[2026-09-20 13:06:31] VUELTA 1 : APERTURA CIEGA (claude-opus-5), retirados: ...
      4209:[2026-09-20 13:23:47]   apertura ciega sellada: deb1a434ca921f6da5ea087833bce388d85e3a8a
      fecha del testigo : 2026-09-20 13:23:41   guardas: gate, guiones, censo_rutas, citas_de_credito

      LAS TRES QUE D.58 QUITA DEL REGIMEN LIGERO, CONTADAS EN ESTA CORRIDA:
        fase ciega abierta : 1     sello escrito : 1     testigo escrito : 1
      [2026-09-20 13:23:40] auditor ciego listo (USD 6.8138440000000005), 1029s

**`LECTURA`: EL EXTRACTOR NO PODIA SABERLO Y NO SE LO CARGO.** Su `PP.2.e` escribio *la fase
ciega no ha vuelto a abrirse en esta corrida* a partir del log, **y era cierto al
escribirlo**: el arnes abrio la suya **un segundo despues** de que su turno cerrara. **Su
lectura de la doctrina era la correcta; lo que no la cumple es la maquina.**

**LO QUE SI CAMBIA, Y POR ESO NO ES UNA CURIOSIDAD:**

| | |
|---|---|
| **`d012` se refuerza** | su motivo escrito (*la fase ciega no existe en ligero*) es falso, **y la deuda se sostiene mejor sin el**: la superficie de la pregunta `9` no ha desaparecido, **sigue abriendose cada vuelta** |
| **el coste tiene un sumando que la doctrina daba por retirado** | **`6,81` USD y `1029` s**, contra un objetivo escrito de `5` por turno |
| **`D.45` me veda el arreglo** | el arnes es suyo. **Lo declaro, lo agendo y no lo toco** |

**NO ES PARADA Y LO MIDO CONTRA LA LETRA:** no es una guarda de DATO (`D.55` cierra esa lista
en cuatro), no bloquea nada, y la regla de correccion que le corresponde existe y es `D.55`:
**se agenda.** Queda como **`d071`**.  *El numero lo asigna `scripts/deuda.py`, no yo: se lo pedi al cerrar y devolvio `d071` y `d072`.*

## 53.10. **EL COSTE DEL TURNO, QUE ES LO QUE ESTA VUELTA VENIA A MEDIR** (`D.55`, y el encargo de la `54`)

**El reporte dijo, con razon, que su propia celda no podia citarla porque el arnes la escribe
al cerrar. Yo si puedo: la escribio a las `13:06:30`.**

<!-- TALLADO: parcial script=.v55aud/coste_corrida.py salida=.v55aud/coste_corrida.txt -->

    $ python .v55aud/coste_corrida.py
      linea de arranque que acota la corrida : [2026-09-20 12:08:04] MODO_INSERCION=cuarentena
      TURNOS CERRADOS DE ESTA CORRIDA, celda a celda y sin media: 2
        2026-09-20 13:06:30  extractor      cuarentena    20.6911 USD    3503 s
        2026-09-20 13:23:40  auditor ciego  cuarentena     6.8138 USD    1029 s
      suma USD de los turnos cerrados de esta corrida : 27.5049
      LA VARA: media USD/turno de extractor en insertar : 26.06 USD
        numerador   990.29  suma de USD de esos turnos
        denominador 38  turnos de extractor en insertar
        el mas barato 7.3521   el mas caro 62.1116
      EL TURNO DE EXTRACTOR DE ESTA CORRIDA             : 20.6911 USD
      CAIDA contra esa vara                             : -20.6 por ciento
      CONTRA EL OBJETIVO ESCRITO DE 5 USD               : 4.14 veces el objetivo
      CONTRA EL DISPARADOR ESCRITO DE 8 USD             : 1 de los 2 turnos cerrados lo pasan

**LAS TRES COSAS QUE ESTO DICE, Y NINGUNA ES LA QUE EL ENCARGO ESPERABA.** *Todas las cifras
del parrafo las imprime `.v55aud/coste_corrida.py`, arriba.*

1. **EL LIGERO SI BAJA EL COSTE:** `20,6911` contra una vara de `26,06`, **un `20,6` por
   ciento menos**. Es una mejora real y medida.
2. **Y AUN ASI ESTA A `4,14` VECES DEL OBJETIVO ESCRITO, EN UNA VUELTA QUE NO MINO NI INSERTO
   NADA.** El propio reporte lo aviso: *esta vuelta juega con ventaja porque no mina.*
3. **EL DISPARADOR DE `8` USD ESTA A UNA VUELTA DE CUMPLIRSE.** El encargo lo escribio asi:
   *si tras DOS vueltas el turno sigue por encima de `8`, el auditor lo declara con el
   desglose y el bucle se para para revisarlo.* **Esta es la PRIMERA**, y va por encima.

**EL DESGLOSE, QUE `D.55` PIDE CUANDO UN TURNO PASA DE `10`**, leido de
`docs/loop/ultimo_extractor.json` y no estimado: **`149` turnos internos, `28.614.782` tokens
de lectura de cache, `310.695` de escritura de cache y `131.014` de salida.** **`LECTURA`: lo
que domina no es lo que el turno escribe, es lo que vuelve a leer en cada iteracion**, y eso
escala con el numero de turnos internos, no con el tamano del lote. **Una vuelta que no mino
nada gasto `149` turnos internos.**

> **Y UNA CORRECCION MIA, HECHA ANTES DE PUBLICAR Y DICHA IGUAL** (`D.59` es exactamente
> esto): mi primer corte acoto la corrida por `MODO_INSERCION=cuarentena` y me dio `35`
> turnos, porque **hay `33` del `10` y el `11` sep anteriores a `D.58`**. La cifra habria sido
> falsa y el parrafo la habria vestido de instrumento. **Lo que acota esta corrida es su linea
> de arranque, no su variable de entorno**, y `.v55aud/coste_corrida.py` lleva ese motivo
> escrito en su cabecera.

## 53.11. **MI PROPIA TANDA: CAE, Y LA CAIDA ES UNA CIFRA DE MI PAGINA SELLADA**

**`CIFRA PUBLICADA PROPIA`** (`5.5` de mi protocolo, `D.38.2`). No me la caza nadie: me la
cazo remidiendo mi propia pagina, que es lo que la `ACTA 52` `52.9` me dejo de costumbre.

**LO QUE MI PAGINA SELLADA PUBLICA**, en la `LECTURA` de su seccion `3` y otra vez en la tabla
de cierre de su seccion `9`:

> *Los **`4`** rancios llevan fecha `2026-09-18`*, y en su tabla de cierre *guardas corridas por mi: ... `rancios`
> **`4`***

**LO QUE EL INSTRUMENTO IMPRIME, EN EL FICHERO QUE YO MISMO GUARDE AL CORRERLO:**

<!-- TALLADO: parcial salida=.v55/rancios.txt -->

    $ head -4 .v55/rancios.txt
    $ python forja.py rancios
    BLOQUE DE VIGENCIA: 79 hallazgo(s) sobre 726 veredicto(s) y 0 cita(s).
      RANCIO 71, SIN HUELLA 8
      lineas declaradas NO CONSUMADAS y por eso no medidas: 14

    $ grep -c "\[RANCIO\]" .v55/rancios.txt
    71

> ### **CORRECCION DECLARADA DE LA `ACTA 53`, SIN BORRAR UNA LINEA DE MI PAGINA SELLADA** (manual principio `6`; y `D.34` me prohibe tocarla)
>
> **Donde `APERTURA_CIEGA.md` linea `210` dice *los `4` rancios* y su linea `624` dice
> *`rancios` `4`*, tiene que leerse `71`**, que es lo que el instrumento imprime en su propia
> linea de resumen. **Lo que NO cambia es la conclusion**: los `71` van de `2026-09-13` a
> `2026-09-18`, **todos anteriores a la vuelta que audito**, y `D.15` dice que un rancio no
> pone el `gate` en rojo. **No se los cargo a esta vuelta, y no se los cargaba antes.**

**COMO ME CAI, PORQUE EL MECANISMO IMPORTA MAS QUE EL NUMERO:** pegue **la cola** de la
salida, conte las lineas que se veian en el pegado, **y la linea que daba la cifra buena
estaba en la CABECERA del mismo fichero**, cuatro renglones antes del primero que pegue. **Es
la figura que la `ACTA 50` le cazo a la vuelta `51`** (*`72` rancios donde el instrumento
escribe `RANCIO 71`*), **y me la he hecho yo en el espejo**: aquella conto de mas por incluir
la linea de resumen; yo conte de menos por no leerla.

**`AUDITOR` SUBE DE `0 de 3` A `1 de 3`.** **Lo subo yo.** No estoy en el penultimo escalon,
asi que `5.5` no me obliga a encargarme un remedio bloqueante; **me lo escribo igual**, porque
es la tercera vez en el historial de esta sede que una cifra de la fase ciega sale de contar
un pegado en vez de leer el instrumento.

> ## **REMEDIO 1 DE LA `ACTA 53`, PARA MI TURNO DE LA `54`**
>
> **TODA CIFRA QUE YO SAQUE DE UNA SALIDA DE INSTRUMENTO SE LEE DE LA LINEA DE RESUMEN DEL
> PROPIO INSTRUMENTO, Y SI PEGO UN EXTRACTO, PEGO ESA LINEA CON EL.** Si el instrumento no
> imprime resumen, **lo digo** y cuento sobre el fichero entero, no sobre el pegado.

**Y LO QUE NO SE ME MOVIO, remedido una a una sobre mi pagina ya sellada:** `346`, `740`, `1`,
`65`; la poblacion `414` con su reparto `346` mas `68` y el `68` con el suyo, `65` mas `3`;
`72` ficheros en `.v54/`; `79` lineas de `cap_02.md`; `7` candidatos y `50` pasos por sus dos
vias; `resolutor 346`; y la huella `d5f4eb83...` de la herencia. **Ninguna se mueve.**

## 53.12. **EL CREDITO AL CERRAR, ANOTADO EN `docs/loop/CREDITO_serial.jsonl`** (`D.48`)

*Tabla de rachas, copiada de `python forja.py credito --anotar` corrido al cerrar esta acta.*

| especie | esta tanda | racha antes | racha ahora | por que |
|---|---|---|---|---|
| **`REPORTE`** | **CAE** | `0 de 3` | **`1 de 3`** | la clasificacion de la pregunta `11`, en CABECERA, TABLA y CONCLUSION (`53.6`) |
| **`CIFRA PUBLICADA`** | **LIMPIA** | `1 de 2` | **`0 de 2`** | tanda limpia de `5.4` y `D.38.1`, con sus escrituras en `DEUDA.jsonl` reproducidas (`53.8`) |
| **`CLASE`** | **LIMPIA** | `0 de 2` | **`0 de 2`** | `740` contra `740`: ni un veredicto escrito |
| **`DATO MOVIDO`** | **LIMPIA** | `0 de 2` | **`0 de 2`** | `git diff` vacio sobre `dataset/`, `bitacora/` y `censos/` |
| **`AUDITOR`** | **CAE** | `0 de 3` | **`1 de 3`** | `rancios 4` donde el instrumento imprime `RANCIO 71`, en mi pagina sellada (`53.11`) |

**DENTRO CONTRA FUERA DEL MARCADO** (`5.3`), que es la cifra que mueve el credito. *Recuento
de la tabla de `53.4`, celda a celda:*

| | |
|---|---|
| discutibles marcados por el extractor | **`10`** |
| se sostienen | **`9`** |
| caen **DENTRO** del marcado | **`1`** (el `1`), **y es la unica que acumula** |
| caen **FUERA** del marcado | **`2`**, las dos de prosa, **y ninguna acumula** |
| relecturas propias mias | **`7`** candidatos de `cap_02`, **`50`** pasos, adjudicados a ciegas |
| puestos releidos | los `50` pasos contra las `79` lineas de fuente, `15` mas `7` informes de aduana, `6` commits de sello, `17` corridas de la prueba intermitente |

## 53.13. **LAS CONDICIONES DE PARADA, MEDIDAS UNA A UNA** (`3`)

| condicion | medida | veredicto |
|---|---|---|
| **doctrina NUEVA necesaria** | la pregunta `11` la adjudico **citando `DATO MOVIDO`**, regla escrita desde el 16 sep, y lo que queda (mover la columna de `5.2`) **es de Alexis y `D.56` lo congela sin parar** | **NO** |
| **contradiccion con una regla vigente** | **la hay**: `D.58` contra el arnes (`53.9`). **Y tiene regla de correccion existente**: no es guarda de DATO (`D.55` cierra la lista en cuatro), no bloquea, y `D.55` manda **agendarla**. Queda como `d071` | **NO** |
| **decision de Alexis** | nada reservado se toca: `config/` y `esquema/` sin tocar, cero remotos, cero merges, umbrales quietos | **NO** |
| **fallo tecnico repetido** | la suite cierra en rojo dos vueltas seguidas, **pero no por la misma causa**: la de la `53` **pasa hoy**, y las dos de hoy son otras y por otro mecanismo (`53.4` `8`). Contador de esta causa: **`1`** | **NO** |
| **credito roto** | `REPORTE 1 de 3`, `CIFRA PUBLICADA 0 de 2`, `CLASE 0 de 2`, `DATO MOVIDO 0 de 2`, `AUDITOR 1 de 3`. **Ninguna en su tope** | **NO** |
| **campania consumada** | el tablero imprime `MUNDO 11: faltan 3 de 3 libros del corte` | **NO** |

**NO ESCRIBO `PARA_ALEXIS.md`**, y el encargo de la vuelta `55` sale de esta sede.

**Y EL AVISO QUE SI SUBE, aunque no sea parada:** el disparador de coste del encargo de la
`54` va por **`1` de `2`** (`53.10`). **Si el turno de la `55` vuelve a pasar de `8`, la
condicion escrita se cumple y el bucle se para**, y lo dejo dicho en el encargo para que nadie
se lo encuentre de sorpresa.

## 53.14. **LO QUE REGISTRO Y NO ADJUDICO** (`D.56`: la cola sigue congelada en `11`)

1. **El `resumen_teorico` viaja dentro del candidato que el prompt manda abrir en la fase
   ciega**, asi que quien lo lea primero corrige el examen con la solucion al lado. Lo
   registro desde mi pagina sellada `5.b`; **no abre pregunta nueva y no va al banco.**
2. **`d028` sigue viva y se cobra en la vuelta que abra tramo**: `cap_07` esta en `1` de los
   `9` nodos que su propia frontera le da, y `forja.py tablero --puedo` manda *continuar desde
   el capitulo siguiente al ultimo minado*, que mandaria saltar a `cap_08` **dejando `8` nodos
   atras**. **Va ENCARGADO en la `55`, no solo agendado** (`1`, punto `4`: la escalada se
   encarga).

## 53.15. **LA DEUDA QUE DEJO ESCRITA, Y NINGUNA BLOQUEANTE**

**`D.55` me deja como maximo UNA tarea bloqueante y solo si cita una guarda de DATO en rojo
que la justifique. NO TENGO NINGUNA GUARDA DE DATO EN ROJO** (`gate` verde, cerrojo y censo
dentro de el, fidelidad `D.30` sin objeto por `53.2`), **asi que NO DEJO NINGUNA
BLOQUEANTE.** Todo lo demas va a `DEUDA.jsonl` con su cita:

| id | que queda escrito |
|---|---|
| **`d071`** | `D.58` quita fase ciega, sello y testigo del regimen ligero **y el arnes hace las tres**. Medido en `53.9`. `D.45` veda el arreglo: **sube al fundador, no se toca** |
| **`d072`** | `construir_flujo_produccion_paso_limitante` contra `identificar_paso_limitante_jornada_desfases`: **par real que ninguna senial levanta por ninguno de sus dos extremos**, medido dos veces por dos corridas independientes (`53.5.a`). **Se cablea el dia de la insercion** |
