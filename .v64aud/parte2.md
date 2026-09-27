## 3. LA FIDELIDAD DE LOS SEIS DE `d005`, ENTERA Y SIN MUESTRA (`D.30`, encargo `T2.a`)

**Cada paso contra su linea de `fuentes/grove_high_output/cap_03.md`**, una fila por paso en
`.v64aud/fidelidad.tsv` con la linea y la frase del libro que lo sostiene. **TRANSCRIPCION** si el libro
pone el medio, la etapa o el objeto; **PUENTE** si lo escribio el extractor.

### 3.1. **`PASOS INVENTADOS POR CAPITULO`, `cap_03`, POBLACION: LOS `41` PASOS DE LAS SEIS FICHAS TAL COMO LAS ESCRIBIO EL EXTRACTOR (version de `067c9df`, antes de cualquier correccion de la `64`). MI LECTURA CIEGA**

    $ python .v64aud/contar_fidelidad.py
    candidato                                        ficha filas   T   P  DUDA
    archivar_indicadores_resolver_problemas              4     4   4   0     0
    construir_grafico_escalonado_pronosticos             8     8   8   0     0
    construir_indicador_tendencia_patron                 6     6   6   0     0
    elegir_fabricar_pedido_pronostico                    9     9   9   0     0
    elegir_indicador_salida_trabajo_administrativo       7     7   7   0     0
    emparejar_indicadores_efecto_contraefecto            7     7   6   1     2
    total cap_03, seis de d005                          41    41  40   1     2
    PUENTE sobre pasos escritos: 1 de 41 = 2.44 por ciento
    si las 2 DUDA cayesen a PUENTE: 3 de 41 = 7.32 por ciento

**El instrumento cuenta los pasos de cada ficha de `067c9df` y comprueba que mi tabla trae una fila
por paso, ni mas ni menos: cero `DESCUADRE`.** Sale **`1` PUENTE de `41`**, y **`3` de `41` si las dos
dudas caen**. Las dos cifras quedan por debajo del `10` de `8.1`, asi que **el escalon no se mueve con
ninguna de las dos lecturas**.

**Y NO ES LA METRICA DE LA VUELTA:** la vuelta `64` es de saneamiento y mide seis fichas de `cap_03`, no
un capitulo entero. **El rotulo dice lo que medi y nada mas**, que es lo que `R8` me pide.

### 3.2. **EL PUENTE Y LAS DOS DUDAS, LOS TRES EN `emparejar_indicadores_efecto_contraefecto`**

| paso | mi clase | la linea del libro, y por que |
|---|---|---|
| `1`, *Antes de soltar un indicador, mira hacia donde va a dirigir la atencion, porque el indicador dirige la atencion... bicicleta* | **PUENTE de clausula** | L31 da **una propiedad** (*Indicators tend to direct your attention toward what they are monitoring... you will probably steer it where you are looking*) y **su remedio** (*you should guard against overreacting. This you can do by pairing indicators*). **La inspeccion previa, *antes de soltar... mira*, no la manda el libro**: el acto que manda es emparejar. El porque del paso si es del libro, y por eso es de clausula y no de paso entero |
| `2`, *Nombra el efecto que ese indicador va a empujar* | **TRANSCRIPCION, con DUDA** | *nombrar* no esta como orden; **pero el libro hace ese razonamiento en su ejemplo** (*you are likely to take action to drive your inventory levels down, which is good up to a point*) **y pone el objeto**, *effect*. Por `D.30` (*el libro pone el objeto*) va a TRANSCRIPCION. El lector estricto lo llama PUENTE, y por eso esta la segunda cifra |
| `3`, *Nombra el contraefecto, que es lo que se estropea si ese empuje se pasa de largo* | **TRANSCRIPCION, con la misma DUDA** | *your inventories could become so lean that you can't react to changes in demand without creating shortages*, y el objeto *counter-effect* |

**LECTURA:** los tres primeros pasos de `emparejar` montan un procedimiento de entrada (mirar, nombrar,
nombrar) sobre un parrafo que da una propiedad, un ejemplo y un remedio. **Es el reparto de `D.30`**: el
puente aparece donde el parrafo es mas pobre en actos. Los pasos `4` a `7` son del libro frase a frase
(L31 y L33).

**LOS OTROS CINCO, LIMPIOS, Y LO QUE MIRE DE CERCA PARA DECIRLO:** `archivar` paso `1` (*en vez de dejar
que se pierdan segun pasan los dias*) es la negacion del mismo acto de L99 (*If you do not
systematically collect and maintain an archive*), no un acto nuevo; `construir_grafico` paso `3`
(*marca con un asterisco*) sale de la leyenda de la figura, L95 (*\* means the actual number for that
month*); `construir_grafico` paso `5` convierte en orden el ejemplo de L93, que el propio libro abre
diciendo que ahi es donde el grafico rinde mas; `elegir_fabricar` paso `3` (*compara tu plazo con el de
tu competencia*) es la condicional de L105 puesta como etapa. **Los cuatro: TRANSCRIPCION.**

## 4. LA CLASE DE CADA UNO DE LOS SEIS COMO NODO, CON SUS LINEAS

| candidato | lineas | mi clase |
|---|---|---|
| `archivar_indicadores_resolver_problemas` | L99 | **nodo**, delgado: `4` pasos de un solo parrafo, pero con su inventario (recoger, banco, repasar, buscar desviaciones) |
| `construir_grafico_escalonado_pronosticos` | L91 a L97 | **nodo**, inventario rico |
| `construir_indicador_tendencia_patron` | L89 | **nodo**; un solo parrafo con cinco actos |
| `elegir_fabricar_pedido_pronostico` | L103 a L109 | **nodo**, inventario rico |
| `elegir_indicador_salida_trabajo_administrativo` | L35 a L67 | **nodo**; el paso `4` es la tabla de L39 a L67 entera |
| `emparejar_indicadores_efecto_contraefecto` | L31 a L33 | **nodo**, con el puente de `3.2` |

