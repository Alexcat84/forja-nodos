---

# TAREA 1. `cap_04`, LA FRONTERA PUBLICADA ANTES DE CORTAR Y EL CANDIDATO CON SU ADUANA EN SECO

*`EXTRACTOR.md` 10 y 12.2: la frontera se publica y se cierra contra el cuerpo antes de contar nodo alguno.*

## 1.a. La unidad que se mina, y el borde heredado de `cap_03`

`cap_03` (Cap. 5, *Call to Action*) quedo minado en la vuelta 1 con su cuerpo cerrado en `L8` a `L81`
(`docs/loop/archivo/marquet_turn_the_ship/REPORTE_frente_hasta_v1.md`, commit `669524a`, seccion `1.b`
de esa vuelta). `cap_04` vive en **otro fichero** (`fuentes/marquet_turn_the_ship/cap_04.md`), asi que no
hay linea que continuar entre los dos: el borde heredado es que `cap_03` esta enterito minado y no queda
hueco de capitulo sin tramo asignado antes de `cap_04`.

| | | de donde sale |
|---|---|---|
| fichero | `fuentes/marquet_turn_the_ship/cap_04.md` | encargo, seccion 2 |
| unidad que el fichero declara | Cap. 6 | `sed -n '4p' fuentes/marquet_turn_the_ship/cap_04.md` |
| titulo textual | *Whatever They Tell Me to Do!* | `sed -n '5p' fuentes/marquet_turn_the_ship/cap_04.md` |
| lineas del fichero | 65 | `wc -l fuentes/marquet_turn_the_ship/cap_04.md` |
| palabras del fichero entero | 1271 | `wc -w fuentes/marquet_turn_the_ship/cap_04.md`, coincide con el encargo |
| cuerpo, desde `L8` (tras el segundo cierre `---` del encabezado, `L7`) | 1238 | `sed -n '8,$p' fuentes/marquet_turn_the_ship/cap_04.md \| wc -w` |

## 1.b. LA FRONTERA ENTERA, PIEZA A PIEZA

<!-- TALLADO: parcial salida=.m2/frontera_bruta.txt -->

La columna de palabras por pieza suma los conteos por linea de `.m2/frontera_bruta.txt` (`awk 'NR>=8{print NR": "NF}'`
sobre `cap_04.md`); la columna *que es* y *clase* es lectura, no instrumento, y se marca aparte.

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| R1 | L9 | 6 | el rotulo del titulo | RESIDUO: rotulo |
| R2 | L11 | 39 | pregunta de apertura al lector sobre que refuerza el modelo de lider a seguidores | POSTURA |
| R3 | L13 | 17 | la fecha, el sitio y la cuenta atras al relevo | RESIDUO: rotulo de fecha |
| R4 | L15 | 42 | dia tranquilo de vacaciones, guardia esqueleto, tareas rutinarias | CASO |
| R5 | L17 | 87 | el protocolo de formalidad de la camara de maniobras, quien puede entrar y como | CASO/contexto |
| R6 | L19 | 89 | la foto viral de la tripulacion informal mostrada en el entrenamiento PCO | CASO |
| R7 | L21 | 80 | contexto sobre el suboficial de primera visto en la foto | CASO |
| R8 | L23 | 24 | pregunta abierta al suboficial para calibrar que cree que es su trabajo | DISCUTIBLE 1, ver 1.d |
| R9 | L25 | 74 | la respuesta cinica *whatever they tell me to do* y su lectura | CASO |
| R10 | L27 | 23 | generalizacion: esa era la actitud en todo el barco | POSTURA |
| R11 | L29 | 6 | rotulo repetido del titulo de la seccion | RESIDUO: rotulo |
| R12 | L31 | 66 | escena: el navegante pregunta al segundo al mando si necesita algo mas | CASO |
| R13 | L33 | 62 | el antipatron: el segundo al mando explica que le gusta que los jefes de departamento reporten para revisar lo que le deben | CASO |
| **P1** | **L35** | **145** | **NODO: el guion correcto del reporte de cierre de jornada, que deja la propiedad del trabajo en el jefe de departamento** | **NODO** |
| R14 | L37 | 55 | los jefes de departamento objetan: quien responde si algo sale mal | POSTURA |
| R15 | L39 | 87 | la resolucion personal del autor: retiene la rendicion de cuentas y suelta el control de las decisiones | POSTURA |
| R16 | L41 | 101 | reflexion sobre la estructura de lider a seguidores, imagen de la fabrica textil | POSTURA |
| R17 | L43 | 23 | pregunta retorica sobre quienes son "ellos" | POSTURA |
| R18 | L45 | 3 | separador de seccion | RESIDUO: separador |
| R19 | L47 | 51 | resumen y transicion: ejemplos del modelo en operaciones, cierre de jornada, reuniones, mensajes, formaciones | POSTURA |
| R20 | L49 | 46 | el problema no era ausencia de liderazgo sino liderazgo del tipo equivocado | POSTURA |
| R21 | L51 | 39 | los costos del modelo: pasividad, falta de iniciativa, espera, paralisis | POSTURA |
| R22 | L53 | 5 | "todo tendria que cambiar" | RESIDUO/POSTURA de transicion |
| R23 | L55 | 3 | rotulo QUESTIONS TO CONSIDER | RESIDUO: rotulo |
| R24 | L57 a L65 | 65 | las cinco preguntas de cierre del capitulo | PENDIENTE DE DOCTRINA, vuelta 25 |
| **el cuerpo entero** | **L8 a L65** | **1238** | **suma de las piezas: 1238** | **residuo sin asignar: 0** |

    piezas: 24   lineas solapadas: 0   cuerpo 1238   suma 1238   residuo 0   lineas con palabras sin cubrir: 0

**LA FRONTERA CIERRA AL DIGITO: cuerpo `1238`, suma de piezas `1238`, residuo `0`, cero solapes y cero lineas
con palabras sin cubrir.** Una sola pieza, `P1`, se mina; las otras 23 son residuo, postura o caso.

## 1.c. LA CITA DE LA PIEZA QUE SE MINA, CON SU `sed` PEGADO (`D.35`)

<!-- TALLADO: parcial salida=.m2/citas_nodos.txt -->

| pieza | linea | la salida de `sed`, pegada | veredicto |
|---|---|---|---|
| P1 | L35 | `I subsequently went over this end-of-day checkout event in detail with all the officers. The problem, I explained, was that in this scenario the XO is the on...` | NODO |

## 1.d. EL DISCUTIBLE 1, MARCADO ANTES DE SABER SI ACIERTO

**`R8` (L23, 24 palabras)** queda fuera. El texto trae una sola pregunta abierta (*"Hi, what do you
do on board?"*) mas una frase de proposito (*by asking open-ended questions like this, I could
better gauge what the crew thought their job was*): **un solo medio, sin inventario que transcribir**.
Escribir pasos alrededor de esta pregunta (como escuchar el tono, o hacer preguntas de seguimiento)
seria inventar lo que el parrafo no dice, y `EXTRACTOR.md` 15.4 pide desconfiar de los pasos propios
justo cuando el parrafo es pobre. **Se sostiene como POSTURA/CASO y no como nodo.**

## 1.e. EL CANDIDATO, ESCRITO Y PASADO POR LA ADUANA EN SECO EN EL MISMO ACTO

`cuarentena/marquet_turn_the_ship/informar_cierre_jornada_conservar_propiedad_trabajo.json`, con
`UNIDAD DE ORIGEN: fuentes/marquet_turn_the_ship/cap_04.md` en su `resumen_teorico` (`D.58` 0.a).
**5 pasos, 5 TRANSCRIPCION, 0 PUENTE** (relectura de fidelidad `D.30` en el acto, seccion 1.b de arriba
cita cada linea).

    $ python forja.py informe cuarentena/marquet_turn_the_ship/informar_cierre_jornada_conservar_propiedad_trabajo.json
    ============================================================================
    INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
    ============================================================================
    candidatos revisados        : 1
    poblacion del barrido       : 447   (346 del grafo mas 101 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

    EL SALDO
      ENTRARIAN sin leer nada          : 1
      BLOQUEARIAN esperando veredicto  : 0   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0

    [ENTRARIA] informar_cierre_jornada_conservar_propiedad_trabajo   (informar_cierre_jornada_conservar_propiedad_trabajo.json)

    NADA SE INSERTO. Este informe es de SOLO LECTURA.

**ENTRARIA al primer intento, 0 CAERIA, 0 BLOQUEARIA.** No hizo falta correccion.

## 1.f. LA MADRE POR LECTURA, buscada aunque la señal no la levante (seccion 11)

Busque en los 6 candidatos de `cap_03` (ya minados en la vuelta 1) si alguno nombra o desarrolla el
cierre de jornada como uno de sus pasos: ninguno lo hace (cubren la reunion rutinaria, el oficial
frustrado, el tramite de firmas, el reparto de mensajes, la formacion y premios, la primera mitad y
segunda mitad del recorrido inicial). **Sin madre declarada; el nodo entra como hermano de los de
`cap_03` bajo el mismo diagnostico de lider a seguidores, y su veredicto frente a ellos es SANO.**

## 1.g. EL SALDO DE LA TAREA

| | |
|---|---:|
| unidades leidas (piezas) | **24** |
| procedimientos | **1** |
| postura/caso/residuo/pendiente | **23** |
| candidatos escritos en `cuarentena/marquet_turn_the_ship/` por esta tarea | **1** |
| candidatos que cayeron en la aduana | **0** |
| discutibles marcados | **1** (seccion 1.d, sostenido) |
