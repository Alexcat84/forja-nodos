
**LOS TRES, Y LAS DOS CAIDAS DE PUERTA QUE ME COMI EN EL PRIMER CAPITULO CON PROCEDIMIENTO DEL LOTE:**

| candidato | unidad | pasos | saldo de su aduana |
|---|---|---:|---|
| `ceder_control_reforzar_competencia_claridad` | `cap_01`, `L97` | **7** | **`BLOQUEARIA`**, 2 vecinos, los dos del propio lote 5 |
| `encargar_meta_especifica_dejar_libre_metodo` | `cap_02`, `L49` mas `L33` | **5** | **`BLOQUEARIA`**, 2 vecinos, los dos del propio lote 5 |
| `cambiar_forma_trabajar_conservar_plantilla` | `cap_02`, `L29` mas `L25` | **5** | **`BLOQUEARIA`**, 1 vecino del propio lote 5, **`0 CAERIA`** tras sus dos correcciones (`S.6.g`) |

**`BLOQUEARIA` NO ES UN RECHAZO Y LA PROPIA ADUANA LO IMPRIME:** *no es rechazo, es cola de lectura*.
Los tres se levantan **entre si** y **ninguno levanta un vecino del catalogo viejo**, que es lo que
uno espera de la primera cosecha de un libro nuevo: **su vocabulario es suyo.** Y **no escribo sus
veredictos hoy**, porque `D.39` dice que un lote ABIERTO no se inserta: **los veredictos se escriben
en el acto de insertar, y ese acto no llega en esta vuelta.**

### S.6.g. **LAS DOS CAIDAS DE PUERTA, DECLARADAS CON SU NOMBRE**

*`D.23` mide que **cuatro de cada diez** candidatos escritos sin las reglas de id delante caen en la
puerta. **Yo escribi tres y cayeron dos veces**, las dos en el mismo candidato y las dos corregidas
antes de que contara como escrito (`EXTRACTOR.md` 16).*

| # | lo que la aduana dijo | que era | como se arreglo |
|---:|---|---|---|
| **1** | `$.denominaciones.otros_idiomas[0]: se esperaba object y llego str` | escribi `otros_idiomas` como **lista de cadenas** y el esquema pide **objetos con `idioma` y `termino`**. **Cayeron los TRES candidatos** | los tres pasaron a `{"idioma": "ingles", "termino": "..."}` |
| **2** | `id 'cambiar_forma_trabajar_sin_renovar_plantilla': preposicion o articulo prohibido: sin (regla 3)` | **la regla 3, que es la que mas cae de todas**, 35 de los 65 del estreno | el id pasa a `cambiar_forma_trabajar_conservar_plantilla`: **el verbo `conservar` dice lo mismo que `sin renovar` y no lleva preposicion** |

> **LAS DOS VAN DECLARADAS DENTRO DEL PROPIO FICHERO, no solo aqui**, porque un candidato que se
> corrige y no lo cuenta **le esconde a quien lo lea manana que llego a caer**. Y las dos son mias de
> cabo a rabo: **las reglas de id y el esquema estaban escritos antes de que yo tecleara el primer
> candidato**, y `EXTRACTOR.md` 15 dice literalmente que **se leen antes de escribir el primer id, no
> despues del primer rechazo.** Las lei y aun asi cai: **la de la regla 3 la cace la aduana, no yo.**
