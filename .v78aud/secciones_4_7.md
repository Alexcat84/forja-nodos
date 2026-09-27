## 4. **MI BARRIDO DE LAS `20`, SOBRE GRAFO MAS BANDEJAS** (`D.38.4`, `D.38.5`)

Copia de `.v76aud/barrido_uno.py` (la ficha normalizada como la aduana, contra `dataset/nodos.jsonl` mas
`aduana.poblacion_de_bandejas`, con `buscar_vecinos` de `src/aduana.py`) y de `.v76aud/barrer.sh` con la lista cambiada a
`.v78aud/las20.txt`, **cinco a la vez, recogido entero dentro de este turno**, lanzado **despues** de que las fichas cambiasen por
ultima vez (seccion `2`: la ultima es de las `13:40:35`). Antes de lanzarlo guarde la huella de cada ficha de la bandeja y del grafo,
y al recogerlo las comprobe:

@@RUN:0::head -1 .v78aud/barrido.log; tail -1 .v78aud/barrido.log; grep -c "rc=0" .v78aud/barrido.log; grep -c "rc=" .v78aud/barrido.log@@
@@RUN:0::wc -l < .v78aud/huellas_al_barrer.txt; sha1sum -c --quiet .v78aud/huellas_al_barrer.txt && echo "las 20 fichas de la bandeja y el grafo: mismas huellas que al barrer"@@

**Poblacion y vecinos por candidato, cada fila de vecino con su senial, y los pares sin orden:**

@@RUN:0::python .v78aud/vecinos_tabla.py | tee .v78aud/vecinos_tabla.txt@@

**LECTURA:**

1. **Las `20` dan `52` filas de vecino en `34` pares sin orden**, `24` entre dos de la tanda y `10` con uno de fuera, todos del
   grafo. **Coincide con los *52 pares* del asunto de `cc46a0da`**, que ahi llama *pares* a mis filas dirigidas, como en la `73` y la
   `76`; y lo digo como coincidencia.
2. **Casi todo lo levanta `similitud_texto` entre fichas del mismo libro, en la banda de `0,35` a `0,46`**: las fichas de Marquet
   comparten la forma (*El texto lo dice asi*, la cita inglesa en el paso) mas que el procedimiento. La unica fila de otra senial es
   `cambiar_forma_trabajar_conservar_plantilla` contra `escuchar_entender_critica_dominar_defensa` de Scott, por `paso_contra_nodo`.
3. **Cuatro fichas no levantan a nadie**: `asignar_responsable_unico_evolucion_planificada`,
   `eliminar_seguimiento_descendente_responsabilizar_dueno`, `identificar_temas_formacion_tarjetas_decision` y
   `repetir_mensaje_invariable_diario_reunion_evento`, y a ninguna de las cuatro la levanta nadie.
4. **Los de fuera son `8` nodos del grafo**: de Gerber, `operar_modelo_gente_destreza_minima`, `cuantificar_impacto_innovacion_6_pasos`,
   `dictar_ritmo_crecimiento_preguntas_escritas`, `interrogar_negocio_cinco_preguntas` y `cambiar_saludo_cliente_dos_ramas`; de Grove,
   `usar_banco_nueve_preguntas_entrevista` y `pedir_critica_anonima_curso_entrenamiento_dictado`; de Scott,
   `escuchar_entender_critica_dominar_defensa`. **De Zhuo, ninguno.** Los levantan `cambiar_forma_trabajar_conservar_plantilla`,
   `informar_cierre_jornada_conservar_propiedad_trabajo` o `seguir_frustrado_preguntar_implantacion_ideas`, siempre desde un solo lado.
5. **El par de mi `CONTINUA` de la seccion `5` NO lo levanta el barrido en ningun sentido**
   (`observar_reunion_rutinaria_senales_plantilla` con `seguir_frustrado_preguntar_implantacion_ideas`): es arista por lectura
   (seccion `6`).
6. **`D.36`, lo que un solo lado levanta dentro de la tanda**: va a la seccion `7`, y no obliga.

**EL RELOJ, medido y no techo:** de punta a punta en el log de arriba, con fichas de estos segundos (la menor y la mayor):

@@RUN:0::grep "rc=" .v78aud/barrido.log | sed 's/.*segundos=//' | sort -n | sed -n '1p;$p'@@

## 5. **MI LECTURA CIEGA DE LOS PARES** (`1.2`, `6.1`, y solo la vara `6.1`)

**Leidos con los pasos de los dos delante**, todos con `pasos_ciego.py` (`R6`): `.v78aud/pasos_20.txt` para las `20` y
`.v78aud/pasos_fuera.txt` para los ocho de fuera. **Una fila por par** en `.v78aud/mis_clases.tsv`, con su razon. **De donde sale cada
fila:** los pares posibles dentro de un mismo capitulo los escribi **antes de recoger ninguna ficha del barrido**, en
`.v78aud/clases_intra.txt`, **salvo uno que me faltaba** (`recorrer` con `seguir`, que el barrido no levanta) y que anadi al recogerlo,
con su nota dentro del fichero; **por eso la hora de ese fichero es de despues**, y lo que queda de la hora de antes es la de
`.v78aud/aristas_lectura.tsv`, que escribi despues de las clases de dentro y antes de que cerrara la primera ficha. **Esa secuencia
no la prueba ningun instrumento: la declaro.** Los de entre capitulos y los de fuera, al recogerlo, en `.v78aud/clases_fuera.txt`:

@@RUN:0::ls -l --time-style=full-iso .v78aud/aristas_lectura.tsv .v78aud/clases_intra.txt .v78aud/clases_fuera.txt | awk '{print $6, substr($7,1,8), $9}'; ls -l --time-style=full-iso .v78aud/vecinos_*.json | awk '{print substr($7,1,8)}' | sort | head -3@@

`armar_clases.py` los junta, y el cruce comprueba que cada par del barrido tiene su fila y cada fila su par:

@@RUN:0::python .v78aud/armar_clases.py@@
@@RUN:0::python .v78aud/cruce_clases.py@@

**LECTURA: LOS `34` PARES QUE EL BARRIDO LEVANTA SON `SANO`, LOS `34`.** Ninguno es `REPITE`: en todos hay procedimiento fuera del
solape en los dos lados, y en casi todos no hay solape de procedimiento sino de forma (seccion `4`, punto `2`). **Ninguno es
`CONTINUA`**: ningun hijo arranca del producto del otro. **Coincide con los *52 veredictos SANO* del asunto de `cc46a0da`** en la clase
de todas las filas del barrido, y lo digo como coincidencia.

**MI UNICO `CONTINUA` ES DE UN PAR QUE EL BARRIDO NO LEVANTA**, y por eso no es linea de veredicto sino arista por lectura con su
veredicto de la lectura (`D.53`; asi entro `fingir` a `recorrer` en la `77`, `ACTA 76` `76.3`):
`observar_reunion_rutinaria_senales_plantilla` **madre de** `seguir_frustrado_preguntar_implantacion_ideas`. Los pasos de los dos:

@@RUN:0::python .v67aud/normal/pasos_ciego.py observar_reunion_rutinaria_senales_plantilla seguir_frustrado_preguntar_implantacion_ideas | cut -c1-200@@

**La condicion del hijo es lo que el paso `7` de la madre deja visto** (*haber visto en una reunion a un responsable frustrado o a la
defensiva*; L21, *frustrated and defensive*), y **el hijo arranca al acabar esa misma reunion** (L23, *After the meeting I followed
Dave*). El hijo trae procedimiento propio y ningun paso de la madre: no es `REPITE`.

**MIS DUDAS, escritas antes de saber, y si alguna me cae, cae dentro de lo que marco aqui:**

- **Ese `CONTINUA` puede leerse `SANO` con la misma arista `D.29`** si el paso `7` se lee como una senial entre ocho y no como el
  producto del nodo. La arista la sostengo en las dos lecturas; lo que cambia es el veredicto de la lectura.
- **`encargar_meta_especifica_dejar_libre_metodo` con `cambiar_forma_trabajar_conservar_plantilla`**, que el barrido levanta por los
  dos lados: `SANO`, las dos caras de la misma conversacion; si el reto de `cambiar` paso `5` se lee como la consecuencia que
  `encargar` paso `4` saca, seria `CONTINUA` con madre `encargar`.
- **`contar_firmas_cadena_tramite_parado` con `seguir_frustrado_preguntar_implantacion_ideas`**, el par mas cercano del capitulo: sus
  condiciones hacen la misma pregunta (la gente o el sistema) y los dos acaban en el mismo veredicto (falla el sistema). `SANO`: fuera
  de esa pregunta, procedimiento en los dos lados y ningun paso comun.
- **`auditar_formacion_premios_ultima_fila` con `observar_reunion_rutinaria_senales_plantilla`**: la misma familia (leer una rutina
  por sus seniales de gente), `SANO` por `6.1` sin bascula.

**Las madres del grafo que busque por asunto y el barrido no levanta**, leidas con sus pasos y descartadas: Scott
`pasear_organizacion_hallar_problemas_pequenios` (la hora semanal de paseo del jefe de jefes) contra `recorrer`; Scott
`repartir_decision_cercanos_hechos` (su paso `7`, *mira a la sala, no al que habla*) contra `observar`; Zhuo
`comunicar_valores_diez_formas` (*decirlo de diez formas distintas*) contra `repetir_mensaje` (*No cambies el mensaje*); Scott
`ceder_autoridad_unilateral_equipo` contra `ceder_control`; Grove `decidir_nivel_competente_inferior` contra el ejercicio de `cap_06`.
**Dos doctrinas legitimas en cada par, con procedimiento propio en los dos lados, y ninguna es la condicion de la otra**: sin linea,
porque no los levanta el barrido, y sin arista, porque no son madre e hijo. **El de mas peso es el de Zhuo con `repetir_mensaje`**: no
lo leo contradiccion (Zhuo varia la forma y la via; Marquet no cambia el contenido), y lo dejo escrito por si alguien lo lee frontera.

## 6. **LAS ARISTAS POR LECTURA** (`D.29`, `D.37`, `D.53`)

**Las que mi lectura sostiene o descarta**, una fila cada una en `.v78aud/aristas_lectura.tsv`, con su tramo de madre, de hijo y su
linea del libro, **escritas antes de que cerrara la primera ficha del barrido** (seccion `5`), **mirando tambien madres que viven en el
grafo** (la busqueda por asunto, abajo). El cruce dice si el barrido levanto el par y donde vive hoy cada extremo:

@@RUN:0::python .v78aud/cruce_aristas.py@@

**La busqueda por asunto**, por id y titulo sobre grafo mas bandejas:

@@RUN:0::python .v78aud/temas.py | grep -v "^    "@@

(La salida entera, un id por linea con su sede y su libro, en `.v78aud/temas.txt`.)

**LECTURA:**

- **MI UNICO `SOSTENGO` ES `observar_reunion_rutinaria_senales_plantilla` A `seguir_frustrado_preguntar_implantacion_ideas`, POR
  `D.29`**, citando el paso `7` de la madre (`cap_03` L21 y L23), con veredicto de la lectura `CONTINUA` (seccion `5`). El barrido no la
  levanta en ningun sentido: **es arista por lectura, no linea** (`D.53`). **El asunto de `cc46a0da` dice *1 arista por lectura***:
  coincide en la cuenta, y **si no es la misma, difiere de la mia en el par**; lo cruzo par a par en mi turno normal.
- **CUATRO `D.29` DESCARTADAS CON DUDA ESCRITA**, las cuatro por la misma razon: el libro las pone una detras de otra o por analogia,
  pero el hijo no usa el producto de la madre. **`informar_cierre` a `eliminar_seguimiento`** (`cap_09` L43: el tickler se suprime
  *modelado* sobre el cierre de jornada); **`recorrer` a `contar_firmas`** (el paseo es la ocasion, `cap_03` L37); **`encargar_meta` a
  `cambiar_forma`** (la consecuencia de `cap_02` L49 es el reto de L29; este par el barrido si lo levanta, y es su linea `SANO`); y
  **`aplicar_ejercicio` a `identificar_temas_formacion`** (dos ejercicios hermanos de tarjetas; el segundo ataca la preocupacion de
  competencia que `cap_06` L113 nombra, pero sin usar las tarjetas del primero).
- **`D.37` NO DISPARA EN ESTA TANDA.** La unica ficha cuyo texto cuenta partes y las nombra es `ceder_control_reforzar_competencia_claridad`
  (su paso `5`, *las dos cosas*: competencia tecnica y claridad organizativa, `cap_01` L97), y **ninguna de las dos partes existe como
  nodo**: los mecanismos de la bandeja que el libro pone bajo cada pilar son ejemplares del pilar, no el pilar (`D68.7`; la `76` leyo
  asi los tres tipos de sistemas de Gerber). Las listas del libro que si cuentan o enumeran (las frases de `cap_07`, los tres casos de
  urgencia de `cap_08`, los pasos de los dos ejercicios) **son los propios pasos de su ficha**, y ninguna parte vive como nodo aparte.
- **Ninguna madre del grafo para las `20`**, por mi lectura (seccion `5`, ultimo parrafo).

## 7. **EL ORDEN QUE MI LECTURA OBLIGA** (`D.36`)

**No es un orden: son las restricciones**, escritas antes de ver el del extractor. Madre antes que hijo por mis `CONTINUA` y mis
`SOSTENGO` con los dos extremos en la tanda, y cuantas cumple el orden de pieza del libro, **que saco de mi fidelidad** (capitulo y
primera linea), porque `.v78aud/las20.txt` va alfabetica:

@@RUN:0::python .v78aud/restricciones_orden.py@@

**LECTURA:** **la unica que obliga** (`observar` antes que `seguir`, por la arista de la seccion `6`) **la cumple ya el orden de pieza
del libro**. De las `6` de `D.36` de un solo lado, **dos no las cumple** (`reforzar_principios_guia_lenguaje_prueba_conocimiento` antes
que `declarar_intencion_reemplazar_peticion_permiso`, e `inspeccionar_reparto_informacion_notas_jefe` antes que
`recorrer_organizacion_escuchar_plantilla`); **son informativas y no obligan**, porque la aduana de `insertar` mide grafo mas bandejas
(`D.38.5`) y el par se levanta igual desde el lado que entre despues. **Su orden, contra estas siete, lo compruebo en mi turno normal.**

