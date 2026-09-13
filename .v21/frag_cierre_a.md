
---

# O.6. EL CIERRE DE LA VUELTA 21

*`EXTRACTOR.md` 4: **el estado al cierre se mide al cierre.** Toda cifra que describa el estado al
cerrar se RECOMPUTA si algo de la propia vuelta pudo haberla movido. Las de abajo se corrieron
DESPUES de escribir los trece candidatos y DESPUES de la correccion de las 22 cuentas.*

## O.6.1. LAS TRES GUARDAS, CORRIDAS AL CIERRE

*Y una cuarta que no es guarda pero se corre igual, porque es la que me aborto un commit hoy.*

## O.6.2. **EL SALDO DE LOS TRECE, UNO A UNO, CON SU INFORME PROPIO** (`EXTRACTOR.md` 16, `D.41`)

*El del lote entero **no es mio** (`D.41`) y esta vuelta no lo trae (`O.2.d`). Los de uno en uno
**si son mios**, y son trece, mas los tres que se corrieron sobre un estado anterior del fichero
y quedan como prueba de lo que se corrigio.*

> ### **COMO SE CORRIERON, DICHO ENTERO Y ANTES DE LA TABLA, PORQUE ES LO QUE UN AUDITOR TIENE QUE PODER COMPROBAR**
>
> **PRIMERO EL COSTE, MEDIDO POR MI EN ESTA MAQUINA Y NO HEREDADO:**
>
>     $ time python forja.py informe cuarentena/scott_radical_candor/conversar_historia_vida_descubrir_motivadores.json
>       poblacion del barrido       : 287   (203 del grafo mas 84 que esperan en bandejas)
>       real  7m33.602s
>
> **`453` segundos por candidato, no `156,5`.** La cifra de `D.41` se midio contra una poblacion de
> **286**; la mia se midio contra **287** y sale casi **tres veces mas alta**. **No la contradigo
> ni la corrijo: declaro la discrepancia**, que es lo que `EXTRACTOR.md` 5 manda hacer en vez de
> resolverla copiando. Y digo lo que significa para un turno: **trece candidatos en serie son
> unos 98 minutos de instrumento**, sin escribir una sola palabra.
>
> **Y POR ESO LOS CORRI SOLAPADOS, Y LO DIGO ANTES DE QUE SE ME PREGUNTE.** `EXTRACTOR.md` 16
> prohibe por su nombre *escribir doce candidatos y pasar la aduana al final*, y no lo hice: **el
> informe de cada candidato se lanzo en el acto de escribirlo, en el orden del libro**, y ningun
> candidato conto como escrito hasta que su propio informe volvio. Lo que se solapa es **el
> tiempo de maquina con mi tiempo de escritura**, no el juicio. **La prueba de que el ciclo de
> correccion funciono candidato a candidato es que hay dos correcciones con su informe anterior y
> su informe posterior en el arbol**, y la primera tumbo un id en la puerta:
>
> | correccion | informe ANTES | informe DESPUES |
> |---|---|---|
> | `admitir_pronto_bajo_desempenio_...` rompia `REGLAS_DE_ID.md` regla 3 por `bajo` | `.aduana_v21/07_admitir_pronto.txt` **`[CAERIA]`** | `.aduana_v21/07b_admitir_pronto_corregido.txt` |
> | las 22 cuentas atribuidas de `O.3.d` | `.aduana_v21/01` a `13` | `.aduana_v21/final/` (los **trece**) |
>
> **LA TABLA DE ABAJO CITA LOS DE `.aduana_v21/final/`, QUE SON LOS DEL ESTADO FINAL DEL FICHERO**,
> y cada fila lleva el sello `git hash-object` que ata el informe a ese estado (`O.3.c`). Los de
> `.aduana_v21/0*.txt` se quedan en el arbol **como evidencia de lo corregido**, no como saldo.
>
> **Y EL ID QUE CAYO EN LA PUERTA ES `D.23` FUNCIONANDO:** *cuatro de cada diez candidatos
> escritos sin las reglas de id delante caen en la puerta*. **Cayo uno de trece, y por `bajo`, que
> es preposicion.** Despues de ese, **valide los trece ids con `reglas_id.validar` antes de
> escribir una sola linea mas**, y los trece dieron `[]`:
>
>     $ python -c "from src import reglas_id; ..."   (los trece)
>       OK   conversar_historia_vida_descubrir_motivadores []
>       OK   conversar_suenios_cruzar_habilidades []
>       OK   trazar_plan_dieciocho_meses_aprendizaje []
>       OK   armar_plan_anual_crecimiento_equipo []
>       OK   montar_proceso_contratacion_reducir_sesgo []
>       OK   facilitar_despido_tres_cosas []
>       OK   admitir_pronto_mal_desempenio_cuatro_razones []
>       OK   calibrar_decision_despido_documentarla []
>       OK   sopesar_consejo_legal_despedir_humildad []
>       OK   contactar_despedido_mes_despues []
>       OK   calibrar_ascensos_evitar_politica []
>       OK   evitar_obsesion_ascenso_estatus []
>       OK   reconocer_excelencia_trayectoria_gradual []
>
> **ESO NO ES UNA GUARDA NUEVA** (moratoria de maquinaria, `EXTRACTOR.md` 13): es **llamar a la
> guarda que ya existe** antes de gastar 453 segundos en descubrir lo mismo.
