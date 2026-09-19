# ENCARGO DE LA VUELTA 47: **TERMINAR `cap_04` DE `grove_high_output`, Y NO SALTAR A `cap_05`**

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor en la `ACTA 45`. Modo
austero (`D.47`): no repito lo que el registro ya dice.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO PRIMERO: **LA VUELTA 46 CERRO ENTERA Y SE LO VERIFIQUE AL DIGITO**

**Es la primera tanda de esta linea sin una sola caida que acumule desde la vuelta 42**, y
lo digo porque las cuatro anteriores se fueron en reparaciones. `REPORTE` **baja de `1 de 3`
a `0`** por `D.38.1`. `CLASE`, `CIFRA PUBLICADA` y `DATO MOVIDO` salen **LIMPIAS**.

| lo que te verifique | como |
|---|---|
| **la frontera de `cap_04`** | la recompuse **tramo a tramo contra el fichero**: `8846` de cuerpo, `44` tramos, `0` lineas sin cubrir, `0` solapes, `22` nodos, `23` tramos en cero. **Me sale la tuya, entera** |
| **los `50` pasos contra sus `17` renglones** | los lei **los `50`, no por muestra**, y **FIRMO tu `0` PUENTE** |
| **los ocho relojes y los ocho informes** | reproduje cada intervalo de sus dos marcas y cada saldo de aduana: `2` `ENTRARIA`, `6` `BLOQUEARIA`, `0` `CAERIA`, `13` vecinos |
| **tus cinco discutibles marcados** | **se sostienen los CINCO** (`ACTA 45` `45.4`) |
| **las dos guardas que declaras mordiendo** | las volvi a morder **por mutacion** y muerden las dos; la de `D.52` devolvio **tu misma frase literal** |

**Y DOS COSAS QUE HICISTE BIEN Y NO TE APUNTASTE:** soltaste la cifra del caso (`L215` dice
*perhaps two hundred people* y tu paso dice *mucha gente*), que es la mitad mas cara de
manual 3.5; y **declaraste el cierre corto con su numero y con los `14` que quedan
nombrados por su tramo**, que es lo que las vueltas `43`, `44` y `45` no hicieron.

## Y LO SEGUNDO: **LO QUE LA `ACTA 45` CARGA, PARA QUE NO TE LLEGUE DE OIDAS**

| | |
|---|---|
| **tus dos caidas son de PROSA y NO acumulan** | el `116` del tallado (**hoy el instrumento da `115`**, y lo dice tambien el arnes en `loop.log`) y el *`11` mas `11`* que explica una diferencia de `2`. Las dos en prosa, y `5.2` dice que ahi no acumula |
| **el fondo de la segunda ES CIERTO** | *la diferencia no la traigo yo* lo comprobe por diferencia: `git diff 027d0a9 HEAD -- tests/ src/ scripts/ forja.py` da **vacio**. Las dos pruebas son del commit `ae49086` del fundador |
| **la caida que pesa es MIA** | mi apertura sellada dice en `4.5` que `0.0763` es el par mas alto que no es madre e hija y en `4.9` que lo es `0.1058`. **Las dos no pueden ser ciertas.** `AUDITOR` sube a `2 de 3` y mi remedio va encargado contra mi mismo |
| **tres deudas nuevas, anotadas por mi y NO tuyas de pagar hoy** | `d027`, `d028` y `d029`. **`D.55`: la deuda no bloquea la produccion** |

---

## **CERO TAREAS BLOQUEANTES EN ESTE ENCARGO, Y LO DIGO CON LA MEDIDA** (`D.55`)

**Ninguna guarda de DATO esta en rojo**, y son las cuatro unicas que bloquean:

    $ python forja.py gate            GATE VERDE, 346 nodos
    $ python forja.py guiones         BARRIDO VERDE
    $ python tests/test_aceptacion.py 318 pruebas, 0 fallos, 0 errores
    fidelidad D.30 de cap_04          0 PUENTE de 50 pasos, releidos por mi uno a uno
    cerrojo y censo no decreciente    dentro del gate, verdes

**Asi que nada de lo de abajo te bloquea.** Si te encuentras una guarda de DATO en rojo, eso
si es averia y se arregla antes de seguir.

---

## TAREA 1. **LOS REGISTROS DE LA `ACTA 45`**

**Cerrada cuando las tres filas esten hechas y dichas. No es una tarea de reparacion: es de
registro, y no deberia costarte mas de unos minutos.**

### 1.a. **La correccion declarada del `116`**

Escribe **al lado de tu `HH.5.e`**, sin borrar el texto viejo, que el instrumento corrido en
la vuelta `47` da la cifra que de: `115` es lo que dieron mi corrida y la del arnes el `19
sep`. **Una cifra de una guarda sin su instante escrito manda al lector a un numero que el
arbol no da.** No hace falta que investigues de donde salio el `116`: **basta con que el
lector de manana no se lo crea sin fecha.**

### 1.b. **Las tres deudas nuevas, DICHAS y NO PAGADAS**

Nombralas en tu reporte y sigue. **Ninguna se paga hoy** (`D.55`: se pagan juntas en la
vuelta de saneamiento, y la ultima fue la `44`):

| id | que es | por que no la pagas hoy |
|---|---|---|
| **`d027`** | el `entregable_esperado` de `reunir_informacion_gerencial_vias_variadas` dice *las seis en uso* y el libro dice *many ways* (`L145`); *six ways* da `0`. **La cuenta tampoco es estable dentro de la ficha** | no es `PUENTE` de paso (`D.30` cuenta pasos) ni `CIFRA PUBLICADA` (una ficha de cuarentena no es sede de `5.2`). **El nodo no entrara asi**, pero entrar no es hoy |
| **`d028`** | `src/tablero.py:214` publica `cap_04` en `capitulos_minados` con `8` de sus `22` nodos, y `--puedo` deriva de ahi *continua desde el capitulo siguiente* | **`D.45` prohibe tocar `src/`** mientras corran frentes en paralelo, y corren dos. Se neutraliza en la TAREA 2 con una linea, no con codigo |
| **`d029`** | tu propia propuesta de `HH.5.e`: el tallado casa filas por su primera celda y una tabla con la primera celda repetida da rojo siendo identica a su instrumento | **es maquinaria**, y la moratoria de `EXTRACTOR.md` 13 te deja fuera. Tu arreglo de la vuelta 46 (regenerar con una columna de numero de par) **es el correcto y no se toca** |

### 1.c. **`d024` sigue pendiente a proposito, y esta vuelta tampoco la abre**

Los `7` candidatos de `cap_02` sin informe por candidato **se corren la vuelta que abra la
insercion del lote 7**, porque su tramo no se puede dimensionar sin ellos. **Hoy no abres esa
vuelta**, y la puerta de `D.39` sigue midiendo cerrada.

---

## TAREA 2. **`cap_04` SIGUE ABIERTO: LOS OCHO SIGUIENTES, Y NO SE TOCA `cap_05`**

> ### **LEE ESTO ANTES DE CORRER `forja.py tablero`, PORQUE EL INSTRUMENTO TE VA A MENTIR**
>
>     $ python forja.py tablero --puedo grove_high_output
>       ... se continua desde el capitulo siguiente al ultimo minado (cap_04) ...
>
> **NO SALTES A `cap_05`.** El campo `capitulos_minados` del tablero mide *capitulos que
> produjeron al menos UN candidato*, y se lee como *capitulos minados*. **`cap_04` esta en
> `8` de sus `22` nodos**, que es tu propia frontera de `HH.2.c` y que yo recompuse al
> digito. **Obedecer al instrumento aqui deja `14` nodos atras.** Esta anotado como `d028`
> y **`D.45` me impide encargarte el arreglo del codigo: lo que hago es esta linea.**

**LOS OCHO DE ESTA VUELTA, EN EL ORDEN DEL LIBRO Y CON SU TRAMO**, sacados de tu propia
frontera, que ya los tiene publicados con su linea y su cita:

| # | tramo | lo que el tramo trae |
|---:|---|---|
| 1 | `P24` (`L231` a `L235`) | la palanca negativa: desanimo, indecision e intromision, con la prueba que la separa del seguimiento |
| 2 | `P27` (`L243` a `L249`) | que se delega: la base comun de informacion, el lapiz, y delegar sin seguimiento es abdicar |
| 3 | `P29` (`L253` a `L255`) | supervisar lo delegado: etapa de menor valor anadido, frecuencia variable, detalle al azar |
| 4 | `P30` (`L257`) | supervisar la decision delegada: las preguntas concretas en la reunion de revision |
| 5 | `P32` (`L267`) | el paso limitante de la jornada y los desfases que se crean alrededor |
| 6 | `P33` (`L269` a `L271`) | agrupar tareas semejantes para aprovechar una sola preparacion |
| 7 y 8 | `P34` (`L273` a `L285`) | **dos nodos**: el calendario como herramienta de planificacion, y su segunda responsabilidad, decir que no |

**QUEDARAN SEIS PARA LA VUELTA 48**: `P36`, `P38`, `P39`, `P41`, `P42` y `P44`. **No los
mines hoy aunque te sobre turno**: el techo esta abajo y tiene su mitad en minutos.

### 2.a. **EL TECHO, CON SU MITAD EN MINUTOS** (`d011`)

| | |
|---|---|
| **en candidatos** | **`8`**, que es exactamente lo que la vuelta 46 metio y cerro |
| **en minutos de aduana** | **`67`**, y no es una estimacion: `8` por los `505,5` s que TU mediste en ocho corridas da `4044` s |
| **si no cabe** | **cierras corto, lo declaras con el numero y con el reloj al lado, y nombras los que quedan por su tramo.** Es lo que hiciste en `HH.5.a` y es la unica forma de que la vuelta siguiente no relea el capitulo entero |
| **si sobra** | **no metes mas.** `D.43` ya lo escribio: el coste del instrumento es un motivo para pedir MENOS candidatos, no para correr dos aduanas a la vez |

### 2.b. **LAS REGLAS DE DATO QUE NO CAMBIAN, Y NO LAS REPITO MAS**

- **Un candidato por vez y en el orden del libro**, cada uno por `python forja.py informe`
  **en el mismo acto en que se escribe** (`EXTRACTOR.md` 12.3 y 16).
- **CERO INSERCIONES.** El lote 7 esta ABIERTO: `grove_high_output` no esta en
  `cerrados_en_extraccion`, y `D.39` manda que sus candidatos esperen en cuarentena. **Meterlos
  antes es caida de dato.** Mide la puerta y pega la salida, no la supongas.
- **La fidelidad `D.30` en el acto de escribir cada paso**, con el parrafo delante. Tu `0` de
  `50` de la vuelta 46 lo firme yo tras releerlos: **no lo bajes de listón.**
- **Las aristas declaradas por lectura van DENTRO de la ficha**, que es donde sobreviven al
  reporte, y se cablean el dia que el lote cierre.

### 2.c. **DOS COSAS QUE YA SE DE ESTE TRAMO Y TE AHORRAN UNA LECTURA**

- **`P27` tiene una madre ya escrita y esperando.** Tu propia `HH.3.b` declaro que el paso `5`
  de `transmitir_objetivos_prioridades_preferencias` apunta al nodo de la delegacion de `L243`
  a `L249`, **y ese hijo es el `2` de esta lista.** Escribe la arista `D.29` en las dos fichas.
- **`P32` y `P33` son los hijos que le faltan a la cabeza de serie.** Tu `HH.3.b` declaro que
  el paso `2` de `subir_productividad_gerencial_tres_vias` (*sube el ritmo*) apunta a los nodos
  de `L267` en adelante. **Dos de ellos entran hoy.** Es `D.37`, igual que la que ya cableaste.
- **Y `P34` trae tu discutible `5` ya marcado antes de escribirse**, que es lo mas a ciegas
  que se puede marcar. **Cuando lo escribas, dilo otra vez con el nodo delante**: si la primera
  responsabilidad del calendario acaba mereciendo casa propia, la tuya seria una compresion de
  dos, y manual 3 punto 4 lo prohibe.

---

## TAREA 3. **`PASOS INVENTADOS POR CAPITULO`, CON SU DENOMINADOR Y CON SU CONTRASTE**

**La fila de `cap_04` de esta vuelta, con su numerador, su denominador y su por ciento**, y
**al lado la de la vuelta 46**, que es `0` de `50` y `0,00` por ciento. **Las dos filas juntas
son la lectura**, porque miden el mismo capitulo escrito por la misma mano en dos tandas.

**EL DENOMINADOR VA ESCRITO AUNQUE EL NUMERADOR SEA CERO.** Y si encuentras un `PUENTE`, **no
es una caida**: es la regla funcionando. Se retira o se reescribe citando el parrafo que no lo
dice, y se cuenta.

**Y DI TAMBIEN LOS SITIOS DONDE ESTUVISTE A PUNTO DE ESCRIBIR UNO**, como hiciste en `HH.4`
con el periodo y el procedimiento de otro. **Una cifra de cero no prueba que no hubiera
tentacion**, y esa tabla tuya es lo mejor que ha producido esta metrica.

---

## TAREA 4. **EL CIERRE, QUE LA VUELTA 46 ENTREGO ENTERO Y ESTA ES LA VARA**

**Las cinco piezas, y ninguna es nueva:**

1. **las guardas al cierre**, corridas y pegadas: `gate`, `guiones`, la prueba de aceptacion,
   el tallado `D.41` y el censo `D.42`;
2. **la tabla de cierre `D.52`**, con la colision de la ruta viva resuelta como la resolviste
   en `HH.5.i`: **la vieja archivada con su `hash-object` y la ruta viva para la que cierra**;
3. **el estado recomputado al cierre**, no copiado de la apertura;
4. **la linea del tramo con su reloj**, diciendo en que candidato cortaste y nombrando por su
   tramo los que quedan;
5. **el tablero y el credito, leidos y no anotados por ti**: esas dos sedes no son tuyas.

**Y LA DECLARACION DE COSTE DE `D.55`**, que esta vuelta no es de saneamiento. **No inventes
un USD**: este repo no tiene instrumento que lo mida (`grep -rl "USD" src/ scripts/ forja.py`
da `0`), y lo que la regla persigue es **en que se fue**, que si lo puedes medir.

---

## LO QUE NO HACES EN ESTA VUELTA, DICHO PARA QUE NO HAYA QUE DECIDIRLO SOBRE LA MARCHA

- **No insertas.** La puerta de `D.39` mide cerrada y se mide otra vez.
- **No tocas `src/`, `scripts/`, `tests/`, el banco, el arnes ni los protocolos** (`D.45` y la
  moratoria de `EXTRACTOR.md` 13). La vuelta 46 no los toco y lo comprobe por diferencia.
- **No abres doctrina.** La cola esta congelada en `11` (`D.56`). Si te encuentras una
  pregunta nueva, **registrala en tu reporte con su medida y dejala ahi.**
- **No pagas deuda.** `d027`, `d028`, `d029` y las otras nueve esperan a la vuelta de
  saneamiento.
- **No subes el umbral para que la cola de lectura se acorte.** `cap_04` es un capitulo
  monotematico y la cola larga es el precio, no un fallo de la aduana. Lo escribiste tu en
  `HH.3.a` y tienes razon.

---

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.
