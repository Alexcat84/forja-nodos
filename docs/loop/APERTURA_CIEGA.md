# APERTURA CIEGA DEL AUDITOR, vuelta 8 del lote 2 (`smart_who`)

**Fecha: 10 sep 2026. Rama `extraccion-mundo-11`. HEAD leido al abrir: `71ac002`.**
Escrita bajo `D.34` (`AUDITOR_FORJA.md` seccion 1.5): el arnes retiro
`docs/loop/REPORTE.md` del arbol antes de invocarme, yo clasifico el material por mi
cuenta, el arnes sella este fichero, y solo despues se me expone el reporte.

**COMPROBADO POR MI AL ABRIR, y se dice porque es la condicion de todo lo demas:**

    $ ls -la docs/loop/REPORTE.md
    ls: cannot access 'docs/loop/REPORTE.md': No such file or directory
    $ git status --short docs/loop/REPORTE.md
     D docs/loop/REPORTE.md

**NO lo he recuperado de git ni por ninguna otra via**, ni con `git show`, ni con
`git checkout`, ni leyendo `ultimo_extractor.json`. Lo unico que lei de `docs/loop/`
fue `AUDITOR_FORJA.md`, `ORDEN_DE_LOTES.md`, el `tail` de `loop.log` y **mi propia
acta** de la vuelta 7 (secciones 1.8 y 3.2), que es sede mia y no del extractor.

## 0.1. LA CONTAMINACION QUE SI TENGO, declarada antes que mi primera clase

Una apertura que se llama ciega y no dice por donde entra la luz miente. Lo que supe
del trabajo del extractor **antes** de escribir ninguna clase, y de donde:

| lo que supe | de donde | que me contamina |
|---|---|---|
| los **15 ids** de los candidatos | `ls cuarentena/smart_who/` | **es la contaminacion grave: se que corto antes de leer el libro.** Mi frontera no es virgen, es una frontera releida sabiendo el resultado |
| los tramos **A (cap_06 L247-455), B (cap_07 L9-41) y C (cap_07 L43-429)** | asuntos de commit del `git log` | supe los cortes, no los juicios |
| que el tramo B dio **cero candidatos** y el C **siete piezas y cero minables** | asuntos de commit | **sabia el resultado de B y de C antes de leerlos.** Mi lectura de esos dos tramos vale como confirmacion, no como lectura ciega |
| que el informe del lote dio **15 candidatos, 0 caerian, 0 chocan** | asunto de commit `4934ba1` | cifra de aduana, no de clase |

**NO supe, y por eso lo de abajo si es lectura propia:** que piezas marco discutibles,
que pasos declaro PUENTE, que cifra de `PASOS INVENTADOS` publica, ni con que razon
dejo fuera lo que dejo fuera.

**EL ORDEN REAL EN QUE TRABAJE, y es el correcto:** lei el tramo A entero
(`sed -n '247,455p'`), luego el B y el C, **y solo despues** volque los 15 JSON campo
a campo. Las clases de la seccion 1 estan escritas contra el libro, no contra los
ficheros. **Pero conocia los 15 nombres desde el `ls` inicial**, y eso no se deshace
diciendolo: se declara y se resta al valor de la coincidencia.

---

# 1. MI FRONTERA DEL TRAMO A: `cap_06.md` L247 a L455

**Siete piezas de nivel de seccion**, cortadas por titulo, con el rango que yo mismo
imprimi. La columna de clase es mia y esta escrita antes de abrir ningun JSON.

| # | pieza | lineas | mi clase |
|---:|---|---|---|
| A1 | `HOW TO INSTALL THE A METHOD FOR HIRING IN YOUR COMPANY` | L247 a L295 | **MINABLE. Serie numerada de diez con cabeza** |
| A2 | `LEGAL TRAPS TO AVOID` | L297 a L317 | **MINABLE. Serie numerada de cuatro con cabeza** |
| A3 | `THOUGHTS ON BUILDING YOUR TEAM` | L319 a L331 | **NO MINABLE** |
| A4 | `RIDING THE RISING TIDE` | L333 a L349 | **NO MINABLE**, y es discutible |
| A5 | `WHAT TYPES OF CEOS MAKE MONEY FOR INVESTORS?` (recuadro) | L351 a L393 | **MINABLE. Un nodo, y es discutible** |
| A6 | `BEYOND HIRING` | L395 a L415 | **MINABLE. Un nodo, y es el mas discutible del lote** |
| A7 | `YOU CAN DO IT` | L417 a L455 | **NO MINABLE**, y es la que un segundo lector podria defender |

## 1.1. A1, las diez cosas: pieza a pieza, con la linea que la sostiene

**La cabeza esta en L251** (*"You have to do ten things if you want to install the A
Method for Hiring in your business"*), y por manual 3.4 una serie enumerada da cabeza
mas miembros. Mi juicio de cada miembro:

| cosa | linea | mi clase | por que |
|---:|---|---|---|
| 1. Make people a top priority | L253 | **NO da nodo propio. LIMITE** | fija una prioridad y manda comunicar urgencia, pero **el procedimiento de hacerlo ya vive en el grafo**: `reservar_media_hora_semanal_talento` es literalmente como se pone a la gente en la agenda. Lo que queda fuera es postura, y una postura no ejecuta (vara 6.1) |
| 2. Follow the A Method yourself | L255 | **NO da nodo. Claro** | postura pura (*"They lead by example"*) y **REPITE `aplicar_metodo_ghsmart_contratacion`** por entero: nombrar el metodo no es procedimentarlo (`P.5.1`) |
| 3. Build support among your executive team or peers | L257 | **MINABLE** | cuatro medios propios: comprometer al equipo, relaciones personales, repartir libros, jornadas y talleres |
| 4. Cast a clear vision | L259 | **MINABLE** | trae tres mensajes tipo literales y el respaldo con actos |
| 5. Train your team on best practices | L261 | **MINABLE, y es el mas flaco de los ocho** | un solo medio propio: el taller practico que pone las herramientas en la mano. Pasa, pero por poco |
| 6. Remove barriers | L263 | **MINABLE** | nombra el con quien (personal) y las tres clases de barrera |
| 7. Implement new policies | L265, con L267, L269 y L271 | **MINABLE, el mas rico** | tres politicas escritas con su umbral del noventa por ciento y su guardian |
| 8. Recognize and reward | L273 | **MINABLE** | reconocimiento publico mas variable atado a un resultado concreto |
| 9. Remove managers not on board | L275 | **MINABLE** | tiene condicion de disparo, cautela previa y acto |
| 10. Celebrate wins and plan for more change | L277 | **MINABLE** | tres recompensas nombradas y el cierre de ciclo sobre la cosa uno |
| moral del COO y del *"you don't have to be the CEO"* | L279 a L295 | **NO da nodo propio** | relato mas moral; la moral cabe como ultimo paso de la cabeza, y ahi es donde debe estar |

**MI CUENTA DE A1: cabeza mas OCHO miembros, es decir NUEVE nodos.** Las cosas 1 y 2
se quedan fuera con la razon escrita arriba.

## 1.2. A2, las cuatro cautelas legales: **AQUI ESTA MI DISCREPANCIA**

Cabeza en L299 a L305 (*"To stay well within the law, we suggest you respect these
four areas of caution"*), con el marco legal de L301 y la linea de fondo de L317.

| cautela | linea | mi clase |
|---:|---|---|
| 1. Relevance | L307 | **MINABLE** |
| 2. Standardization of hiring process | L309 | **MINABLE. Y NO HAY CANDIDATO PARA ELLA** |
| 3. Use nondiscriminatory language | L311 | **MINABLE** |
| 4. Avoid asking candidates illegal questions | L313 | **MINABLE** |

**MI CUENTA DE A2: cabeza mas CUATRO miembros, es decir CINCO nodos. En cuarentena hay
CUATRO.**

**EL HUECO ES LA CAUTELA DOS**, y lo sostengo con la simetria del propio tramo. L309
dice entero: *"Standardization of hiring process. Use the same process for all
candidates regardless of their demographic group. Managers get into trouble when they
consciously or inadvertently put different groups through different processes. A
standard process ensures fairness across all groups."*

Eso es **un imperativo, su modo de fallo y su razon**: exactamente la misma forma y
casi el mismo tamaño que L311, la cautela tres, **que si tiene nodo**
(`usar_lenguaje_no_discriminatorio_entrevista`, cuatro pasos, tres de ellos
reformulaciones de la misma linea). **Si L311 procedimenta, L309 procedimenta.** Y su
contenido no vive en ningun otro sitio del grafo:
`seleccionar_jugador_cuatro_entrevistas` manda el orden de las cuatro entrevistas, pero
**ninguno de los 52 nodos vivos dice que el proceso tiene que ser el mismo para todos
los grupos demograficos.**

**Mi clase: falta un candidato**, cuyo id natural seria
`estandarizar_proceso_todos_candidatos`. **Se anota como discrepancia, no como caida
todavia**: si el reporte lo marco como discutible, la comparacion existe y se adjudica;
si lo dejo fuera sin declararlo, es un hueco de serie no declarado en una serie que el
propio titulo enumera (`D.37`).

## 1.3. A3, A4 y A7: por que las dejo fuera, con su linea

**A3, `THOUGHTS ON BUILDING YOUR TEAM` (L319 a L331). NO MINABLE, y sin duda.** Es
doctrina defensiva, no procedimiento: contesta al miedo de *"aren't A Players the
athletes who don't work well together?"* (L323) recordando la definicion de jugador A
que ya esta en el grafo (L325, *"An A Player is someone who accomplishes the goals on
the scorecard"*). El unico criterio operativo, L327 (*"If teamwork is a core value in
your company, then a star athlete who wants the spotlight is not an A Player"*), **es
`identificar_competencias_tarjeta_puntuacion` mas `evaluar_cultura_empresa_adjetivos`
aplicados**, y no añade paso.

**A4, `RIDING THE RISING TIDE` (L333 a L349). NO MINABLE, pero es discutible y lo
digo.** Lo que podria defenderse esta en L345, la cita de Leahy (*"You have to have a
culture that is supportive and gives people room and tolerates a bit of difference in
personality"*): es una postura sobre la cultura de acogida, **no una busqueda que
alguien pueda ejecutar** (vara 6.1, *una advertencia es linea*). Y la unica frase con
forma de procedimiento, L347 (*"Building a team of A Players means thinking long and
hard about your business strategy and contemplating what roles you need to fill"*),
**REPITE `desplegar_estrategia_tarjeta_puntuacion`**. Sostengo dejarla fuera.

**A7, `YOU CAN DO IT` (L417 a L455). NO MINABLE, y es la pieza que un segundo lector
puede defender contra mi.** El caso a favor de cortarla existe y lo escribo entero
antes de rechazarlo: L427 y L429 traen un procedimiento que **no esta en ninguno de los
52 nodos**, el del entrenador del MIT (*"He organized the team to minimize each guy's
individual weaknesses... he did not let each of us do what we stank at"*), y L439 trae
una escala calificada con umbral (*"I rated them on a 1 to 10 scale in all categories.
They had to have a 9 or 10 on attitude and teamwork"*).

**Lo rechazo por dos razones citables.** Primera: **todo eso esta en boca de un tercero
dentro de un relato**, y el libro nunca lo dice en su propia voz como instruccion;
`D.30` avisa de que un parrafo asi no produce un nodo pobre sino **un nodo inventado**,
y aqui el inventario esta, pero prestado. Segunda: lo que el libro si dice en su voz,
L437 (*"Koch built the equivalent of a scorecard and evaluated all of his sailors
against the criteria, just as you will when you begin using the A Method"*), **es
explicitamente un reenvio a `crear_tarjeta_puntuacion_puesto`**, no un procedimiento
nuevo. **Sostengo dejarla fuera, y la declaro como el corte que mas facilmente podria
adjudicarse al reves.**

---

# 2. TRAMO B: `cap_07.md` L9 a L41. **MI CLASE: CERO CANDIDATOS**

*Sabia por el asunto de commit que el extractor declaro cero. Esto es confirmacion, no
lectura ciega, y por eso vale menos.*

Es la peroracion del libro. L13 a L17 (*"Who, not what"*) es lema; L29 a L41 es cierre
de arenga. **El unico riesgo esta en L21 a L27, que recapitulan los cuatro pasos**, y
los cuatro son repeticion literal de nodos vivos:

| linea | recapitula | nodo que ya lo tiene |
|---|---|---|
| L21 | como pensar la tarjeta de puntuacion | `crear_tarjeta_puntuacion_puesto`, `definir_resultados_tarjeta_puntuacion` |
| L23 | abastecerse por referidos y reclutadores | `abastecer_flujo_candidatos` |
| L25 | seleccionar con el proceso riguroso y la diana de habilidad y voluntad | `seleccionar_jugador_cuatro_entrevistas`, `calificar_tarjeta_puntuacion_habilidad_voluntad` |
| L27 | vender recordando las cinco efes | `abordar_cinco_efes_venta` |

**L19 (*"a who lens through which to view your entire business"*) es la unica idea que
no tiene nodo, y es una metafora, no un paso.** Coincido: cero.

# 3. TRAMO C: `cap_07.md` L43 a L429. **MI CLASE: CERO CANDIDATOS**

*Misma advertencia: sabia el resultado por el asunto de commit.*

**Yo cuento OCHO piezas, no siete**, y digo donde puede estar la diferencia:

| # | pieza | lineas | que es |
|---:|---|---|---|
| C1 | `FOOTNOTES` | L43 a L51 | dos notas bibliograficas |
| C2 | `KEYNOTES AND WORKSHOPS` | L53 a L71 | folleto comercial de ghSMART |
| C3 | `BEST CAREER OPPORTUNITY` | L73 a L77 | anuncio de empleo de ghSMART |
| C4 | `BIOGRAPHIES OF CAPTAINS OF INDUSTRY` | L79 a L259 | metodo muestral y nomina de entrevistados |
| C5 | `ACKNOWLEDGMENTS` | L261 a L285 | agradecimientos |
| C6 | `ABOUT THE AUTHORS` | L287 a L295 | fichas de autor |
| C7 | `ACCLAIM FOR Who` | L297 a L419 | blurbs |
| C8 | creditos de edicion y `LIBRARY OF CONGRESS CATALOGING-IN-PUBLICATION DATA` | L420 a L429 | datos de edicion |

**Si el reporte dice siete, la diferencia mas probable es que C7 y C8 vayan juntos como
una sola pieza de creditos.** Es una diferencia de corte, no de clase, y **no rompe
nada**: las ocho dan cero.

**Cero minable, y sin ningun caso limite.** C4 tiene cifras (*"Billionaires = over 20"*,
L91 en adelante) pero son estadisticas de la muestra del libro, no procedimiento.

**UNA COSA QUE SI ANOTO DE C8:** L420 a L429 llevan editorial, sello y datos de
catalogo. **Eso es material de ficha de fuente, no de nodo**, y para `smart_who` la
ficha ya esta cerrada en `fuentes/FUENTES_CANONICAS.json`. Lo digo porque el lote 8,
`bernerslee_bananas`, tiene la ficha abierta justamente por no haber localizado su
pagina de copyright: **este es el sitio del recorte donde se busca.**

---

# 4. LOS 15 CANDIDATOS, UNO A UNO

Volcados campo a campo despues de leer el libro. **Ninguno de los 15 ids existe en
`dataset/nodos.jsonl`** (52 nodos, comprobado por mi con un cruce de conjuntos), y **en
los 15 el nombre del fichero y el campo `id` dicen lo mismo**. Los 15 traen
`dominio: contratacion`, `estado: vivo` y la misma fuente `smart_who` con fecha
`2026-09-10`.

**Columna `puentes` = pasos que el candidato escribe y el libro NO dice**, contados por
mi contra el parrafo, que es lo que la seccion 8.3 me obliga a contar yo y no a copiar.

| # | id | pasos | mi clase | puentes | linea que lo sostiene |
|---:|---|---:|---|---:|---|
| 1 | `instalar_metodo_contratacion_empresa` | 11 | **SOSTENIDO. Cabeza de serie** | **0** | L251, y los diez de L253 a L277; el paso 11 es L295 |
| 2 | `construir_apoyo_equipo_directivo_metodo` | 5 | **SOSTENIDO** | **0** | L257 entera; el paso 5 (pares) lo licencia el propio titulo del item |
| 3 | `comunicar_vision_jugadores_organizacion` | 6 | **SOSTENIDO** | **0** | L259, con los tres mensajes tipo literales |
| 4 | `formar_equipo_practicas_metodo` | 3 | **SOSTENIDO, el mas flaco** | **0** | L261 |
| 5 | `retirar_barreras_politicas_metodo` | 5 | **SOSTENIDO** | **0** | L263 |
| 6 | `implantar_politicas_respaldan_metodo` | 5 | **SOSTENIDO** | **0** | L265, L267, L269, L271 |
| 7 | `reconocer_recompensar_uso_metodo` | 5 | **SOSTENIDO** | **0** | L273 |
| 8 | `retirar_directivos_rechazan_metodo` | 4 | **SOSTENIDO** | **0** | L275 |
| 9 | `celebrar_logros_planificar_cambio` | 4 | **SOSTENIDO** | **0** | L277 |
| 10 | `respetar_cautelas_legales_contratacion` | 9 | **SOSTENIDO. Cabeza de serie** | **0** | L301, L305, L307 a L313, L317 |
| 11 | `rechazar_candidato_razones_relevantes` | 5 | **SOSTENIDO** | **0** | L307 |
| 12 | `usar_lenguaje_no_discriminatorio_entrevista` | 4 | **SOSTENIDO** | **0** | L311 |
| 13 | `evitar_preguntas_ilegales_entrevista` | 10 | **SOSTENIDO** | **0** | L313, materia por materia |
| 14 | `distinguir_perfil_guepardo_cordero` | 7 | **SOSTENIDO, y lo marco DISCUTIBLE** | **0** | L357, L369, L371, L373, L375, L377, L379, L391 |
| 15 | `aplicar_metodo_promocion_sucesion` | 7 | **SOSTENIDO, y lo marco DISCUTIBLE** | **0 en estricto, 5 si el relato cuenta** | L397, L399, L403, L405, L407, L409 |
| | **total** | **90** | | **0 a 5** | |

## 4.1. Mis dos discutibles, escritos con su contrario delante

**DISCUTIBLE 1: `distinguir_perfil_guepardo_cordero`.** El contra es serio: el recuadro
de L351 a L393 es **un hallazgo de investigacion**, con su muestra (313 entrevistas,
L365), sus tasas (57 por ciento y 100 por ciento, L371 y L375) y su caso ilustrativo
(Bassoul, L383 a L389); una taxonomia con dos nombres no es un procedimiento, y `P.5.1`
dice que nombrar no es procedimentar.

**Lo sostengo igual**, y por lo que el propio recuadro añade encima del nombre: **una
regla de decision ejecutable**, L391 (*"if you have the choice to be or hire somebody
who errs on the side of being too fast and focused versus being slow and extremely
collaborative, we recommend going with the fast and focused option"*), **con su
subordinacion escrita a la tarjeta de puntuacion**, L357 (*"It depends on the
scorecard"*), y **con su propio techo**, el `No` de L391. Eso es un clasificador con
criterio, decision y limite, y el candidato lo recoge en ese orden. **Y no choca con
nada**: ningun nodo del grafo distingue perfiles de primer ejecutivo.

**DISCUTIBLE 2: `aplicar_metodo_promocion_sucesion`, y es el mas serio del lote.** El
contra: **el libro no da aqui ninguna instruccion.** L403 a L407 son el relato de lo que
el equipo de Bililies hizo en un banco, en pasado y en tercera persona (*"the ghSMART
team built scorecards for each role"*, *"ghSMART conducted a Who Interview with each
individual business leader"*, *"the team presented this thorough X-ray"*). Los pasos 2 a
6 del candidato son **ese relato puesto en imperativo**. `D.30` dice exactamente que un
parrafo asi no produce un nodo pobre, produce **un nodo inventado**.

**Lo sostengo, y con la cuenta doble delante para que la adjudicacion sea posible:**

- **En estricto son 0 puentes**: cada uno de los siete pasos tiene una frase detras, y
  la comprobe una a una. El plazo de dos a tres años esta en L403, el rango de doce a
  veinte colegas en L405, el destino de la radiografia en L407, y las tres acciones
  finales (acelerar, colocar en sucesion, sacar o recolocar) en L407.
- **Si la casa cuenta el paso de relato a imperativo como PUENTE, son 5 de 7 en este
  nodo**, y el lote entero pasa de 0 a 5 sobre 90.

**Y lo que me hace sostenerlo pese al contra es que el marco NO es relato:** L397
(*"most managers fall back on voodoo hiring methods when thinking about development,
promotions, and succession planning"*) y L399 (Clark: *"What got you promoted to one
rank won't necessarily get you promoted to the next rank"*, mas *"The scorecard changes
the higher somebody climbs"*) **dicen en voz del libro que el metodo se aplica a
promocion y sucesion, y por que**. El relato solo pone el como. **Y el ambito es nuevo:
`detectar_metodos_vudu_contratacion` cubre el vudu al CONTRATAR, no al promocionar.**

## 4.2. Lo que mire buscando REPITE, y no encontre

Cruce los 15 contra los 52 nodos vivos por palabra clave y abri los cinco vecinos mas
cercanos campo a campo. **Ninguno de los 15 repite a un nodo vivo.** Los tres roces
reales, con su razon de por que son CONTINUA y no REPITE, por direccion y sin bascula
(vara 6.1):

| par | por que no es duplicado |
|---|---|
| `celebrar_logros_planificar_cambio` contra `celebrar_aceptacion_primer_dia` | comparten el verbo y nada mas: uno celebra el logro del EQUIPO para reabrir el ciclo de instalacion, el otro celebra el SI de un candidato para no perderlo antes del primer dia |
| `implantar_politicas_respaldan_metodo` paso 2 contra `pedir_referencias_empleados` paso 1 | los dos ponen un resultado en la tarjeta de un directivo, **pero no el mismo resultado**: tasa de exito en contratacion del noventa por ciento contra cinco jugadores A abastecidos al año |
| `rechazar_candidato_razones_relevantes` pasos 2 y 3 contra `definir_resultados_tarjeta_puntuacion` | el candidato **cita** la tarjeta como garantia legal del descarte; no enseña a escribirla. Lo que añade el hijo es el uso, que la madre no tiene |

## 4.3. UNA COSA QUE ANOTO DE LOS 15 A LA VEZ: **CERO ARISTAS**

**Los 15 traen `nodos_previos: []` y `nodos_siguientes: []`.** Los nodos ya insertados
del mismo libro si las tienen (`vender_puesto_jugador` apunta a
`abordar_cinco_efes_venta` y a `planificar_cinco_olas_venta`).

**Lo declaro sin llamarlo caida, y digo las dos lecturas:** el commit `30b9e9d` de esta
misma vuelta declaro 28 aristas de serie de los candidatos YA insertados como operacion
aparte, asi que **la casa parece tener el habito de que el candidato viaja sin cables y
la arista se declara por lectura al insertar** (`D.37`). Si eso es la regla, esto es
correcto y no hay nada que decir.

**Pero la cuenta queda escrita aqui para que no se pierda**, porque este lote trae dos
series que el titulo enumera y `D.37` las cubre: **11 aristas de serie pendientes**,
ocho de la cabeza `instalar_metodo_contratacion_empresa` a sus miembros presentes (las
cosas 3 a 10) y tres de `respetar_cautelas_legales_contratacion` a las cautelas 1, 3 y
4. **Doce si la cautela 2 acaba teniendo nodo.** Mas el cierre de ciclo de
`celebrar_logros_planificar_cambio` sobre la cosa uno de la cabeza, que el propio paso 4
del candidato escribe.

---

# 5. `PASOS INVENTADOS POR CAPITULO`: MI CIFRA A CIEGAS

**Es la cifra que yo firmo y no copio (seccion 8.3), asi que la escribo antes de ver la
suya.**

| capitulo | tramo | pasos escritos | puentes (mi cuenta) | por ciento |
|---|---|---:|---:|---:|
| **Cap. 6, `Your Greatest Opportunity`** | `cap_06.md` L247-455 | **90** | **0 en estricto** | **0,0 %** |
| | | | *5 si relato a imperativo cuenta* | *5,6 %* |
| **Cap. 6, cuerpo final** | `cap_07.md` L9-41 | 0 | 0 | sin poblacion |
| **cierre de libro** | `cap_07.md` L43-429 | 0 | 0 | sin poblacion, y no es capitulo |

**LA LINEA BASE ES EL 36 POR CIENTO** del lote 1. Mi cifra de este tramo esta muy por
debajo, y las dos puntas de eso hay que decirlas:

1. **Es un tramo excepcionalmente rico en inventario.** De sus 90 pasos, **75 salen de
   dos series numeradas que el libro escribe ya en imperativo** (las diez cosas y las
   cuatro cautelas). `D.30` y la seccion 8.4 lo dicen al reves y aqui se ve derecho: un
   capitulo con inventario abundante baja la cifra sin que nadie lo haga mejor. **Esta
   cifra mide la mano contra el libro que le toco, y a esta mano le toco un manual.**
2. **La seccion 8.3 me avisa del error que esta metrica invita a cometer**, que es
   marcar un puente como transcripcion porque baja la cifra y sube el volumen del lote
   siguiente. **Por eso publico las dos cuentas del caso 15 y no solo la que me
   conviene**, y por eso digo que **un cero limpio en 90 pasos es un resultado que
   merece ser desconfiado antes que celebrado**.

**AVISO DE ATRIBUCION, y no es menor para esta metrica:** la cabecera de
`fuentes/smart_who/cap_06.md` dice `unidad: Cap. 5`, pero **el contenido de L247 a L455
es Cap. 6 del libro**: el Cap. 5 muere en el recuadro `HOW TO SELL A PLAYERS` de L217 a
L225, y mi propia acta de la vuelta 7 (seccion 3.1) ya sostuvo por `P.17` que la lectura
vence al metadato de la cabecera. **La fila de esta tabla se llama Cap. 6 y no
`cap_06.md`.** Si el reporte la titula Cap. 5, es un error de nombre de capitulo en una
metrica que la seccion 8.2 obliga a publicar POR capitulo, y lo nombrare.

**Y NO PUBLICO TODAVIA EL TOTAL DEL LOTE 2.** Me faltan las filas de las vueltas 5, 6 y
7 medidas por mi, y la seccion 8.3 dice que si no puedo verificarla no la firmo. La armo
en el acta.

---

# 6. RESUMEN DE MI APERTURA, PARA COMPARAR

**Lo que sostengo:** los 15 candidatos, los 15. Ninguno cae, ninguno repite a un nodo
vivo, ninguno choca de id.

**Lo que marco discutible por mi cuenta, y son dos:**
1. `aplicar_metodo_promocion_sucesion`, por relato puesto en imperativo (L403 a L407).
2. `distinguir_perfil_guepardo_cordero`, por taxonomia con regla de decision (L351 a
   L393).

**Lo que declaro como discrepancia mia contra el corte:** **falta la cautela dos de las
cuatro legales, L309, `estandarizar_proceso_todos_candidatos`.** Cuatro miembros
enumerados, tres nodos.

**Lo que declaro como limite de mi propio corte, por si el reporte lo corto y yo no:**
`YOU CAN DO IT` (L417 a L455), que tiene inventario prestado en boca de terceros, y **la
cosa uno de las diez** (L253), que es la mas cercana a la frontera de las dos que deje
fuera.

**Lo que dejo anotado sin llamarlo caida:** los 15 candidatos viajan con cero aristas, y
`D.37` deja 11 aristas de serie pendientes en este lote.

**Lo que NO he podido clasificar a ciegas de verdad:** los tramos B y C, cuyo resultado
supe por los asuntos de commit antes de leerlos.

---

**FIN DE LA APERTURA CIEGA. No vuelvo a tocar este fichero** (`D.34`: el sello se
verifica al terminar mi turno y un sello roto detiene la corrida). **No lo commiteo: lo
sella y lo commitea el arnes.**
