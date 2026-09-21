
## BC.4. **TAREA 2, BLOQUEANTE: LA FIDELIDAD `D.30` DE LOS SEIS, CORRIDA ANTES DE QUE ENTRE NADA**

*`EXTRACTOR.md` 15.4. Los seis candidatos estaban ya escritos y pasados por la aduana en la vuelta 37,
asi que esta no es la relectura del acto de escribir: es **la de toda vuelta antes de cualquier
insercion**, que es la que la regla llama obligatoria. **Y ha encontrado tres cosas.***

### BC.4.a. LA TABLA, TALLADA DE SU INSTRUMENTO

<!-- TALLADO: script=.v38/fidelidad.py salida=.v38/fidelidad_tabla.txt -->

    $ python .v38/fidelidad.py
    RELECTURA DE FIDELIDAD D.30, VUELTA 38, ANTES DE LA PRIMERA INSERCION
      candidato                                            cap      pasos  PUENTE releidos por ciento
      --------------------------------------------------------------------------------------------------------
      mejorar_consciencia_propia_relacional_dos_practicas  cap_13      13       0        3       0,00
      contar_cuatro_historias_propias_ver_hueco_intencion  cap_13      17       0        8       0,00
      practicar_triangulo_critica_tres_papeles             cap_13      15       0        4       0,00
      pedir_critica_primero_crear_seguridad_psicologica    cap_13      17       2       12      11,76
      elegir_pregunta_recurrente_pedir_critica             cap_13      24       0        5       0,00
      resolver_dudas_frecuentes_pedir_critica              cap_13      15       0        5       0,00
      --------------------------------------------------------------------------------------------------------
      LA FILA DEL CAPITULO                                 cap_13     101       2       37       1,98

      un solo capitulo en el tramo: la fila por capitulo y el total son la misma fila.
      techo de PASOS INVENTADOS (AUDITOR_FORJA.md 8.1): 10 por ciento. Medido: 1,98.
      pasos releidos enteros por nombrar persona, cuenta, escalon o adjetivo de
      sentimiento (lo que el encargo manda declarar aunque sea cero): 37 de 101.

      LOS PUENTE, UNO A UNO:
        pedir_critica_primero_crear_seguridad_psicologica paso 6
        pedir_critica_primero_crear_seguridad_psicologica paso 15

**LA FILA POR CAPITULO ES UNA SOLA PORQUE EL TRAMO ES DE UN SOLO CAPITULO**, y lo digo en vez de
publicar una media disfrazada de fila: los seis salen de `cap_13`. **`2` de `101`, `1,98` por ciento,
contra un techo de `10`.**

### BC.4.b. **LOS `37` PASOS QUE RELEI ENTEROS, Y LOS TRES DEFECTOS QUE SALIERON DE AHI**

*El encargo manda declarar la cifra **aunque sea cero**. No es cero: son **`37` de `101`**, el `36,6`
por ciento del tramo. **Y los tres defectos que he encontrado estan los tres dentro de esos `37`.***

| # | donde | lo que decia | lo que la linea dice | especie |
|---:|---|---|---|---|
| **1** | `pedir_critica_primero...` `P06` | *las dos historias mas repetidas del libro eran las de una jefa **dando** critica* | `L87` las **contrasta**: *One was about a boss giving feedback successfully. The other was about what happens when a boss **fails** to give feedback* | **`PUENTE`** |
| **2** | `pedir_critica_primero...` `P15` | *cuando **quien manda** pide critica* | `L109` escribe *When the **CEO** solicits criticism*, y la frase entera va de que la senial baja **del CEO a los jefes intermedios** | **`PUENTE`** |
| **3** | `practicar_triangulo...` `P10` | *conteste con grosería* | `L65` dice *responds rudely*, o sea que el contenido esta bien; lo que estaba mal es **la tilde** | **no es `D.30`**: grafia |

**EL `P06` LLEVABA ADEMAS LA CAUSA INVERTIDA, y es lo mas gordo de los tres.** El paso decia que la
impresion de los lectores venia de que **hubiera** historias de dar critica. `L89` dice lo contrario:

    $ sed -n "89p" fuentes/scott_radical_candor/cap_13.md | cut -c1-260
    Unfortunately, the book didn't have a similarly memorable story about a boss soliciting feedback from an employee. As a result, many readers came away with the impression that Radical Candor is primarily about bosses criticizing employees. Nothing could be

**La causa que el libro escribe es una AUSENCIA**, la de una historia memorable de una jefa **pidiendo**.
El paso la habia convertido en una presencia. **Los dos pasos van reescritos contra `L87` y `L89`, y la
cita de `P06` pasa de la linea `89` sola a las lineas `87` y `89`.**

### BC.4.c. **EL TERCERO NO ES `D.30` Y NO LO CUENTO COMO `PUENTE`, pero lo arreglo**

**Era el unico caracter acentuado de los seis candidatos**, y uno de los dos unicos de todo el dataset:

<!-- TALLADO: parcial salida=.v38/fidelidad_correcciones.txt -->

    $ python .v38/no_ascii.py
    mejorar_consciencia_propia_relacional_dos_practicas  solo ascii
    contar_cuatro_historias_propias_ver_hueco_intencion  solo ascii
    practicar_triangulo_critica_tres_papeles             solo ascii
    pedir_critica_primero_crear_seguridad_psicologica    solo ascii
    elegir_pregunta_recurrente_pedir_critica             solo ascii
    resolver_dudas_frecuentes_pedir_critica              solo ascii

**Esa es la salida DESPUES de corregir.** Antes, `practicar_triangulo_critica_tres_papeles` traia
`0xed LATIN SMALL LETTER I WITH ACUTE x1`. **`dataset/nodos.jsonl` tiene `167` enies, `1` i acentuada
y `1` u con dieresis en `318` nodos**, asi que la grafia de la casa es clara y esta estaba fuera.
**Ninguna guarda la ve**, igual que la vuelta 37 encontro `seniallaras` con doble ele en este mismo
lote: **es la misma familia de defecto, y la caza la misma relectura.**

### BC.4.d. **LO QUE ESTO CONFIRMA DEL AVISO DEL ENCARGO, con mi cifra y no con la suya**

> El encargo me dejo medido que **los tres `PUENTE` del tramo anterior fueron la misma especie**: una
> palabra cambiada dentro de una clausula por lo demas fiel. **Mis dos son de esa misma especie**, y
> los dos cayeron en la clase que el encargo mando releer entera. **La regla caza: `37` pasos
> releidos, `3` defectos, y `0` defectos en los `64` pasos de fuera de esa clase.**

**LO QUE NO PUEDO DECIR**, y lo digo para no venderlo de mas: **no he medido si en esos `64` no hay
nada**, solo que yo no lo he encontrado sin el aviso delante. La cifra honesta es **`3` de `37` con
aviso**, no **`0` de `64` sin el**.
