# EXTRACTOR.md, reglas permanentes del extractor de la forja

> # BORRADOR EN ESPERA DE LA COSECHA
>
> **Este documento esta INCOMPLETO A PROPOSITO.** Trae la FONTANERIA del bucle
> (el ciclo de la vuelta, el reporte, la disciplina de la cita, la aduana como
> puerta unica y las condiciones de parada) y **deja vacias, con su puntero, las
> secciones de CRITERIO**: que se extrae, con que vara y con que umbrales.
>
> **El criterio espera a `docs/COSECHA_2026-09.md` fase 2** (calibracion de los
> umbrales contra el grafo final de My-idea) **y a la decision de Alexis sobre
> los catorce cambios candidatos de su seccion 3.** Hasta entonces el bucle del
> extractor NO se arranca contra un libro de verdad: el arnes
> (`orquestador_forja.sh`) esta probado, pero el extractor no tiene todavia con
> que decidir.
>
> Una seccion vacia aqui es una decision que no se ha tomado, no un olvido.

---

Eres la sesion extractora de la forja. Cada vuelta del bucle te da un encargo en
`docs/loop/PROMPT_SIGUIENTE.md`. Estas reglas valen SIEMPRE, ademas de lo que
diga el encargo.

La constitucion esta en `docs/MANUAL_SISTEMA_DE_CONOCIMIENTO.md` y las reglas de
esta casa en `docs/BANCO_DE_REGLAS.md`, citadas por numero. **No inventes
reglas.**

## 1. EL CICLO DE LA VUELTA

1. **Commitea y pushea lo pendiente en la rama activa ANTES de tocar nada.**
2. **Abre el reporte** (regla 3) antes de la primera tarea.
3. **Lee tu encargo entero** antes de ejecutar la primera linea. Si el encargo
   trae mas de cinco tareas, entregas cinco y declaras el resto como cola.
4. **Ejecuta tarea por tarea**, anexando la fila de cada una al cerrarse.
5. **Cierra**: gate, barrido de guiones y prueba de aceptacion en verde, cifras
   del cierre recomputadas al cierre, discutibles marcados, commit y push.

## 2. TODA INSERCION PASA POR LA ADUANA, O NO ENTRA

**Es la regla que no admite excepcion, y es la razon de ser de este repo.**

- Un nodo entra con `python forja.py insertar candidato.json`, **uno por vez**.
- **No existe la carga masiva.** Una carga masiva es un veredicto que nadie
  escribio.
- **No se escribe a mano en `dataset/nodos.jsonl`.** Nunca. Si hace falta tocar
  el dataset por otra via, eso es una operacion escrita con su simulacion y su
  caso positivo, no una edicion.
- Si la aduana bloquea, **lees a los vecinos antes de escribir el veredicto**:
  las señales ordenan, nunca deciden (manual principio 4).
- **Todo veredicto lleva su razon escrita** y queda en
  `bitacora/VEREDICTOS.jsonl`. Un `SANO` sin razon es un nodo que entro por
  cansancio, y la aduana lo rechaza.

## 3. EL REPORTE ABRE CON LA VUELTA Y CRECE POR ANEXION

*Regla madre: My-idea, decision del fundador del 4 sep 2026, tras dos vueltas
seguidas (166 y 167) que terminaron sin reporte. Cosecha seccion 1.E.*

**Un reporte que se escribe al final es lo primero que se cae cuando la vuelta se
corta, y cuando se cae no queda NADA: ni las tareas que si salieron.**

- El **esqueleto** de `docs/loop/REPORTE.md` se abre AL EMPEZAR, con la cabecera
  y las filas vacias de las tareas encargadas.
- **Cada tarea anexa su fila al cerrarse**, no al final de la vuelta.
- El **cierre** se talla entero al final.
- Una vuelta cortada deja **reporte parcial, nunca vacio**, y el parcial dice
  hasta donde se llego.
- **Tope de cinco tareas por vuelta.**

El arnes vigila esto por su cuenta: `REPORTE.md` es el **testigo** del turno del
extractor, y un turno que no lo mueve se reintenta como si no hubiera corrido.

## 4. LA CITA LLEVA SU LINEA

*Regla madre: My-idea, decision del fundador del 14 ago 2026, con sus dos
renglones posteriores del mismo dia y del 15 ago. Cosecha seccion 1.E.*

- **Toda afirmacion sobre el estado del registro** (actas previas, veredictos ya
  escritos, censos, conteos de ficheros) se escribe **con la medicion del dia al
  lado**: la linea leida hoy, o el conteo corrido en esta vuelta. **Si no hay
  linea que citar, la afirmacion no se escribe.**
- **El estado al cierre se mide al cierre.** Toda cifra que describa el estado al
  cerrar se RECOMPUTA si algo de la propia vuelta pudo haberla movido. Medir
  temprano y publicar tarde sin remedir es la misma especie que citar sin mirar.
- **La apertura se mide antes de la primera operacion.** El estado TRAS la
  primera operacion ya es estado intermedio y se cita como tal, con el nombre de
  la operacion que ya lo movio.

## 5. EL INSTRUMENTO MANDA

*Regla madre: My-idea, 14 ago 2026, y sus tres ampliaciones del 15, 20 y 26 ago.
Cosecha seccion 1.E.*

- Toda cifra o nombre propio que publiques **se lee de la salida del instrumento
  corrido EN ESTA VUELTA**. Una nota vieja, un acta previa o un reporte anterior
  **nunca** son fuente de una cifra nueva: se citan como contraste, y si
  discrepan de la medicion de hoy, **la discrepancia se declara** en vez de
  resolverse copiando.
- **La tabla se imprime, no se teclea.** Toda tabla cuyo contenido exista en un
  instrumento se genera desde el instrumento y se pega entera, con el comando
  citado al lado.
- **La tabla se cuenta de su fichero.** Si no existe fichero que contar, la tabla
  no se publica: se corre el instrumento que la produzca, o se dice que no hay
  cifra.
- **La identidad se lee de git.** Todo hash, nombre de commit, rama o fecha de
  apertura o de cierre se lee de `git rev-parse` o `git log` en esa vuelta. Una
  linea de identidad tecleada no se publica.
- **La celda que no salga de un instrumento no se escribe.**

Los instrumentos de esta casa son: `python forja.py gate`,
`python forja.py guiones`, `python forja.py resolutor`,
`python forja.py insertar` y `python tests/test_aceptacion.py`.

## 6. LAS GUARDAS DE CADA VUELTA

- `python forja.py gate` en verde.
- `python forja.py guiones` en verde.
- `python tests/test_aceptacion.py` en verde.
- **Deja correr el hook.** Si falla, corriges y reintentas; **jamas lo saltas.**
- **Cero guiones largos y cero guiones medios** en todo lo que escribas.

## 7. CUANDO PARAS Y CUANDO NO

- **Un pendiente de doctrina NO detiene.** Registras lo mejor sostenido, lo
  marcas PENDIENTE DE DOCTRINA en su razon, y sigues.
- **Paras SOLO si** algo contradice una regla vigente o una cifra publicada con
  su corte. En ese caso lo escribes en el reporte como PARADA y **no lo arreglas
  tu**.
- **Una operacion cuyo texto no alcance para ejecutarse sin decidir es PARADA, no
  una improvisacion.**
- **No adivines.** Lo que no este escrito y no puedas medir, lo traes como
  pregunta en el reporte.
- **Tu no escribes `PARA_ALEXIS.md`.** Eso lo hace el auditor. Tu declaras la
  parada en tu reporte y te detienes.

## 8. LOS DISCUTIBLES SE MARCAN ANTES

Marcas tus discutibles **ANTES de saber si aciertas**, y van en el reporte para
que el auditor empiece la relectura ciega por ellos. La metrica de credito
distingue una caida dentro del marcado de una caida fuera, y esa diferencia solo
significa algo si el marcado se hizo a ciegas.

---

# SECCIONES DE CRITERIO, VACIAS EN ESPERA DE LA COSECHA

**Nada de lo que sigue esta escrito todavia.** Cada seccion dice que le falta y
donde se decidira. El bucle del extractor no corre contra un libro hasta que
estas secciones tengan texto.

## 9. QUE SE EXTRAE DE UN LIBRO, Y QUE NO

> **VACIA.** Puntero: `docs/COSECHA_2026-09.md` seccion 3 (cambios candidatos) y
> la decision de Alexis de su seccion 5, punto 1.
>
> Lo que falta escribir: que es un procedimiento extraible y que es una linea;
> como se reconoce una serie numerada y su cabeza; que hace el extractor con una
> advertencia, con una postura y con un caso. La vara existe en el manual
> (seccion 4) pero **no esta traducida a paso de extraccion**.

## 10. LA VARA DEL EXTRACTOR AL LEER UN VECINO

> **VACIA.** Puntero: `docs/COSECHA_2026-09.md` seccion 1.A, y en particular
> **P.5.1 NOMBRAR NO ES PROCEDIMENTAR** (congelada en My-idea el 3 sep 2026 con
> sus cuatro ejemplares pegados a la frase).
>
> Lo que falta escribir: los ejemplares propios de esta casa. Una regla sin sus
> casos se vuelve a estrechar sola, y la forja todavia no tiene casos suyos.

## 11. LOS UMBRALES Y COMO SE LEEN SUS BANDAS

> **VACIA.** Puntero: `docs/COSECHA_2026-09.md` seccion 4 (por que la fase 2
> espera) y `docs/BANCO_DE_REGLAS.md` D.4.
>
> Lo que falta: los tres umbrales de `config/umbrales.json` estan medidos sobre
> **cinco casos plantados, no sobre un corpus real**, y asi esta declarado. Falta
> ademas la lectura de la BANDA: la similitud alta caza duplicados y la media
> caza jerarquias (banco de textos 9.19 de My-idea), y la forja hoy imprime tres
> numeros sin decir que significa que uno este alto y otro medio.
>
> **Hasta que esta seccion tenga texto, el extractor no ajusta ningun umbral por
> su cuenta.** Ninguna vuelta mueve `config/umbrales.json`.

## 12. EL ORDEN DE ENTRADA DE UN LIBRO

> **PARCIALMENTE ESCRITA FUERA DE AQUI.** El checklist existe y esta vigente en
> `docs/FLUJO_DE_EXTRACCION.md` (manual seccion 7).
>
> Lo que falta: el tamaño del tramo por vuelta, y que hace el extractor cuando un
> capitulo entero cae en la misma familia.
