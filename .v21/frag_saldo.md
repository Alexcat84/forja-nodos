
**LA TABLA LA IMPRIME `.t1_v21/saldo21.py`, QUE LEE LOS TRECE FICHEROS Y TRANSCRIBE LO QUE DICEN**
(`EXTRACTOR.md` 5: la tabla se imprime, no se teclea, y se cuenta de su fichero):

    $ python .t1_v21/saldo21.py

| # | pieza | id | dictamen | poblacion (grafo mas bandejas) | vecinos levantados |
|---:|---|---|---|---|---|
| 1 | `P7` | `conversar_historia_vida_descubrir_motivadores` | **ENTRARIA** | **299** (203 mas 96) | ninguno |
| 2 | `P8` | `conversar_suenios_cruzar_habilidades` | **ENTRARIA** | **299** (203 mas 96) | ninguno |
| 3 | `P9` | `trazar_plan_dieciocho_meses_aprendizaje` | **BLOQUEARIA** | **299** (203 mas 96) | `calibrar_decision_despido_documentarla` por `similitud_texto` |
| 4 | `P13 a P17` | `armar_plan_anual_crecimiento_equipo` | **BLOQUEARIA** | **299** (203 mas 96) | `disenar_equipo_plan_anual` por `familia_id` |
| 5 | `P19 y P21` | `montar_proceso_contratacion_reducir_sesgo` | **ENTRARIA** | **299** (203 mas 96) | ninguno |
| 6 | `P24` | `facilitar_despido_tres_cosas` | **ENTRARIA** | **299** (203 mas 96) | ninguno |
| 7 | `P25` | `admitir_pronto_mal_desempenio_cuatro_razones` | **BLOQUEARIA** | **299** (203 mas 96) | `trazar_plan_dieciocho_meses_aprendizaje` por `similitud_texto`; `sopesar_consejo_legal_despedir_humildad` por `similitud_texto` |
| 8 | `P26` | `calibrar_decision_despido_documentarla` | **BLOQUEARIA** | **299** (203 mas 96) | `sopesar_consejo_legal_despedir_humildad` por `similitud_texto` |
| 9 | `P27` | `sopesar_consejo_legal_despedir_humildad` | **BLOQUEARIA** | **299** (203 mas 96) | `calibrar_decision_despido_documentarla` por `similitud_texto`; `admitir_pronto_mal_desempenio_cuatro_razones` por `similitud_texto` |
| 10 | `P28` | `contactar_despedido_mes_despues` | **ENTRARIA** | **299** (203 mas 96) | ninguno |
| 11 | `P30` | `calibrar_ascensos_evitar_politica` | **BLOQUEARIA** | **299** (203 mas 96) | `evitar_obsesion_ascenso_estatus` por `familia_id` |
| 12 | `P33` | `evitar_obsesion_ascenso_estatus` | **BLOQUEARIA** | **299** (203 mas 96) | `calibrar_ascensos_evitar_politica` por `familia_id` |
| 13 | `P34 a P36` | `reconocer_excelencia_trayectoria_gradual` | **ENTRARIA** | **299** (203 mas 96) | ninguno |
| | | **trece informes** | **6 ENTRARIA, 7 BLOQUEARIA, 0 CAERIA** | | **9 filas de vecino** |

> ### **CERO `CAERIA` EN LOS TRECE. SEIS ENTRARIAN SIN LEER NADA Y SIETE ABREN COLA DE LECTURA, QUE NO ES RECHAZO.**
> **Y NINGUN LOTE SE CIERRA CON CANDIDATOS QUE YO SEPA QUE CAERIAN** (`EXTRACTOR.md` 16): el unico
> que caia es el id de `bajo`, y esta corregido con sus dos informes en el arbol.

**LA POBLACION ES `299` EN LOS TRECE, Y SU REPARTO ES LO QUE HAY QUE CITAR** (`D.38.5`): **`203`
del grafo mas `96` que esperan en bandejas**. Los trece se midieron **con los trece ya escritos**,
que es lo que hace comparables sus trece filas entre si.

> ### **Y LA CIFRA QUE NO PUEDO PUBLICAR, DICHA CON SU RAZON TECNICA Y NO CON UNA EXCUSA**
>
>     $ python .t1_v21/saldo21.py | grep -A1 "CHOCAN"
>       valor de CHOCAN entre si dentro del lote en los trece : ['0']
>         ES ESTRUCTURAL Y NO MEDIDO (D.41): de uno en uno nunca hay dos candidatos.
>
> **Los trece informes imprimen `CHOCAN entre si dentro del lote : 0`, y ese cero NO es una
> medida.** `D.41` lo dice con estas palabras: *es la unica salida del informe que un informe de uno
> en uno NO PUEDE VER, porque el choque es entre dos candidatos del mismo lote, y de uno en uno
> nunca hay dos*. **Publicarlo como si fuera un saldo seria publicar una cifra falsa**, asi que lo
> publico como lo que es: **estructural**. La cifra de verdad la trae el informe de lote del arnes,
> y **esta vuelta no lo trae** (`O.2.d`).
