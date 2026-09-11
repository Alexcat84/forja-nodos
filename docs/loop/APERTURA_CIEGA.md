# APERTURA CIEGA DEL AUDITOR, VUELTA 12, LOTE 3 `zhuo_manager`

*Escrita el 11 sep 2026, ANTES de ver `docs/loop/REPORTE.md`. Cumple `D.34.2` y su
ampliacion del 11 sep (`D.38.3`), y `AUDITOR_FORJA.md` seccion 1.5.*

> **LO QUE NO HE ABIERTO, Y LO DIGO YO PRIMERO.** `docs/loop/REPORTE.md`,
> `docs/loop/loop.log`, `docs/loop/ultimo_extractor.json` y
> `docs/loop/ultimo_auditor.json` **no estan en el arbol y no los he recuperado de
> git ni por ninguna otra via.** No he corrido `git show`, ni `git stash`, ni he
> leido ningun blob de esos cuatro ficheros. **Lo unico que he leido de la vuelta
> 12 es el material: los sesenta candidatos de `cuarentena/zhuo_manager/` y los
> cuatro capitulos de `fuentes/zhuo_manager/`.**

---

## 0. QUE HE LEIDO, Y CON QUE

| lo que abri | cuanto |
|---|---|
| `docs/loop/AUDITOR_FORJA.md` | entero |
| `docs/MANUAL_SISTEMA_DE_CONOCIMIENTO.md` | entero |
| `docs/BANCO_DE_REGLAS.md` | `D.27`, `D.28`, `D.29`, `D.30`, `D.35`, `D.37`, `D.38` |
| `docs/loop/ORDEN_DE_LOTES.md` y `docs/loop/PROMPT_SIGUIENTE.md` | enteros |
| `fuentes/zhuo_manager/cap_07.md` a `cap_10.md` | **enteros, linea a linea** |
| `cuarentena/zhuo_manager/*.json` | **los 60, todos los pasos de todos** |
| `dataset/nodos.jsonl` | los 135 ids y titulos, y 16 vecinos abiertos paso a paso |
| `esquema/nodo.schema.json`, `config/umbrales.json` | enteros |

**NO HE CORRIDO `python forja.py informe` NI NINGUNA SEÑAL EN ESTA FASE, Y ES A
PROPOSITO.** `D.19` dice que ninguna señal separa jerarquia de ruido y que **una
discrepancia nunca se adjudica citando una señal**. Todo lo que clasifico aqui
esta adjudicado **leyendo los pasos de los dos lados**. El instrumento lo corro en
mi turno normal, como manda la seccion 1.1, y **si su cola discrepa de esta
lectura, la discrepancia se declara y no se resuelve copiando.**

---

## 1. LA FRONTERA QUE YO LEO, CON SU SALIDA PEGADA (`D.35`)

**Esta es mi frontera, no la del extractor.** La saque de los encabezados a
columna cero de cada fichero, que es como esta marcado el libro en esta copia
(los parrafos del cuerpo van sangrados con tabulador). Salida literal del
comando que la produjo:

    $ python - <<'EOF'   # lineas a columna cero, sin frontmatter, por capitulo
    for c in ['cap_07','cap_08','cap_09','cap_10']:
        L=io.open('fuentes/zhuo_manager/%s.md'%c,encoding='utf-8').read().split('\n')
        for n,l in enumerate(L,1):
            if n<8 or not l.strip(): continue
            if l[0] not in ' \t' and len(l)<80: print('%4d:%s'%(n,l))
    EOF

    cap_07.md                                        cap_08.md
       9:Chapter Six                                    9:Chapter Seven
      45:WHAT IS A GREAT OUTCOME FOR YOUR MEETING?     39:DESIGN YOUR TEAM INTENTIONALLY
      53:Making a Decision                             63:HIRING IS YOUR RESPONSIBILITY
      97:Sharing Information                           73:Describe Your Ideal Candidate as Precisely as You Can
     117:Providing Feedback                            79:Develop a Sourcing Strategy
     133:Generating Ideas                              87:Deliver an Amazing Interview Experience
     151:Strengthening Relationships                   97:Show Candidates How Much You Want Them
     169:INVITE THE RIGHT PEOPLE                      105:HIRING IS A GAMBLE, BUT MAKE SMART BETS
     187:GIVE PEOPLE A CHANCE TO COME PREPARED        121:Examine Past Examples of Similar Work
     209:MAKE IT SAFE FOR PEOPLE TO CONTRIBUTE        129:Seek Out Trusted Recommendations
     219:Be Explicit about the Norms You Want to Set  143:Get Multiple Interviewers Involved
     231:Change Up Your Meeting Format to Favor P...  149:Look for Passionate Advocates Rather Than Consensus
     243:Manage Equal Airtime                         157:Prepare Your Interview Questions Ahead of Time
     257:Get Feedback about Your Meeting              177:Reject Anyone Who Exhibits Toxic Behavior
     267:SOME MEETINGS DON'T NEED YOU AND SOME DO...  181:Build a Team with Diverse Perspectives
                                                      197:Hire People Who Are Capable of More
    cap_09.md                                         209:Meeting Frogs Is Part of the Deal, but Believe in the Process
       9:Chapter Eight                                221:HIRING WHEN YOU NEED FIVE, TEN, OR HUNDREDS OF PEOPLE
      31:START WITH A CONCRETE VISION                 237:Successful Hiring Is All about Diligent Execution
      59:Create a Believable Game Plan                247:Do Your Research When Hiring Leaders
      73:Craft a Plan Based on Your Team's Strengths  259:Take the Long View with Top Talent
      81:Focus on Doing a Few Things Well             273:Build a Great Bench
      99:Define Who Is Responsible for What           291:Create a Culture That Prioritizes Hiring Well
     115:Break Down a Big Goal into Smaller Pieces
     141:PERFECT EXECUTION OVER PERFECT STRATEGY      cap_10.md
     175:Balancing Short-Term and Long-Term Outcomes     9:Chapter Nine
     181:HIRING                                        33:BIG TEAMS VERSUS SMALL TEAMS
     189:PLANNING                                      39:Direct to Indirect Management
     197:MANAGING PERFORMANCE                          49:People Treat You Differently
     207:Define a Long-Term Vision and Work Backward   63:Context Switching All Day, Every Day
     223:Take a Portfolio Approach                     73:You Pick and Choose Your Battles
     235:Talk about How Everything Relates to the V...  81:The Skills That Matter Become More and More People-Centric
     251:GOOD PROCESS IS EVER EVOLVING                 89:THE TIGHTROPE ACT OF GREAT DELEGATION
                                                      109:GIVING PEOPLE BIG PROBLEMS IS A SIGN OF TRUST
                                                      125:TWO HEADS, ONE SHARED VISION
                                                      147:WHAT TO DO WHEN A MANAGER STRUGGLES
                                                      173:AIM TO PUT YOURSELF OUT OF A JOB

**Nota sobre las anclas del encargo:** el `PROMPT_SIGUIENTE.md` pegaba catorce
anclas y avisaba de que eran *"las anclas que yo vi, no tu frontera"*. Mi frontera
es mas ancha porque incluye los encabezados de segundo nivel; **las catorce suyas
estan todas dentro de la mia, en la misma linea**, y ademas `cap_09` L181 `HIRING`,
que su lista no traia y que es el primero de los tres escenarios de equilibrio.

**LA CUENTA DE MI FRONTERA, PIEZA A PIEZA:**

| capitulo | encabezados | piezas que yo haria nodo | piezas que yo NO haria nodo | candidatos que hay |
|---|---:|---:|---:|---:|
| `cap_07` | 15 | **16** | 2 | **16** |
| `cap_08` | 23 | **21** | 2 | **21** |
| `cap_09` | 16 | **14** | 2 | **14** |
| `cap_10` | 12 | **9** | 3 | **9** |
| | | **60** | **9** | **60** |

> ### **MI FRONTERA COINCIDE CON EL LOTE: 60 Y 60, Y PIEZA A PIEZA.**
>
> No es que cuadren los totales: es que **cada candidato cae en la pieza que yo
> habria cortado**, incluidos los tres cortes que no siguen a un encabezado. Esto
> lo escribo antes de ver el reporte, y **si el reporte declara una frontera
> distinta de esta, uno de los dos se equivoca y se adjudica leyendo.**

### 1.1. Los tres cortes que NO siguen a un encabezado, y que yo tambien haria

| corte | lineas | por que se parte |
|---|---|---|
| `cap_07` L187 se parte en dos | L189 a L201 preparacion, **L203 a L207 seguimiento** | el seguimiento tiene entregable propio, el resumen con sus cuatro contenidos, y ejecutor en otro momento. Da `repartir_material_antes_reunion` y `cerrar_reunion_pasos_siguientes` |
| `cap_07` L231 se parte en dos | la rueda de la sala, **y L237 a L241 las notas adhesivas** | el arranque con notas adhesivas trae caja de tiempo, diez a quince minutos, y secuencia propia que la rueda no tiene. Da `cambiar_formato_reunion_favorecer_participacion` y `abrir_discusion_notas_adhesivas` |
| `cap_09` L141 se parte en dos | el caso de los ciclos cortos, **y L159 a L173 las siete señales** | la lista de siete señales es una comprobacion con su propio si o no. Da `ejecutar_ciclos_cortos_aprender` y `comprobar_equipo_ejecuta_bien` |

### 1.2. Las NUEVE piezas que yo NO haria nodo, y por que

| pieza | lineas | mi lectura |
|---|---|---|
| `cap_07` apertura | L17 a L43 | la reunion de estado fallida y los cinco sentimientos de una buena reunion. **Los cinco son FINES, no medios: `D.27` restriccion 1.** Caso, no nodo |
| `cap_07` **MAKE IT SAFE FOR PEOPLE TO CONTRIBUTE** | L209 a L217 | cierra con *"try the following"* y **no cuenta las tacticas ni trae inventario propio**. Un nodo cabeza aqui solo llevaria el nombre de las otras cuatro: **NOMBRAR NO ES PROCEDIMENTAR** (`P.5.1`). Las cuatro tacticas son **hermanas, no hijas** |
| `cap_08` apertura | L17 a L37 | el candidato Tom y la doctrina *"contratar no es un problema que resolver sino una oportunidad"*. Postura con caso |
| `cap_08` **HIRING IS A GAMBLE, BUT MAKE SMART BETS** | L105 a L119 | trae **tres razones** por las que la entrevista no predice. **Razones no son medios, etapas ni objetos: `D.27` restriccion 1.** Y L119 cierra con *"be smart about your approach"*, que es **adjetivo de adecuacion: restriccion 2**. No es nodo, y es el mejor ejemplar de casa de las dos restricciones a la vez |
| `cap_09` apertura | L17 a L29 | Instagram y la definicion de proceso. Caso mas definicion |
| `cap_09` cierre de Heraclito | L283 a L287 | metafora de cierre |
| `cap_10` apertura | L17 a L31 | las sillas que no llegaban en la critica. Caso |
| `cap_10` **You Pick and Choose Your Battles** | L73 a L79 | *"you must prioritize"* y *"perfectionism is not an option"* **sin ningun inventario**. Postura pura, y su procedimiento ya vive en `priorizar_pocas_cosas_bien` |
| `cap_10` **The Skills That Matter...** | L81 a L87 | nombra cuatro habilidades: contratar lideres, construir equipos autosuficientes, fijar vision, comunicar bien. **Son METAS de desarrollo, no medios: `D.27` restriccion 1** |

> **LO QUE HABRIA SIDO CAIDA Y NO LO ES: las tres cifras citadas del bloque
> `HIRING IS A GAMBLE` no se han perdido al no hacerlo nodo.** Las busque una a una
> y viven redistribuidas en el nodo que cada una sostiene: **Google y su *"zero
> relationship"*** en `examinar_trabajo_pasado_candidato`; **el estudio de Harvard
> de las audiciones a ciegas** en `preparar_preguntas_entrevista_antemano`; y
> **Laszlo Bock** en `buscar_recomendaciones_confianza`. Es lo que pide el reparto
> de perdidas del manual seccion 5: la persuasion es contenido y viaja. **Lo
> compruebo yo y lo declaro yo, porque era el sitio donde habria esperado la
> perdida.**

---

## 2. LA COMPROBACION MECANICA, QUE ES MIA Y LA CORRI YO

    $ python -c "...60 ficheros: id contra nombre, esquema, fuentes, aristas, guiones..."
    cap_07: 16 candidatos, 124 pasos
    cap_08: 21 candidatos, 162 pasos
    cap_09: 14 candidatos, 131 pasos
    cap_10:  9 candidatos,  80 pasos
    TOTAL: 60 candidatos, 497 pasos
    sin asignar: set()  inexistentes: set()
    PROBLEMAS ESTRUCTURALES: ninguno
    ids que ya viven: set()

**Lo que ese comando comprobo, uno a uno sobre los 60:** que el nombre del fichero
y el campo `id` dicen lo mismo; que el `id` es snake_case sin sufijo numerico
(`D.22`); que `fuentes` es exactamente `zhuo_manager` con fecha `2026-09-11`; que
`nodos_previos` y `nodos_siguientes` estan **vacios**, que es lo que `D.29` manda
para cuarentena; que el dominio es `gestion_equipos` y el estado `vivo`; que no hay
ningun campo fuera de los diecisiete del esquema, que declara
`additionalProperties: false`; que no hay **ni un guion largo ni un guion medio**;
y que **ninguno de los 60 ids choca con los 135 que ya viven**.

`escala_minima` aparece en tres candidatos, `abrir_discusion_notas_adhesivas`,
`auditar_calendario_reuniones_semana` y `disenar_equipo_plan_anual`, y **es campo
legitimo del esquema**, no un extra.

---

## 3. `PASOS INVENTADOS POR CAPITULO`, MI CUENTA CIEGA (`AUDITOR_FORJA.md` 8)

**Lei los 497 pasos y los cuatro capitulos enteros.** Esta es mi marca de `D.30`
hecha por mi cuenta, sin ver la del extractor.

| capitulo | pasos escritos | puentes que YO nombro | por ciento |
|---|---:|---:|---:|
| `cap_07` Amazing Meetings | 124 | **1** | **0,81** |
| `cap_08` Hiring Well | 162 | **0** | **0,00** |
| `cap_09` Making Things Happen | 131 | **0** | **0,00** |
| `cap_10` Leading a Growing Team | 80 | **0** | **0,00** |
| **total del lote** | **497** | **1** | **0,20** |

**EL UNICO PUENTE QUE SE SOSTENER, Y ES MEDIO PASO:**

- `cambiar_formato_reunion_favorecer_participacion`, **paso 5**: *"Prueba tambien la
  otra tactica que el libro nombra en esta misma seccion, el arranque con notas
  adhesivas, **que trae pasos propios y una caja de tiempo que esta rueda no
  tiene**."* La primera mitad es del libro (L237: *"Another tactic I like is the
  'Post-it note' opening"*). **La segunda mitad no la dice el libro: es comentario
  de esta casa sobre su propio corte de nodos**, metido dentro de un paso
  accionable. El libro no compara las dos tacticas ni dice que una tenga caja de
  tiempo y la otra no.

**DONDE MIRE CON MAS DUREZA Y NO ENCONTRE PUENTE**, porque es donde `D.30` dice que
sube la cifra (*"el puente sube cuando baja el inventario del parrafo"*):

- `rechazar_conducta_toxica_entrevista`: el parrafo mas pobre del lote, **L179, una
  sola linea de texto**, produce 8 pasos. Los conte contra la linea: **son las cinco
  señales con su frase entre comillas, mas la remision de apertura y el mandato de
  rechazo.** Transcripcion entera. Es el caso que mas se parece al parrafo 32 del
  lote 1, que dio 83 por ciento, y aqui da cero.
- `preguntar_contratar_unica_prioridad`: seis pasos sobre una sola pregunta. Los
  seis salen de L225 a L233.
- `repartir_equipo_cartera_horizontes`: los tercios son del libro (L231).
- `pasar_direccion_directa_indirecta`: las quince horas y los ocho reportes son del
  libro (L43).

> **LO DIGO CON SU LIMITE, PORQUE ES CIFRA MIA (`8.3`): esta es mi cuenta de auditor
> sobre el texto, no una firma de la cifra del extractor.** Si su reporte desglosa
> por capitulo, comparo fila a fila. **Si no desglosa, eso es caida de especie
> `REPORTE` y la nombro**, porque la cifra agregada no se desglosa despues.

**Y LA CONSECUENCIA DE VOLUMEN, QUE ES PARA LO QUE SIRVE LA METRICA:** mi peor
capitulo es `cap_07` con **0,81 por ciento**, muy por debajo del freno del **10 por
ciento** (decision del fundador 5.8). **Con mi lectura, el lote 4 no baja escalon:
sigue a cuatro capitulos por vuelta.**

---

## 4. MI CLASIFICACION DE LOS 60, CANDIDATO A CANDIDATO

**Clases que uso:** `SANO` entra sin madre; `SANO + ARISTA` entra y pide arista
declarada por lectura (`D.29`), con el paso de la madre citado; `CONTINUA` es hijo
de un nodo que ya vive y la arista es obligatoria; `FRONTERA` son dos doctrinas
legitimas que se escriben las dos (manual seccion 4); `REPITE` no entraria.

> **NINGUNO DE LOS 60 ES `REPITE` EN MI LECTURA, Y NINGUNO ES `MUTUO`.** Lo pongo
> arriba porque es la afirmacion mas fuerte de esta pagina y la mas facil de
> desmentirme. La razon es la misma en todos los pares apretados: **la vara no tiene
> bascula, y lo que queda fuera del solape es procedimiento en los dos lados.**

### 4.1. `cap_07`, Amazing Meetings (16)

| # | candidato | pasos | lineas que lo sostienen | mi clase |
|---:|---|---:|---|---|
| 1 | `fijar_resultado_excelente_reunion` | 10 | L45 a L51, L165 a L167 | **SANO, CABEZA.** Aristas a los cinco de abajo **por `D.29` y NO por `D.37`**: L51 dice *"a handful of reasons"* y **no dice cuantas** |
| 2 | `dirigir_reunion_decision` | 14 | L53 a L95 | SANO + ARISTA, hija de 1 |
| 3 | `dirigir_reunion_informativa` | 8 | L97 a L115 | SANO + ARISTA, hija de 1 |
| 4 | `dirigir_reunion_revision_trabajo` | 7 | L117 a L131 | SANO + ARISTA, hija de 1 |
| 5 | `dirigir_reunion_generar_ideas` | 7 | L133 a L149 | SANO + ARISTA, hija de 1 |
| 6 | `dirigir_reunion_reforzar_relaciones` | 8 | L151 a L163 | SANO + ARISTA, hija de 1. Vecino `dirigir_reunion_individual_semanal`, que ya vive: L155 nombra *"some 1:1s"* como medio. **Hermanos, no madre e hija** |
| 7 | `invitar_personas_necesarias_reunion` | 8 | L169 a L185 | SANO |
| 8 | `repartir_material_antes_reunion` | 7 | L187 a L201 | SANO |
| 9 | `cerrar_reunion_pasos_siguientes` | 7 | L203 a L207 | SANO. Solapa con el cuarto logro de 4 (L131) y con 1: **hermanos** |
| 10 | `decir_normas_participacion_voz_alta` | 8 | L219 a L229 | SANO. **DISCUTIBLE 7** con `facilitar_gente_diga_verdad` del `cap_10` |
| 11 | `cambiar_formato_reunion_favorecer_participacion` | 6 | L231 a L236 | SANO, madre de 12 por **`D.29`**: L235 y L237 enumeran **sin contar**. **Lleva mi unico puente, paso 5** |
| 12 | `abrir_discusion_notas_adhesivas` | 6 | L237 a L241 | SANO + ARISTA, hija de 11, citando su paso 5 |
| 13 | `mediar_tiempo_palabra_reunion` | 6 | L243 a L255 | SANO |
| 14 | `pedir_opinion_propia_reunion` | 6 | L257 a L265 | **CONTINUA** de `pedir_opinion_otros_mejorar`, que ya vive: estrecha el objeto a la reunion propia y trae la pregunta literal. **DISCUTIBLE 6** |
| 15 | `auditar_calendario_reuniones_semana` | 10 | L267 a L281 | SANO |
| 16 | `avisar_organizador_reunion_prescindible` | 6 | L283 a L289 | SANO. Unica pieza del capitulo cuyo ejecutor no es quien convoca |

### 4.2. `cap_08`, Hiring Well (21). Aqui trabaja la aduana de verdad: 59 nodos de `smart_who` enfrente

| # | candidato | pasos | lineas | mi clase y el vecino que lei paso a paso |
|---:|---|---:|---|---|
| 1 | `disenar_equipo_plan_anual` | 13 | L39 a L61 | SANO. Vecino `desplegar_estrategia_tarjeta_puntuacion`: hermanos |
| 2 | `repartir_papeles_directivo_reclutador` | 7 | L63 a L71 | SANO, CABEZA de 3 a 6 por **`D.29`**: L71 dice *"Here's how you should approach working together"* **sin contar**. Tiene procedimiento propio, el reparto de que trae cada parte, asi que no es solo el nombre de las otras |
| 3 | `describir_candidato_ideal_precision` | 5 | L73 a L77 | **FRONTERA con `crear_tarjeta_puntuacion_puesto`. DISCUTIBLE 2** |
| 4 | `desarrollar_estrategia_busqueda_candidatos` | 5 | L79 a L85 | SANO. Vecino `abastecer_flujo_candidatos`, *"con sus seis vias"*: **no es `D.37`**, porque esta no es ninguna de las seis. Cierre literal de `D.37`: *son hermanos, y su veredicto es `SANO`* |
| 5 | `entregar_experiencia_entrevista_excelente` | 8 | L87 a L95 | SANO. Vecino `organizar_jornada_entrevistas_candidato`: hermanos |
| 6 | `mostrar_candidato_cuanto_quieres` | 8 | L97 a L103 | **CONTINUA de `sostener_contacto_oferta_aceptacion`. DISCUTIBLE 1, el mas apretado del lote** |
| 7 | `examinar_trabajo_pasado_candidato` | 7 | L121 a L127 | SANO |
| 8 | `buscar_recomendaciones_confianza` | 10 | L129 a L141 | SANO + TRES ARISTAS. **DISCUTIBLE 4** |
| 9 | `involucrar_varios_entrevistadores` | 5 | L143 a L147 | SANO. **DISCUTIBLE 5** con `asignar_entrevistas_enfocadas_equipo` |
| 10 | `rechazar_contratacion_tibia` | 6 | L149 a L155 | SANO, roza FRONTERA con `decidir_contratacion_final`: alli se decide por calificacion A sobre la tarjeta, aqui por intensidad del defensor. **No chocan, se cruzan** |
| 11 | `preparar_preguntas_entrevista_antemano` | 12 | L157 a L175 | SANO. Vecino `conducir_entrevista_cronologica_trayectoria`: dos guiones distintos, procedimiento en los dos lados |
| 12 | `rechazar_conducta_toxica_entrevista` | 8 | L177 a L179 | **FRONTERA con `revisar_banderas_rojas_candidato`. DISCUTIBLE 3** |
| 13 | `construir_equipo_perspectivas_diversas` | 8 | L181 a L195 | SANO. Vecinos `usar_lenguaje_no_discriminatorio_entrevista` y `evitar_preguntas_ilegales_entrevista`: alli es cumplimiento legal, aqui es composicion del equipo |
| 14 | `contratar_personas_capaces_mas` | 6 | L197 a L207 | SANO |
| 15 | `calcular_embudo_reclutamiento_propio` | 6 | L209 a L219 | SANO, hermano de 17. **DISCUTIBLE 9, intra lote** |
| 16 | `preguntar_contratar_unica_prioridad` | 6 | L221 a L233 | SANO. **DISCUTIBLE 10**: es el candidato mas fino del lote frente a `D.27` |
| 17 | `ejecutar_embudo_reclutamiento_escala` | 8 | L237 a L245 | SANO, hermano de 15 |
| 18 | `investigar_antes_contratar_lideres` | 10 | L247 a L257 | SANO. Vecino `distinguir_perfil_guepardo_cordero`: hermanos |
| 19 | `cultivar_relacion_talento_largo_plazo` | 7 | L259 a L271 | SANO. **DISCUTIBLE 8** con `reservar_media_hora_semanal_talento` |
| 20 | `probar_banquillo_vacaciones_largas` | 9 | L273 a L289 | SANO |
| 21 | `repartir_responsabilidad_contratar_equipo` | 8 | L291 a L301 | SANO. Vecinos `instalar_metodo_contratacion_empresa` y `formar_equipo_practicas_metodo`: hermanos, porque alli se instala un metodo nombrado y aqui se reparte la responsabilidad |

### 4.3. `cap_09`, Making Things Happen (14)

| # | candidato | pasos | lineas | mi clase |
|---:|---|---:|---|---|
| 1 | `fijar_vision_concreta_equipo` | 14 | L31 a L57 | SANO, CABEZA del capitulo |
| 2 | `crear_plan_creible_equipo` | 6 | L59 a L71 | SANO + ARISTA, hija de 1: L61 dice *"Let's say you have a concrete vision... Now you have to figure out a plan"* |
| 3 | `ajustar_plan_fuerzas_equipo` | 7 | L73 a L79 | SANO + ARISTA, hija de 2 por **`D.29`**: L71 enumera **sin contar** |
| 4 | `priorizar_pocas_cosas_bien` | 9 | L81 a L97 | SANO + ARISTA, hija de 2. Vecino `repartir_tiempo_atencion_mejores_equipo`, que ya vive: **el mismo principio aplicado a personas y no a tareas. Hermanos** |
| 5 | `definir_quien_responde_cada_cosa` | 9 | L99 a L113 | **CONTINUA de `fijar_proceso_trabajo_equipo`. DISCUTIBLE 11** |
| 6 | `partir_meta_grande_hitos` | 13 | L115 a L139 | SANO + ARISTA, hija de 2 |
| 7 | `ejecutar_ciclos_cortos_aprender` | 10 | L141 a L157 | SANO |
| 8 | `comprobar_equipo_ejecuta_bien` | 7 | L159 a L173 | SANO. Su paso 6, *"cada tarea tiene un quien y un para cuando"*, nombra a 5: arista `D.29` |
| 9 | `equilibrar_corto_largo_plazo` | 12 | L175 a L205 | SANO, CABEZA **con inventario propio**: tres escenarios con su situacion y sus dos riesgos, escritos por el libro en L181, L189 y L197. **Por eso esta si es nodo y las dos cabezas de 1.2 no lo son**, y estoy de acuerdo |
| 10 | `definir_vision_larga_trabajar_atras` | 9 | L207 a L221 | SANO + ARISTA, hija de 9 |
| 11 | `repartir_equipo_cartera_horizontes` | 6 | L223 a L233 | SANO + ARISTA, hija de 9 |
| 12 | `ligar_tareas_proposito_organizacion` | 8 | L235 a L249 | **CONTINUA de `alinear_equipo_proposito_comun`. DISCUTIBLE 12** |
| 13 | `hacer_repaso_posterior_proyecto` | 10 | L251 a L263 | SANO |
| 14 | `crear_manuales_jugadas_repetibles` | 11 | L265 a L281 | SANO. **Absorbe el caso del correo semanal, L271 a L281, en vez de hacerlo nodo, y eso es lo correcto** por manual seccion 3.5 |

### 4.4. `cap_10`, Leading a Growing Team (9)

| # | candidato | pasos | lineas | mi clase |
|---:|---|---:|---|---|
| 1 | `pasar_direccion_directa_indirecta` | 7 | L39 a L47 | SANO. Vecino `planificar_reduccion_trabajo_individual`: alli se suelta trabajo de contribuidor individual, aqui se ponen capas de direccion. **Hermanos** |
| 2 | `facilitar_gente_diga_verdad` | 8 | L49 a L61 | SANO. **DISCUTIBLE 7** |
| 3 | `sostener_cambio_contexto_continuo` | 8 | L63 a L71 | SANO. Vecinos `disenar_entorno_rendir_mejor` y `establecer_limites_cuidado_personal`: hermanos |
| 4 | `equilibrar_microdireccion_ausencia` | 8 | L89 a L107 | SANO, CABEZA del bloque de delegacion |
| 5 | `entregar_problema_dificil_reporte` | 9 | L109 a L123 | SANO + ARISTA, hijo de 4. **Deja fuera la historia de la abuela, L111 a L115, y hace bien**: es fondo, no procedimiento |
| 6 | `alinear_prioridades_reporte_directivo` | 11 | L125 a L145 | **CONTINUA de `revisar_proposito_personas_proceso`. DISCUTIBLE 13** |
| 7 | `decidir_directivo_no_encaja_papel` | 9 | L147 a L171 | **CONTINUA de `mover_rapido_persona_papel_equivocado`. DISCUTIBLE 14, el de mayor riesgo de `REPITE` del lote entero** |
| 8 | `reemplazarse_trabajo_propio` | 11 | L173 a L199 | SANO. **DISCUTIBLE 15** |
| 9 | `reservar_valor_unico_prioridades_arriba` | 9 | L201 a L221 | SANO, hermano de 8. **DISCUTIBLE 16, intra lote** |

---

## 5. MIS DISCUTIBLES, EN ORDEN DE CUANTO ME COSTARON

**Estos son los pares que yo marco ANTES de ver si el extractor los marco.** Esa
diferencia es lo unico que hace informativa la metrica (`5.1`), y por eso van aqui,
sellados.

### 1. `mostrar_candidato_cuanto_quieres` contra `sostener_contacto_oferta_aceptacion`

**La ventana de activacion es LA MISMA en los dos**: desde que entregas la oferta
hasta que el candidato responde. Los dos dicen que no te apartes y que mantengas el
contacto.

- **Paso 3 de la madre** (`smart_who`, ya vive): *"Manten el contacto con ella con
  regularidad."*
- **Paso 3 del candidato** (`zhuo_manager`): *"Despues de entregar la oferta,
  contacta con el candidato **cada dos dias**..."*, y su paso 2 pone el
  contraejemplo tambien con numero, *"dejando pasar una semana entre
  comunicaciones"*.

**MI ADJUDICACION: `CONTINUA`, y la arista es obligatoria.** El hijo **pone numero
donde la madre pone un adverbio**: eso es exactamente *una linea que tarda varios
pasos en ejecutarse* (manual seccion 4). La madre conserva procedimiento propio
fuera del solape, las cinco efes, la familia, la libertad, la fortuna y la
diversion, cada una ya con su nodo, asi que **no es `REPITE`**. La arista se
declara por `D.29` **citando el paso 3 de la madre**.

### 2. `describir_candidato_ideal_precision` contra `crear_tarjeta_puntuacion_puesto`

Mismo acto, definir el puesto antes de buscar. Y **los dos libros se contradicen
sobre el instrumento**, que es lo que lo hace interesante:

- `asignar_entrevistas_enfocadas_equipo` (de `smart_who`, ya vive), **paso 1**:
  enfoca la entrevista en la tarjeta *"y no en una **descripcion de puesto**
  vagamente definida"*.
- `zhuo_manager`, **L75**: *"Write the job description yourself and be specific."*

**MI ADJUDICACION: `FRONTERA DECLARADA`, no duplicado.** Manual seccion 4: *dos
doctrinas legitimas no son duplicado, son frontera declarada; se escriben las dos
posiciones con sus fuentes.* **Una frontera se pierde por poda, no por fusion.**

### 3. `rechazar_conducta_toxica_entrevista` contra `revisar_banderas_rojas_candidato`

**El choque esta en el verbo operativo, y es literal:**

- `revisar_banderas_rojas_candidato` (ya vive), **paso 1**: *"Trata estas pistas
  como banderas, **no como motivos de descarte**. Las banderas en si no matan el
  trato."*
- El candidato, **paso 8**: *"**Rechaza** a quien exhiba esa conducta."* Y L177 es
  el titulo literal del libro: *Reject Anyone Who Exhibits Toxic Behavior*.

Y las dos listas se cruzan en contenido: *hablar mal de jefes anteriores* esta en
las dos, y *culpar a otros de los fracasos* esta en las dos, alli como *pasar la
pelota* y *poner excusas*.

**MI ADJUDICACION: `FRONTERA DECLARADA`.** Un libro dice explorar, el otro dice
rechazar, y **ninguno de los dos es un error del otro**. Esto es doctrina que hay
que escribir por los dos lados, no fundir. **Si alguien funde estos dos, la casa
pierde la contradiccion mas util que han producido tres libros.**

### 4. `buscar_recomendaciones_confianza` contra tres nodos de `smart_who` a la vez

Es el candidato con mas solape del lote: toca `pedir_referencias_empleados` (L133,
la varita magica al equipo propio), `pedir_referencias_red_personal` (L137, la
conexion comun de confianza) y `conducir_llamadas_referencia` (L135 a L139, la
comprobacion de referencias).

**MI ADJUDICACION: `SANO` con tres aristas declaradas.** Lo que queda fuera del
solape es procedimiento en los dos lados: alli, el sistema con prima por referencia
y las siete llamadas con su codigo; aqui, **los dos correctivos al evaluar**,
descontar la opinion negativa que no sea reciente (L139) y vigilar que la red propia
no estreche el grupo de candidatos (L141), que ninguno de los tres tiene.

> **Y MI RESERVA, QUE DECLARO PORQUE ES MIA: este es el candidato del lote que mas
> cerca esta de ser DOS nodos**, abastecer por recomendacion y evaluar referencias.
> Lo dejo en uno porque el libro lo escribe bajo una sola doctrina en una sola
> seccion, pero **si el extractor lo partio, su lectura tambien se sostiene y lo
> dire asi.**

### 5. `involucrar_varios_entrevistadores` contra `asignar_entrevistas_enfocadas_equipo`

Cinco pasos frente a seis, y los dos dicen *reparte la entrevista entre varios que
pregunten cosas distintas*.

**MI ADJUDICACION: `SANO`.** Fuera del solape, el candidato trae **el registro
independiente antes de la puesta en comun, con su razon nombrada por el libro, el
pensamiento de grupo** (L147), que el nodo que vive no tiene en ninguno de sus seis
pasos; y el que vive trae el reparto por resultados y competencias de la tarjeta y
la caja de cuarenta y cinco a sesenta minutos. **Procedimiento en los dos lados.**

### 6. `pedir_opinion_propia_reunion` contra `pedir_opinion_otros_mejorar`

**`CONTINUA`.** El hijo estrecha el objeto a *tu propia reunion* y trae la pregunta
literal (L263). La arista cita el paso de la madre que manda pedir opinion a todo el
mundo todo el tiempo.

### 7. `decir_normas_participacion_voz_alta` (`cap_07`) contra `facilitar_gente_diga_verdad` (`cap_10`)

**Intra lote, y los dos son del mismo libro.** Los dos dicen *di en voz alta que
quieres que te contradigan*.

**MI ADJUDICACION: `SANO`, hermanos.** El del `cap_07` esta acotado a una reunion y
su procedimiento es **un parlamento troceado en tres frases** (L227); el del
`cap_10` esta acotado al **desnivel de autoridad** y su procedimiento son **cuatro
contramedidas** (L61), de las que solo una es decir la norma. Solapan en una de las
cuatro, no en las cuatro.

### 8 a 16, los que marco sin desarrollar porque los resolvi rapido

| # | par | mi clase |
|---:|---|---|
| 8 | `cultivar_relacion_talento_largo_plazo` contra `reservar_media_hora_semanal_talento` | SANO. Alli, media hora fija los lunes con guion de llamada; aqui, congresos, reputacion del equipo y que decir a quien te dijo que no |
| 9 | `calcular_embudo_reclutamiento_propio` contra `ejecutar_embudo_reclutamiento_escala` | SANO, hermanos. Uno produce **la ecuacion** (L217), el otro **el reparto entre directivos y semanas mas el programa de formacion** (L241) |
| 10 | `preguntar_contratar_unica_prioridad` frente a `D.27` | ENTRA, en el filo. Lo salva que la pregunta trae el acto que la ejecuta, mirar el calendario propio contra ella, y que el libro escribe el antes y el despues (L225 a L229) |
| 11 | `definir_quien_responde_cada_cosa` contra `fijar_proceso_trabajo_equipo` | **CONTINUA.** El paso 2 de la madre es *"Contesta quien debe hacer que y para cuando"*: **una linea. El hijo la ejecuta en nueve pasos, con dos frases literales** (L113). Arista obligada, citando ese paso 2 |
| 12 | `ligar_tareas_proposito_organizacion` contra `alinear_equipo_proposito_comun` | **CONTINUA.** Lo que añade el hijo y la madre no tiene: **el aviso de no confundir el proposito con el indicador que lo mide**, con su ejemplo numerico y su consecuencia observable (L245 a L247) |
| 13 | `alinear_prioridades_reporte_directivo` contra `revisar_proposito_personas_proceso` | **CONTINUA, y la que mas me hizo dudar de las tres.** Los tres cubos, proposito, personas y proceso, son **los mismos tres**. Lo que lo salva de `REPITE`: alli los tres cubos ordenan **tu propio trabajo de directivo**; aqui son **la agenda de alineamiento con un reporte que ya es directivo**, con su segunda capa de preguntas escrita por el libro (L137, L143, L145). Arista obligada |
| 14 | `decidir_directivo_no_encaja_papel` contra `mover_rapido_persona_papel_equivocado` y `elegir_recolocar_despedir_persona` | **CONTINUA, y el de mayor riesgo de `REPITE` del lote entero.** Lo que añade: **el objeto es un DIRECTIVO** y no un contribuidor; **el patron del equipo que crecio mas que su jefe sin que nadie hiciera nada mal** (L155 a L157); y **la pregunta del puesto abierto** (L165), que no es la misma que la del nodo que vive, *"recomendaria yo que otro equipo la contratara"*. **Dos preguntas parecidas del mismo libro en capitulos distintos: se declaran las dos, no se funden** |
| 15 | `reemplazarse_trabajo_propio` contra `planificar_reduccion_trabajo_individual` | SANO. Alli el disparador tiene numero, cuatro o cinco personas, y el objeto es trabajo de contribuidor individual; aqui la regla es continua y el objeto es **cualquier** trozo del trabajo, con la regla de la interseccion (L189) |
| 16 | `reemplazarse_trabajo_propio` contra `reservar_valor_unico_prioridades_arriba` | **Intra lote, y mi mayor duda de frontera del `cap_10`.** Son **las dos mitades de la misma regla** de L189: una dice que se entrega, la otra que se guarda. Los dejo **hermanos con arista** porque los entregables son opuestos y el segundo trae tres patrones propios con nombre (L205, L209, L211), pero **acepto de antemano que un solo nodo tambien se sostiene**, y si el extractor lo hizo asi no lo llamo caida |

---

## 6. LO QUE SE ME QUEDA ABIERTO Y VERIFICO EN MI TURNO NORMAL

1. **Las aristas.** En mi lectura este lote pide **al menos veintiuna aristas
   declaradas por lectura**: las cinco de la cabeza de reuniones, la de las notas
   adhesivas, las cuatro de la cabeza del reclutador, las cinco del `cap_09`, las
   dos del `cap_10`, y las cinco `CONTINUA` contra nodos que ya viven. **Ninguna la
   levanta una señal** (`D.19`: `paso_contra_nodo` caza el 3 por ciento de las
   aristas declaradas). Verifico que esten declaradas, con su paso citado, y que la
   madre entre primero.
2. **`fijar_proceso_trabajo_equipo` paso 7 es madre de medio lote, y nadie lo ha
   dicho todavia.** Nombra *"dirigir reuniones eficaces, blindarte contra los
   errores del pasado, planificar el maniana y cultivar una cultura sana"*: eso
   apunta al `cap_07` entero, a `hacer_repaso_posterior_proyecto`, a
   `crear_plan_creible_equipo`, y al `cap_11` que todavia no se ha minado.
   **Enumera sin contar, asi que es `D.29` y no `D.37`**, y cada arista necesita su
   razon escrita. **Es el hueco de jerarquia mas grande que veo en el lote.**
3. **`D.37` no se aplica ni una vez en los sesenta**, en mi lectura. Ninguna cabeza
   de estos cuatro capitulos **dice cuantas partes tiene**: *a handful of reasons*,
   *a few key skills*, *some things to keep in mind*, *here are some ways*. **Cero
   cabezas pasan, y todas caen en `D.29`.** Es la misma lectura estrecha que la
   vuelta 11 sostuvo y que el fundador ratifico el 11 sep.
4. **El informe y su reloj.** No lo he corrido. Con la bandeja en 60 y `_insertados`
   ya archivado, si el coste sigue creciendo eso es del instrumento y se trae
   (decision del fundador 5.6), no se arregla.
5. **Las cuatro guardas y la mutacion.** Se corren en mi turno: **toda guarda que el
   reporte declare mordiendo se re corre mutando el valor esperado** (cosecha 7.C),
   o se declara que no hay caso rojo automatico.
6. **La muestra pineada de los SANO** (seccion 7): la semilla se escribe en el acta
   y el sorteo se hace **despues** de tener la nomina de veredictos de la tanda, que
   todavia no existe. **No la invento aqui.**

---

## 7. MI PREDICCION, SELLADA ANTES DE LEER EL REPORTE

*Esto no es medida: es lo que espero, escrito para poder fallar por escrito.*

| espero | mi apuesta |
|---|---|
| frontera del extractor | **igual a la mia, pieza a pieza** |
| sus puentes por capitulo | **entre 0 y 3 en todo el lote**, y que incluya alguno que yo no vi |
| coincidencia en el puente que yo nombro | **baja**: es comentario de casa dentro de un paso, y desde dentro no se ve |
| sus discutibles marcados | **`rechazar_conducta_toxica_entrevista` y `mostrar_candidato_cuanto_quieres` casi seguro**; los `CONTINUA` del `cap_09` y del `cap_10` contra nodos de vueltas anteriores, **menos seguro**, porque piden acordarse del grafo y no del libro |
| donde creo que puedo estar yo equivocado | en llamar `CONTINUA` a `alinear_prioridades_reporte_directivo`. Los tres cubos repetidos **tambien admiten leerse como hermanos**, y si el extractor lo argumenta leyendo los pasos, **su lectura vence a la mia si yo publico metadato y el publica lectura** (`P.17`) |

---

**Sesenta candidatos leidos, 497 pasos contados, cuatro capitulos leidos enteros,
un puente nombrado, dieciseis discutibles marcados, cero `REPITE`, y cero ficheros
retirados recuperados.**

*Fin de la apertura ciega. El arnes sella este fichero, y despues de sellado no lo
toco.*
