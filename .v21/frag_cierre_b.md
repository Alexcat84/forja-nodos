
## O.6.3. **`PASOS INVENTADOS POR CAPITULO`, FILA POR CAPITULO MAS TOTAL DEL LOTE** (lo pide el encargo)

*La tabla la imprime `.t1_v21/reparto21.py`, y el reparto de candidatos por capitulo **no se
teclea**: se deduce del `resumen_teorico` de cada fichero. **El numerador de `cap_04` y `cap_05` es
HEREDADO: lo cito y no lo firmo**, igual que la `ACTA 20` `6.2`. El de `cap_10` **lo firmo yo**.*

    $ python .t1_v21/reparto21.py

| unidad | rotulo | cuerpo | candidatos | numerador | denominador | **tasa** | quien la firma |
|---|---|---:|---:|---:|---:|---:|---|
| `cap_00` | `Copyright Page` | 218 | 0 | **0** | **0** | **sin definir** | denominador **mio** |
| `cap_01` | `Preface` | 2.846 | 1 | **0** | **9** | **0,00** | denominador **mio** |
| `cap_02` | `Introduction` | 3.908 | 0 | **0** | **0** | **sin definir** | denominador **mio** |
| `cap_03` | `How to Use This Book` | 627 | 1 | **0** | **7** | **0,00** | denominador **mio** |
| `cap_04` | `Cap. 1` | 6.263 | 6 | **3** | **48** | **6,25** | denominador **mio**; **numerador heredado, lo cito y no lo firmo** |
| `cap_05` | `Cap. 2` | 8.756 | 8 | **2** | **76** | **2,63** | denominador **mio**; **numerador heredado** |
| `cap_06` | `Cap. 3` | 11.587 | 10 | **0** | **117** | **0,00** | denominador **mio** |
| `cap_07` | `Cap. 4` | 13.678 | 25 | **0** | **225** | **0,00** | denominador **mio** |
| `cap_08` | `Cap. 5` | 6.140 | 12 | **0** | **102** | **0,00** | denominador **mio** |
| `cap_09` | `Cap. 6` | 17.482 | 20 | **0** | **272** | **0,00** | denominador **mio** |
| **`cap_10`** | **`Cap. 7`** | **8.976** | **13** | **0** | **194** | **0,00** | **numerador y denominador LOS FIRMO YO** (`O.3.d`) |
| | **lote 4 hasta `cap_10`** | **80.481** | **96** | **5** | **1050** | **0,48** | denominador remedido entero por mi |

| fila de residuo | valor | los nombres |
|---|---:|---|
| `SIN` unidad deducible del `resumen_teorico` | **0** | lista vacia |

    PEOR UNIDAD (la que decide la escalada) : cap_04 con 6.25 contra tope 10
    candidatos repartidos                   : 96
    candidatos en la bandeja                : 96

> ### **LA FILA QUE DECIDE ES LA PEOR, Y SIGUE SIENDO `cap_04` CON `6,25` CONTRA UN TOPE DE `10`. EL FRENO NO SE DISPARA Y EL TRAMO NO BAJA.**
>
> **LAS OCHO FILAS HEREDADAS REPRODUCEN AL DIGITO LAS DE LA `ACTA 20` `6.2`:** `cap_01` **9**,
> `cap_03` **7**, `cap_04` **48** y **6,25**, `cap_05` **76**, `cap_06` **117**, `cap_07` **225**,
> `cap_08` **102**, `cap_09` **272**. Y el total del lote hasta `cap_09` sale de restar:
> **`1050` menos `194` son `856`**, que es la cifra que el acta firmo.
>
> **Y LOS DOS CUERPOS TAMBIEN REPRODUCEN, por resta y no por copia:** `80.481` menos `8.976` son
> **`71.505`** (`cap_00` a `cap_09`, la cifra del acta), y `27.680` de `cap_11` a `cap_14` mas
> `8.976` son **`36.656`** (la otra cifra del acta).

### O.6.3.b. **UNA CAIDA DE MI PROPIO INSTRUMENTO, CAZADA POR MI ANTES DE PUBLICARLA** (ORDEN B de la `ACTA 19` `7.4`)

*La cuento porque el remedio de esta casa que ha funcionado es el que obliga a teclear algo, y
porque publicar la tabla buena sin decir que la primera salio mal seria ORDEN B rota.*

**MI PRIMERA CORRIDA DE `reparto21.py` DIO ESTO, Y ES FALSO:**

    cap_04:  5 candidatos,  41 pasos,  tasa 7,32
    lote 4 hasta cap_10:   95 candidatos,  1043 pasos
    FILA DE RESIDUO 'SIN' -> 1 id: ['invitar_desafio_reciproco_equipo.json']

**LA CAUSA, medida y no supuesta:** mi patron era `cap_(\d+)\.md`, **con extension**, y
`invitar_desafio_reciproco_equipo` nombra su capitulo en prosa y sin extension.

    $ python (re.findall de cap_\d+ en su resumen_teorico)
      ['cap_04']

**SE ME PERDIAN 7 PASOS DE `cap_04` Y LA TASA SUBIA DE `6,25` A `7,32`.** Ensanche el patron a
`cap_(\d+)`, que es **la misma anchura que el instrumento de la vuelta 20**, el cual ya habia
resuelto este caso exacto (`REPORTE` `O.2.e`). **Y esto es la leccion en una linea: el fallo no
fue de lectura, fue de haber reescrito un instrumento que ya existia sin copiarle la anchura.**

## O.6.4. LAS COLAS DE ARISTA, **NINGUNA ESCRIBIBLE HOY**, Y AHORA SON TRES ESPECIES

*El encargo de la vuelta 20 mandaba repetirlas al cierre hasta que el lote 4 cierre, **sin
inventarles sede y sin resumirlas**. Las **doce** heredadas siguen enteras y **no las toco**;
esta vuelta abre **tres `D.37`** y **un par de lectura adjudicado**, y van en filas aparte porque
**no son la misma especie y sumarlas mentiria**.*

### O.6.4.a. LAS DOCE `D.29` HEREDADAS, **SIN CAMBIO**

| # | madre | hijo o hijos | por que hoy no |
|---:|---|---|---|
| **1** | `revisar_ciclo_responsabilidades_relaciones` **P3** | las cabezas de `cap_05`, `cap_06` y `cap_07` | la madre vive en cuarentena |
| **2** | `gestionar_personas_equipo` **P2** (Zhuo, **en el grafo**) | `desplegar_marco_franqueza_radical` (bandeja) | el hijo vive en un lote **ABIERTO**, y **cruza de libro** |
| **3** | `empezar_cultura_franqueza_radical` **P3, P5 y P6** | `pedir_critica_equipo_premiarla`, `elogiar_trabajo_especifico_contexto`, `criticar_trabajo_evitar_desanimo` | los cuatro en cuarentena |
| **4** | `repartir_tiempo_atencion_mejores_equipo` **P3** (Zhuo, **en el grafo**) | `acompaniar_mejores_equipo_socio` (bandeja) | el hijo vive en un lote **ABIERTO**, y **cruza de libro** |
| **5** | `recorrer_rueda_hacer_cosas_equipo` **P2 a P8**, radio `LISTEN` | `adaptar_escucha_cultura_ajena` | los dos en cuarentena, y `LISTEN` no tiene cabeza propia |
| **6** | `dominar_arte_socializar_trabajo` **P9** | `evitar_presion_social_actos_equipo` | los dos en cuarentena |
| **7** | `practicar_franqueza_radical_jefe_propio` **P14** (`L217`) | **SEIS hijos** de `cap_09` | los siete en cuarentena. `D.29` y **no** `D.37`: el texto los nombra y **no dice `six`** |
| **8** | `evitar_personalizar_guia_aceptar_personal` **P5** (`L169`) | `dar_guia_humilde_tres_tecnicas` | los dos en cuarentena |
| **9** | `exigir_critica_jefe_reticente` **P9** (`L299`) | `abrazar_incomodidad_arrancar_critica_equipo` | los dos en cuarentena |
| **10** | `elogiar_publico_criticar_privado_sus_tres_matices` **P9** (`L163`) | `fomentar_guia_reciproca_companieros` | los dos en cuarentena |
| **11** (del auditor, `ACTA 19` `1.b`) | `evitar_personalizar_guia_aceptar_personal` | `manejar_enfado_persona_desafiada` | los dos en cuarentena, **mismo libro** |
| **12** (de la vuelta 20) | `conducir_reuniones_salto_nivel_diez_reglas` (`P27`) | `resolver_dudas_frecuentes_reuniones_salto_nivel` (`P28`) | los dos en cuarentena. `D.29` porque `L417` dice `some of the questions` |

### O.6.4.b. **LAS TRES `D.37` DE ESTA VUELTA, QUE NO SON `D.29` Y NO SUMAN EN LAS DOCE**

*Enteras en `O.4`, con su `--paso 11` y su razon. Aqui van en su fila porque la cuenta de `D.29` no
las incluye: **la cuenta esta escrita en `L173`**, y eso es lo que las hace `D.37`.*

| # | madre | hijo | `--paso` | por que hoy no |
|---:|---|---|---:|---|
| **`D.37`.1** | `facilitar_despido_tres_cosas` | `admitir_pronto_mal_desempenio_cuatro_razones` | 11 | **los dos en cuarentena.** `forja.py arista` lo rechaza con su salida pegada (`O.4.b`) |
| **`D.37`.2** | `facilitar_despido_tres_cosas` | `calibrar_decision_despido_documentarla` | 11 | idem |
| **`D.37`.3** | `facilitar_despido_tres_cosas` | `sopesar_consejo_legal_despedir_humildad` | 11 | idem |

### O.6.4.c. **EL PAR DE LECTURA ADJUDICADO, QUE TAMPOCO ES `D.29` NI `D.37`**

| madre | hijo | `--paso` | veredicto | por que hoy no |
|---|---|---:|---|---|
| `reconocer_recompensar_gente_estable` (`cap_06`) | `reconocer_excelencia_trayectoria_gradual` (`cap_10`) | 2 | **`CONTINUA` con arista**, adjudicado por la decision 3 del fundador | los dos en cuarentena, **y la aduana NO lo levanta** (`O.5.b`) |

> ## **DIECISEIS ARISTAS PENDIENTES EN TRES ESPECIES, Y **QUINCE** SE DESBLOQUEAN CON EL MISMO ACTO: EL CIERRE DEL LOTE 4.**
> **Solo las `D.29` numeros 2 y 4 necesitan dos cierres, porque cruzan de libro.** Y la serie de
> la cifra sigue: **cuatro al cerrar la 17, seis la 18, diez la 19, doce la 20, dieciseis hoy.**
> **La deuda de aristas del lote 4 no se estabiliza, se acumula**, y lo digo con las cinco cifras
> al lado en vez de repetir las colas sin contarlas. **No es parada**: el encargo lo pone por su
> nombre en lo que no para, y dice que once de las doce se desbloquean de golpe.

## O.6.5. **LOS VEREDICTOS DE LA COLA DE LECTURA QUE LA ADUANA SI LEVANTO, LEIDOS UNO A UNO**

*`EXTRACTOR.md` 2: **si la aduana bloquea, lees a los vecinos antes de escribir el veredicto.**
Los he leido, con los dos ficheros abiertos, y escribo el veredicto con su razon. **No van a
`bitacora/`**, porque hoy no se inserta y esa sede la escribe la aduana (`O.5.c`).*
