# -*- coding: utf-8 -*-
"""Anexa el cierre de la vuelta 46, con la tabla D.52 que el instrumento recomputa despues."""
import io

RELOJ = io.open(".v46/tanda_cap_04.txt", encoding="utf-8").read().split("\n")
i = RELOJ.index("4. EL RELOJ DE LA ADUANA EN SECO, QUE ES LO QUE DECIDE EL TRAMO")
reloj = "\n".join(("    " + l).rstrip() for l in RELOJ[i + 2:] if l.strip())

TXT = u"""
## HH.5. TAREA 5. **EL CIERRE, QUE ES LA FILA QUE LA VUELTA 45 NO ENTREGO**

### HH.5.a. **LA LINEA DEL TRAMO, CON SU NUMERO Y SU MEDIDA AL LADO**

> **La vuelta cierra en el candidato `8` de `22`; los `14` que quedaban pasan a la vuelta
> siguiente.**

**Y ESTOS SON LOS `14`, NOMBRADOS POR SU TRAMO para que la vuelta siguiente no vuelva a leer el
capitulo entero:** `P24` (la palanca negativa y la intromision), `P27` (que se delega y la base
comun), `P29` (supervisar lo delegado), `P30` (supervisar la decision delegada), `P32` (el paso
limitante de la jornada), `P33` (agrupar tareas semejantes), `P34` (**dos nodos**: el calendario y
decir que no), `P36` (el inventario de proyectos discrecionales), `P38` (seis a ocho
subordinados), `P39` (la regularidad), `P41` (las respuestas estandar), `P42` (agrupar las
interrupciones) y `P44` (el cartel y la hora de oficina). **La frontera de `HH.2` ya los tiene
publicados con su linea y su cita.**

### HH.5.b. **POR QUE CORTE EN `8` Y NO EN `15`: EL RELOJ, QUE ES LA MEDIDA QUE EL ENCARGO PIDE**

<!-- TALLADO: script=.v46/tanda.py salida=.v46/tanda_cap_04.txt -->

%(reloj)s

**EL ENCARGO ESTIMABA `385` s por candidato y mi medida de ocho corridas da `505,5`.** Lo digo
como discrepancia y no la resuelvo copiando (`EXTRACTOR.md` 5): **la poblacion del barrido crecio
dentro de mi propia vuelta**, de `372` a `379`, porque cada candidato que escribo entra en la
bandeja y lo ve el siguiente. **La estimacion del encargo no estaba mal medida: estaba medida
sobre otra poblacion.**

**Y LA CUENTA QUE DECIDE:** el techo de `15` habria costado **`126,4` minutos de aduana sola**, y
los `22` de la frontera **`185,3`**. **`8` costaron `67,4`.** La frase del encargo es la que
aplico: *si no cabe, escribes que no cabe, con el reloj al lado, y cierras igual*, porque *un
turno que se queda sin cierre por una corrida que no cabia pierde las dos cosas*.

**LO QUE NO HAGO CON ESTA MEDIDA, y lo digo para que no se lea como una peticion:** no pido mas
candidatos por vuelta ni propongo correr dos aduanas a la vez. **`D.43` ya lo escribio contra el
propio extractor:** *el coste del instrumento es un motivo para pedir MENOS candidatos, no para
correr dos a la vez.*

### HH.5.c. **EL ESTADO AL CIERRE, RECOMPUTADO AL CIERRE** (`EXTRACTOR.md` 4)

<!-- TALLADO: parcial salida=.v46/cierre_estado.txt -->

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
    $ ls cuarentena/grove_high_output/*.json | wc -l
    30
    $ ls cuarentena/_insertados/grove_high_output/*.json | wc -l
    1

**LAS TRES CIFRAS DEL DATO NO SE MOVIERON, Y ESO ES EL RESULTADO CORRECTO:** `346`, `740` y `1`
son exactamente las de la apertura. **Una vuelta que no inserta no debe mover el dataset, la
bitacora ni los pares mutuos**, y si alguna se hubiera movido seria la caida que buscar.
**Lo que si crecio es la bandeja: `22` mas `8` igual a `30`.**

### HH.5.d. **LAS GUARDAS AL CIERRE**

<!-- TALLADO: parcial salida=.v46/cierre_guardas.txt -->

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

<!-- TALLADO: parcial salida=.v46/cierre_pruebas.txt -->

    $ python tests/test_aceptacion.py
      total: 318 pruebas, 0 fallos, 0 errores

### HH.5.e. **LO QUE PROPONGO Y NO ADJUDICO** (`EXTRACTOR.md` 14)

**EL TALLADO DE `D.41` CASA LAS FILAS POR SU PRIMERA CELDA, Y UNA TABLA CON LA PRIMERA CELDA
REPETIDA DA ROJO SIENDO IDENTICA A SU INSTRUMENTO.** Me paso en esta vuelta, con la tabla de la
cola de lectura: `empujar_persona_reunion_direccion_preferida` ocupaba la primera celda de **cinco
filas seguidas** y el tallado emparejo mal las cinco.

    DIFIERE  docs/loop/REPORTE.md linea 44050
      declara: .v46/tanda_cap_04.txt
      2 fila(s) distintas de su instrumento:
        `empujar...` vecino  reporte `transmitir...`  instrumento `reunir...`

**LO ARREGLE REGENERANDO Y NO TECLEANDO**, que es lo que `D.41` manda: **le puse al instrumento
una columna de numero de par**, con lo que cada fila tiene clave propia, y volvi a pegar la tabla
entera. **El tallado quedo verde con `116` tablas.** No toco `scripts/tallar_reporte.py`: **la
moratoria de maquinaria** (`EXTRACTOR.md` 13) y `D.45` lo dejan fuera de mi mano, y **esto no es
una caida de DATO**. Lo dejo escrito aqui como propuesta, **hermano de la deuda `d022`**, que es
la que ya dice que `scripts/tabla_de_cierre.py` localiza su tabla por un sitio fragil.

**Y UN SEGUNDO EJEMPLAR, SIN BUSCARLO, DE LA PREGUNTA DE `D.55` QUE LA `ACTA 44` `44.5.b` DEJO
ABIERTA:** la cifra de fidelidad que corregi en `HH.1` era falsa **dentro de una ficha en
cuarentena**, y ninguna guarda la ve. **Lo que esta vuelta anade es el remedio barato que se me
ocurrio mientras lo pagaba:** el instrumento `.v46/tanda.py` **se para y no publica la tabla** si
una ficha declara mas pasos de los que tiene. No cubre el caso de la `ACTA 44` (una cifra de
`TRANSCRIPCION` falsa con el numero de pasos correcto), pero **cubre la mitad, y cuesta cuatro
lineas.** Lo dejo escrito, no lo llevo a `src/`.

### HH.5.f. **LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO** (`EXTRACTOR.md` 8)

**Van por numero y linea, sin reabrir el argumento** (modo austero), y **los cuatro estaban
escritos en su ficha antes de que ninguna senal hablara**:

| # | donde | el discutible, en una linea |
|---:|---|---|
| 1 | `subir_productividad_gerencial_tres_vias` y `buscar_actividad_alta_palanca_tres_vias` | **son cabezas de serie de cuatro pasos que solo nombran sus vias**: un lector estricto dira que eso es NOMBRAR y no PROCEDIMENTAR. **Si uno cae, caen los dos.** Es el par que ademas trae la unica similitud por encima de `0,40` de la tanda |
| 2 | `empujar_persona_reunion_direccion_preferida` | el libro literalmente dice *Let us call it nudging*: **puede leerse como DEFINICION de una categoria**, de las que la tabla de 9 tumba |
| 3 | `programar_visita_area_observar_despachar`, pasos `6`, `7` y `8` | **salen del caso** de la inspeccion de Mister Limpio, y un caso no deberia poner pasos |
| 4 | `elegir_momento_actividad_palanca_maxima`, pasos `2`, `3` y `4` | **salen del caso** de la planificacion anual, mismo reparo que el `3` |

**Y EL QUINTO, QUE ES DE FRONTERA Y NO DE FICHA:** `P34` es el unico tramo al que le doy **dos**
nodos, y **no le doy tres**. El libro numera *two things* para el calendario, y el manual manda
un nodo por paso mas una cabeza; **la primera responsabilidad es una sola frase que el libro no
despliega**, asi que la meto como paso de la cabeza en vez de darle casa. **Ese nodo aun no esta
escrito** (cae en los `14` del tramo siguiente), asi que el discutible queda marcado **antes** de
escribirlo, que es lo mas a ciegas que puedo marcarlo.

### HH.5.g. **LA TABLA DE CIERRE DE TAREAS** (`D.52`)

| # | tarea | como cerro |
|---:|---|---|
| 1 | los registros de la `ACTA 44`: `d021` y `d023` por correccion declarada | **CERRADA**: las tres patas reparadas sin borrar el texto viejo y **registradas**, que es lo que faltaba; `d024` y la pregunta de doctrina dichas y no tocadas |
| 2 | la frontera de `cap_04`, cerrada contra el cuerpo, y la heredada citada | **CERRADA**: `8846` contra `8846`, cero lineas sin cubrir, cero solapes, y `22` nodos contra un techo de `15` |
| 3 | minar `cap_04`, cada candidato por su aduana en el acto, cero inserciones | **CERRADA EN `8` DE `22` del capitulo**: `0` `CAERIA`, `13` pares de cola publicados par a par, **cero inserciones** |
| 4 | `PASOS INVENTADOS` de `cap_04` con su denominador | **CERRADA**: `0` PUENTE de `50` pasos escritos, `0,00` por ciento contra un tope de `10` |
| 5 | el cierre, con sus guardas, su tabla `D.52` y su linea de tramo | **CERRADA**: las cinco guardas en verde, el estado recomputado al cierre y la linea del tramo escrita con su reloj |
"""
with io.open("docs/loop/REPORTE.md", "a", encoding="utf-8", newline="\n") as f:
    f.write(TXT % {"reloj": reloj})
print("anexado")
